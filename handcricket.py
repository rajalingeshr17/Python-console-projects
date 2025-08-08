import random

print('\t«« READY TO PLAY »»\n\t"Rock Paper Scissor"\n')
print('ENTER:\n\tR for ROCK\n\tP for PAPER\n\tS for SCISSOR\n')

choices = ['R', 'P', 'S']
bot_score, you_score, tied = 0, 0, 0
choice_names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissor'}

for i in range(1, 11):
    bot_choice = random.choice(choices)
    your_choice = input(f'Round {i} - Enter your choice: ').upper()

    if your_choice not in choices:
        print("Invalid choice! Please enter R, P, or S.")
        continue

    print(f'You chose: {choice_names[your_choice]}')
    print(f'Bot chose: {choice_names[bot_choice]}')

    if your_choice == bot_choice:
        print("Match tied!")
        tied += 1
    elif (your_choice == 'R' and bot_choice == 'S') or \
         (your_choice == 'P' and bot_choice == 'R') or \
         (your_choice == 'S' and bot_choice == 'P'):
        print("You won this round!")
        you_score += 1
    else:
        print("Bot won this round!")
        bot_score += 1

print("\n«« FINAL SCORE »»")
print(f"Your score: {you_score}")
print(f"Bot score: {bot_score}")
print(f"Tied matches: {tied}")

if you_score > bot_score:
    print("🎉 YOU WON THE SERIES! 🎉")
elif bot_score > you_score:
    print("🤖 BOT WON THE SERIES! 🤖")
else:
    print("⚖ MOST MATCHES TIED ⚖")
