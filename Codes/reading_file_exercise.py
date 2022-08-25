
with open('nameSalary.txt' , 'r') as f:
    with open('nameSalary_solution.txt' , 'a') as w:
        
        for i in f.readlines():
            name , salary = i.split(',')
            w.write(f'name is {name} and salary is {salary}')

        

