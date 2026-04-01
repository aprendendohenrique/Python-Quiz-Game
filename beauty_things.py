colors = {'none': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
          'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
          'purple': '\033[35m', 'cyan': '\033[36m', 'gray': '\033[37m'}

def text_color(txt='', color='\033[m'):
    """
    -> It colors the text
    :param txt: the str to be colored
    :param color: the color
    :return: the colored text string
    """
    return f'{color}{txt}{colors['none']}'