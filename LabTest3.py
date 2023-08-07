# OPEN THE FILE TO ACCESS GRADES
with open('labGrades.txt', 'r') as f:
    lines = [line.rstrip() for line in f] # PUT THEM IN A LIST

# INITIALIZING VARIABLES AND CREATING A LIST FOR THE GRADES
total = 0
count = 0
listOfGrades = []

# A FOR LOOP TO GO THROUGH EACH STUDENT'S GRADE TO CALCULATE THE TOTAL AND NUMBER OF STUDENTS
for line in lines:
    i = line.find(" ")
    stu_grade = line[i:].strip()
    if stu_grade.isdigit():
        stu_grade = int(stu_grade)
        listOfGrades.append(stu_grade)
        total = stu_grade + total
        count = count + 1
    else:
        break

# CALCULATE THE AVERAGE
average = total / count

# IF STATEMENT'S TO DECIDE THE RIGHT STEP IN NORMALIZING THE GRADES
if average > 16:
    minusAmount = average - 16
    # OPEN A NEW FILE FOR THE NORMALIZED GRADES
    outfile = open("normalizedLabGrades.txt", "w")
    for i in range(len(listOfGrades)):
        outfile.write(f"{lines[i]} {listOfGrades[i] - minusAmount}\n") # BASIC FORMATTING
    outfile.close()

elif average < 16:
    plusAmount = 16 - average
    outfile = open("normalizedLabGrades.txt", "w")
    for i in range(len(listOfGrades)):
        outfile.write(f"{lines[i]} {listOfGrades[i] + plusAmount}\n")
    outfile.close()

elif average == 16:
    outfile = open("normalizedLabGrades.txt", "w")
    for i in range(len(listOfGrades)):
        outfile.write(f"{lines[i]} {listOfGrades[i]}\n")
    outfile.close()
