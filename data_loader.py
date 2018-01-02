import tensorflow as tf

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import model


def _load_samples(csv_name):
    filename_queue = tf.train.string_input_producer(
        [csv_name])

    reader = tf.TextLineReader()
    _, csv_filename = reader.read(filename_queue)

    record_defaults = [tf.constant([], dtype=tf.string),
                       tf.constant([], dtype=tf.string)]

    filename_i, filename_j = tf.decode_csv(
        csv_filename, record_defaults=record_defaults)

    file_contents_i = tf.read_file(filename_i)
    file_contents_j = tf.read_file(filename_j)

    # TODO: make it cleaner. decode_png also works for jpeg.
    image_decoded_A = tf.image.decode_png(
            file_contents_i, channels=model.IMG_CHANNELS)
    image_decoded_B = tf.image.decode_png(
            file_contents_j, channels=model.IMG_CHANNELS)

    # if '.jpg' in filename_i:
    #     image_decoded_A = tf.image.decode_jpeg(
    #         file_contents_i, channels=model.IMG_CHANNELS)
    # elif '.png' in filename_i:
    #     image_decoded_A = tf.image.decode_png(
    #         file_contents_i, channels=model.IMG_CHANNELS, dtype=tf.uint8)
    #
    # if '.jpg' in filename_j:
    #     image_decoded_B = tf.image.decode_jpeg(
    #         file_contents_j, channels=model.IMG_CHANNELS)
    # elif '.png' in filename_j:
    #     image_decoded_B = tf.image.decode_png(
    #         file_contents_j, channels=model.IMG_CHANNELS, dtype=tf.uint8)

    return image_decoded_A, image_decoded_B, filename_i, filename_j


def load_data(csv_name, image_size_before_crop,
              do_shuffle=True, do_flipping=False):
    """

    :param dataset_name: The name of the dataset.
    :param image_size_before_crop: Resize to this size before random cropping.
    :param do_shuffle: Shuffle switch.
    :param do_flipping: Flip switch.
    :return:
    """
    # if dataset_name not in cyclegan_datasets.DATASET_TO_SIZES:
    #     raise ValueError('split name %s was not recognized.'
    #                      % dataset_name)

    image_i, image_j, _, _ = _load_samples(
        csv_name)
    inputs = {
        'image_i': image_i,
        'image_j': image_j
    }

    # Preprocessing:
    inputs['image_i'] = tf.image.resize_images(
        inputs['image_i'], [image_size_before_crop, image_size_before_crop])
    inputs['image_j'] = tf.image.resize_images(
        inputs['image_j'], [image_size_before_crop, image_size_before_crop])

    if do_flipping is True:
        inputs['image_i'] = tf.image.random_flip_left_right(inputs['image_i'])
        inputs['image_j'] = tf.image.random_flip_left_right(inputs['image_j'])

    inputs['image_i'] = tf.random_crop(
        inputs['image_i'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3])
    inputs['image_j'] = tf.random_crop(
        inputs['image_j'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3])

    inputs['image_i'] = tf.subtract(tf.div(inputs['image_i'], 127.5), 1)
    inputs['image_j'] = tf.subtract(tf.div(inputs['image_j'], 127.5), 1)

    # Batch
    # TODO: fix the problem of train.batch skip files
    # if do_shuffle is True:
    #     inputs['images_i'], inputs['images_j'] = tf.train.shuffle_batch(
    #         [inputs['image_i'], inputs['image_j']], 1, 5000, 100)
    # else:
    #     inputs['images_i'], inputs['images_j'] = tf.train.batch(
    #         [inputs['image_i'], inputs['image_j']], 1)

    inputs['images_i'] = tf.expand_dims(inputs['image_i'], 0)
    inputs['images_j'] = tf.expand_dims(inputs['image_j'], 0)

    return inputs

def load_data_test(csv_name, image_size_before_crop,
              do_shuffle=True, do_flipping=False):
    """

    :param dataset_name: The name of the dataset.
    :param image_size_before_crop: Resize to this size before random cropping.
    :param do_shuffle: Shuffle switch.
    :param do_flipping: Flip switch.
    :return:
    """
    # if dataset_name not in cyclegan_datasets.DATASET_TO_SIZES:
    #     raise ValueError('split name %s was not recognized.'
    #                      % dataset_name)

    image_i, image_j, name_i, name_j = _load_samples(
        csv_name)
    print name_i
    inputs = {
        'image_i': image_i,
        'image_j': image_j,
        'name_i': name_i,
        'name_j': name_j,
    }

    # Preprocessing:
    inputs['image_i'] = tf.image.resize_images(
        inputs['image_i'], [image_size_before_crop, image_size_before_crop])
    inputs['image_j'] = tf.image.resize_images(
        inputs['image_j'], [image_size_before_crop, image_size_before_crop])

    if do_flipping is True:
        inputs['image_i'] = tf.image.random_flip_left_right(inputs['image_i'])
        inputs['image_j'] = tf.image.random_flip_left_right(inputs['image_j'])

    inputs['image_i'] = tf.random_crop(
        inputs['image_i'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3])
    inputs['image_j'] = tf.random_crop(
        inputs['image_j'], [model.IMG_HEIGHT, model.IMG_WIDTH, 3])

    inputs['image_i'] = tf.subtract(tf.div(inputs['image_i'], 127.5), 1)
    inputs['image_j'] = tf.subtract(tf.div(inputs['image_j'], 127.5), 1)

    inputs['images_i'] = tf.expand_dims(inputs['image_i'], 0)
    inputs['images_j'] = tf.expand_dims(inputs['image_j'], 0)
    inputs['names_i'] = tf.expand_dims(inputs['name_i'], 0)
    inputs['names_j'] = tf.expand_dims(inputs['name_j'], 0)

    return inputs
