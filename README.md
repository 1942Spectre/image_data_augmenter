# image_data_augmenter

I created those functions because the image data generator in keras was slowing down the training process to much by using the gpu for augmenting. This way , the augmentation is done in the beginning by cpu and the image data is stored in the RAM. This makes GPU to just work on training so makes it faster. If you have lots of RAM , I think its better doing it this way.
