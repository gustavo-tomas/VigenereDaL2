# Steps
# -> Format/Validate input
# -> Cypher/Decypher
# -> Key recovery

from part1 import cypher, decypher
from part2 import key_decypher, EN, BR

def main():

  [message, key] = read_input()

  # enc_message = cypher(message, key)
  # dec_message = decypher(enc_message, key)
  guess_key = key_decypher("input/cryptogram.txt", EN)
  rec_message = decypher(str(open("input/cryptogram.txt").read()).lower(), guess_key)
  
  # print("MESSAGE:\t", message)
  # print("KEY:\t\t", key)
  # print("CRYPTOGRAM:\t", enc_message)
  # print("DEC_MESSAGE:\t", dec_message)
  print("KEY GUESS:\t", guess_key)
  print("REC MESSAGE:", rec_message)

  return

#############################
#   Format/Validate input   #
#############################

# Read input: message, key
def read_input():
  
  # Format input to lowercase
  message = str(open("input/message.txt").read()).lower()
  key = str(open("input/key.txt").read()).lower()

  return message, key

if __name__ == "__main__":
  main()