#!/bin/bash

python -m main \
    --to_train=0 \
    --log_dir=output/exp_06/ \
    --config_filename=configs/exp_06_test.json \
    --checkpoint_dir=output/exp_06/20171221-190923
