# week1 homework2

## [wip] 問題

## 実行方法
以下を実行すると、各テキストファイル(`large.txt`, `medium.txt`, `small.txt` )の単語の合計スコアが返ってくる。
```
$STEP2023  python3 first_week/homework2/score_checker.py first_week/homework2/small.txt
```

## ファイル構成
```
.
├── README.md
├── __init__.py
|
├── save_sorted_dictionary.py: これを実行するとscore順にsortされた辞書(`sorted_by_score_words.txt`)ができる
├── score_checker.py: これを上記のように実行するとscoreが返ってくる
|
├── words.txt: 辞書
├── sorted_by_score_words.txt: score順にsortされた辞書
|
├── large.txt
├── medium.txt
└── small.txt
```

## [wip]アルゴリズム
1. まず辞書(`words.txt`)の中身をスコア順にsortしなおす<br>
その結果が`sorted_by_score_words.txt`<br>
※ これは`large.txt`でスコア算出をする際に処理が遅すぎたため追加した

2. テキストファイル内(`large.txt`, `medium.txt`, `small.txt` etc.)内の各単語に対して、スコア順にsortされた辞書`sorted_by_score_words.txt`の上からanagramが作れないかを探索して、見つかったらそこで処理を終了する<br>
anagramが作れるかの判定は与えられたものをそのまま使っていて、辞書内の単語とanagramが作れるか判定したい単語に対して、各アルファベットが何回登場するかを初めにカウントしておいて、同じindexのものを引き算したときに0未満にならないかで判定している。

## 備考
- 現時点で`large.txt`のスコアは15sくらいで返ってくる
