import random
from art import logo, vs
from game_data import data

print(logo)

score = 0

def format_data(account):
    """Format data into printable format """
    account_name = account["name"]
    account_dis = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_dis}, {account_country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """ Use if statement to check if user is correct and returns if they got it right."""
    if a_follower_count > b_follower_count:
        return guess == "a"
        # if guess == "a":
        #     return True
        # else:
        #     return False
    else:
        return guess == "b"


game_continue = True
accountB = random.choice(data)

while game_continue:
    #chooce random data from dictionary
    accountA = accountB
    accountB = random.choice(data)
    #in case if both data are same
    while accountA == accountB:
        accountB = random.choice(data)


    print(f"Compare A: {format_data(accountA)}.")
    print(vs)
    print(f"Against B: {format_data(accountB)}.")

    #Ask for a guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    #Check if answer is correct
    a_follower_count = accountA['follower_count']
    b_follower_count = accountB['follower_count']


    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry that's wrong. Final Score: {score}.")