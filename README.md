# texgraph
\LaTeXにより，データファイルからグラフを描画するマクロパッケージ

\LaTeX上のコマンドでグラフ作成と装飾の設定が完結する。

**注意**　浮動小数点数の数値計算を一部pythonに行わせているため，pythonの導入とtypeset時に--shell-escapeを必要とする。

## 導入方法
1. このリポジトリをclone or download
2. texgraph.sty, tgepspreamble.styを./texmf/tex/latex/texgraphに配置（ここに限らずtexmfツリーの適当な場所で好い）。
他のファイルはなくても動作に影響しない
3. (必要ならば)mktexlsrを叩く
4. Enjoy!

## 使用方法
texgraph/doc/texgraph-doc.pdfをご覧ください。
