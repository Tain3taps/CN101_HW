import random
money = int(input("Enter your money : "))
keep_going = 'y'
while keep_going=='y':
    x1 = random.randint(0,9)
    x2 = random.randint(0,9)
    x3 = random.randint(0,9)
    #loop1
    while(True): 
	    bet = int(input('Enter your bet : '))
	    if bet not in range(0,999): 
		        print("enter a valid number between 0 and 999") 
	    else: 
                print('Your bet is : ', bet) 
                break 
    #loop1
    print("The output from slot machine is ",x1,x2,x3)
    if bet <= money:
        if x1==x2 and x2==x3:
            print("You won! Your reward is x10")
            reward = bet*10
            print("Your reward is", reward)
            money = money+reward
            print("Your money now is : ", money)
        else:
            print("You lost!")
            money = money-bet
            print("Your money now is : ", money)
    else:
        print("Not enough money. You have ", money)
    keep_going=input("Do you want to continue?\nif yes press y no press n : ")
print(f"Game over you've got {money}")
