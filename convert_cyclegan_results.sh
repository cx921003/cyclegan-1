#!/bin/bash
set -e  # Exit on error.

nsample=100

out_fp=$1

expID=06

if [ -e ${out_fp} ]; then
    echo "Output folder exists: ${out_fp}. Please pick a non-existing folder." >&2
    exit 1
fi

mkdir ${out_fp}/images -p
# convert CycleGAN output too clothNet format
for sample_idx in $(seq 0 $((${nsample}-1))); do
    fullid=$(printf "%04d" ${sample_idx})
    convert output/exp_${expID}/samples/imgs/fakeA_0_${sample_idx}.jpg ${out_fp}/images/${fullid}_outputs.png
    convert output/exp_${expID}/samples/imgs/inputA_0_${sample_idx}.jpg ${out_fp}/images/${fullid}_inputs.png
    convert output/exp_${expID}/samples/imgs/inputB_0_${sample_idx}.jpg ${out_fp}/images/${fullid}_targets.png
done

echo Generating HTML...
./generate_index.py ${out_fp}/images
echo Done.

