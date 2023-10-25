def operation_Listes (list=[]) :
    maximum = max(list)
    minimum = min(list)
    moyenne = sum(list)/len(list)
    return [maximum , minimum , moyenne ]

print(operation_Listes([1,2,3,4 , 34 , 50 , 35]))