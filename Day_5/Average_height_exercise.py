# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# print(student_heights)
for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights=0
num_0f_student=0
for i in student_heights:
    total_heights+=i
    num_0f_student+=1
average_height=round(total_heights/num_0f_student)
print(average_height)
