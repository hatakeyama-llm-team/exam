# 文法理解のための特訓データセット作成

## 主に、Jasterベンチマークを想定して、Zero-shot推論能力を向上させるためのデータセットを生成するレポジトリです。
# setup
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

## 未対応のデータ
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
- wiki_coreference: フレーズ抽出
    - 例
        - Q: ギタリストは、ギター演奏者の通称。ギタープレイヤーとも称される。
        - A: ギタリスト ギター演奏者 通称 ギタープレイヤー\nギター ギター
- wiki_pas: 述語項構造を全て抽出
    - 例
        - Q: ギタリストは、ギター演奏者の通称。ギタープレイヤーとも称される。
        - A: 通称 ガ：ギタリスト\n称される ガ：ギタリスト ト：ギタープレイヤー
- wiki_ner: 固有表現の抽出
    - 例
        - Q: オーストラリア・ドル（英語:　Australian　Dollar）は、オーストラリア連邦で用いられる通貨の名称である。通貨コードはAUDであり、A$、豪ドルなどと称する。なお、オーストラリア領土以外では、ポリネシアのナウル・ツバル・キリバスでも用いられている。
        - A: オーストラリア（地名） オーストラリア連邦（地名） 豪（地名） オーストラリア（地名） ナウル（地名） ツバル（地名） キリバス（地名）


## 使っていないデータセット
- LLM-jp-eval 
- JMT-Bench
- MMLU
- MT-Bench

# upload
~~~
huggingface-cli upload --repo-type=dataset (データセット名) ./jsonl
~~~
=======


