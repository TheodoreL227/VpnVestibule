# consolecolors.py

text_colors = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37
}

bg_colors = {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47
}

formatting = {
    "reset": 0,
    "bold": 1,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "reverse": 7
}

def apply_formatting(code):
    return f"\033[{code}m"

def text(color_name):
    color_code = text_colors.get(color_name.lower(), 0)
    return apply_formatting(color_code)

def bg(color_name):
    color_code = bg_colors.get(color_name.lower(), 0)
    return apply_formatting(color_code)

def format(format_name):
    format_code = formatting.get(format_name.lower(), 0)
    return apply_formatting(format_code)

class p:
    @staticmethod
    def text(message, bg_color=None, c=None, style=None):
        formatted_text = ""
        
        if c:
            formatted_text += text(c)
        if bg_color:
            formatted_text += bg(bg_color)
        if style and isinstance(style, list):
            for s in style:
                formatted_text += format(s)
        
        formatted_text += message + apply_formatting(0)  # Reset formatting
        print(formatted_text)

# Example usage

'''



p.text("Colored and styled message", bg_color="yellow", c="blue", style=["bold", "underline"])
p.text("Red text on green background", bg_color="green", c="red")



'''
