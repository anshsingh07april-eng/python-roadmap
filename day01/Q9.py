#Q9. Fix your old Q1. Rewrite your palindrome program from the zip file so it runs without an indentation error.
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
     print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")