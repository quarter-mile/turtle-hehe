from time import *
from sys import *

class text:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  NEUTRAL = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  LOADING = '\033[33m'
  QUESTION = '\033[34m'
    

def check(i):
  j = ""
  for m in i:
    if(m == 'i'):
      j = j + '1'
    elif(m == 'w'):
      j = j + '2'
    elif(m == 'k'):
      j = j + '3'
    elif(m == 't'):
      j = j + '4'
    elif(m == 'y'):
      j = j + '5'
    elif(m == 'p'):
      j = j + '6'
    elif(m == 'q'):
      j = j + '7'
    elif(m == 'e'):
      j = j + '8'
    elif(m == 'r'):
      j = j + '9'
    elif(m == 'u'):
      j = j + '0'
    elif(m == 's'):
      j = j + '@'
    elif(m == 'o'):
      j = j + 'O'
    elif(m == 'a'):
      j = j + '!'
    elif(m == 'A'):
      j = j + '!'
    elif(m == 'd'):
      j = j + '#'
    elif(m == 'm'):
      j = j + '$'
    elif(m == 'h'):
      j = j + ')'
    elif(m == 'g'):
      j = j + '%'
    elif(m == 'f'):
      j = j + '('
    elif(m == 'j'):
      j = j + '*'
    elif(m == 'l'):
      j = j + '['
    elif(m == 'z'):
      j = j + 'H'
    elif(m == 'x'):
      j = j + 'n'
    elif(m == 'c'):
      j = j + 'w'
    elif(m == 'v'):
      j = j + '.'
    elif(m == 'b'):
      j = j + 'i'
    elif(m == 'B'):
      j = j + 'i'
    elif(m == '5'):
      j = j + '='
    elif(m == 'n'):
      j = j + '?'
    elif(m == ' '):
      j = j + ']'
    elif(m == '('):
      j = j + 'q'
    elif(m == ')'):
      j = j + 'k'
    elif(m == '.'):
      j = j + '<'
    elif(m == '\''):
      j = j + '>'
    elif(m == '"'):
      j = j + 'T'
      
  return j

correct = 0
loading_string = "...loading..."
print(f"{text.LOADING}")
for letter in loading_string:
  sleep(0.1) # In seconds
  stdout.write(letter)
  stdout.flush()

sleep(2)

passA = ["i", "!", "!"]

print("\n")

print(f"{text.HEADER}\t\t\t\t-----  Its Quiz Time! -----")

sleep(1)

question_1 = "Question\t| Which command can be used to set the fill color to red?\n\t\t\t| a) color(\"red\")\n\t\t\t| b) fillcolor(\"red\")\n\t\t\t| c) fillcolor(red)"
print(f"{text.QUESTION}")
count = 0
for letter in question_1:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print("")
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")
if (check(ans) == passA[0]):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Great answer! That's correct!\n")
else:
  print(f"{text.FAIL}Response\t| \"fillcolor(\"red\")\" sets the color of the fill to red\n\t\t\t| whereas \"color(\"red\")\" sets the turtle color to red.\n")

sleep(3)

question_2 = "Question\t| Does the following draw a circle? \n\t\t\t| for i in range(0, 90):\n\t\t\t|  forward(2)\n\t\t\t|  left(4)\n\t\t\t| a) Yes\n\t\t\t| b) No"
print(f"{text.QUESTION}")
count = 0
for letter in question_2:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print()
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")

if ((check(ans) == passA[1]) & (correct == 1)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Whoa, another correct! \n\t\t\t| Nice work!\n")
elif ((check(ans) == passA[1]) & (correct == 0)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Well done, you're correct!! \n")
else:
  print(f"{text.FAIL}Response\t| There are 90 loops and every loop the turtle turns\n\t\t\t| left 4 degrees. 4 x 90 = 360 degrees, which\n\t\t\t| draws a circle!\n")

sleep(3)

question_3 = "Question\t| What will the following draw? \n\t\t\t| for i in range(0, 360):\n\t\t\t|  forward(10)\n\t\t\t|  left(4)\n\t\t\t| a) About 4 circles\n\t\t\t| b) A square\n\t\t\t| c) The Mona Lisa"
print(f"{text.QUESTION}")
count = 0
for letter in question_3:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print()
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")

if ((check(ans) == passA[2]) & (correct == 2)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| WOW! You got every single one!! Yowza!! \n\t\t\t| Really well done!\n")
elif ((check(ans) == passA[2]) & (correct == 1)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Dayamn!! You got 2/3 correct?! That's very good!\n")

elif ((check(ans) == passA[2]) & (correct == 0)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Brilliant! You got the hardest one and you\n\t\t\t| coded today, you've done amazingly!\n")
else:
  print(f"{text.FAIL}Response\t| It draws 4 circles, all on top of each other!")