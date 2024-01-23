number=int(input("enter any value"))
temp=number
reverse=0
while(number>0):
    dig=number%10
    reverse=reverse*10+dig 
    number=number//10 
if temp==reverse:
    print('number is a palindrome')
else:
    print('number is not palindrome') 


a=str(input("enter string"))
b=a[-1::-1]
if(a==b):
    print('palindrome string')
else:
    print('not palindrome string')