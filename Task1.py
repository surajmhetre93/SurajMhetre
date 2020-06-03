"""
1.	Create three variables in a single line and assign different values to them and make sure their data types are different.
Like one is int, another one is float and the last one is a string.
"""
var1, var2, var3 = 1, 2.5, "Suraj"
print(var1, var2, var3)

"""
2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
"""
var4, var5 = 2+1j, 5
print("Before Swapping:\nvar4=", var4, "\nvar5=", var5)
var4, var5 = var5, var4
print("After Swapping:\nvar4=", var4, "\nvar5=", var5)

"""
3. 	Swap two numbers using the third variable as result name and do the same task without using any third variable.
"""
# Using 3rd variable
var6, var7 = "Consultadd", 52.52
print("Before Swapping:\nvar6=", var6, "\nvar7=", var7)
varTemp = var6
var6 = var7
var7 = varTemp
print("After Swapping:\nvar6=", var6, "\nvar7=", var7)

# Without using third variable
var6, var7 = "Consultadd", 52.52
print("Before Swapping:\nvar6=", var6, "\nvar7=", var7)
var6, var7 = var7, var6
print("After Swapping:\nvar6=", var6, "\nvar7=", var7)

"""
4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
"""
userInput1 = input("Enter any value:")
print("Value entered is:", userInput1)

"""
5. 	Write a program to complete the task given below:
Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
Use z for adding 30 into it and print the final result by using variable result.
"""
number1, number2 = input("Enter 2 numbers between 1 and 10 separated by space:").split(" ")
z = int(number1) + int(number2)
z += 30
print("z:", z)

"""
Write a program to check the data type of the entered values. HINT: Printed output should say -  
The input value data type is: int/float/string/etc
"""
input_value = eval(input("Enter any value:"))
print("The input value data type is:", str(type(input_value)))

"""
8. 	If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. 
Will it change the value. If Yes then Why?
-- Yes. Variables by definition can hold any type of data and can be assigned values multiple times.
"""