def factorial(n):
     if n==0 or n==1:
          return 1
     else:
         return n*factorial(n-1)
def npr(n,r):
     if n<r:
        return "error:n should be greater than or equal to r:"
     else:
         return factorial(n)
n_value=int(input("enter the value of n:"))
r_value=int(input("enter the value of r:"))
result=npr(n_value,r_value)
print(f"{n_value}p{r_value}is:{result}")                          
