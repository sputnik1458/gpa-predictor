#! /usr/bin/env python

uwGrades = {'A': 4.0, 'B+': 3.0, 'B': 3.0, "C+": 2.0, "C": 2.0, "D+": 1.0, "D": 1.0, "F": 0.0}
coreAPGrades = {'A': 5.0, 'B+': 4.0, 'B': 4.0, "C+": 3.0, "C": 3.0}
coreHonorsGrades = {'A': 4.5, 'B+': 3.5, 'B': 3.5, "C+": 2.5, "C": 2.5} 

def choice():
    choice = raw_input("Which GPA would you like to predict(Unweighted or Core): ").lower()
    if choice == "unweighted" or choice == "core":
        return choice
    else:
        print "Error: Not a supported GPA type.\n "
        main()

def main():
    gpaType = choice()
    userData = getData()
    userGPA = userData[0]
    userCredits = userData[1]
    
    predictedData = newGrades(gpaType)
    predictedGrades = predictedData[0]
    predictedCredits = predictedData[1]

    predictedGPA = newGPA(userGPA, userCredits, predictedGrades, predictedCredits)
    print predictedGPA


def getData():
    data = []
    gpa = input("Enter your current GPA: ")
    credits = 2 * input("Enter your current credit amount: ")
    

    data.append(gpa)
    data.append(credits)

    return data

def newGrades(x):
    data2 = []
    gradeValue = 0
    newCredits = 0
    
    if x == "unweighted":
        grades = raw_input("Enter your predicted grades here: ").split()
        newCredits = len(grades)
        for i in grades:
            gradeValue += uwGrades[i]
    elif x == "core":
        collegeGrades = raw_input("Enter your college-level grades: ").split()
        honorsGrades = raw_input("Enter your honors-level grades: ").split()
        regularGrades = raw_input("Enter your regular-level grades: ").split()

        newCredits = len(collegeGrades) + len(honorsGrades) + len(regularGrades)

        for i in collegeGrades:
            if i != "D+" and i != "D" and i != "F":
                gradeValue += coreAPGrades[i]
            else:
                gradeValue += uwGrades[i]

        for j in honorsGrades:
            if j != "D+" and j != "D" and j != "F":
                gradeValue += coreHonorsGrades[j]
            else:
                gradeValue += unGrades[j]

        for k in regularGrades:
            gradeValue += uwGrades[k]

    
    data2.append(gradeValue)
    data2.append(newCredits)

    return data2


def newGPA(oldGPA, oldCredits, addGrades, addCredits):
    grossValue = oldGPA * oldCredits
    newCredits = oldCredits + addCredits
    newValue = grossValue + addGrades
    gpa = newValue / newCredits

    return gpa
    

main()

