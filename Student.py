import sys

course1=sys.argv[1]
marks1=int(sys.argv[2])

course2=sys.argv[3]
marks2=int(sys.argv[4])

course3=sys.argv[5]
marks3=int(sys.argv[6])

total=marks1+marks2+marks3
average=total/3
largest=max(marks1,marks2,marks3)
smallest=min(marks1,marks2,marks3)

print("\n--Student Details--")
print(f"Course 1: {course1}, Marks: {marks1}")
print(f"Course 2: {course2}, Marks: {marks2}")
print(f"Course 3: {course3}, Marks: {marks3}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Largest Marks: {largest}")
print(f"Smallest Marks: {smallest}")