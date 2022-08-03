from utils import value, get_keystream

############
#  Cypher  #
############

# Cypher: Ci = (Mi + Ki) mod 26 (+ 97 for Unicode characters)
def cypher(message, key):
  result = ""
  for m, k in zip(value(message), value(get_keystream(message, key))):
    if m >= 0 and m <= 25: # Ignores non-alphabetic characters
      result += chr((m + k) % 26 + 97)
    else:
      result += chr(m + 97)
  return result

##############
#  Decypher  #
##############

# Decypher: Mi = (Ci - Ki) mod 26 (+ 97 for Unicode characters)
def decypher(cryptogram, key):
  result = ""
  for c, k in zip(value(cryptogram), value(get_keystream(cryptogram, key))):
    if c >= 0 and c <= 25: # Ignores non-alphabetic characters
      result += chr((c - k) % 26 + 97)
    else:
      result += chr(c + 97)
  return result
