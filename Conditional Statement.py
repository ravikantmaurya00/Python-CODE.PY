print("if")
a=int(input("Enter the value1:-"))
if a%2==0:
	print(a,"Even Numbers")
print()
print('if else')
b=int(input("Enter the value1:-"))
if b%2==0:
	print(b,"Even Numbers")
else:
	print(b,"Odd Numbers")
print()
print("if elif else")
c=int(input("Enter the value1:-"))
if c>=60:
	print(c,"First Division")
elif c>=45:
	print(c,"Second Division")
elif c>=35:
	print(c,"Third Division")
else :
	print(c,"Fail")