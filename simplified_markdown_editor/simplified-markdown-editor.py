markdowns = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line"]
list_commands = ["!help", "!done"]

out_help = "Available formatters"
out_range = "The level should be within the range of 1 to 6"
out_commands = "Special commands"
out_choice = "Choose a formatter: "
out_fail = "Unknown formatting type or command"

text_input = "Text: "
level_input = "Level: "
label_input = "Label: "
url_input = "URL: "

class Markdown:
    list_markdown = []

    def checkFormatting(self, value):
        if value == list_commands[1]:
            return
        if value == list_commands[0] or value in markdowns:
            return True
        else:
            return False

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
