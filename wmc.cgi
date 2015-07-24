#!/usr/local/bin/perl
# wmc.cgi upldホルダ内wmaFile変換　1回1ホルダのみ$wmacで処理、ホルダ内子ホルダは非処理のまま移送
#						
# $wmacエラー時、処理済未処理File含め結果dirに移送、ソースdirに残さない
# 061130 061129 061127create
$srcdir="wmcs";	# /FLD/XX.wma  ソースdir　 (ホルダ無い場合$tmpwmcにupld、$wmac処理後dwld)
$dstdir="wmcd";	# /FLD/XX.wma  変換結果dir (dwld後ホルダ含め削除すること)
$wmac="wmac2.cgi";				# use Unicode::Japanese
$tmpwmc="wmc";					# wmac.cgi変換dir
for $fld (readd($srcdir)){
  if(-d "$srcdir/$fld"){
	map{rename "$srcdir/$fld/$_","$tmpwmc/$_"} readd("$srcdir/$fld");	# file移送
	mkdir "$dstdir/$fld"; rmdir "$srcdir/$fld";				# dir移送
	require $wmac;	# html出力末尾"Nfile converted"、global変数 $Err_code設定有り
	chdir "..";	# dir戻し、(正常異常終了共変換F存在dirをｶﾚﾝﾄdirとしてﾘﾀﾝのため)
	map{rename "$tmpwmc/$_","$dstdir/$fld/$_"} readd($tmpwmc);
	$Err_code || rename "$dstdir/$fld","$dstdir/Err-$fld";	# 変換異常時 Err-ホルダ名
	print " on $dstdir/",($Err_code ? "" : "Err-"),"$fld<br>";
	goto Fine;					   	# 1ホルダ処理で終り
  }
}
print "Content-type: text/html\n\n<html>Err no Folder on $srcdir/,<p> on $dstdir/";	# 対象ホルダ無し
Fine: 1;
$,="<br>";
print "<br>",readd($dstdir);
#
sub readd{opendir D,shift; my @rd=readdir D; close D; sort grep(!/^\./,@rd);}	# "." ".."除去
#
__END__
$cgi="tmp.txt"; print`perl -cw $cgi 2>&1`; print`cat -n $cgi`; rename"tmp.cgi","wmc.cgi";

# globは指定親dirも含む、"." ".."は含まない # opendirは指定親dirを含まない、"." ".."を含む
