# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_student_heights = 0
len_student_heights = 0
for height in student_heights:
    sum_student_heights += height
    len_student_heights += 1
average_student_height = sum_student_heights/len_student_heights
print(round(average_student_height))