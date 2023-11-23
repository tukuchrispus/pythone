#declare and initialize two variable
num1=6
num2=9
#print the out put
print('This is output')
#coverting int Data into str
#there are two types of conversion in python
#IMPLICITY-AUTOMATIC TYPE CONVERSION
#EXPLICITY-MANUAL TYPE CONVERSION

#CONVERTING INTEGER INTOFLOAT
integer_number=123
float_number=1.23
new_number=integer_number+float_number#Displays new value and resolution Data type
print("value:",new_number)
print("Data Type:",type(new_number))#output
#value:124.23
#Data Type:<class 'float'>
num_string='12'
num_iteger=23
print("Data type of num_string before Type casting:",type(num_string))
#Explicity type conversion
num_string=int(num_string)
print("Data type of num_string after Type casting:",type(num_string))
num_sum=num_integer+num_string
print("sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
#output
#Data type of num_string before Type Casting:<class str>
#Data type of num_string after Type casting:<class int>
#sum:35
#Data type of num_sum: <class int>

