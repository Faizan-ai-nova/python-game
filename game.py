import random

print("🎮 Welcome to Guess the Number Game!")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("1 se 100 ke beech number guess karo: "))
    attempts += 1

    if guess < number:
        print("📉 Bahut chhota!")
    elif guess > number:
        print("📈 Bahut bada!")
    else:
        print(f"🎉 Mubarak ho! Aapne {attempts} attempts me sahi number guess kar liya.")
        break
