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
3. 	Create a list of given structure and run 
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list [1, 2, 3, 4]
Access list [600,  700]
Access list [100, 300, 500, 600, 800]
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list [10]
Access list [ ]
"""
x: List[Union[int, List[Union[int, List[int]]]]]=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
x1 = x[5][:4]
x2 = x[6:7]
x3 = x[::2]
x4 = x[::-1]
x5 = x[5][5][0]

"""
4. 	Create a list of thousand number using range and xrange and see the difference between each other.
"""
from typing import List, Union

from pip._vendor.msgpack.fallback import xrange
lst1 = list(range(1, 1001))
lst2 = list(xrange(1, 1001))
print("List using range():", lst1)
print("List using xrange():", lst2)

"""
5. 	How Tuple is beneficial as compare to the list?
ANSWER:
Tuple can also be used as key in dictionary due to their hashable and immutable nature 
whereas Lists are not used as key in a dictionary because list can't handle __hash__() and have mutable nature.
"""


"""
6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 2 == 0:
        print(i, end=' ')

"""
7. 	Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.
"""
user_string = input("Enter a string:")
for ch in user_string[::-1]:
    if ch.isalpha() and ch.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(ch, user_string.index(ch))
"""
8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.
"""
string_list = "hello my name is abcde".split(' ')
for word in string_list:
    if len(word) % 2 == 0:
        print(word)

"""
9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
"""
result_number = 8
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
x.sort()
for i in x:
    if result_number-i in x:
        print(i, result_number-i)

"""
10. 	Write a program in Python to complete the following task:
*Create two different list as in even_list and odd_list
*Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
*Keep that in mind you can only add 5 items in each list
*Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.
"""
def main() -> object:
    even_list = []
    odd_list = []

    count_even = 0
    count_odd = 0

    while count_even < 6 and count_odd < 6:
        try:
            input_number = int(input("Enter a number for either of odd list/even_list:"))
            if input_number % 2 == 0 and input_number in range(1, 51):
                even_list.append(input_number)
                count_even += 1
            elif input_number in range(1, 51):
                odd_list.append(input_number)
                count_odd += 1
            else:
                raise ValueError
        except ValueError:
            print("Make sure to enter the integer number in the range of 1,50. Try again!")
        except Exception as ex:
            print(ex.msg)
    return sum(even_list), max(even_list), sum(odd_list), max(odd_list)


print("""
Sum of even_list = %d
Max of even_list = %d
Sum of odd_list = %d
Max of odd_list = %d
""" % main())

"""
11. Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  
    Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
"""
example = "12abcbacbaba344ab"
result = {}
for ch in example:
    if ch.isalpha():
        if ch not in result.keys():
            result[ch] = 1
        elif ch in result.keys():
            result[ch] += 1

print(result)

"""
12. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""
given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
another_tuple = (i for i in given_tuple if i % 2 == 0)
print(another_tuple)