markdowns = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line"]
list_commands = ["!help", "!done"]

out_help = "Available formatters"
out_range = "The level should be within the range of 1 to 6"
out_commands = "Special commands"
out_choice = "Choose a formatter: "
out_fail = "Unknown formatting type or command"
number_of_rows_fail = "The number of rows should be greater than zero"

text_input = "Text: "
level_input = "Level: "
label_input = "Label: "
url_input = "URL: "
number_of_rows_input = "Number of rows: "

class Markdown:
    list_markdown = []

    def checkFormatting(self, value):
        if value == list_commands[1]:
            return
        if value == list_commands[0] or value in markdowns:
            return True
        else:
            return False

    def unorderedList(self):
        rows = int(input(number_of_rows_input))
        try:
            if rows > 0:
                for value in range(rows):
                    element_text = input(f"Row #{value + 1}: ")
                    if len(self.list_markdown) > 0:
                        self.list_markdown.append(f"\n* {element_text}")
                    else:
                        self.list_markdown.append(f"* {element_text}")
            else:
                print(number_of_rows_fail)
        except ValueError:
            print(out_fail)

    def orderedList(self):
        rows = int(input(number_of_rows_input))
        if rows > 0:
            try:
                for value in range(rows):
                    element_text = input(f"Row #{value + 1}: ")
                    if len(self.list_markdown) > 0:
                        self.list_markdown.append(f"\n{value + 1}. {element_text}")
                    else:
                        self.list_markdown.append(f"{value + 1}. {element_text}")
            except ValueError:
                print(out_fail)
        else:
            print(number_of_rows_fail)

    def newLine(self):
        self.list_markdown.append(f"\n")

    def header(self, value, level):
        if level not in range(1, 6):
            print(out_range)
        else:
            if len(self.list_markdown) > 0:
                self.list_markdown.append(f"\n{'#' * level} {value}")
            else:
                self.list_markdown.append(f"{'#' * level} {value}")

    def help(self):
        print(f"{out_help}:", *markdowns, sep=" ")
        print(f"{out_commands}", *list_commands, sep=" ")

    def plain(self, value):
        if len(self.list_markdown) > 0:
            self.list_markdown.append(f"\n{value}")
        else:
            self.list_markdown.append(f"{value}")
    
    def bold(self, value):
        if len(self.list_markdown) > 0:
            self.list_markdown.append(f"\n{value}")
        else:
            self.list_markdown.append(f"**{value}**")

    def italic(self, value):
        if len(self.list_markdown) > 0:
            self.list_markdown.append(f"\n{value}")
        else:
            self.list_markdown.append(f"*{value}*")

    def inlineCode(self, value):
        if len(self.list_markdown) > 0:
            self.list_markdown.append(f"\n`{value}`")
        else:
            self.list_markdown.append(f"`{value}`")

    def link(self, label, url):
        if len(self.list_markdown) > 0:
            self.list_markdown.append(f"\n[{label}]({url})")
        else:
            self.list_markdown.append(f"[{label}]({url})")

    def markdownFormat(self, type):
        if type == "plain":
            plain_text = input(text_input)
            self.plain(plain_text)
            print(*self.list_markdown)
        elif type == "bold":
            bold_text = input(text_input)
            self.bold(bold_text)
            print(*self.list_markdown)
        elif type == "italic":
            bold_text = input(text_input)
            self.italic(bold_text)
            print(*self.list_markdown)
        elif type == "inline-code":
            bold_text = input(text_input)
            self.inlineCode(bold_text)
            print(*self.list_markdown)
        elif type == "new-line":
            self.newLine()
            print(*self.list_markdown)
        elif type == "link":
            label_text = input(label_input)
            url_text = input(url_input)
            self.link(label_text, url_text)
            print(*self.list_markdown)
        elif type == "header":
            try:
                header_text = input(text_input) 
                header_level = int(input(level_input))
                self.header(header_text, header_level)
                print(*self.list_markdown) 
            except ValueError:
                print(out_fail)  
        elif type == "unordered-list":
            self.unorderedList()
            print(*self.list_markdown)
        elif type == "ordered-list":
            self.orderedList()
            print(*self.list_markdown)
        elif type == "!help":
            self.help()


def main():
    markdown = Markdown()
    markdown.help()

    while True:
        u_input = input(out_choice)
        formatted = markdown.checkFormatting(u_input)
        if formatted:
            markdown.markdownFormat(u_input)
        elif formatted == False:
            print(out_fail)
        else:
            break
    

if __name__ == "__main__":
    main()
