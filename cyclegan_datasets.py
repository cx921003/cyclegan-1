"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    #'horse2zebra_train': 1334,
    #'horse2zebra_test': 140
    'sketch2image_train': 23000
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    #'horse2zebra_train': '.jpg',
    #'horse2zebra_test': '.jpg',
    'sketch2image_train': '.png'
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    #'horse2zebra_train': './input/horse2zebra/horse2zebra_train.csv',
    #'horse2zebra_test': './input/horse2zebra/horse2zebra_test.csv',
    'sketch2image_train': './input/sketch2image/sketch2image_train.csv'
}
