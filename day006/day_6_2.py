### indentation in python
###PEP 8 – Style Guide for Python Code:
### https://peps.python.org/pep-0008/
### tabs or spaces? spaces are the prefered indentation
### in py 3 you cannot mix tabs and spaces
#####################################################################################
### While loops
### For
### for item in list_of_items:
###     do something to each item
### for number in range(a, b):
###     print(number)
### While
### while something_is_true:
###     do something repeatedly
### only when the something becomse false does the loop stop
### for the hurdle challenge 
# ### reborg does hurdle 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def one_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     one_hurdle()
#     number_of_hurdles -= 1
### using the "at goal" condition
# while at_goal() == False:
#     one_hurdle()
#########################################################
### while loops can be more dangerous than for loops because if the conditon
### is never met they can become an infinite loop

### hurdle 3
# while at_goal() == False:
#     while front_is_clear() == True:
#         move()
#     while front_is_clear() == False:
#         one_hurdle()




