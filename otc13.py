import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if (a+b)>c and (b+c)>a and (a+c)>b:
   p=(a+b+c)/2
   S=math.sqrt(p*(p-a)*(p-b)*(p-c))
   print("Dien tich=",round(S,3),sep="")
else:
  print("Khong hop le")