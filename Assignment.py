# firs we get the name and their favorite from the user
name : str =  (input ("Enter your name "))
Numbers = []
Numbers.append (int (input ("Enter your first name : ")))
Numbers.append (int (input ("Enter your 2nd name : ")))
Numbers.append (int (input ("Enter your 3rd name : ")))
#her we print the greeting message to th user with their name 
print (f"\nHello, {name}!Welcome to the number exploration tool")
# here we find even and odd using for loop
for number in Numbers:
  if number%2 == 0:
   print (f"The number {number} is even ")
else :
   print (f"The number {number} is odd")
# here we find the square of numbers given y the user
for number in Numbers:
    print (f"The number {number} and its square is : {number,number**2}")
    # here we find the sum of numbers given by the user
total = sum(Numbers)
print (f"\nAmazing! The sum of your favorite number is : {total}")

# Step 6: Check if the sum is a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(total):
    print(f"The sum, {total}, is a prime number!")
else:
    print(f"The sum, {total}, is not a prime number.")