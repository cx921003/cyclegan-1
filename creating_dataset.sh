#!/bin/bash

python -m create_cyclegan_dataset \
	--image_path_a ~/data/sketch2image/trainA \
	--image_path_b ~/data/sketch2image/trainB \
	--dataset_name="sketch2image_trainval_shuffled" \
	--do_shuffle=1

