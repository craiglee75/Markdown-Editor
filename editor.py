# Markdown Editor
import os


class Editor:

    def __init__(self):
        self.text = ''
        self.output = ''
        self.commands = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line', 'ordered-list', 'unordered-list']
        self.specials = ['!help', '!done']
        self.unavailable = 'Unknown formatting type or command'
        self.saved_file = os.getcwd()

    def convert(self):
        while True:
            req = input('Choose a formatter: ')
            if req not in self.commands and req not in self.specials:
                print(self.unavailable)
            elif req == '!help':
                print('Available formatters: ', *self.commands)
                print('Special commands: ', *self.specials)
            elif req == '!done':
                self.save()
            elif req == 'plain':
                self.plain()
            elif req == 'bold':
                self.bold()
            elif req == 'italic':
                self.italic()
            elif req == 'inline-code':
                self.inline_code()
            elif req == 'link':
                self.link()
            elif req == 'header':
                self.header()
            elif req == 'new-line':
                self.new_line()
            elif req == 'ordered-list' or req == 'unordered-list':
                self.lists(req)
            print(self.output)

    def plain(self):
        self.text = input('Text: ')
        self.output += self.text

    def bold(self):
        self.text = input('Text: ')
        self.output += f'**{self.text}**'

    def italic(self):
        self.text = input('Text: ')
        self.output += f'*{self.text}*'

    def inline_code(self):
        self.text = input('Text: ')
        self.output += f'`{self.text}`'

    def link(self):
        self.text = input('Label: ')
        url = input('URL: ')
        self.output += f'[{self.text}]({url})'

    def header(self):
        level = input('Level: ')  # levels 1 - 6
        if int(level) not in range(1, 7):
            print('The level should be within the range of 1 to 6')
            return self.header()
        else:
            self.text = input('Text: ')
            self.output += int(level)*'#' + ' ' + self.text + '\n'

    def new_line(self):
        self.output += '\n'

    def lists(self, req):
        while True:
            rows = input('Number of rows: ')
            if int(rows) <= 0 or rows.isalpha():
                print('The number of rows should be greater than zero')
                continue
            else:
                break

        for i in range(1, int(rows) + 1):
            self.text = input(f'Row #{i}: ')
            if req == 'unordered-list':
                self.output += '*' + ' ' + self.text + '\n'
            else:
                self.output += f'{i}. {self.text}\n'

    def save(self):
        filename = 'output.md'
        with open(filename, 'w') as f:
            f.write(self.output)
            print(f'file saved to {self.saved_file}')
            return exit()


def main():
    my_text = Editor()
    my_text.convert()


if __name__ == '__main__':
    main()
