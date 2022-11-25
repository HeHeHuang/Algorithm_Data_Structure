# # 闭包
# # def config_name(name):
# #     def say_info(info):
# #         print(name + ':' + info)
# #     return say_info


# # f = config_name('张三')
# # f2 = config_name('HH')

# # f('我回家啦')
# # f2('好的,收到')

# # 面向对象之搬家具
# # class Hourse():
# #     def __init__(self, location, area, left):
# #         self.location = location
# #         self.area = area
# #         self.left = left
# #         self.furnList = []

# #     def containFur(self, Furn):
# #         self.furnList.append(Furn)
# #         print(self.furnList)

# #     def __str__(self):
# #         return f'location is {self.location}, area is {self.area} , left area is {self.left}, furn is {self.furnList}'


# # class Furn():
# #     def __init__(self, name, area):
# #         self.name = name
# #         self.area = area

# #     def showInfo(self):
# #         print(self.name + 'Area:' + str(self.area))


# # table = Furn('table', 33)
# # chair = Furn('chair', 22)

# # table.showInfo()
# # chair.showInfo()


# # haoji = Hourse('haoji', 33, 11)
# # print(haoji)
# # haoji.containFur(table)
# # haoji.containFur(chair)
# # for i in haoji.furnList:
# #     print(i.name)

# # # 继承
# # class Father0(object):
# #     def func01(self):
# #         print('this is father')


# # class Children(Father0):
# #     def __init__(self):
# #         self.name = 'Father'

# #     def func01(self):
# #         print('this is son')

# #     def func02(self):
# #         print('this is son')

# #     def callFather(self):
# #         # why need this?  如果不初始化 Father的属性, Fun01就答应不了Father的属性
# #         Father0.__init__(self)
# #         Father0.func01(self)   # 这里的self 指的是children的实例么? 如果没有,会发生什么? 会报错.
# #         # 因为, 不通过实例 找不到Father的. 也就报错了.
# #     def callFartherSuper(self):
# #         super().func01()
# #         super(Children,self).func01()


# # f1 = Father0()
# # c1 = Children()

# # c1.func01()
# # c1.func02()
# # c1.callFather()
# # c1.callFartherSuper()


# # # 多态
# # # 使用多态去实现上传功能

# # # 1. 定义父类
# # class Upload(object):
# #     def uploadDocs(self):
# #         print("upload documents....")

# # # 2. 定义子类继承父类


# # class UploadExcel(Upload):
# #     def uploadDocs(self):
# #         print("upload excel....")


# # class UploadWrod(Upload):
# #     def uploadDocs(self):
# #         print("upload Word....")


# # class UploadPPT(Upload):
# #     def uploadDocs(self):
# #         print("upload ppt....")

# # # 调用者 需要传入父类, 使用父类的方法


# # class Person(object):
# #     def uploadDocuments(self, Upload):
# #         Upload.uploadDocs()


# # p1 = Person()
# # u1 = UploadExcel()
# # u2 = UploadWrod()
# # u3 = UploadPPT()

# # ulist = []
# # ulist.append(u1)
# # ulist.append(u2)
# # ulist.append(u3)
# # for i in ulist:
# #     p1.uploadDocuments(i)

# # #static method
# # class Dog(object):
# #     @staticmethod
# #     def infoprint():
# #         print("this is static method")


# # wangcai = Dog()
# # wangcai.infoprint()
# # Dog.infoprint()


# # # exception

# # try:
# #     print(num)
# # except (NameError, Exception) as result:
# #     print(result)


# # try:
# #     print(num)
# # except (Exception) as result:
# #     print(result)
# # else:
# #     print('print information that program not throw erro')
# # finally:
# #     print('Do the thing no matter there is exception or not')

# # # Self define exception


# # class ShortItemException(Exception):
# #     def __init__(self, length, min_len):
# #         self.length = length
# #         self.min_len = min_len

# #     def __str__(self):
# #         return f'the minimun length of input is {self.min_len}, you fill {self.length}'


# # def main():
# #     try:
# #         password = input("please fill in password")
# #         if len(password) < 3:
# #             raise ShortItemException(len(password), 3)
# #     except Exception as result:
# #         print(result)
# #     else:
# #         print('Password set successfully')


# # main()

# # # 递归

# # def return_num(num):
# #     if num == 1:
# #         return 1
# #     return num + return_num(num-1)

# # print(return_num(3))


# # # lambda
# # print(lambda: 100)
# # def func(): return 100
# # func = lambda: 100

# # print(func)
# # print(func())


# # func01 = lambda a,b: a+b
# # print(func01(1,2))

# # #lambda with parameters, and default parameters.
# # func01 = lambda a, b , c= 100 : a+b+c
# # print(func01(1,2))
# # print(func01(1,2,3))


# # #lambda with *args   return: tuple
# # func02 = lambda *args : args
# # print(func02(1,2,3,4))
# # print(func02(1,2,3))

# # #lambda with **kwargs
# # func03 = lambda **kwargs : kwargs

# # print(func03(name='HH'))
# # print(func03(name='HH',age = 18))

# # #lambda with if
# # func04 = lambda a,b :a if a > b else b
# # print(func04(100,50))

# # #lambda with sort function
# # students = [{'name' : 'HH','age' : 18},{'name' : 'QQ','age' : 19}]

# # #func05 = lambda x : x['name']
# # students.sort(key=lambda x : x['name'])
# # print((students))

# # Advance function

# # TODO: #函数式编程


# # def handleNum(a,b,f):
# #     return f(a) + f(b)

# # print(handleNum(-1,2,abs))
# # print(handleNum(1.2,1.9,round))


# # #NOTE: MAP() 
# # def numQuart(x):
# #     return x ** 2

# # lit = [1,2,3,4,5]
# # print(map(numQuart,lit ))  # return 迭代器 
# # print(list(map(numQuart,lit)))

# # # #NOTE: Reduce()
# # def numMul(a,b):
# #     return a * b 

# # lit = [1,2,3,4,5]

# # import functools

# # result = functools.reduce(numMul,lit)
# # print(result)

# #NOTE: filter 

# lit = [1,2,3,4,5]
# def filterNum(x):
#     return x > 4

# result = filter(filterNum,lit)
# print(result)
# print(list(result))

# def filterNum1(x):
#     return x % 2 ==0 

# result1= filter(filterNum1,lit)
# print(result1)
# print(list(result1))