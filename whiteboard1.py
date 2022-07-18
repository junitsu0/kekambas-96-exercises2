```
#write function of random number
def even_or_odd(num):
#determine if number is even dividing by 2
    if num%2==0:
#return FIZZ if true
        return "FIZZ"
#if false then its odd
    if num%2!=0:
#return BUZZ
        return "BUZZ"


print(even_or_odd(1002))