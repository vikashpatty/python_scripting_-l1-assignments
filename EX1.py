# Exercise – 1: Filename: ex1.py
# Implement the function ruler() which takes a number (for example, 43) as argument,
# and produces output as shown below.
#  1 2 3 4
#  1234567890123456789012345678901234567890123
# (note: 1st row values are aligned to respective 0s of the 2nd row)
# Test correctness of the function with the following values :
#  5, 10, 25, 51 and 80
#


 def  ruler(x):
  i=1
  count=0
  while True:
    for i in range(i,10):
      if(count !=x):
        print(i,end='')
        count=count+1
      else:
        break
    i=0
x=int(input("Please Enter the num"))
ruler(x)
ruler(5)
ruler(10)
ruler(25)
ruler(51)
ruler(80)
