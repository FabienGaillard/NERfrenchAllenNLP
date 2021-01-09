echo 'Creating dataset ...'
cd data/source/
python3 more_exs.py
cd ../..
echo '... Dataset successfully created'
cat data/source/addons_train/*.txt data/source/source_train.txt > data/train.txt
echo 'Train set built'
cat data/source/addons_validation/*.txt data/source/source_validation.txt > data/validation.txt
echo 'Validation set built'

if [ "$#" -eq  "0" ]
  then
    echo "No arguments supplied -- Training & Predicting"
    echo 'Training begins ...'
    allennlp train -f --include-package tagging -s /tmp/tagging/lstm configs/train_lstm.jsonnet
    echo 'Training complete'
else
    echo "Argument supplied -- Just predicting ..."
fi
echo 'Predicting ...'
bash pred.sh
echo 'Prediction result > prediction.json (raw data), predics.txt'
