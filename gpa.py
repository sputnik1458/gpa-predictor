#! /usr/bin/env python

uwGrades = {'A': 4.0, 'B+': 3.3, 'B': 3.0, "C+": 2.3, "C": 2.0, "D+": 1.3, "D": 1.0, "F": 0.0}

def main():
    userData = getData()
    userGPA = userData[0]
    userCredits = userData[1]
    
    predictedData = newGrades()
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

def newGrades():
    data2 = []
    gradeValue = 0
    
    grades = raw_input("Enter your predicted grades here: ").split()
    newCredits = len(grades)
    for i in grades:
        gradeValue += uwGrades[i]

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

