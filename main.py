import os


def show_menu():
    print("""
    *********** Commands ***********
    c : compress image(s)
    e : change extension of image(s)
    t : make a thumbnail of image(s)
    """)


def get_directory():
    return repr(input("Enter the directory location(absolute path): "))


def change_extension(path, ext):
    pass


def compress_image(path):
    pass


def watermark_image(path):
    pass


if __name__ == "__main__":
    choice = "q"
    while choice != "q" or choice != "quit":
        show_menu()
        choice = input("    Enter command: ")


