import random
a = input('Select the number range from 1 to: ')
r = random.randint(1 , int(a))
import time
print('Guess the number from 1 to' , a)
time.sleep(1)
t = input('How many guess do you want to have: ')
t = int(t)
if int(t) > 15:
	print ("You can't have more than 15 guesses.")
	while int(t) > 15:
		t = input ('How many guess do you want to have: ')
t = int(t)
print('Now you have' , t , 'opportunities')
if int(t) < 0:
	print ('What do you mean negative guess???')
while int(t) > 0:
	i = input('please guess a number: ')
	if int (i) == r:
		print('CONGRATS!!!, you are right')
		break
	elif int (i) > r:
		print ('please guess a number below', i )
	else:
		print ('please guess a number above', i )
	t = t - 1
	if int(t) <= 5:
		print ('You have' , t , 'opportunities left')
print("The correct number is " , r)
