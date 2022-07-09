import re
import math
import numpy as np
from utils import value, format_string

EN_LETTER_FREQUENCIES = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.996, 0.153,
                          0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
                          2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

BR_LETTER_FREQUENCIES = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40,
                          0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34,
                          4.63, 1.67, 0.01, 0.21, 0.01, 0.47]

BR = 0
EN = 1                         

########################
#   Guess key length   #
########################
def guess_key_length(string):

  MIN_SIZE = 3
  MAX_SIZE = int(math.sqrt(len(string)) + 1)

  reps = set()
  for tam in range(MIN_SIZE, MAX_SIZE):
    for i in range(len(string) - (tam - 1)):
      seq = string[i:i+tam]
      indexes = [w.start() for w in re.finditer(seq, string[i:])]
      
      if(len(indexes) > 1):
        reps.add(indexes[-1] - indexes[-2])

  if len(reps) > 0:
    ceil = math.ceil(math.sqrt(max(reps)))
    frequencies = {}

    for div in range(2, ceil + 1):
      count = 0
      for distance in reps:
        if(distance % div == 0):
          if div in frequencies:
            frequencies[div] += 1
          else:
            frequencies[div] = 0

    sorted_freq = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
    most_frequent = list(sorted_freq.keys())

    print("Frequencies:", sorted_freq)
    print("Most freq:", most_frequent)
    
    return most_frequent[2] # @TODO: choose frequency
    
  return 0 # Deu ruim

###########################
#   Get letter frequency  #
###########################
def get_letter_freq(cryptogram, pos, guesslen):
  LLF = [0] * 26
  looptot = round(len(cryptogram) / guesslen)
  for posl in range(pos, len(cryptogram), guesslen):
    LLF[value(cryptogram[posl])[0]] += 100 / looptot

  return LLF

##########################
#  Decypher without key  #
##########################
def key_decypher(cryptogram, lan):
  cryptogram = format_string(cryptogram)
  keylen = guess_key_length(cryptogram)
  key = []
  
  for keypos in range(keylen):
    smallest_diff = 1e9
    letter = 0
    LLF = get_letter_freq(cryptogram, keypos, keylen)

    for each in range(26): 
      temp = np.roll(LLF, -each)
      if(lan == EN):
        diff = sum(abs(np.subtract(EN_LETTER_FREQUENCIES, temp)))
      else:
        diff = sum(abs(np.subtract(BR_LETTER_FREQUENCIES, temp)))

      if(diff < smallest_diff):
        smallest_diff = diff
        letter = each

    key.append(letter)
  
  # Converts key to char
  chave = ""
  for each in key:
    chave += chr(each + 97)
  return chave
