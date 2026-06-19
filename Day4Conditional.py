#conditional statements in Python

light = "green"

if light =="red":
    print("stop")
elif light =="green":
    print("go")  
elif light =="yello":
    print("look")  
print("end of code")    



age = 21 
if age >=18:             
    print("can vote")
else:   
    print("cannot vote ")  



#grade student based on marks
marks = int(input("enter the marks"))

if marks>=90:
    print("Grade A") 
elif marks >=80 and marks <90:
    print("Grade B")
elif marks >=70 and marks <80: 
      print("Grade C") 
else:
    print("grade D ")

print("marks of student ")  


#nesting 
age = 90

if (age >=18):
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive") 

print("driving information")

#Q WAp to check if number entered by the user is odd or even.

num = int(input("enter number: ")) 

if(num % 2 ==0):
    print("even")
else:
    print("odd")    


#QWAP to find the gretest of 3 numbers entered by the user.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if (a>=b and b>=c):
    print("first num is large",a)
elif(b>=c):
    print("second num lagre",b)
else:
    print("third num lagre",c)        


#Q WAP to check if a number is a multiple of 7 or not.

x = int(input('enter number:'))


if(x % 8 == 0):
    print("multiple of 8")
else:
    print("not multiple 8")    

