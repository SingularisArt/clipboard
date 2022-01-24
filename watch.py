#!/usr/bin/python3.10

import os
from pyperclip import paste

home = os.path.expanduser('~')
file = '{}/.copied.txt'.format(home)


def prepend_line(file_name, line):
    """Insert given string as a new line at the beginning of a file"""

    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)

    os.remove(file_name)
    os.rename(dummy_file, file_name)


def check_copied_string(current_copied_string):
    os.system("sed -i '/^$/d' {}".format(file))

    if current_copied_string != paste():
        current_copied_string = paste()

        prepend_line(file, current_copied_string)
        print('Copied: {}'.format(current_copied_string))

        return current_copied_string
    else:
        return current_copied_string


current_copied_string = ''

while True:
    current_copied_string = check_copied_string(current_copied_string)
