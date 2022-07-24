# Q1 Write a program to calculate the sum of first n terms of a geometric progression with scale factor a and common ratio r.
# (Example of input and output: Input: n = 4, a = 2, r = 3. Output will be sum of 2 + 6 + 18 + 54 = 80)

def sumofGP(a, r, n):
    sum = 0
    i = 0
    while i < n:
        sum = sum + a
        a = a * r
        i = i + 1
    return sum


print(sumofGP(2, 3, 4))


# Q2  notes:500,200,100,50   # amount = 3.350.000
def countNote(amount):
    notes = [500000, 200000, 100000, 50000]
    notesCount = {}
    for note in notes:
        if amount >= note:
            notesCount[note] = amount//note
            amount = amount % note
    for key, value in notesCount.items():
        print('{0} money notes of {1}'.format(value, key))


notesCount = countNote(3350000)

# Q3  calculate the sum of numbers from N to M in Fibonacci sequence


def sumofFibo(n, m):
    if n < 0:
        return 0
    if n > m:
        return 'please in order'
    fibo = [0] * (m + 1)
    fibo[1] = 1
    sum = fibo[0] + fibo[1]
    for i in range(2, m+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
    return fibo[n:m+1].sum()


# print(sumofFibo(3,2))
print(sumofFibo(3, 5))


# Q4 list occurrence
def listOccurrence(str):
    a = str.split(" ")
    match = {}
    outputlist = []
    for i in range(0, len(a)):
        match[a[i]] = a.count(a[i])

    for k, v in match.items():
        if v > 1:
            outputlist.append(k)
    print(outputlist)


str = "I want to know how to achieve the things I want"
m = listOccurrence(str)


# Q5 Implement this BinaryTree class
# with method getMaxDepth() to calculate the highest depth of the binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    if node is None:
        return -1
    else:
        leftDepth = maxDepth(node.left)
        rightDepth = maxDepth(node.right)

        if (leftDepth > rightDepth):
            return leftDepth+1
        else:
            return rightDepth+1


# test function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxDepth(root))
