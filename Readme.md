edit 複数行コピペするとブラウザクラッシュするためtemporely生成
wmac変換操作法(改150908)：
  wmaｿｰｽは、WMA9,CBR,32Kb,mono、最低限wmaﾀｸﾞ1個を含むこと。
  wmac変換後、wmaﾀｸﾞ再編集とolympusｺﾒﾝﾄ再編集が必須(*1)●。
    (補足1) wav生成、wav-wma変換、CDﾘｯﾋﾟﾝｸﾞ直接wma変換等の問題は特に無し。
    (補足2) olympusｺﾒﾝﾄ部分内の x00 nulｺｰﾄﾞをx20 SPにﾊﾞｲﾅﾘ変換すればolympusｺﾒﾝﾄの復元可。
  (*1)wmac詳細：wmaﾀｸﾞ(title artist comment)維持、(albun trackNo 年号)消去、但しジャンル0化あり。
                olympusｺﾒﾝﾄ生成は複数のwmaﾀｸﾞの内最初の1個(通常title)のみ、wmaﾀｸﾞ無ければolpsｺﾒﾝﾄ生成も無し。

  (* )wmac Olympusファイルヘッダ変換仕様-詳細：
     wmaﾀｸﾞ(title artist comment)維持、(albun trackNo 年号)消去、ジャンル0化あり。
     olympusｺﾒﾝﾄ生成は複数のwmaﾀｸﾞの内最初の1個(通常title)のみ、wmaﾀｸﾞ無ければolpsｺﾒﾝﾄ生成も無し。
----------------------------------------------------------------------------------
Olympus DSSPlayer(DS-10用)仕様：DSSPlayer→DS-10ｱｯﾌﾟﾛｰﾄﾞ転送時8ﾊﾞｲﾄ以上のﾌｧｲﾙ名は××～1.wmaに変換、更にdwldしても復元せず。
sansa-e120仕様：                title/track名のタグ無い場合 曲名にファイル名が表示される
------------------------------------------------------------------------------------


