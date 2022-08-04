# using print() display variables value 
# by using(,)
name="ANJALI"
age=25
cgpa=9.27
print("\n OUTPUT USING (,) ")
print('NAME = ',name)
print('AGE = ',age)
print('CGPA = ',cgpa)

# by using (+)
# (+) operator can only be used when strings are to be
# concatinte else covert int and float to str and then use (+) operator
print("\n OUTPUT USING (+) ")
print('NAME = '+name)
print('Age = '+str(age))
print("CGPA = "+str(cgpa))

# print() using sep attribute
# sep = seperator attribute; seperates two values by provided symbol
print("\n USE OF SEP ATTRIBUTE")
x=10
y=5
print(x,y,sep=",")

# output without sep 
print("\n WITHOUT SEP ATTRIBUTE ")
print(x,y)
print("x=",x,"y=",y)

# different way of storing values 
x,y,z = 10,20,30
print(" \n DIFFERENT STORING METHOD")
print(x,y,z)

# STORING BOOL VALUE AND OBTAINING OUTPUT
male = True   
# for bool T of True should be always capital followed by lowercase ; same for F of False
print("\n BOOLEAN OUTPUT ")
print(male)