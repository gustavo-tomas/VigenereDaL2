# Steps
# -> Format/Validate input
# -> Cypher/Decypher
# -> Key recovery

from utils import get_file_content
from part1 import cypher, decypher
from part2 import key_decypher, EN, BR

def main():

  message = get_file_content("input/message.txt")
  key = get_file_content("input/key.txt")
  cryptogram = get_file_content("input/cryptogram.txt")

  # Part 1
  enc_message = cypher(message, key)
  dec_message = decypher(enc_message, key)
  
  print("PART 1 ------------------------------------------------------------")
  print("MESSAGE:\t\t", message)
  print("KEY:\t\t\t", key)
  print("CRYPTOGRAM:\t\t", enc_message)
  print("DEC_MESSAGE:\t", dec_message)
  print("\n")
  
  # Part 2
  print("PART 2 ------------------------------------------------------------")
  guess_key = key_decypher(cryptogram, EN)
  rec_message = decypher(cryptogram, guess_key)
  
  print("CRYPTOGRAM:\t", cryptogram)
  print("KEY GUESS:\t", guess_key)
  print("REC MESSAGE:", rec_message)
  print("\n")

  return

if __name__ == "__main__":
  main()