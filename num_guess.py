import numpy as np

LowerBound = 0
UpperBound = 10

Rand = np.random.randint(LowerBound,UpperBound+1)

MaxGuess = 5
for i in range(1,MaxGuess+1):
    
    print(f'You have {MaxGuess+1-i} chance(s) left!!')
    guess = int(input('Enter an integer between 0 and 10: '))
    
    if i == MaxGuess:
        print('You lost.')
    else:
        if guess == Rand:
            print('You WON!!')
            break
        else:
            print('Incorrect guess.')
            if guess >= Rand:
                print('The number is Smaller.')
            else:
                print('The number is Greater.')
            
