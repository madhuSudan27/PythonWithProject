
# # function in python 

# def say_myName():
#     print("Anand")

# # say_myName()
# # default argument
# def greeting(name ,greet='Hello'):
#     print(f'{greet} {name}!')

# greeting('anand')


# #  named argument 
# greeting(name='Shreyash', greet='Hey')

# def sum(a,b):
# return a+b

def calculateFoodTotal(food_amount: float , tip_percentage: float)-> float:
    return (food_amount+(food_amount*(tip_percentage/100)))

# print(calculateFoodTotal(120.3,24))

# lamda function  <-  anonymous function

def sum(a,b):
    return a+b

# implicit return 
sum2= lambda a,b:a+b
# lambda arg1, arg2 : <expression>

# print(sum2(1,2))

greet = lambda name, greet :f'{greet} {name}'

# print(greet('Rohan','Hello'))

# Assert testing 



# arrays <-- list
'''
numbers=[10,20,30]
numbers.append(40)
print(numbers)

# slicing 
print(numbers[0:2])
n=len(numbers)
print('Hi my name is anand'[0:5])
print(numbers[::-1])
'''
#  dictionary 
Person={
    'name':'anand',
    'shirt':'black'
}

#touples
# touples are immutable

# number=(1,2)

# sets -> {}


# LOOP CONCEPTS 
# number=[1,2,3,4,5,6,7,8]
# for num in number:
#     print(num)

fruits=['banana','apple','orange','kiwi','mango','pulm','grapes']

# for fruit in enumerate(fruits):
#     print(fruit[0])
#     print(fruit[1])

# for num in range(10):
#     print(num)

#  this double wii double all the elements of array 
def double(numbrs : list) ->list :
    temp=[]
    for num in numbrs:
        temp.append(num*2)
    return temp

def count_word(phrase : str)-> int:
    #  this will count each character including space 
    #  need to split 
    counter=0
    # split will convert into a  list 
        # for word in phrase.split():
        #     counter+=1

    return len(phrase.split())
    # return counter

# print(double([1,2,3,4,5]))
# print(count_word("hi my name"))

def find_max(numbers :list) ->int:
    max_value=numbers[0]
    for num in numbers:
        if(max_value<num):
            max_value=num
    
    return max_value

# print(find_max([1,2,4,546,768,9879,54643,34,432,34,43,435465]))

#  dictionary practice
    # dictionary can have only unique key inside 
def word_frequency(words: str)-> int:
    result={}
    #  we need to split the word for freq count 
    for word in words.split():
        if word not in result:
            result[word]=1
        else:
            result[word]+=1
        
    return result


# print(word_frequency("i am madhusudan i am from bihar  i love coding and problem solveing , i do leetcode regularly"))


#  higher order function 

    # map
    # filter

#  map

def double_number( number: int)-> int:
    return number*2


# print(list(map(double_number,[1,2,3,4,5,6])))


#  we can do it on the fly using lambda function 
    #  this will double it on the fly 
# print(list (map(lambda num :num*2,[1,2,3,4,5])))


#  filter 


numbers=[1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15]

# print(list(filter(lambda num:num%2==0,numbers)))


#  list comprehension 


print([number for number in numbers if number%2==0])
#             .....................
#      ......                       ..............

print([ number for number in numbers if number%2!=0])

print([ number*2 for number in numbers ])


# we have some built in functions like:- sum, max, min 





