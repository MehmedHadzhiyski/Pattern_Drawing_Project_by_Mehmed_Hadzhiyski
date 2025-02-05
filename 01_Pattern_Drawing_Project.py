# 🖼️ Python Pattern Drawing Project
from colorama import init, Fore, Style

init()


def right_angled_triangle(rows: int, selected_color) -> str:
    """Return a right-angled triangle based on the rows and the selected color"""
    triangle = ""
    for row in range(1, rows + 1):
        triangle += selected_color + '*' * row + Style.RESET_ALL + '\n'  # Add a new line
    return triangle


def square_with_hollow_center(size: int, selected_color) -> str:
    """Return a square with a hollow center based on the size and the selected color"""
    square = ""
    for row in range(size):
        if row in (0, size - 1):
            square += selected_color + '*' * size + Style.RESET_ALL + "\n"
        else:
            square += selected_color + '*' + Style.RESET_ALL
            for spaces in range(size - 2):
                square += " "
            square += selected_color + '*' + Style.RESET_ALL + "\n"
    return square


def diamond(rows: int, selected_color) -> str:
    """Return a diamond pattern based the rows and the selected color"""
    diamond_pattern = ""
    if rows % 2 == 0:
        rows -= 1

    for upper_rows in range(1, rows + 1, 2):
        for spaces in range((rows - upper_rows) // 2):
            diamond_pattern += ' '
        for stars in range(upper_rows):
            diamond_pattern += selected_color + '*' + Style.RESET_ALL  # DON'T USE \n
        diamond_pattern += "\n"

    for lower_rows in range(rows - 2, -1, -2):
        for spaces in range((rows - lower_rows) // 2):
            diamond_pattern += ' '  # DON'T USE \n
        for stars in range(lower_rows):
            diamond_pattern += selected_color + '*' + Style.RESET_ALL  # DON'T USE \n
        diamond_pattern += "\n"
    return diamond_pattern


def left_angled_triangle(rows: int, selected_color) -> str:
    """Return a left-angled_triangle based on the rows and the selected color"""
    triangle = ""
    for row in range(rows, 0, -1):
        for column in range(row):
            triangle += selected_color + '*' + Style.RESET_ALL
        triangle += "\n"
    return triangle


def hollow_square(size: int, selected_color) -> str:
    """Return a hollow square based on the size and the selected color"""
    square = ""
    for row in range(size):
        if row in (0, size - 1):
            for stars in range(size):
                square += selected_color + '*' + Style.RESET_ALL
        else:
            square += selected_color + '*' + Style.RESET_ALL
            for spaces in range(size - 2):
                square += ' '
            square += selected_color + '*' + Style.RESET_ALL
        square += "\n"
    return square


def pyramid(rows: int, selected_color) -> str:
    """Return a pyramid based on the rows and the selected color"""
    pyramid_pattern = ""
    for row in range(1, rows + 1, 2):
        for spaces in range((rows - row) // 2):
            pyramid_pattern += ' '
        for stars in range(row):
            pyramid_pattern += selected_color + '*' + Style.RESET_ALL
        pyramid_pattern += "\n"
    return pyramid_pattern


def reversed_pyramid(rows: int, selected_color) -> str:
    """Return a reversed pyramid based on the rows and the selected color"""
    reverse_pyramid_pattern = ""
    if rows % 2 == 0:
        rows -= 1

    for row in range(rows, 0, -2):
        for spaces in range((rows - row) // 2):
            reverse_pyramid_pattern += ' '
        for stars in range(row):
            reverse_pyramid_pattern += selected_color + '*' + Style.RESET_ALL
        reverse_pyramid_pattern += "\n"
    return reverse_pyramid_pattern


def rectangle_with_hollow_center(size: int, selected_color) -> str:
    """Return a rectangle with a hollow center based on the size, the width and height and the selected color"""
    rectangle = ""
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    for row in range(height):
        if row in [0, height - 1]:
            for stars in range(width):
                rectangle += selected_color + '*' + Style.RESET_ALL
        else:
            rectangle += selected_color + '*' + Style.RESET_ALL
            for spaces in range(width - 2):
                rectangle += ' '
            rectangle += selected_color + '*' + Style.RESET_ALL
        rectangle += "\n"
    return rectangle


def main():
    """Run the entire Pattern_Drawing_Project"""
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    request = input('Are you ready to start the program? (Yes or No): ')

    if request == 'Yes':
        while request == 'Yes':
            # Pattern Menu
            print("Choose a pattern type:")
            print("1. Right-angled Triangle")
            print("2. Square with Hollow Center")
            print("3. Diamond")
            print("4. Left-angled Triangle")
            print("5. Hollow Square")
            print("6. Pyramid")
            print("7. Reverse Pyramid")
            print("8. Rectangle with Hollow Center")

            # Choice for a pattern
            choice = int(input("Enter the number corresponding to your choice: "))
            rows_for_pattern, size_for_pattern = 0, 0

            # Get dimensions based on choice
            if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
                rows_for_pattern = int(input("Enter the number of rows: "))
            elif choice in [2, 5, 8]:  # Patterns that need size
                size_for_pattern = int(input("Enter the size of the square/rectangle: "))
            else:
                print("❌ Invalid choice! Please restart the program.")
                # Optional - Allow the user to restart or exit
                request = input('Would you like to restart the program? (Yes or Exit): ')
                continue

            print("Choose a color for your pattern:")
            print("1. Red  2. Green  3. Yellow  4. Blue  5. Cyan")
            color_choice = int(input("Enter your color choice: "))
            color_map = {1: Fore.RED, 2: Fore.GREEN, 3: Fore.YELLOW, 4: Fore.BLUE, 5: Fore.CYAN}
            selected_color_for_pattern = color_map.get(color_choice, Fore.WHITE)

            if choice == 1:  # Right-angled Triangle
                print(right_angled_triangle(rows_for_pattern, selected_color_for_pattern))
            elif choice == 2:  # Square with Hollow Center
                print(square_with_hollow_center(size_for_pattern, selected_color_for_pattern))
            elif choice == 3:  # Diamond
                print(diamond(rows_for_pattern, selected_color_for_pattern))
            elif choice == 4:  # Left-angled Triangle
                print(left_angled_triangle(rows_for_pattern, selected_color_for_pattern))
            elif choice == 5:  # Hollow Square
                print(hollow_square(size_for_pattern, selected_color_for_pattern))
            elif choice == 6:  # Pyramid
                print(pyramid(rows_for_pattern, selected_color_for_pattern))
            elif choice == 7:  # Reverse Pyramid
                print(reversed_pyramid(rows_for_pattern, selected_color_for_pattern))
            elif choice == 8:  # Rectangle with Hollow Center
                print(rectangle_with_hollow_center(size_for_pattern, selected_color_for_pattern))

            request = input('Would you like to restart the program? (Yes or Exit): ')

    elif request == 'No':
        print('Have a nice day!')
    else:
        print('Invalid request. Please try again.')

    if request == 'Exit':
        print('Thank you for using the Python Pattern Drawing Program!\nHave a nice day!')


if __name__ == "__main__":
    main()
