### debugging the infinite loop
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# count = 0

# while not at_goal():
#     if front_is_clear() and count <4:
#         move()        
#         if right_is_clear():           
#             turn_right()
#             count += 1
#             print(count)               
#     elif front_is_clear():
#         turn_left()
#         if front_is_clear():
#             move()
#             count = 0
#         else:
#             turn_right()
#             if front_is_clear():
#                 move()
#                 count = 0
#     else:
#         turn_left()
#         count = 0 
### this is what I came up with, I probably shouldn't have spent time doing it but
### it seemed like a fun challenge and i found a solution that works 
### professor solution below