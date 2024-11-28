import math
import cmath

a=30 # team number

def move(pos, moves): # function responsible for moving DI Irrational around
    """LOCAL VALUE u RESPONSIBLE FOR MOVEMENT"""
    u=(math.sqrt(2))/1+1j
    """LOOP RESPONSIBLE FOR GETTING THE POSITION WHEN MOVED i TIMES"""
    for i in range(moves):
        pos/=u
    return pos

def room_one(team): # function responsible for giving back the result of Zinitial 1
    Z_ini_1 = (1+1j) / ((math.sqrt(2)) * (1j**4) * (((1+1j) / abs(1+1j)) ** team))
    return Z_ini_1

def room_two(team): # function responsible for giving back the result of Zinitial 2
    Z_ini_2 = ((math.sqrt(2)) * (1+1j)) / (((1+1j) / (math.sqrt(2))) ** team)
    return Z_ini_2

def mean_moves(pos, moves): # function responsible for returning the answer to question 1.1
    """OPEN LOCAL LIST AND TOTAL"""
    positions=[]
    total=0
    """FOR EVERY COUNT, MOVE POSITION BASED ON i"""
    for i in range(moves):
        pos=move(room_one(a), i)
        positions.append(pos)
    """FOR EVERY NUMBER IN A POSITION, ADD TO A TOTAL"""
    for num in positions:
        total+=num
    """GET MEAN VALUE OF TOTAL"""
    total/=moves
    return total

def list_all(pos, moves): # function mainly used for testing, returns a list of all steps taken
    positions=[]
    for i in range(moves):
        pos=move(room_one(a), i)
        positions.append(pos)
    return positions

def main():
    print("this is the starting position based on our team number")
    print("\n", room_one(a))
    print()
    print()
    print("this is the answer to question 1.1")
    print("\n", mean_moves(room_one(a), 64))

main()