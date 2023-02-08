### holy shit this was by far the hardes challenge I have done so far
### I am sure there is a better way to do this. I will post the professor's
### solution below but here is mine. It is ugly but it works
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() == False:
#     if wall_in_front() == True and wall_on_right() == True:
#         turn_left()
#         move()
#         turn_right()
#     elif wall_on_right() == True and wall_in_front() == False:
#         move()
#     elif wall_in_front() == True and wall_on_right() == False:
#         turn_left()
#         if wall_in_front() == True:
#             turn_left()
#         else:
#             move()
#             turn_right()
#     elif wall_in_front() == False and wall_on_right() == False:
#         move()
#         turn_right()
#         move()
#         turn_right()
#     else:
#         move()
#         turn_right()
#         move()
#         turn_left()
################################################################
# from the comments. Holy shit I really over complicated this  

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#         if right_is_clear():
#             turn_right()
#     else:
#         turn_left()      
#################################################################
# Professor's solution:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left() 

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
###########################################################
### Maze ####
### The solution provided in the comments of the last hurdle game also works for this
### project but I wanted to find my own solution. 
### This does just about the same thing but with a syntax that I am more 
### comfortable with. 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while at_goal() == False:
#     if wall_in_front() == False and wall_on_right() == False:
#         turn_right()
#         move()
#     elif wall_in_front() == True and wall_on_right() == False:
#         turn_right()
#         move()
#     elif wall_in_front() == False and wall_on_right() == True:
#         move()
#     else:
#         turn_left()
### bonus it works with the previous one as well.
### I think the take away from all this struggle for me is to address the edge cases first. 
### for this the edge case is when there is no wall to the right or the front. 
### if this is the case we can assume that we are facing away from the previous wall
### and becuase of that we turn right then move. 