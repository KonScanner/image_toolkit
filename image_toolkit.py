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

    def _save_image(self, counter: int, image_object, transformation: str = 'None'):
        image_object.save(str(self.output_path) + '/' +
                          '{0}{1}{2}'.format(self.file_names[counter], transformation, self.img_type))

    def _greyscale(self):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image).convert('LA')
            self._save_image(counter=c, image_object=img,
                             transformation=f'{self._greyscale.__name__}')

    def _resize_symmetric(self, scale):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image)
            img = img.resize((scale, scale), Image.ANTIALIAS)
            self._save_image(counter=c, image_object=img,
                             transformation=f'{self._resize_symmetric.__name__}')

    def _resize_proportionally(self, width):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image)
            wpercent = (width/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((width, hsize), Image.ANTIALIAS)
            self._save_image(counter=c, image_object=img,
                             transformation=f'{self._resize_proportionally.__name__}')

    def _mirror(self):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image).transpose(Image.FLIP_LEFT_RIGHT)
            self._save_image(counter=c, image_object=img,
                             transformation=f'{self._mirror.__name__}')

    def _rotate(self, degrees):
        for c, image in enumerate(self.image_dirs):
            img = Image.open(image).rotate(degrees)
            self._save_image(counter=c, image_object=img,
                             transformation=f'{self._rotate.__name__}')


if __name__ == "__main__":

    in_path = str(sys.argv[1])
    out_path = str(sys.argv[2])
    type_ = str(sys.argv[3])
    img_type = str(input('png or jpg: '))
    init = Image_stuff(input_path=in_path,
                       output_path=out_path, img_type='.'+img_type)

    if type_ == 'resize_sym':
        resize_val = int(
            input('Insert a width value for symmetric resizing: '))
        init._resize_symmetric(resize_val)

    elif type_ == 'resize_prop':
        resize_val = int(
            input('Insert a width value for proportional resizing: '))
        init._resize_proportionally(resize_val)

    elif type_ == 'mirror':
        init._mirror()

    elif type_ == 'gray':
        init._greyscale()

    elif type_ == 'rotate':
        degrees = int(input('Insert a value in degrees for rotation: '))
        init._rotate(degrees)

    else:
        print('Incorrect type\nTry:\nresize_sym,resize_prop,mirror,gray')
