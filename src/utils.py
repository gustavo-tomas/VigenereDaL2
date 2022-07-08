# Return the value of each character (a - z = 0 - 25) in a string
def value(text):
  return [ord(x) - 97 for x in text]

# Formats a key to match the length of a message/cryptogram
def get_keystream(message, key):

  keystream = key

  # Checks the length of the key
  dif = len(message) - len(key)

  # Key needs padding
  if dif > 0:
    keystream = ""
    curr_idx = 0
    for m in value(message):
      if (m < 0 or m > 25):
        keystream += chr(m + 97)
      else:
        keystream += key[curr_idx]
        curr_idx = (curr_idx + 1) % len(key)

  return keystream

# Removes any non-alphabetic character from a string
def format_string(string):
  for s in value(string):
    if (s < 0 or s > 25):
      string = string.replace(chr(s + 97), "")
  
  return string