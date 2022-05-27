from prettytable import PrettyTable
from numpy import *
from lib.alternative import *
from lib.criteria import *

table = PrettyTable()

criteria_list = []
alternative_list = []

def input_criteria(total):
    for i in range(total):
        criteria_name = input("Criteria name "+str(i+1)+" : ")
        criteria_list.append(Criteria(criteria_name))

        while True:
            criteria_desc = input("Criteria "+criteria_name+" incldude (profit/loss) : ")
            if criteria_list[i].validate_desc(criteria_desc):
                criteria_list[i].desc = criteria_desc
                break
            else:
                print("Please input 'profit' or 'loss'")
                continue

        while True:
            criteria_sub = input("Criteria "+criteria_name+" include sub criteria (y/n) : ")
            if criteria_list[i].validate_have_sub_criteria(criteria_sub):
                break
            else:
                print("Please input 'y' or 'n'")
                continue
        
        if criteria_sub == "y":
            while True:
                criteria_sub_count = input("How many sub criteria of "+criteria_name+" : ")
                if criteria_sub_count.isdigit():
                    break
                else:
                    print("Please input number")
                    continue
            
            for j in range(int(criteria_sub_count)):
                criteria_list[i].add_sub_criteria(input("Sub criteria name number "+str(j+1)+" : "))
            

        while True:
            criteria_priority = input("Input priority for criteria '"+criteria_name+"' (1-100) : ")
            if criteria_priority.isdigit():
                if criteria_list[i].validate_priority(int(criteria_priority)):
                    criteria_list[i].priority = int(criteria_priority)
                    break
                else:
                    print("Please input number between 1-100")
                    continue
            else:
                print("Please input number")
                continue


def input_alternative(total):
    for i in range(total):
        alternative_name = input("Input alternative name number "+str(i+1)+" : ")
        alternative_list.append(Alternative(alternative_name))

        for j in range(len(criteria_list)):
            if criteria_list[j].sub_criteria == []:
                while True:
                    alternative_value = input("Input value for criteria '"+criteria_list[j].name+"' : ")
                    if alternative_value.isdigit():
                        alternative_list[i].add_attribute(int(alternative_value))
                        break
                    else:
                        print("Please input number")
                        continue
            else:
                while True:
                    alternative_value = input("Input value for criteria '"+str(criteria_list[j].sub_criteria)+"' : ")
                    if alternative_value in criteria_list[j].sub_criteria:
                        break
                    else:
                        print("Please choose one between '"+str(criteria_list[j].sub_criteria)+"'")
                        continue
                get_index_attribute = criteria_list[j].sub_criteria.index(alternative_value)
                alternative_list[i].add_attribute(get_index_attribute+1)
        

        
# input case title
title = input("Input your case title : ")

# input criteria
while True:
    totalCriteria = input("How many criteria : ")
    if totalCriteria.isdigit() :
        input_criteria(int(totalCriteria))
        break
    else:
        print("Please input number")
        continue


# input alternative
while True:
    totalAlternative = input("How many alternative : ")
    if totalAlternative.isdigit():
        input_alternative(int(totalAlternative))
        break
    else:
        print("Please input number")
        continue

# create table
tableTitle = ["Alternative"]
for criteria in criteria_list:
    tableTitle.append(criteria.name)
table.field_names = tableTitle

for i in range(len(alternative_list)):
    content = []
    content.append(alternative_list[i].name)
    for attr in alternative_list[i].attribute:
        content.append(attr)
    table.add_row(content)

print("============================")
print("alternative table")
print(table)

# normalization
matrix_data = []
for row in range(len(alternative_list)):
    matrix_data_list = []
    for col in range(len(criteria_list)):
        value = alternative_list[row].attribute[col]
        division_value = []
        for i in range(len(alternative_list)):
            division_value.append(alternative_list[i].attribute[col])

        if criteria_list[col].desc == "profit":
            result = value/max(division_value)
        else:
            result = min(division_value)/value
        
        matrix_data_list.append(result)
    matrix_data.append(matrix_data_list)

# visualize matrix
print("============================")
print("matrix result")
visualize_matrix = reshape(matrix_data, (len(matrix_data), len(matrix_data[0])))
print(visualize_matrix)

# ranking
ranking = []
for row in range(len(matrix_data)):
    value = 0
    value_per_row = []
    for col in range(len(matrix_data[row])):
        priority_value = criteria_list[col].priority/100
        position = matrix_data[row][col]
        valuePerPosition = position * priority_value
        value_per_row.append(valuePerPosition)
    for item in value_per_row:
        value += item
    ranking.append(value)

print("============================")
print("ranking result")
for i in range(len(ranking)):
    print(alternative_list[i].name+" => "+str(ranking[i]))

# conclusion
print("============================")
alternative_result = ranking.index(max(ranking))
print("recommendation for case "+title+" is : "+alternative_list[alternative_result].name)