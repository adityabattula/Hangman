a = 'yes'
b = 'no'
c = ["KOBE", "HOUR", "BEST", "MAIN", "HANG", "STOP", "FIVE", "SAIF", "NOAH", "SOAP", "SONG", "REPO", "PETE"]
x = " _ "
y = " _ "
z = " _ "
Hangman_Display = input("Do you want to play Hangman? ")
if Hangman_Display == a:
 print('Ok, Lets do it! :)')
if Hangman_Display == b:
 print("Well.....we are going to do it anyway ")
d = input("Give me a number from 1 to 11. ")
e = int(d) - 1
print(c[int(e)][0] + x + y + z )
first_letter = c[int(e)][0]
g = input("Now you have to guess the remaining three letters. ")
if g == c[int(e)][1]:
 x = g
 print(first_letter + x + y + z)
elif g == c[int(e)][2]:
 y = g
 print(first_letter + x + y + z)
elif g == c[int(e)][3]:
 z = g
 print(first_letter + x + y + z)
h = input("Good, now find the remaining two letter. ")
if h == c[int(e)][1]:
 x = h
 print(first_letter + x + y + z)
elif h == c[int(e)][2]:
 y = h
 print(first_letter + x + y + z)
elif h == c[int(e)][3]:
 z = h
 print(first_letter + x + y + z)
else:
 input("Incorrect. But keep on trying. ")
 
i = print("Good, now find the remaining letter. ")
if i == c[int(e)][1]:
 x = i
 print(first_letter + x + y + z)
elif i == c[int(e)][2]:
 y = i
 print(first_letter + x + y + z)
elif i == c[int(e)][3]:
 z = i
 print(first_letter + x + y + z)
else:
 input("Incorrect. But keep on trying. ")
