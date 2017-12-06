-------------------
171206 WMAタグ変換 総括まとめ (●要参照 ma:evernote,sb:github/wmac/wmcReadme他)
  Olympus DS-10専用コメントを書けるようにする
①orgnlファイルのタグ タイトル(タグは1個のみ必須)のみとし他(artist,album,trkNo,date,junre等)はできるだけ全て消去、
  Winﾌﾟﾛﾊﾟﾃｨ,STEP,Bz184等で確認
②lilithファイル変換操作：WinMediaAudio V9.2 CBR 32K mono タグを無視
③cb/wma/にファイルupld、cb/wmac2.cgi実行(171204現在 tk243aym2 #061208版のみ実装 TOK)、
  (複数フォルダ一括変換時cb/wmcs/にファイルupld、cb/wmc.cgi実行、cb/wmcd/に変換結果ファイル生成 詳細cb/wmc.cgi要参照)
④olpsDSSplayerでのｺﾒﾝﾄ編集で異体字は??となり使えない(F構造上はS-JIS扱いとなっとる)
  sansa e120 でalbumタグ表示(no album表示となる対策)
①albumに異体字が入るとno albumとなる、(できればTrkNo.全て消去(Winﾌﾟﾛﾊﾟﾃｨ,STEp,lilithの全てで))
②title,artistに異体字使用可、Winﾌﾟﾛﾊﾟﾃｨで操作する
③STEpで異体字操作してもタグ更新で□?に文字化け、ファイル名も同様。必要部分のみWinﾌﾟﾛﾊﾟﾃｨで修正操作、
④STEpでTrkNo.等操作しタグ更新するとファイルヘッダが大きくなってしまう??
---------------------- 
141111 標準wmaファイルを Olympus Voice Trek DS-10用フォーマット変換仕様 操作法

・wavからwma変換：Project9k_lilith0.991b リサンプリング(int16,mono-ch,44.1k,quality3)、WinMediaAudioV9.1(CBR,32Kbbs)
・タグ編集      ：STEPver1.03(*1)
    1個以上のタグ必須。(*2)
    track(title)、artist、album、coemntの4項目編集可、但しOlympusでは最初の1個のタグのみ表示。(*3)
    全項目編集し後改めてOlympusのｺﾒﾝﾄ編集で修正するか、又はtrack(title)かcoemntのみとする。(*4)
    ﾌｧｲﾙ名はOlympusDS-10端末へ転送時8ﾊﾞｲﾄ(何とか~1.wma)に縮小され、ﾘﾓｰﾄへ再度戻しても8ﾊﾞｲﾄのまま。
・OlympusDS-10ﾌｫｰﾏｯﾄ変換：wmc.cgi,wmac2.cgi,wmcReadme(yymmdd).txt(メインxre~hbr、コピー(tk2~hbr evernote github)。
　　(1)複数ﾌｧｲﾙ処理 ：cb/wmc/にｿｰｽwmaFileを置き、wmac2.cgi実行、      結果は同名のwmaFileに、ｿｰｽﾌｧｲﾙは消去。
　　(2)複数ﾌｫﾙﾀﾞ処理：cb/wmcs/にﾌｫﾙﾀﾞ付ｿｰｽwmaFileを置き、wmc.cgi実行、結果はcb/wmacdにﾌｫﾙﾀﾞ付wmaFileで、
      ﾌｫﾙﾀﾞ付ソースは残置

(*1) audacityでmono,CBR32k化可能なるもタグ編集不良(タグがダブる 消える 日本語使用でFileが壊れる等々)、wmc(wmac)変換ヘッダーがOlympus DS-10用に合わない。
(*2) 全タグ無しでは、wmacタグ変換時チャンクIDkey"3&ｲu伺ﾏｦ…"missingエラー、その時点で処理中止。
(*3) wmacタグ変換は[nul]文字セパレータでtrk[nul]artist[nul]album[nul]cmntの連結でolympsコメント部にsjisで記録、
    但しolympusタグ表示はﾘﾓｰﾄ端末共初めのtrkタグの後の[nul]で表示が止まってしまう。
 　  初めのtrk表示のみで使用も可、但しtrkタグ表示のみからﾘﾓｰﾄ又は端末でコメント編集するとセパレータ含め全て書き換わってしまう。
　   ﾌｧｲﾙｻｲｽﾞを変えないようﾊﾞｲﾅﾘｴﾃﾞｨﾀ上書きで[nul]文字をsjisに書換ると既存のタグが復活する。
(**) bugFixpending
     *2)のタグ用チャンクIDkey"3&ｲu伺ﾏｦ…"missingエラー処理中止、をエラースキップして以降の処理継続させ終了。
     *3)のタグ変換時[nul]文字セパレータ除去修正。
     wmac2.cgi→wmac.cgi正規化の為名前変更。
-----------------------------------------------------------------------------------------
141107 OLYMPUSヘッダー化 project9k_lilith STEPタグエディタ wmac2.cgi(メイン最新_xre~hbr) 変換仕様 
　　１ ilithのwav-wma変換はlilith wav-wma変換 ﾘｻﾝﾌﾟﾘﾝｸﾞ(mono int16 blackman 44100 quality=3) CBR 32kcb。
　　　同時タグ編集はwav既存タグの継承のみで編集追加共に不可。
　　２ STEPタグエディタ編集時comentタグ必須、如何なるタグ追加編集しても可。lilithのヘッダーは温存。
　　３ wmac2変換は、comentタグが無いとチャンクIDkey"3&ｲu伺ﾏｦ…"missingエラー、その時点で処理中止、以降
　　　の処理も行われない。comentタグが存在すれば複数ファイル処理可。
　　　タイトル(トラック)名、アーティスト名、コメントが存在すればこの順に連結されてolpsヘッダーのコメン
　　　トとなる。
　　５ 日時は？ 再生所要時間のみ時分秒に変換OLYMPUSヘッダー書込。

    ◎wmc.cgi仕様 cb/wmcs 内の元wmaFile変換　1回1ホルダのみwmac2.cgiで処理、結果cb/wmcdに格納、子ホルダは非処理のまま移送。
     cb/wmcs無くばcb/wmcを使ってる模様？？
