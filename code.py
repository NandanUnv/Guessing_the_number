
import random as ra

while True:
    print('------------------------------------')
    print('let me guess number from 1 to 50')
    d = ra.randint(1,51)
    lives = 10
    a = input("chose the difficulty level.... Type 'easy' or 'hard':")
    if a=='hard':
        lives=5
    elif a=='easy':
        pass
    else:
        print("Invalid lives")
    while lives>=1:
        print(f'your lives is/are :{lives}')
        b = int(input("Guess your number:"))
        if d==b:
            print('your guess is correct')
            break
        elif b<d:
            lives-=1
            print("guess is low")
        elif b>d:
            lives-=1
            print("guess is high")
        else:
            break
        if d!=b and lives>1:
            print("guess again")
    if lives==0:
        print('out of lives')
        print(f"All your guesses are wrong,the number I chose is {d}.")
    z = input("Do you want to play again(Y/N):")
    if z=='Y' or z=='y':
        pass
    else:
        break
print("Thank you")
