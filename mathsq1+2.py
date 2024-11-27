import math
import cmath

a=30 # team number
def move(position, movements):
    u=(math.sqrt(2))/1+1j
    for i in range(movements):
        position/=u
    return position

def room_one(team):
    Z_ini_1 = (1+1j) / ((math.sqrt(2)) * (1j**4) * (((1+1j) / abs(1+1j)) ** team))
    return Z_ini_1

def room_two(team):
    Z_ini_2 = ((math.sqrt(2)) * (1+1j)) / (((1+1j) / (math.sqrt(2))) ** team)
    return Z_ini_2

