import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    chamber = spin_chamber()
    bullet = random.randint(1,6)
    if chamber == bullet:
        print("Your are dead!")
    else :
        print ("Keep playing!")



print(fire_gun())