student_heights = input("Input a list of student heights \n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
heights = 0
for i in student_heights:
    heights += i
    count += 1
print(round(heights / count))
