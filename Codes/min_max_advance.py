print("min() and max() function use ")

number=[1,2,3,4,5,6,7,8]
print(f"min value number : {min(number)}")
print(f"max value number : {max(number)}")

name = ["hari","dev","krishna"] # lenth of name max 

def function(item):
    return len(item)

print(max(name,key= function)) # krishna
print(min(name,key= function)) # dev
print(max(name,key= lambda item : len(item))) # krishna

students=[
    {"name":"hari","score":90,"age":22},
    {"name":"krishna","score":80,"age":24},
    {"name":"narayan","score":70,"age":20},
    {"name":"sagar","score":95,"age":26}
]

print(max(students,key= lambda i : i.get("score"))) # {'name': 'sagar', 'score': 95, 'age': 26}
print(max(students,key= lambda i : i.get("score"))["name"]) # sagar

data_students={
    "sagar" : {"score":90,"age":23},
    "hari" : {"score":94,"age":22},
    "narayan" : {"score":99,"age":25}
}

print(max(data_students,key= lambda i : data_students[i]["score"])) # narayan



# For Strings:

names="kareem shareef is good boy".split(" ")
length=[len(i) for i in names]
print(max(length))#  7

