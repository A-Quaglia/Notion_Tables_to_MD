import pyperclip

from mdkit import md_table

if __name__ == '__main__':
    table = pyperclip.paste()
    new_table = md_table(table)
    print(new_table)
    pyperclip.copy(new_table)