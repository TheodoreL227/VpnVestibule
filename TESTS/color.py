def change_text_color(color_code):
    print("\033[" + str(color_code) + "m", end="")

def reset_text_color():
    print("\033[0m", end="")

# Change text color to red
change_text_color(31)
print("This text is red.")

# Change text color to green
change_text_color(32)
print("This text is green.")

# Reset text color back to default
reset_text_color()
print("This text is back to default color.")
