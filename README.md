# Jasterの特訓をするためのデータセットを生成するレポジトリです。
## エキスパートモデルの一つとして､「ガリ勉たぬき」を作ります｡

## setup
~~~
bash download.sh
~~~

## タスク生成
- [ひらがなを作るタスク](./hiragana.ipynb)
    - wikipediaの記事より自動生成
- [YES/NOを答えるタスク](./boolq.ipynb)
    - BoolQという英語のデータセットから生成
    - 120件くらいしか作っていないので､スコアが低い場合は､要拡充
        - データ自体は沢山あるが､自動翻訳なので品質チェックが必要
- [文章を読解して単語を答えるタスク](./dokkai.ipynb)
    - GoldPデータセットの日本語を使用
- [entailmentを答えるタスク](./entailment.ipynb)
    - JSNLIというデータセットを使用
        - JasterではJNLIを使用
        - JSNLIは自動翻訳なので､質が低いという理由で[JNLIを構築](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E8-4.pdf)したとのこと
- [仮説・前提などを答えるタスク](./kasetsu.ipynb)
    - [Textual Entailment 評価データ](https://nlp.ist.i.kyoto-u.ac.jp/?Textual+Entailment+%E8%A9%95%E4%BE%A1%E3%83%87%E3%83%BC%E3%82%BF)をもとに､適当に作りました｡
    - 件数も少ない上､カテゴリもあってるか不安です
- [Q&Aクイズ](./QandA.ipynb)
    - [JAQKET: クイズを題材にした日本語QAデータセット](https://www.nlp.ecei.tohoku.ac.jp/projects/jaqket/)から生成
- [算数の計算](./sansu.ipynb)
    - MGSMデータセットの日本語版(200件ほど)から生成
    - データ数が足りない場合は､適当な英語のデータセットを自動翻訳する

## TODO
- niilc: カンマ区切りでクイズに答える
    - 例
        - Q：日本の三大美林とは？
        - A: 青森ヒバ（青森県）,秋田スギ（秋田県）,木曽ヒノキ（長野県の木曾谷）
    - こまりごと:
        - 良いデータセットが見つからない

- wiki_dependency: かかり受け解析
    - 例
        - Q: ギタリストは、ギター演奏者の通称。ギタープレイヤーとも称される。
        - A: ギタリストは、 -> 通称。\nギター演奏者の -> 通称。\nギタープレイヤーとも -> 称される。
    - こまりごと:
        - GINZAとかで機械的に正解を作れそうだが､あまり詳しくない
- wiki_coreference: フレーズ抽出
    - 例
        - Q: ギタリストは、ギター演奏者の通称。ギタープレイヤーとも称される。
        - A: ギタリスト ギター演奏者 通称 ギタープレイヤー\nギター ギター
    - こまりごと:
        - LLMで答えを自動生成 or 類似データセットを探す
- wiki_pas: 述語項構造を全て抽出
    - 例
        - Q: ギタリストは、ギター演奏者の通称。ギタープレイヤーとも称される。
        - A: 通称 ガ：ギタリスト\n称される ガ：ギタリスト ト：ギタープレイヤー
    - こまりごと:
        - 問題の意味がわからない

- chabsa: 意味不明なので､評価指標から外れるかも

## 使ってはいけないデータセット
- LLM-jp-eval (= Jaster/JGLUE: trainも不可)
- JMT-Bench
- MMLU
- MT-Bench