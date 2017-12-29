#!/bin/bash

python -m create_cyclegan_dataset \
	--image_path_a ~/data/sketch2image/testA \
	--image_path_b ~/data/sketch2image/testB \
	--output_path ~/workspace/cyclegan-1/input/sketch2image/sketch2image_test_unshuffled.csv \
	--do_shuffle=0
#	--dataset_name="sketch2image_nonvis_unshuffled" \


#python -m create_cyclegan_dataset \
#	--image_path_a ~/data/sketch2image_simplified/trainA \
#	--image_path_b ~/data/sketch2image_simplified/trainB \
#	--output_path ~/workspace/cyclegan-1/input/sketch2image_simplified/sketch2image_simplified_shuffled.csv \
#	--do_shuffle=1
#	--dataset_name="facades_train" \


#python -m create_cyclegan_dataset \
#        --image_path_a ~/data/cityscapes/trainA \
#        --image_path_b ~/data/cityscapes/trainB \
#        --dataset_name="cityscapes_train" \
#        --do_shuffle=1

