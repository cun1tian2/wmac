●●(ma)github/wmac/readme.md  (sb)evernote 

installed tk2aym2(42, xrehbr112    (tk2nan旧ver060517wmac.cgi tk2hbr112NG)
wmac2.cgi ﾌｫﾙﾀﾞ cb/wmc (src multi Files, dst          (●● don't use wmac.cgi)
wmc.cgi   ﾌｫﾙﾀﾞ cb/wmc (src multi folders, dst
depend on lib cb/Unicode/Japanese.pm、olmpsテンプレートファイル./twma(ｺｰﾃﾞｨﾝｸﾞは../twma)
------------------------------------------------------------------------------------------
wmac変換操作法(要再改150917)：
wmp12のCDﾘｯﾋﾟﾝｸﾞwavﾌｧｲﾙはlilihtやhStepでope不可、lilithﾘｯﾋﾟﾝｸﾞ時直接wma変換ﾀｸﾞ(除くalbm等)付け同時施工要。(*1)
lilith：CDﾘｯﾋﾟﾝｸﾞwma9変換(ﾘｻﾝﾌﾟﾙ mono CBR 32k)、同時ﾀｸﾞ付加(title artist wmComment)、(wmac変換時3&ﾁｬﾝｸ用ﾀｸﾞ1個以上必須)
wmac：  olympusﾀｸﾞ変換
step：  ﾀｸﾞ修正 Album追加、TrackとGenre消去(wmacで変換せずﾃﾞﾌｫﾙﾄ値or空白とする為)
DssPlayer: olympus用ﾌｧｲﾙ名、olympusｺﾒﾝﾄ修正(必要に応じてｱﾙﾊﾞﾑ名追加等)
(注:lilithﾘｯﾋﾟﾝｸﾞ時ﾀｸﾞ操作法によっては次のwmac変換で生成された結果がWMPで再生できない場合がある)
------------------------------------------------------------------------------------------
wmac変換操作法(改150910)：

Lilith変換 ：wav->wma、CDﾘｯﾋﾟﾝｸﾞ->wma、ﾀｸﾞ編集(wma変換と同時、ﾘｻﾝﾌﾟﾘﾝｸﾞ無しﾀｸﾞ編集のみの単独変換) 何れも可。
           ：WMA9 CBR 32k monoﾘｻﾝﾌﾟﾙ。
           ：olympusﾍｯﾀﾞはLilithに変換される。ﾘｻﾝﾌﾟﾘﾝｸﾞ無しでﾀｸﾞ編集すると0&.ﾍｯﾀﾞﾁｬﾝｸ肥大化する為使用禁止●●
STEpﾀｸﾞ編集：STEpとLilith操作順問わず可能。
Trk番号の扱：TrackNumber/曲順 LilithとSTEpの扱いは異なり不可解->無視又は消去とする
wmac変換   ：ｿｰｽﾌｧｲﾙ条件 WMA9 CBR 32k mono、。
           ：●ｱﾙﾊﾞﾑ ﾀｸﾞ(含むAlbumTitle Year Genrue GenreID Track等)は消去。(簡易ﾃﾝﾌﾟﾚｰﾄ 使用の為(*1))、事後必要ﾀｸﾞ要追加。
           ：DSSPlayerｺﾒﾝﾄは ﾀｲﾄﾙ 参加ｱｰﾃｨｽﾄ ｺﾒﾝﾄ をIFS="nul"で連結生成(*2)。
           ：wmac変換後ﾀｸﾞ編集可(Lilithﾘｻﾝﾌﾟﾘﾝｸﾞ無しﾀｸﾞ編集を除く)。 
           ：●ﾀｲﾄﾙ 参加ｱｰﾃｨｽﾄ ｺﾒﾝﾄを含む(3&.ﾁｬﾝｸ) 不存在時->"3&.ﾁｬﾝｸnotFound ｴﾗｰ"。
           ：●0&.ﾍｯﾀﾞｰﾁｬﾝｸ(6&.ﾁｬﾝｸの前まで) 8kB超の場合"6&.ﾁｬﾝｸnotFound ｴﾗｰ"。
                 lilith(ﾘｻﾝﾌﾟﾘﾝｸ無しでﾀｸﾞ編集ﾞすると肥大する為禁止
sansaPlayer：e-130表示窓 ﾀｸﾞ表示㊤artist ㊥title ㊦album、[○]釦押し時のｴﾝｺｰﾄﾞ表示例 "wma, 32kbps, 44khz"。
           ：(*1)ｱﾙﾊﾞﾑ ﾀｸﾞ不存在時"unkown album"となる。
DSSPlayer  : 記録可能時間 HQﾓｰﾄﾞwmaで4H20M 大量保存不可
           ：(*2)DSSPlayerｺﾒﾝﾄ表示は最初の項目(通常ﾀｲﾄﾙ)のみ。(IFS="nul"に続く項目表示不可)
           ：Pcから端末DSS-10へのupld時ﾌｧｲﾙ名縮小8ﾊﾞｲﾄ化例 "何とか~1".wma、再dwldしても復元不可

-------+------------------------------------------------------------------------------------
 項目  | 細目           Windows＞File＞Property の詳細 ".."途中省略  ":"値格納例
-------+----------------------------------------------
説明 ﾀｲﾄﾙ:たいとる ｻﾌﾞﾀｲﾄﾙ 評価 ﾀｸﾞ ｺﾒﾝﾄ:こめんと
ﾒﾃﾞｨｱ 参加ｱｰﾃｨｽﾄ:あちすと ｱﾙﾊﾞﾑのｱｰﾃｨｽﾄ ｱﾙﾊﾞﾑ:あるばむ 年:2015 ﾄﾗｯｸ番号:1 ｼﾞｬﾝﾙ 長さ:00:00:30
ｵｰﾃﾞｨｵ ﾋﾞｯﾄﾚｰﾄ:32kbps
元ﾉ場所 ﾌﾟﾛﾃﾞｭｰｻ 発行元 ..  ｴﾝｺｰﾄﾞ方式 .. 著作権
ｺﾝﾃﾝﾂ 保護者による制限 .. 作曲者 指揮者 ..  保護:いいえ ..
ﾌｧｲﾙ 名前:kamo1.wma 項目の種類:WinMediaｵｰﾃﾞｨｵﾌｧｲﾙ ﾌｫﾙﾀﾞﾊﾟｽ:C:\... 作成日時:2015/09/10 3:48 更新日時:2015/09/10 3:48
ｻｲｽﾞ:131kB 属性:A .. 所有者:nec\t ｺﾝﾋﾟｭｰﾀ:NEC
-------+------------------------------------------------------------------------------------

・ﾀｸﾞの書換え：winFileﾌﾟﾛﾊﾟﾃｨの値を書換えて[OK/適用]で更新日時が更新され書換完了する。STEpで書換えてもOK。
   Lilithではﾌｧｲﾙ変換-ﾀｸﾞ書換え-ﾘｻﾝﾌﾟﾙ無し[開始]でOK (同一ﾌｫﾙﾀﾞ時ｿｰｽに"_Dec000"付加新File生成、
     ﾘｻﾝﾌﾟﾙ無しで他のmp3とかWM9のCBR/VBR/ﾋﾞﾄﾚｰﾄ変更するとエラーで中止)。
   更新確認法は winFileﾌﾟﾛﾊﾟﾃｨ/STEp/Lilith 何れでも可。
・sansa e-130表示窓  ﾀｸﾞ表示㊤artist  ㊥title ㊦album、[○]釦押し時の圧縮ｺｰﾄﾞ表示例"wma, 32kbps, 44khz"。

・0&.u.f(ascii)ﾁｬﾝｸID x-3026 b275 8e66 cf11 a6d9 00aa .. 内に(utf16)WM/AlbumTitle Year Genrue GenreID Track等有り。
・3&.u.f(ascii)ﾁｬﾝｸID x-3326 b275 8e66 cf11 a6d9 00aa .. 内に(utf16) ﾀｲﾄﾙ 参加ｱｰﾃｨｽﾄ ｺﾒﾝﾄ等有り。

(*1) 151129-151209バグフィックス＆関係記事メモ   Lilith CDﾘｯﾋﾟﾝｸﾞ直接wma変換→sansaでｱﾙﾊﾞﾑﾀｸ不表示の問題
①olps用wmac変換時0&ﾍｯﾀﾞ部(WM/albumTitle:albm WM/YearYear:9999 WM/Track:-)はolpsﾃﾝﾌﾟﾚｰﾄに交換され無効となる。②wmp12でCDﾘｯﾋﾟﾝｸﾞしたwavﾌｧｲﾙはSTEpとLilithに追加openできない。その他trackNo.曲順ﾀｸﾞの挙動不審等不詳。
よってLilithでCDﾘｯﾋﾟﾝｸﾞ時ﾀｸﾞ付け(ｱﾙﾊﾞﾑはwmac変換時無効)とwma(32kCBRﾘｻﾝﾌﾟﾘﾝｸﾞmono)変換し、olps用wmac変換とする。
ﾍｯﾀﾞﾀｸﾞ情報確認操作法 ①winﾌﾟﾛﾊﾟﾃｨでは通常IDﾀｸﾞのみ表示、wmp12のﾌﾟﾚｲﾋﾞｭｰ/ﾗｲﾌﾞﾗﾘ●画面下部のﾌｧｲﾙ>ﾌﾟﾛﾊﾟﾃｨ>ﾌｧｲﾙﾀﾌﾞに(ﾋﾞｯﾄﾚｰﾄ71kbps,ｺｰﾃﾞｯｸwma9.2,48kbps,44kHz,stereo,2-pass,VBR)表示。

●● 要debug Plan
(1) DSSPlayerｺﾒﾝﾄ部の連結用IFSとなってる"nul"->"sp"化 
(2) 0&ﾁﾍｯﾀﾞﾁｬﾝｸ内のｱﾙﾊﾞﾑその他ﾀｸﾞの復元 0&ﾁｬﾝｸ内WM/AlbumTitle部にﾊﾞｲﾄ数とあるばむ名が入ってる
(3) 0&ﾁｬﾝｸ8kB超 ｿｰｽFileﾍｯﾀﾞｻｲｽﾞ9kbの物がある
(4) 3&ﾁｬﾝｸ不存在時でもｴﾗｰとせず実行継続、ﾀｲﾄﾙ 参加ｱｰﾃｨｽﾄ ｺﾒﾝﾄの3ﾀｸﾞ全部含まない場合がある。
(5) wmc.cgi 合体化と操作法簡素化
(6) 変換結果のファイル名sjis要utf8化 <head><meta http-equiv=Content-Type content=text/html;charset=UTF-8></head>
(7) olmpsテンプレートファイルのｺｰﾃﾞｨﾝｸﾞは、ｶﾚﾝﾄﾜｰｷﾝｸﾞdirが./wmcの為 "../twma"となっとる、
( ) 
