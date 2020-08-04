import os
from PIL import Image

def change_extension(path, ext):
    os.chdir(path)
    if not os.path.exists(os.path.join(path, "newImages")):
        os.mkdir("newImages")    
    for file in os.listdir():
        try:
            img = Image.open(file)
            filename = os.path.splitext(file)[0]
            img.save(f"newImages\\{filename}.{ext}")
        except Exception as err:
            print("Something went wrong!", err)


def compress_image(path):
    os.chdir(path)
    if not os.path.exists(os.path.join(path, "compressed")):
        os.mkdir("compressed")
    factor = 0.5

    for file in os.listdir():
        try:
            img = Image.open(file)
            l, b = img.size
            img = img.resize((int(l * factor), int(b * factor)), Image.LANCZOS)
            img.save(f"{path}\\compressed\\{file}", optimize=True, quality=85)
        except Exception as err:
            print("Something went wrong!", err)



def watermark_image(path):
    pass


def create_thumbnail(path):
    os.chdir(path)
    if not os.path.exists(os.path.join(path, "thumbnails")):
        os.mkdir("thumbnails")
    for file in os.listdir():
        if os.path.isfile(os.path.join(path, file)):
            try:
                img = Image.open(file)
                newimg = img.copy()
                size = (700, 700)
                newimg.thumbnail(size)
                newimg.save(f"{path}\\thumbnails\\{file}")
            except Exception as err:
                print("Something went wrong!", err)


# v : invert image(s) vertically
# h : invert image(s) horizontally
def rotate_image(path, opt):
    os.chdir(path)
    newpath = os.path.join(path, "rotatedImages")
    if not os.path.exists(newpath):
        os.mkdir("rotatedImages")
    for file in os.listdir():
        if os.path.isfile(os.path.join(path, file)):
            try:
                img = Image.open(file)
                if opt.isnumeric():
                    deg = int(opt)
                    newimg = img.rotate(deg)
                    newimg.save(f"{newpath}\\{file}")
                elif opt == "v":
                    newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
                    newimg.save(f"{newpath}\\{file}")
                elif opt == "h":
                    newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
                    newimg.save(f"{newpath}\\{file}")
                else:
                    raise Exception("Invalid input")
            except Exception as err:
                print("Something went wrong!", err)