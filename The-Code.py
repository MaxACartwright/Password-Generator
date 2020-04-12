import random as r
chars = '`1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?'

number = input('Number of Passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
  password = ''
  for c in range(length):
    password+= r.choice(chars)
  print(password)
