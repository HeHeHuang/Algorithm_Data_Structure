
# Drop contants,  if pass 10 and print 20 , we wouldnt 
#say it O(2n), we drop contant

def print_item(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
        
print_item(10)