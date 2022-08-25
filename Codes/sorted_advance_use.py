students=[
    {"name":"hari","score":90,"age":22},
    {"name":"krishna","score":80,"age":24},
    {"name":"narayan","score":70,"age":20},
    {"name":"sagar","score":95,"age":26}
    
]

sorted_students = sorted(students , key = lambda a : a['age'],reverse= True)
print(sorted_students)

fruits = ('apple','mango','grapes') 
print(sorted(fruits)) # ['apple', 'grapes', 'mango'] same for sets
