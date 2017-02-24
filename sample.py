'''
The sampe class for the imgprep script. One object of this class contains
three images of the sample. It also defines the methods used to process
the images.
'''

import skimage
import skimage.io


class Sample(object):

    def __init__(self, sample_name):
        '''
        Creates instances of the Sample class.
        '''

        self.name = sample_name

        self.image_pathes = []
        self.images = []

    def crop(self):
        '''
        Crops the image(s) to the square that was detected. Use only after
        square_detect() or it has no effect.
        '''
        pass

    def load_images(self):
        '''
        Loads microscope images of the sample as numpy arrays and saves the
        image metadata. Make sure to have filenames and image_pathes set so
        load the images.
        '''
        self.image_count = len(self.image_pathes)
        self.images = [None] * self.image_count

        if self.image_count > 1:
            self.images = skimage.io.imread_collection(self.image_pathes)
        else:
            self.images = skimage.io.imread(str(self.image_pathes))

        self.images = skimage.img_as_float(self.images)
        # TODO: Save metadata
        # TODO: Maybe rotate the second polarized image by -45°

    def square_detect(self, which='all'):
        '''
        Detect a drawn square in the microscope images for later cropping.
        '''
        if which != 'all':
            pass
        else:
            for image in self.images:
                break
        # Copypasted, functionality not guaranteed
        # cols = (image[..., 0] == 255).sum(0)
        # left = cols.argsort()[-2:].min()
        # right = cols.argsort()[-2:].max()
        pass

    # TODO: Recognize the Magnification and calculate scale-bar dimensions
    # TODO: Recognize the Red square coordinates
    # TODO: Crop the images and place them next to each other
    # TODO: Create three scale-bars and insert them into the images
