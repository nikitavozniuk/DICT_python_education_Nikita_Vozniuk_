import random

result = dict()
default_value = 0
total = 0
friends = []
message_start = "Enter the number of friends joining (including you): "
message_friends = "Enter the name of every friend (including you), each on a new line: "
message_friends_zero = "No one is joining for the party"
message_lucky = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:'


def dinner_party():
    number = int(input(message_start))

    if number != 0:
        print(message_friends)
        for item in range(number):
            inp = input()
            friends.append(inp)
            result[inp] = default_value

        total = int(input('Enter the total amount: '))

        choice = input(message_lucky)

        if choice == "Yes":
            lucky_one = friends[random.randint(0, len(friends)-1)]
            print('{} is the lucky one!'.format(lucky_one))

            value = round(total / (number - 1), 2)

            for item, index in enumerate(range(number)):
                friend = friends[index]
                if friend == lucky_one:
                    result[friend] = 0
                else:
                    result[friend] = value

            print(result)
            return
        elif choice == "No":
            print('No one is going to be lucky')
            return
    else:
        print(message_friends_zero)


dinner_party()
