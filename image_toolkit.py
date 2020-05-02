from PIL import Image
import os
import sys


class Image_stuff:
    def __init__(self, input_path, output_path, img_type='.png'):
        self.input_path = input_path
        self.output_path = output_path
        self.img_type = img_type
        self.image_dirs = self._image_dirs()
        self.file_names = self._image_names()

    def _image_dirs(self):
        return [
            str(self.input_path) + '/' + file for file in os.listdir(self.input_path)]

    def _image_names(self):
        return [file.strip(self.img_type) for file in os.listdir(self.input_path)]

    def _greyscale(self):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image).convert('LA')
            img.save(str(self.output_path) + '/' +
                     '{0}_greyscale{1}'.format(self.file_names[c], self.img_type))

    def _resize_symmetric(self, scale):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image)
            img = img.resize((scale, scale), Image.ANTIALIAS)
            img.save(str(self.output_path) + '/' +
                     '{0}_rescaled_sym{1}'.format(self.file_names[c], self.img_type))

    def _resize_proportionally(self, width):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image)
            wpercent = (width/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((width, hsize), Image.ANTIALIAS)
            img.save(str(self.output_path) + '/' +
                     '{0}_rescaled{1}'.format(self.file_names[c], self.img_type))

    def _mirror(self):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image).transpose(Image.FLIP_LEFT_RIGHT)
            img.save(str(self.output_path) + '/' +
                     '{0}_mirrored{1}'.format(self.file_names[c], self.img_type))


if __name__ == "__main__":

    in_path = str(sys.argv[1])
    out_path = str(sys.argv[2])
    type_ = str(sys.argv[3])
    init = Image_stuff(input_path=in_path, output_path=out_path)

    if type_ == 'resize_sym':
        init._resize_symmetric(28)

    elif type_ == 'resize_prop':
        init._resize_proportionally(28)

    elif type_ == 'mirror':
        init._mirror()

    elif type_ == 'gray':
        init._greyscale()

    else:
        print('Incorrect type\nTry:\nresize_sym,resize_prop,mirror,gray')
