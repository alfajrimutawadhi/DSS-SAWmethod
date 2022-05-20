from prettytable import PrettyTable
from numpy import *
table = PrettyTable()

criteria = []
criteriaDescription = []
subCriteria = []
priority = []
alternative = []

def inputCriteria(count):
    for i in range(count):
        criteria.append(input("Criteria name "+str(i+1)+" : "))

        while True:
            describe = input("Criteria  "+criteria[i]+" incldude (profit/loss) : ")
            if describe == "profit" or describe == "loss":
                criteriaDescription.append(describe)
                break
            else:
                print("Please input 'profit' or 'loss'")
                continue

        while True:
            subCriteriaInput = input("Criteria "+criteria[i]+" include sub criteria (y/n) : ")
            if subCriteriaInput == "y" or subCriteriaInput == "n":
                break
            else:
                print("Please input 'y' or 'n'")
                continue

        if subCriteriaInput == "y":
            while True:
                subCriteriaCount = input("How many sub criteria : ")
                if subCriteriaCount.isdigit():
                    subCriteriaCount = int(subCriteriaCount)
                    break
                else:
                    print("Please input number")
                    continue
            
            subCriteriaList = []
            for j in range(subCriteriaCount):
                subCriteriaList.append(input("Sub criteria name "+str(j+1)+" : "))
            subCriteria.append(subCriteriaList)
        else:
            subCriteria.append([])

def inputPriority(value):
    for x in range(value):
        while True:
            prioriyInput = input("Input priority for criteria '"+criteria[x]+"' (1-100) : ")
            if prioriyInput.isdigit():
                priority.append(int(prioriyInput))
                break
            else:
                print("Please input number")
                continue

def inputAlternative(totalAlternative, criteriaData, subCriteriaData):
    for x in range(totalAlternative):
        alternativeName = input("Input alternative name number "+str(x+1)+" : ")
        alternativeValue = []
        for y in range(len(criteriaData)):
            if subCriteriaData[y] == []:
                while True:
                    inputValue = input("Input value for '"+criteriaData[y]+"' : ")
                    if inputValue.isdigit():
                        alternativeValue.append(int(inputValue))
                        break
                    else:
                        print("Please input number")
                        continue
            else:
                while True:
                    inputValue = input("Input value for '"+str(subCriteriaData[y])+"' : ")
                    if inputValue in subCriteriaData[y]:
                        break
                    else:
                        print("Please choose one between '"+str(subCriteriaData[y])+"'")
                        continue
                alternativeValue.append(subCriteriaData[y].index(inputValue)+1)
        alternative.append([alternativeName, alternativeValue])


# input case title
title = input("Input your case title : ")

# input criteria
while True:
    totalCriteria = input("How many criteria : ")
    if totalCriteria.isdigit() :
        inputCriteria(int(totalCriteria))
        inputPriority(len(criteria))
        break
    else:
        print("Please input number")
        continue


# input alternative
while True:
    totalAlternative = input("How many alternative : ")
    if totalAlternative.isdigit():
        inputAlternative(int(totalAlternative), criteria, subCriteria)
        break
    else:
        print("Please input number")
        continue


# create table
tableTitle = ["Alternative"]
for item in criteria:
    tableTitle.append(item)
table.field_names = tableTitle

for i in range(len(alternative)):
    content = []
    content.append(alternative[i][0])
    for item in alternative[i][1]:
        content.append(item)
    table.add_row(content)

print("============================")
print("alternative table")
print(table)


# normalization
matrixData = []
for row in range(len(alternative)):
    matrixDataList = []
    for col in range(len(criteria)):
        value = alternative[row][1][col]
        divisionValue = []
        for i in range(len(alternative)):
            divisionValue.append(alternative[i][1][col])

        # print(divisionValue)

        if criteriaDescription[col] == "profit":
            result = value/max(divisionValue)
        else:
            result = min(divisionValue)/value
        
        matrixDataList.append(result)
    matrixData.append(matrixDataList)


# visualize matrix
print("============================")
print("matrix result")
visualizeMatrix = reshape(matrixData, (len(matrixData), len(matrixData[0])))
print(visualizeMatrix)


# ranking
ranking = []
for row in range(len(matrixData)):
    value = 0
    valuePerRow = []
    for col in range(len(matrixData[row])):
        priorityValue = priority[col]/100
        position = matrixData[row][col]
        valuePerPosition = position*priorityValue
        valuePerRow.append(valuePerPosition)
    for item in valuePerRow:
        value += item
    ranking.append(value)

print("============================")
print("ranking result")
for i in range(len(ranking)):
    print(alternative[i][0]+" => "+str(ranking[i]))

# conclusion
print("============================")
alternativeNameResult = ranking.index(max(ranking))
print("recommendations for cases "+title+" is : "+alternative[alternativeNameResult][0])

