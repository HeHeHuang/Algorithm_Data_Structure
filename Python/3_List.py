# from fileinput import close


# bicyle = ['treck','sumrun','papaer']
# print(bicyle)
# for i in bicyle:
#     print(i,end = '\t')
 
# print('\n-------------')
# for i in bicyle:
#     print(i)

# #Try it 
# names = ['hh','qq','mm']
# for i in names:
#     print(f'hello, {i}')

# # add 
# # append
# names.append('yy')
# print(names)
# #insert
# names.insert(2,'zz')
# #change
# print(names[1])
# names[1] = 'ss'
# print(names[1])
# print(names)
# # remove 
# del names[2]
# print(names)
# #pop without index, it will return the last item in list 
# print(names)
# last_person_name= names.pop()
# print(last_person_name)
# # with index, it will return the item where the index is 
# print(names)
# first_person_name = names.pop(0)
# print(first_person_name)
# print(names)
# #remove item by value 
# names.remove('ss')
# print(names)

# # Try it 

# names = ['hh','ss','qq','mm']
# print(names)
# names[1]= 'yy'
# print(names)
# names.insert(0,'aa')
# names.insert(2,'ll')
# names.append('zz')
# print(names)
# uninvite_name = names.pop()
# print(names)
# print(f'{uninvite_name}, i am sorry.')

# # # remove name one by one using for loop 
# # for i in range(2,len(names)):
# #     uninvite_name = names.pop()
# #     print(f'{uninvite_name}, I am sorry!')

# print(names)

# # remove name one by one using while loop 
# num =len(names)
# while num > 2:
#     uninvite_name = names.pop() 
#     print(f'{uninvite_name}, I am sorry!')
#     num -=1

# del names[1]

# del names[0]
# print(names)


# Origing list 

# names = ['hh','ss','qq','mm']
# for name in names:
#     print(f'{name} welcome to my party!')

 
# pizzas = ['Cheese','Veggie','Pepperoni','Meat','Margherita']
# for pizza in pizzas:
#     print(pizza)

# # make numerical lists
# for i in range(1,5):
#     print(i)

# #make a list of number 
# numbers = list(range(1,5))
# print(numbers)

# numbers_1 = [x for x in range(1,5)]
# print(numbers_1)

# even_number = list(range(2,11,2))
# print(even_number)

# even_number_1 = [x for x in range(2,11,2)]  
# print(even_number_1)

# square_number = [x*2 for x in range(1,7)]
# print(square_number)

#work part of list 


 
pizzas = ['Cheese','Veggie','Pepperoni','Meat','Margherita']
# print(pizzas[0:3])

# print(pizzas[-3:])

# for pizza in pizzas[1:3]:
#     print(f'{pizza} pizza is delivering.')


# copying a list 
#hard copy 
# soft copy 
# import copy
# id(pizzas)
# print(id(pizzas))
# x = copy.copy(pizzas)

# y = copy.deepcopy(pizzas)
# print(id(x))
# print(id(y))


# for pizza in pizzas:
#     print(f'we offer {pizza} pizza.')

# import copy 
# value = 3
# print(id(value) )
# new_value = copy.copy(value)
# print(id(new_value) )


# import copy 
# my_list = [1,2,3,4]
# print(id(my_list) )
# new_list = copy.copy(my_list)
# print(id(new_list) )


# new_list_2 = my_list[:]
# print(id(new_list_2) )


for i, pizza in enumerate(pizzas):
    print(i, pizza)

pizzas_object = enumerate(pizzas)
print(list(pizzas_object))