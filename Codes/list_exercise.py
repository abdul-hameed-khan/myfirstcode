num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_list(l):
    s_list = []
    for i in l:
        s_list.append(i**2)
    return s_list

print(square_list(num))

# # # reversed list

def reverse_list(l):
# # 1
#     # r_list = []
#     # for i in l[::-1]:
#     #     r_list.append(i)
#     # return r_list
# # 2
#     # return l[::-1]
# # 3
#     # return l[::-1]

# # 4
    r_list = []
    for i in range(len(l)):
        i  = l.pop()
        r_list.append(i)
    return r_list

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reverse_list(n))

# even odd

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_odd(l):
    e_list  = []
    o_list  = []
    for i in l:
        if i % 2 == 0:
            e_list.append(i)
        else:
            o_list.append(i)
    w_list = [o_list,e_list]
    return w_list

print(even_odd(num))


# common elements of lists

# n1 = [1, 2, 3, 4, 6, 7, 9, 10]
# n2 = [2,8,4,5,1,9]

# def common_elements(l1,l2):
#     elements = []
#     for i in l1:
#         # for j in l2:
#         #     if i == j: # my own logic
#         if i in l2:
#                 elements.append(i)
#     return elements

# print(common_elements(n1,n2))


# # how much lists inside lists

# num = [1,2,3,[5,6,8],5,[9,5,41]]

# # def no_of_lists(l):
    

# # print(no_of_lists(numb))

# # reversed elements of lists

words = ['abc','mno','tuv','xyz']

def reversed_elments(l):
# # 1
#     # r_list = []
#     # for i in range(len(l)):
#     #     j = l.pop()
#     #     r_list.append(j[::-1])
#     # return r_list[::-1]
# # 2
    r_list = []
    for i in l:
        r_list.append(i[::-1])
    return r_list

print(reversed_elments(words))


