#!/usr/local/bin/perl
# 061208 title,author(artist),description(comment)一括変換、拡張チャンクのalbum,year,genre,trck等は未了
# 061129 exit除去、$Err_code,goto追加、$wkdir="./wmc";に変更
#060517 patch SEEK_SET→0,read.size→(-s SC) unlink除去 wmac→../wmac
# 060119 olpsﾍｯﾀﾞ録音秒修正  秒=ﾌｧｲﾙｻｲｽﾞ(6&ﾁｬﾝｸofst0x10)×8bit/ﾋﾞｯﾄﾚｰﾄ(Gﾁｬﾝｸofst0x64)　SJIS文字,バイナリ値計3箇所埋込
# 050325 ヘッダ4196bの例あり、ヘッダ部読取4k→8Kbに拡大 
# 050127変換後ソースファイル消去(-bk.wmaはやめ)　040706 wma file converter to olympus-header
# 仕様 テンプレト読み、ソースヘッダ部概8k読み、テンプレト0&-chk以外切捨、ソースG-chk移送、
#	ソース&3-chk抽出移送、utf16-sjis変換移送、テンプレト0&ヘッダサイズ修正、ソース6&-chk抽出、
# 	テンプレトとソース6&-chk結合、出力
$and0_id =pack("H32","3026b2758e66cf11a6d900aa0062ce6c");# 0&_chk hdr-size-ofst=0x10 size=var
#							 # csize=0x1e(winのみの場合fix、olmpsは不明)
$olps_c_ofst=0x036c;		# olps-comment 0&開始ofset=0&+0x036c、サイズ上限=100バイト
#
$olmps_id=pack("H16","4f004c0059004d00");		 # olmps_id and0-ofst=0x3a "O.L.M.P."
$G_Seh_id=pack("H32","A1DCAB8C47A9CF118ee400c00c205365");# G_Seh_chk csize-ofst=0x10
# $G_Seh_siz=0x68;					 # G_Seh_chk csize
$and3_id=pack("H32","3326b2758e66cf11a6d900aa0062ce6c"); # 3&_chk csize-ofst=0x10 variable 
$and3_cha_siz_ofs=0x18;				# title-char size(2バイト) ofset
$and3_cha_ofs=0x22;				# title-char 書込み位置 ofset
$and6_id=pack("H32","3626b2758e66cf11a6d900aa0062ce6c");# 6&_chk csize-ofst=0x10 variable
#
$wkdir="./wmc";			# ソース、テンプレートF設置dir				#変更
$tplf="../twma";		# olmpsテンプレートファイル
chdir $wkdir;
open(TP,$tplf); binmode TP;
read(TP,$tpb0,4096);close TP;	# テンプレート全部概ね4Kb読、close
$cnvn=0;			# 変換ファイル数、初期リセット
#
for (glob("*.wma")){
$tpb=$tpb0;			# テンプレートbuf毎回ロード
$srcf=$_;			# MS-WMT標準.wmaソースファイル
# open(SC,"$_") || msgout_ext("can't open src-F=$srcf"); # 中断						#####
unless(open SC,"$_"){ $Err_code=0; msgout_ext("can't open src-F=$srcf");} # 中断		#変更
binmode SC;
read(SC,$scb,8192);				# ヘッダ部概ね8Kb読 ヘッダ4196bの例あり
if (substr($scb,0x3a,length($olmps_id)) eq $olmps_id){
	warn_msg("       $srcf (olps-F) no cnvt");next; # 不変換
}
substr($tpb,chk_size($tpb,$and0_id))="";   # テンプレート&0ヘッダサイズ分以外切捨
substr($tpb,chk_ofst($tpb,$G_Seh_id),chk_size($tpb,$G_Seh_id))=
chk_extr($scb,$G_Seh_id);			# ソースGチャンク、テンプレ移送
# ****** 060118追加　******
# GチャンクからビットレートB_rate(bps)取得、 6&チャンクからファイルサイズF_size(byte)取得
# 演奏秒数算出	P_sec=F_size×8/B_rate
$P_sec=chk_size($scb,$and6_id)*8/chk_size($scb,$G_Seh_id,0x64); # 秒数算出
$hh=int$P_sec/3600; $ms=$P_sec%3600;		# 時分秒分割
$mm=int$ms/60; $ss=$ms%60;
$hhmmss=sprintf("%02d%02d%02d",$hh,$mm,$ss);	# 左を0で埋めた2桁の10進数値×3(時分秒)=計6バイト
$olps_t1_ofst=0x8c;				# CONST olps-playtime S-JIS 0&開始ofset
$olps_t2_ofst=0xd4;				# CONST 同　バイナリ
$olps_t3_ofst=0x24e;				# CONST 同　バイナリ
substr($tpb,$olps_t1_ofst,6)=$hhmmss;		# 時分秒 テンプレ0&上書き
$P_sec_b=pack("V",$P_sec*1000);			# x86系リトルエンディアンの32ビット整数
substr($tpb,$olps_t2_ofst,4)=$P_sec_b;		# バイナリ秒 テンプレ0&上書き
substr($tpb,$olps_t3_ofst,4)=$P_sec_b;		# バイナリ秒 テンプレ0&上書き
# ******  ******#
$sc_and3=chk_extr($scb,$and3_id);					# ソース&3チャンク抽出
substr($tpb,chk_ofst($tpb,$and3_id),chk_size($tpb,$and3_id))=$sc_and3;	# テンプレ移送
#
# 改、title開始点以下最後尾まで(title,author(artist),copyright,description(comment),rating)を抽出
#↓新　→旧 $u16str=substr($sc_and3,$and3_cha_ofs,unpack("v",substr($sc_and3,$and3_cha_siz_ofs,2))-2); # utf16-le抽出
$u16str=substr($sc_and3,$and3_cha_ofs,unpack("v",substr($sc_and3,0x10,2))-$and3_cha_ofs);
#
use Unicode::Japanese;
chdir "..";					### ->newできないため一時chdir
$s=Unicode::Japanese->new();
$getutf8= $s->set($u16str,'utf16-le')->get;	#method分解 # utf16-le sjis変換
$sjstr  = $s->set($getutf8)->sjis;
# $sjstr=$s->set($s->set($u16str,'utf16-le')->get)->sjis;
chdir $wkdir;					### 一時chdir復旧				#改良
substr($sjstr,0x64)="" if length $sjstr > 0x64;	# 100バイト以下に切詰め
substr($tpb,$olps_c_ofst,length($sjstr))=$sjstr;# テンプレ0&上書き
substr($tpb,0x10,4)=pack("V",length($tpb));	# テンプレヘッダサイズ修正
#
seek(SC,chk_size($scb,$and0_id),0);	# ソース6&チャンクにシーク(SEEK_SET初頭から) # SEEK_SET
read(SC,$_,-s SC);close SC;	# ソース6&チャンク全部読、close	# 10000000
open(CV,">tempf"); binmode CV;	# 変換結果出力"tempf"ファイル open
print CV $tpb,$_;close CV;	# 新しいヘッダと6&ボディ書込み、close
#
#rename $srcf,"bk$srcf";	#ソース bkSRC.wmaにリネーム
#unlink $srcf;			#ソース消去
rename "tempf","$srcf";		#変換結果 SRC.wmaにリネーム
++$cnvn;			# ファイル変換数カウントup
warn_msg("<a href=./tmp/$srcf>$srcf</a> (src=bk$srcf)");#変換結果表示
}		# line 4 for{block-end
$Err_code=1;								#追加
msgout_ext("${cnvn}files converted");	# 終り							######
#
#================================
sub chk_ofst{			# getチャンクオフセット arg(buf,idkey)
	my($buf,$idkey)=@_;
	my $ofs=index($buf,$idkey);
	if ($ofs < 0 ){
	  $Err_code=0;							#追加
	  msgout_ext("no chk-idkey=",unpack("H*",$idkey),":$idkey($srcf)");			######
	}
	$ofs;
}
#--------------------------------
sub chk_size{			# getチャンクサイズ arg(buf,idkey[,ofset])
	my($buf,$idkey,$ofset)=@_;
	$ofset=0x10 unless $ofset;
	unpack("V",substr($buf,chk_ofst($buf,$idkey)+$ofset,4));
}
#--------------------------------
sub chk_extr{			# getチャンクbody arg(buf,idkey)
	my($buf,$idkey)=@_;
	substr($buf,chk_ofst($buf,$idkey),chk_size($buf,$idkey));
}
#--------------------------------
sub warn_msg{			# warning msg out, 処理継続
	push(@msgout,"@_\n");
}
sub msgout_ext{			# [error]msg out, 中断、終了
	warn_msg(@_);	
	print "Content-type: text/html\n\n<html><pre>*****\n @msgout*****";
	goto Fine;							#変更				#####
}
#--------------------------------
Fine: 1;								#追加
__END__
$cgi="tmp.txt";print `perl -cw $cgi 2>&1` ,`cat -n $cgi`;
rename "tmp.cgi","wmac.cgi";
==================================================================
unicode tr
$aa=pack("H*","f1588a8d0030715c2c67a690715c");
use Unicode::Japanese;
# $bb=Unicode::Japanese->new($aa,'utf16-le')->get;
# print Unicode::Japanese->new($bb)->sjis;
print Unicode::Japanese->new(Unicode::Japanese->new($aa,'utf16-le')->get)->sjis;
=======================================================================
binary=pack("V",LIST)		# 
LIST=unpack("V",binary);	# binaryを数値にする
n/N/ v/V:　"n"M68系ビッグエンディアンの符合無しshort～"V"x86系リトルエンディアンの32ビット整数
h/H:16進文字列低ニブル先/高ニブル先

0x3132 16進スカラ数	\x3132 16進正規表現

print pack("V","41424344")		=>DCBA、"v"では=>DC
print unpack("V","ABCD")		=>1145258561
print sprintf("%x",unpack("V","ABCD"))	=>44434241 32bitまで
print unpack("H*","ABCDE")		=>4142434445　文字列16進表示
# read(HDL,$var,length,offset);	# offsetは$varの位置
# seek(HDL,offset,whence)	# whence 0=SEEK_SET先頭 1現在 末尾2　(SEEK_SETは不可)
