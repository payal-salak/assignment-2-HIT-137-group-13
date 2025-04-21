"""
HIT137 Assignment 2 - Question 1
A program that use recursive function to generates a tree pattern using Python's 
turtle graphics. The program should take the following parameters from the user: 
Left and right branch angles 
Starting branch length 
Recursion depth 
Branch length reduction factor

Group number CAS/DAN 13
S361253 Ashton Searle
s389249 payal 
S391075 Amanparteek singh
S390786 Anshul
S391273 komalpreet kaur
"""
import turtle

def draw_branch(branch_length, t, left_angle, right_angle, depth, reduction_factor):
    if depth == 0 or branch_length < 1:
        return

    # colour change
    if depth == max_depth:
        t.color("brown")  # stem
    else:
        t.color("green")  # branches

    t.forward(branch_length)
    
    # drawing Left branch
    t.left(left_angle)
    draw_branch(branch_length * reduction_factor, t, left_angle, right_angle, depth - 1, reduction_factor)
    t.right(left_angle)

    # drawing Right branch
    t.right(right_angle)
    draw_branch(branch_length * reduction_factor, t, left_angle, right_angle, depth - 1, reduction_factor)
    t.left(right_angle)

    t.backward(branch_length)

# Getting user inputs
left_angle = int(input("Enter left branch angle: "))
right_angle = int(input("Enter right branch angle: "))
start_length = int(input("Enter starting branch length: "))
global max_depth
max_depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter branch length reduction factor (e.g. 0.7): "))


t = turtle.Turtle()
t.speed('fastest')
screen = turtle.Screen()
screen.bgcolor("white")
t.left(90)
t.up()
t.goto(0, -250)
t.down()

# Draw the tree
draw_branch(start_length, t, left_angle, right_angle, max_depth, reduction_factor)


turtle.done()
