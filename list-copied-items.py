#!/usr/bin/env python3

import os
import pyperclip
import subprocess

home = os.path.expanduser('~')
file = '{}/.copied.txt'.format(home)


def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """

    dummy_file = file_name + '.bak'

    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)

    os.remove(file_name)
    os.rename(dummy_file, file_name)


def get_current_copied_item() -> str:
    proc = subprocess.Popen('xclip -o',
                            stdout=subprocess.PIPE, shell=True)
    return proc.stdout.read()


def return_copied(amount: int) -> str:
    proc = subprocess.Popen('sed 1,{}!d {} | xmenu -i'.format(amount, file),
                            stdout=subprocess.PIPE, shell=True)
    return proc.stdout.read()


def copy_selected_item(string_to_copy):
    pyperclip.copy(string_to_copy)
    prepend_line(file, string_to_copy)


want_to_copy = return_copied(15).decode("utf-8").strip('\n')
copy_selected_item(want_to_copy)
