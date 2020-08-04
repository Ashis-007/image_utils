from sys import exit
from utils import change_extension, compress_image, create_thumbnail 
from utils import watermark_image, rotate_image, edit_image


def show_menu():
    print("""
    *********** Commands ***********
    c : compress image(s)
    e : edit image(s)
    x : change extension of image(s)
    t : make a thumbnail of image(s)
    r : rotate image(s)
    q : quit program
    """)


def get_directory():
    return input("  Enter the directory location(absolute path): ")


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
            print("""
        options:
        e : enhance
        c : color
        t : contrast
        b : brightness
        s : sharpness
            """)
            opt = input("       Choose option: ")
            factor = float(input("Enter factor(1.0 is default): "))
            edit_image(path, opt, factor)

        elif choice == "x":
            path = get_directory()
            ext = input("Enter the new extension(e.g. png): ")
            change_extension(path, ext)

        elif choice == "t":
            path = get_directory()
            create_thumbnail(path)

        elif choice == "r":
            path = get_directory()
            print("""
        options:
        r : rotate by an angle
        v : invert image(s) vertically
        h : invert image(s) horizontally
            """)
            opt = input("       Choose option:")
            if opt == "r":
                opt = input("Enter angle(in degree) to rotate image(s) anti-clockwise: ")
                rotate_image(path, opt)
            else:
                rotate_image(path, opt)

        else:
            print("Invalid command. Please try again.")

    else:
        print("Closing program...")
        print("Program closed")
        exit()


