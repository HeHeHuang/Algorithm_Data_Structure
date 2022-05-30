head = {
    'value': 12,
    'Next': {
        'value':23,
        'Next':{
            'value':18,
            'Next':None
        }
    }
}

print(head['Next']['Next']['value'])
 

# change to linked list mindset
#print(my_linkelist.head.next.next.value)
mylist = [1,2,3,4]
print(id(mylist[0]))
print(id(mylist[1]))
print(id(mylist[2]))
print(id(mylist[3]))
print(id(mylist))


mylist_string = ['1','2','3','4']
print(id(mylist_string[0]))
print(id(mylist_string[1]))
print(id(mylist_string[2]))
print(id(mylist_string[3]))
print(id(mylist_string))