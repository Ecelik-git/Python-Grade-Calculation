#create list to hold grades
participation = []
summative=[]
formative=[]
#ask users to enter grades
#let's say 4 participation, 2 formative
#1 summative grade for 1 quarter
for i in range(4):
    participation_grade=int(input("Enter participation grade: "))
    participation.append(participation_grade)
for a in range(2):
    formative_grade = int(input("Enter formative grade: "))
    formative.append(formative_grade)
for b in range(1):
    summative_grade=int(input("Enter summative grade: "))
    summative.append(summative_grade)
#let's calculate the averages, participation 25%,
#formative 35%, summative 45%
c= sum(participation)/len(participation)*0.25
d= sum(formative)/len(formative)*0.35
e= sum(summative)/len(summative)*0.45
average = c+d+e
#let's print what the letter grade is
if average > 89.5:
  print ("your grade is an A")
elif average > 79.5:
  print ("your grade is a B")
elif average > 69.5:
  print ("your grade is a C")
elif average > 59.5:
  print ("your grade is a D")
else:
  print ("your grade is an F")
