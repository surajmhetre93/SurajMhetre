"""
1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
"""
lst = [1, 2.5, "Consultadd", 1+2j, 2, 54.35, "Training", 9+3j, 2, 8.524]

"""
2. 	Create a list of size 5 and execute the slicing structure 
"""
lst = [1, 2.5, "Consultadd", 1+2j, 2]
print(lst[::-1])
print(lst[::2])
print(lst[2:])
print(lst[:3])

"""
3.  Write a program to get the sum and multiply of all the items in a given list.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = 0
lst2 = 1
for i in lst:
    lst1 += i
for i in lst:
    lst2 *= i
print("Sum of all numbers in the list:", lst1)
print("Multiplication of all numbers in the list:", lst2)

"""
4.  Find the largest and smallest number from a given list.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Largest element:", max(lst))
print("Smallest element:", min(lst))

"""
5. 	Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = [i for i in lst if i % 2 != 0]
print("New list which contains the specified numbers after removing the even numbers:", lst1)

"""
6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
"""
lst = [i*i for i in range(1, 31)]
print("First 5 elements of the list:", lst[:4])
print("Last 5 elements of the list:", lst[-1:-5])

"""
7.	Write a program to replace the last element in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8]
"""
lst1 = [1, 3, 5, 7, 9, 10]
lst2 =  [2, 4, 6, 8]

print(lst1[:-2].extend(lst2))

"""
8.	Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}
"""
a={1:10,2:20}
b={3:30,4:40}
c={}
for k, v in [a, b]:
    c[k] = v
print(c)
"""
9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}
"""
n = 8
dictionary = {}
for i in range(1, n+1):
    dictionary[i] = i**2
print(dictionary)

"""
10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
    Suppose the following input is supplied to the program:
34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’)
"""
from sys import argv
program_name, number1, number2, number3, number4, number5, number6 = argv
lst = list(number1, number2, number3, number4, number5, number6)
tpl = tuple(number1, number2, number3, number4, number5, number6)
print(lst)
print(tpl)