-----------------------------------------------------------------------------------------
その他のFile変換ソフト機能
・  ilith仕様 リサンプリング有り 。
・  Audacity仕様 トラック＞ステレオからモノラルへ可、wma書出optionは(24k 32k 48k … 329k)のみ(44.1kHz変換、CBR/VBR選択不可)。
   メタ(TAG)データ編集可なるも書出してくれない？。
・　Rip!AudiCO仕様 CDリッピング WMA変換 stereo/mono bitrate sampleRate normalize 詳細？ シェアウェア@3112円14日間可、
   Free版は同時処理アイテム登録数5まで

----------------------------------------------------
141000 wmac.cgi設置状況
tk2~aym 無し
tk2~hbr twma(61130 wmac.cgi(------ wmac2.cgi(061201 wmc.cgi(------  wmcReadne.txt(130219  cb/wmc(有	●コピー
tk2~nan twma(60519 wmac.cgi(060519 wmac2.cgi(------ wmc.cgi(------  wmcReadne.txt(130219  cb/wmc(---- cb/wmcd(有 cb/wmcd(有 cb/wm*(残骸有
tk2~h100無し 但しhttp://www42.tok2.com/home/h100/ txt htm jpg等webDav可。ftp不可、cgi存在するも動作不可(mode不詳)。
tk2~hbr(s32 不可

xre~han twma(----- wmac.cgi(060119 wmac2.cgi(------                  cb/wmc(------         
xre~hbr twma(60212 wmac.cgi(060517 wmac2.cgi(061208 wmc.cgi(061130  wmcReadne.txt(130219  cb/wmc(有	●メイン

----130115 再利用時--------
tk2aym tmp -
tk2nan tmp twma060519 wmac.cgi060519
tk2hbr wmc wmcd wmcs twma061130● wmac2.cgi061201 wmc.cgi061201●
wmc.cgi061201 # 061130 061129 061127create
tk2h10 - -
tk2s32hbr接続不可
xrehan tmp wmac.cgi060119
xrehbr   tmp tmp2 twma060212 wmac.cgi060517 wmac2.cgi061208● wmc.cgi061130
wmac2.cgi061208 # 061208 title,author(artist),description(comment)一括変換、拡張チャンクのalbum,year,genre,trck等は未了
xre292 -
xre335ssg接続不可
xres89335 -
-------------------------------------------------------------------------------------------------------
Asfファイルフォーマット参考資料
●ASF ファイルの基本構造 → http://akabeko.me/blog/memo/asf/ http://akabeko.me/blog/memo/asf/objects/
   ASFファイル構造 property object＞タイトルproperty object＞
   識別子 &3...16bytes 0x3326b2758e66cf11a6d900aa0062ce6c タイトル著者著作権説明規制等

HeaderObject GUIDs＞Content Description Object GUID 75B22633-668E-11CF-A6D9-0AA0062CE6C
バイナリダンプ：33 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C 
名前  型   型 サイズ 内容
Object ID GUID Guid 16 75B22633-668E-11CF-A6D9-00AA0062CE6C
Object Size QWORD UInt64 8 オブジェクト全体のサイズ
Title Length WORD UInt16 2 タイトルのバイト数
Author Length WORD UInt16 2 アーティスト名のバイト数
CopyrightLength WORD UInt16 2 著作権情報タイトルのバイト数
DescriptionLength WORD UInt16 2 コメントのバイト数
Rating Length WORD UInt16 2 レーティング ( 保護者による制限 ) のバイト数
Title  WCHAR char * タイトル
Author  WCHAR char * アーティスト名
Copyright WCHAR char * 著作権情報
Description WCHAR char * コメント
Rating  WCHAR char * レーティング ( 保護者による制限 )

コンテンツの基本的なメタデータ、言語非依存で、常にデータ領域が確保されるよう、WMP11の拡張タグエディタで、コメントを言語別にいくつか書いてみたところ、このオブジェクトの Description Lengthは 0、Description は空となり、代りに Metadata Library Object へ言語別に登録されていた。多言語・多ストリームにきちんと対応しているメタデータエディタは少なく、Windows Media Player ですら一部のタグしか対応できていない。一方、ASF や WMA に対応しているアプリケーションなら、大概はこのオブジェクトに書かれるデータに対応していると思われる。

●Asfファイルフォーマット----http://uguisu.skr.jp/Windows/format_asf.html抜粋
Top-level ASF object GUIDs
ASF Header Object    0&  30 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C
ASF Data Object      6&  36 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C
header obj GUID
ASF Header Extension Object  B5 03 BF 5F 2E A9 CF 11 8E E3 00 C0 0C 20 53 65
ASF Codec List Object        40 52 D1 86 1D 31 D0 11 A3 A4 00 A0 C9 03 48 F6

●本家Windows Media フォーマット 9 シリーズ SDK を使った Windows Media サポート → http://www.microsoft.com/japan/windows/windowsmedia/howto/articles/AddingSupport.aspx



