#add item into dictionary
my_dict = {}
my_dict['name']='HH'
print(my_dict)
my_dict_1 = {num: num * num  for num in range(1,10) }
print(my_dict_1)

#modify value 
my_dict_1[9] = 82
print(my_dict_1)
for key in my_dict_1:
    print(key,my_dict_1[key])

# remove key-pair in dictionary

del my_dict_1[9]
print(my_dict_1)

#access value in dictionary
# if we just use the key value ,if will throwing exception when that is no key 

print(my_dict_1.get(2))

print(my_dict_1.get(10))
#print(my_dict_1[10])


#Loop through dictionary 
