import os
from sys import exit
from PIL import Image


def show_menu():
    print("""
    *********** Commands ***********
    c : compress image(s)
    e : change extension of image(s)
    t : make a thumbnail of image(s)
    q : quit program
    """)


def get_directory():
    return input("Enter the directory location(absolute path): ")


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
                l, b = img.size
                factor = 0.8
                size = (700, 700)
                newimg.thumbnail(size)
                newimg.save(f"{path}\\thumbnails\\{file}")
            except Exception as err:
                print("Something went wrong!", err)


if __name__ == "__main__":
    choice = ""
    while choice != "q":
        show_menu()
        choice = input("    Enter command: ")
        choice = choice.lower()

        if choice == "q":
            continue

        elif choice == "c":
            path = get_directory()
            print(path)
            compress_image(path)

        elif choice == "e":
            path = get_directory()
            ext = input("Enter the new extension(e.g. png): ")
            change_extension(path, ext)

        elif choice == "t":
            path = get_directory()
            create_thumbnail(path)

        else:
            print("Invalid command. Please try again.")

    else:
        print("Closing program...")
        print("Program closed")
        exit()


