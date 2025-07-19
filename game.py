import random

def selectFromDict(options, name):
    index = 0
    indexValidList = []
    print('Select a ' + name + ':')
    for optionName in options:
        index += 1
        indexValidList.append(optionName)
        print(str(index) + ') ' + options[optionName])
    
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        inputNo = int(inputRaw) - 1
        if 0 <= inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print('Selected ' + name + ': ' + selected)
            inputValid = True
        else:
            print('Please select a valid ' + name + ' number')
    return selected

user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    print('User Choice: ' + user_choice)
    print('Computer Choice: ' + computer_choice)

    if user_choice == computer_choice: print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        print("You win!")

    else:
        computer_score += 1
        print("Computer wins!")

    print('User Score:', user_score)
    print('Computer Score:', computer_score)


while True:
    user_choice = selectFromDict({'rock': 'Rock', 'paper': 'Paper', 'scissors': 'Scissors'}, 'choice')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('Selected computer choice:', computer_choice)

    determine_winner(user_choice, computer_choice)

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes': break
