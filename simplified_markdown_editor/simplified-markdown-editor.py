markdowns = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line"]
list_commands = ["!help", "!done"]

out_help = "Available formatters"
out_commands = "Special commands"
out_choice = "Choose a formatter: "
out_fail = "Unknown formatting type or command"

def main():
    print(f"{out_help}:", *markdowns, sep=" ")
    print(f"{out_commands}", *list_commands, sep=" ")
    while True:
        u_input = input(out_choice)
        if u_input == list_commands[1]:
            break

        if u_input == list_commands[0]:
            print(f"{out_help}:", *markdowns, sep=" ")
            print(f"{out_commands}", *list_commands, sep=" ")
        elif u_input in markdowns:
            continue
        else:
            print(out_fail)
    



if __name__ == "__main__":
    main()
