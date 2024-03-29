#Q&A dataset
#データソースはCC４ライセンス
#https://www.nlp.ecei.tohoku.ac.jp/projects/jaqket/
cd data
mkdir jsonl
wget https://jaqket.s3.ap-northeast-1.amazonaws.com/data/aio_01/train_questions.json

wget http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/rte/entail_evaluation_set.txt&name=entail_evaluation_set.txt