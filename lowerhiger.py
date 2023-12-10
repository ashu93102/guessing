import art
import random
import game_data
print(art.logo)

#print(range(len(game_data.data)))

def guess():
    play = True
    current_score = 0
    while play:
        comapre1 = game_data.data[random.randint(1, len(game_data.data)) - 1]
        name1 = comapre1['name']
        follower1 = comapre1['follower_count']
        des1 = comapre1['description']
        country1 = comapre1['country']
        print(f"Compare A : {name1}, {des1}, from {country1}")

        print(art.vs)
        comapre2 = game_data.data[random.randint(1, len(game_data.data)) - 1]
        name2 = comapre2['name']
        follower2 = comapre2['follower_count']
        des2 = comapre2['description']
        country2 = comapre2['country']
        print(f"Compare B: {name2}, {des2}, from {country2}")
        user_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()

        if user_choice == 'a' and follower1 > follower2:
            current_score += 1
            print(f"You are right! Current Score: {current_score}")
        elif user_choice == 'a' and follower1 < follower2:
            print(f"Sorry That's wrong. Final Score: {current_score}")
            play = False
        elif user_choice == 'b' and follower2 > follower1:
            current_score += 1
            print(f"You are right! Current Score: {current_score}")
        elif user_choice == 'b' and follower2 < follower1:
            print(f"Sorry That's wrong. Final Score: {current_score}")
            play = False

guess()