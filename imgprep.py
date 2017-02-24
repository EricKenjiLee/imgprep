#!/usr/bin/env python3

'''
This is the "imgprep"-script for treating microscopy images.

It can read in multiple images of a sample slide [images].
Then it can also recognize a unicolor square in each, denoting the object of
interest, to crop the contents of the square. It can put the images next
to each other and insert custom scalebars based on magnification levels.

THIS SCRIPT IS STILL WORK IN PROGRESS!
'''

import argparse

import matplotlib.pyplot as plt

import sample


def main():
    # TODO: Outsource the parser setup into it's own function
    # Create the argparser
    parser = argparse.ArgumentParser(usage=__doc__)

    # Sample-name: Mandatory
    parser.add_argument('sample',
                        help='The name of the sample to be treated.')

    # Load images?
    parser.add_argument('images', nargs='+',
                        help='Filenames of images associated to the sample.')

    # Crop?
    parser.add_argument('-c', '--crop', action='store_true',
                        help='Crop the image to the size of painted-in squares')

    # Show images?
    parser.add_argument('-s', '--show', action='store_true',
                        help='Show the imported images. Only use in con-'\
                        'junction with -i.')

    # Verbosity?
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Add verbosity. Prints more info on the screen.')

    args = parser.parse_args()

#   ----------------------------------------------------------------------------

    # Generating a specimen
    if args.verbose:
        print('Generating a new sample named "{}"'.format(args.sample))
        print('Starting the script with options:\n{}'.format(args))
    specimen = sample.Sample(sample_name=args.sample)

    # Loading image pathes
    if args.verbose:
        print('Loading the specified images.')
    specimen.image_pathes = args.images
    specimen.load_images()

#   ----------------------------------------------------------------------------

    # Cropping
    if args.crop:
        if args.verbose:
            print('Starting the cropping process.')
            print('Detecting the square.')
        # Square detection
        for image in specimen.images:
            specimen.square_detect()

        # Cropping
        if args.verbose:
            print('Cropping the images.')
        for image in specimen.images:
            specimen.crop()

    # Showing the raw images
    if args.show:
        if args.verbose:
            print('Showing the raw images.')
        for image in specimen.images:
            plt.imshow(image)
            plt.show()


if __name__ == "__main__":
    main()
