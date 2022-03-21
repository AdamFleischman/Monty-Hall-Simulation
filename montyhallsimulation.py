#montyhallsimulation.py
#In my mind, I feel like it doesn't matter if you switch your box or not, but I've heard of this simulation before and I think it's supposedly better to switch. I think it's something to do with the chance going from 33% to 50% but not on the one you selected, I can't quite remember.


#Simulation:
import random
total_result = 0
numtrials = 1000
for x in range(numtrials):
	winningDoor = random.randint(0,2)

	door = 0
	openedDoor = random.randint(1,2)
	while openedDoor == winningDoor:
		openedDoor = random.randint(1,2)

	if openedDoor == 1:
		otherDoor = 2
	else:
		otherDoor = 1

	if door == winningDoor:
		correct = 1
	else:
		correct = 0

	total_result += correct

print(total_result/numtrials)
#We win about 33% of the time
total_result = 0
for x in range(numtrials):
	winningDoor = random.randint(0,2)

	door = 0
	openedDoor = random.randint(1,2)
	while openedDoor == winningDoor:
		openedDoor = random.randint(1,2)

	if openedDoor == 1:
		otherDoor = 2
	else:
		otherDoor = 1

	if otherDoor == winningDoor:
		correct = 1
	else:
		correct = 0

	total_result += correct

print(total_result/numtrials)
#We win about 66% of the time!

#When you initially pick a door, it has a 33% chance to be correct and a 66% chance to be incorrect. This means that if you never switch doors, there is a 33% chance you select the right door, but if you always switch doors, there is a 66% chance you select the right door.