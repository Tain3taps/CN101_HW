#Question 1
name = input('Insert your name : ')
print('Hi',name,'hope you guy enjoy this quiz :D ')
print('>>Please answer the following questions<<')
print('Which day is weekend ? \na.Monday \nb.Sunday \nc.Tuesday \nd.Birthday')
answer_1 = input('Answer : ')
score = 0
if answer_1 =='b' or answer_1 == 'Sunday' :
    score += 1
    print('Godd job bro !! you gotta point now')
    print('Score : ', score)
    print('\n')
else :
    print('Nice try The answer is Sunday')
    print('Score : ', score)
    print('\n')
#Question 2
print('What is the answer for 2+2*2')
answer_2 = input('Answer : ')
if answer_2 == '6' :
    score += 1
    print('Well done !! you gotta point now')
    print('Score : ', score)
    print('\n')
else :
    print('Nice try The answer is 6')
    print('Score : ', score)
    print('\n')
#Question 3
answer_3 = input('Type any positve value : ')
if answer_3 > '0' :
    score += 1
    print('Correctly !! you gotta point now')
    print('Score : ', score)
    print('\n')
else :
    print('Nice try')
    print('Score : ', score)
    print('\n')
#Question 4
answer_4 = int(input('Type a number that is divisible by 3 : '))
if answer_4%3 == 0  :
    print('Nice try but your number can visible by 3')
    print('Score : ', score)
    print('\n')
else :
    score += 1
    print('Correctly !! you gotta point now')
    print('Score : ', score)
    print('\n')
#Question 5
print('Sort the following names in ascendance order : Anna, Peter, John')
answer_5 = input('answer : ')
if answer_5 == 'Anna, John, Peter'  :
    score += 1
    print('Nice!! you gotta point now')
    print('Score : ', score)
    print('\n')
else :
    print('Nice try')
    print('Score : ', score)
    print('\n')


if score >= 3 :
    print('Congratulation !! you pass this quiz')
else :
    print('Fail !! you can try it again ')