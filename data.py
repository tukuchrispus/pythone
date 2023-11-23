num1=5
print(num1,'is of type' ,type(num1))
num2=2.0
print(num2,'is of type',type(num2))
num3=1+2j
print(num3,'is of type',type(num3))

#python list Data Type
languages=["swift","Java","python"]
print(languages)
#Access element at index 0
print(languages[0])#swift
print(languages[2]) #python

#python turple Data TYPE
Product=('xbox',499.99)
print(Product)
#acessing TURPLE
Product='microsoft', 'xbox',499.9
#Acessing element at index 0
print(Product[0])
print(Product[1])    
#string data types
name='python'
print(name)
message='python for beginners'
print(message)
#python set Data type
#create set name student_id
student_id={112,113,114,116,118,115}
#display student_id
print(student_id)
#output
#{112,113,114,116,118,115}
#<class 'set,>

#dictionary Data type
#create adictionary named capital_city
capital_city={'Nepal':'kathmandu','italy':'rome','England':'London'}
print(capital_city)
#int the above example we have created a dictionary capital_city
#1.KEYS are 'Nepal','italy','England'
#2.Values are 'KATHMANDU','Rome','London

#Access Dictionary named Capital_city
capital_city={'Nepal':'Kathmandu','italy':'Rome','England':'London'}
Print(capital_city['Nepal'])#Prints Kathmandu
print(capital_city['Kathmandu'])#Throwsnerror message
