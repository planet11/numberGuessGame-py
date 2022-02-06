import random
# random.randint(-5, 5)  # from -5 to 5
# random.randrange(-5, 5)  #from -5 to 4

top_of_range = input("Type a number: ")

if top_of_range.isdigit():  # will check if input is a digit / number
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0!")
        quit()
else:
    print("Please type a number next time!")
    quit()
rand_num = random.randrange(0, top_of_range)
total_guess = 0

while True:
    total_guess += 1
    guess = input("Guess the number:  ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number! ")
        continue
    if guess == rand_num:
        print("You are correct!")
        break
    elif guess < rand_num:
        print(f"Incorrect!\nYou gussed too low, guess a higher number!")
    else:
        print(f"Incorrect!\nYou guessed too high, guess a lower number!")
print(f'You got it in {total_guess} gusses!')
print("You got it in", total_guess, "gusses!")