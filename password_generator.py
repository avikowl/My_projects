import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
l= int(input("How many letters would you like in your password?\n"))
s = int(input(f"How many symbols would you like?\n"))
m = int(input(f"How many numbers would you like?\n"))

for n in range (0, l):
  letters[n]=letters[random.randint(0,51)]
for n in range (0, s):
  symbols[n]=symbols[random.randint(0,8)]
for n in range (0, m):
  numbers[n]=numbers[random.randint(0,9)]
total=""
total_let=str(total)
for i in range (0,l):
  total_let+=letters[i]
total_sym=str(total)
for i in range (0,s):
  total_sym+=symbols[i]
total_num=str(total)
for i in range (0,m):
  total_num+=numbers[i]
password= total_let + total_sym + total_num
print(password)
shuffled_password="".join(random.sample(password,len(password)))
print(shuffled_password)
