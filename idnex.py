'''
n = 6

 result_list = [ i**2 for x in range(0, n+1) ]

'''
'''
n = 5 
result = [1 for x in range(n)]
'''


''' 
list_nums = [12, 19 , 27 , 89 , 23]

result = [i%3 == 0 for i in list_nums]
'''

'''
list_nums = [12, 19 , 27 , 89 , 23]

result = [i*2 for i in list_nums if i%3 ==0]
'''

'''
inp = input("type numbers with spaces: ")

result = [i for i in inp.split(' ')]
'''
'''
text = 'python'

result = [el for el in text]
'''
'''
result = [x for x in range(100 , 201) if x%2 == 0 or x%3 == 0]
'''
'''
names = ['gaga' , 'gio' , 'irakli' , 'nikolozi']

result = [x for x in names if len(x) >=4]
'''



'''
nums = [12,32,2,424,24353,244535,4342,232455326854]

result = ['even' if x%2 == 0 else 'odd' for x in nums ]
'''

'''
nums = [12,32,2,424,24353,244535,4342,232455326854]

result = [f'{x} is even' if x%2 == 0 else f' {x} is odd' for x in nums ]
'''

'''
list1 = [1,2,3]

list2 = [11,22,33]

result = [(i , j)
    for i in list1
    for j in list2
]
'''
'''ls = [10,11,12,13]

ite = iter(ls)

print(next(ite)) #გამოიტანა current ელემენტი, ანუ ls[0]
print(next(ite))
print(next(ite))
print(next(ite)) #ბევრჯერ გამოძახებით გამოაქ შემდეგი ელემენტი'''


'''
result = [ [f'{i} * {j} = {i *j}' ]
    for i in range(0 , 11)
    for j in range(0 , 11)
]
'''


'''
matrix = [ [1,2,3] , [4,5,6] , [7,8,9] ]

result = [x for combos in matrix for x in combos]
'''

'''
matrix = [ [1,2,3] , [4,5,6] , [7,8,9] ]

result = [ [x**2 for x in combos] for combos in matrix ]
'''



'''result = [x**2 for x in [x+5 for x in range(1,6)] ]


print(result)'''


'''dict = {
    "gio" : 1,
    "nika" : 2,
    "luka" : 3,
    "sandro" : 4
}'''

'''list = [
    ['ch',1,'playoff1'],
    ['geo',2,'playoff2'],
    ['alb',3,'playoff3'],
    ['uk',4,'playoff4']
]

dict_transform = {key:(value,place) for key,value,place in list}

print(dict_transform)'''


'''ls = [10,11,12,13]

gen = (x**2 for x in ls)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))'''


ls = [x for x in range(10000)]

for i in ls:
    if i>1000:
        break
        print(x,end="")