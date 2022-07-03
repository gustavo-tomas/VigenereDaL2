import re
import math
from collections import Counter
# Steps
# -> Format/Validate input
# -> Cypher/Decypher
# -> Key recovery

def main():

  [message, key] = read_input()
  cryptogram = cypher(message, key)
  dec_message = decypher(cryptogram, key)
  prob_length = guessKeyL(cryptogram)

  print("MESSAGE:\t", message, "- KEY:\t\t", key)
  print("CRYPTOGRAM:\t", cryptogram, "- DEC_MESSAGE:\t", dec_message)
  print(prob_length)

  return

# Read input: message, key
def read_input():
  
  # Format input to lowercase
  message = input().lower()
  key = input().lower()

  # Removes any character that isnt a-z and spaces
  for m in value(message):
    if (m < 0 or m > 25) and chr(m + 97) != " ":
      message = message.replace(chr(m + 97), "")
  
  for k in value(key):
    if (k < 0 or k > 25) and chr(k + 97) != " ":
      key = key.replace(chr(k + 97), "")

  # Invalid message or key
  if len(message) <= 0 or len(key) <= 0:
    print("Invalid Message or Key")
    exit(0)

  # Checks the length of the key
  dif = len(message) - len(key)

  # Key needs padding
  if dif > 0:
    for i in range(dif):
      key += key[i % len(key)]

  # Key needs trimming
  if dif < 0:
    key = key[:dif]

  return message, key

# Cypher: Ci = (Mi + Ki) mod 26 (+ 97 for Unicode characters)
def cypher(message, key):
  result = ""
  for m, k in zip(value(message), value(key)):
    if m >= 0 and m <= 25: # Ignores spaces
      result += chr((m + k) % 26 + 97)
    else:
      result += chr(m + 97)
  return result

# Decypher: Mi = (Ci - Ki) mod 26 (+ 97 for Unicode characters)
def decypher(cryptogram, key):
  result = ""
  for c, k in zip(value(cryptogram), value(key)):
    if c >= 0 and c <= 25: # Ignores spaces
      result += chr((c - k) % 26 + 97)
    else:
      result += chr(c + 97)
  return result

# Return the value of each character (a - z = 0 - 25) in a string
def value(text):
  return [ord(x) - 97 for x in text]

def divisors(n):
    divs = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    divs.extend([n])
    return list(set(divs))

def guessKeyL(stringu):
    possi = []
    temp = []
    keylenghtpos = []
    tam = 3
    for tam in range(3,10):
        for i in range(len(stringu)-(tam-1)):
            seq = stringu[i:i+tam] 
            indexes = [w.start() for w in re.finditer(seq, stringu[i:])]
            if(len(indexes)>1):
                possi.append(indexes[-1]-indexes[-2])


    for distance in Counter(possi):
        for num in divisors(distance):
            temp.append(num)


    return(sorted(Counter(temp), key=lambda i: -Counter(temp)[i]))

if __name__ == "__main__":
  main()