# Steps
# -> Format/Validate input
# -> Cypher/Decypher
# -> Key recovery

from utils import get_file_content, set_file_content
from part1 import cypher, decypher
from part2 import key_decypher, EN, BR

CYPHER = 0
DECYPHER = 1
KEY_RECOVERY = 2

def main():

  action = int(input("Choose an action (0 - Cypher | 1 - Decypher | 2 - Key recovery): "))

  if action == CYPHER:
    message_file = input("Choose a file with a message: ")
    key_file = input("Choose a file with a key: ")
    
    message = get_file_content(message_file)
    key = get_file_content(key_file)

    cyphered_message = cypher(message, key)
    set_file_content("output/" + message_file.split("/")[-1].strip(".txt") + "_cyphered.txt", cyphered_message)
  
  elif action == DECYPHER:
    cryptogram_file = input("Choose a file with a cryptogram: ")
    key_file = input("Choose a file with a key: ")

    cryptogram = get_file_content(cryptogram_file)
    key = get_file_content(key_file)

    cyphered_message = decypher(cryptogram, key)
    set_file_content("output/" + cryptogram_file.split("/")[-1].strip(".txt") + "_decyphered.txt", cyphered_message)
  
  elif action == KEY_RECOVERY:
    cryptogram_file = input("Choose a file with a cryptogram: ")

    cryptogram = get_file_content(cryptogram_file)

    rec_key = key_decypher(cryptogram, EN)
    rec_message = decypher(cryptogram, rec_key)
    set_file_content("output/" + cryptogram_file.split("/")[-1].strip(".txt") + "_recovered_key.txt", rec_key)
    set_file_content("output/" + cryptogram_file.split("/")[-1].strip(".txt") + "_recovered_message.txt", rec_message)
  
  else:
    print("dumb lol")
    return

  return

if __name__ == "__main__":
  main()