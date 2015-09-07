installed tk2aym2(42, xrehbr112    (tk2nan旧ver060517wmac.cgi tk2hbr112NG)
wmac2.cgi ﾌｫﾙﾀﾞ cb/wmc (src multi Files, dst		(●● don't use wmac.cgi)
wmc.cgi   ﾌｫﾙﾀﾞ cb/wmc (src multi folders, dst
depend on lib cb/Unicode/Japanese.pm、olmpsテンプレートファイル./twma(ｺｰﾃﾞｨﾝｸﾞは../twma)

wmac変換操作法：wmac変換後、wmaﾀｸﾞ再編集とolympusｺﾒﾝﾄ再編集が必須(*1)●。 (改150908)
                (補足) wav生成、wav-wma変換、CDﾘｯﾋﾟﾝｸﾞ直接wma変換等の問題は特に無し。
                (補足2) olympusｺﾒﾝﾄ部分内の x00 nulｺｰﾄﾞをx20 SPにﾊﾞｲﾅﾘ変換すればolympusｺﾒﾝﾄの復元可。
  (*1)wmac詳細：wmaﾀｸﾞ(title artist comment)維持、(albun trackNo 年号)消去、ジャンル0化あり。
        olympusｺﾒﾝﾄ生成は複数のwmaﾀｸﾞの内最初の1個(通常title)のみ、wmaﾀｸﾞ無ければolpsｺﾒﾝﾄ生成も無し。
        
wmac Olympusファイルヘッダ変換仕様：
3行以上のコピペでIEエラー???-> evernoteに残置 -> 再起動事後やり直し

dbgPlan：
olpsコメントタグ生成時nullが入るとDS-10やdssPlayerでolpsコメントが表示されない
wmc.cgi 合体化と操作法簡素化
変換結果のファイル名sjis要utf8化 <head><meta http-equiv=Content-Type content=text/html;charset=UTF-8></head> 当面の措置 IE11>表示>エンコード> でコードutf8化に加えて更新も実行される。

コード解析：olmpsテンプレートファイルのｺｰﾃﾞｨﾝｸﾞは、ｶﾚﾝﾄﾜｰｷﾝdirが./wmcの為 "../twma"
            エラー処理 olmps_idヘッダ "O.L.M.P."が無い場合(olps-F) no cnvtスキップ、
            no chk-idkeyで中断 ???
            
(注)FTP ﾃﾞｨｽｸｸｵｰﾀecceededでupld不可、要大容量サイト使用 xreｸｵｰﾀ1Gb(s600以前は50MB)。
