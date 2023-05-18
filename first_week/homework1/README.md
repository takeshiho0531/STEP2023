# week1 homework1

## [wip] 問題

## 実行方法
以下を実行して、`http://127.0.0.1:8000/docs`を開くとSwagger UIの画面が開く。
```
$STEP2023  uvicorn first_week.homework1.api:router --reload
```
queryの部分にanagramか判定したい単語を入力してrequestすると、anagramだった時は並べ替えた際のvalid wordが返ってきて、anagramでない時は"your word is not an anagram!"と返ってくる

## ファイル構成
```
.
├── README.md
├── __init__.py
|
├── anagram.py
├── api.py
├── save_dict.py: これを実行するとsorted_words.txtができる
|
├── words.txt
├── sorted_words.txt: words.txt内の単語を(元の単語をアルファベット順に並べた文字列, 元の単語)の組にして、さらにアルファベット順の文字列同士を比較してアルファベット順に並べたもの
|
└── tests
    ├── __init__.py
    └── test_anagram.py

```

## [wip]アルゴリズム
1. まず辞書(`words.txt`)内の単語を(元の単語をアルファベット順に並べた文字列, 元の単語)の組にする。<br>
さらにそのセット同士を、[元の単語をアルファベット順に並べた文字列]の方で比較してアルファベット順になるように並べる。<br>
その結果が`sorted_words.txt`で、`save_dict.py`を実行することで得られる<br>
```
$STEP2023  python3 first_week/homework1/save_dict.py
```

2. まずanagramか判定したい単語もアルファベット順に並べる。<br>
その文字列が、`sorted_words.txt`に格納されている[元の単語をアルファベット順に並べた文字列]の中に存在すればよい。<br>
存在するかについては二分探索している。(そのために1.で[元の単語をアルファベット順に並べた文字列]同士をさらにアルファベット順に並べた。)

## 備考
- アナグラム複数のものに対応していなかったことに今気がついた(24.5.18.22.15)