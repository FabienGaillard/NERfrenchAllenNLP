export OUTPUT_FILE=predictions_raw.json

allennlp predict \
  --output-file $OUTPUT_FILE \
  --include-package tagging \
  --predictor enp_fr_predictor \
  --use-dataset-reader \
  --silent \
  /tmp/tagging/lstm/ \
  data/pred.txt
