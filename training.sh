#!/bin/bash

exp_id=$1
fullid=$(printf "%02d" ${exp_id})
echo configs/exp_${fullid}.json
python -m main \
    --to_train=1 \
    --log_dir=output/exp_${fullid}/ \
    --config_filename=configs/exp_${fullid}.json
