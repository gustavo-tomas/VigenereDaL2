
from operator import imod


import numpy as np

EN_LETTER_FREQUENCIES = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.996, 0.153,
                             0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
                             2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

stringu = "almostbeforeweknewitwehadleftthegroundhoggreenarrowpathmontainskysnowstonerockmegamanwhite"
stringu1 = "kpkywrlidyvcgiixiusxuolynpcpxrriebssxhfykebicxepbsuzerrqmxxysrqucqxsucxmxipygiwiekqyxafsxc"
stringu2 = "abcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyz"
stringu3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbcc"
def value(text):
  return [ord(x) - 97 for x in text]


pos = 0
guesslen = 3
#local letter frequency
LLF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 	0, 	0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0] 



def test(s,pos):
    looptot = round(len(s)/guesslen) #n sei se round sempre funciona
    print(looptot)
    for posl in range(pos, len(s), guesslen):
        LLF[value(s[posl])[0]] += 100/looptot



# for posl in range(len(stringu3)):
#     #print(stringu2[posl][0])
#     LLF[value(stringu3[posl])[0]] += 100/looptot








key = []
for keypos in range(guesslen):
    diferenca = 1e9
    letra = 0
    test(stringu1,keypos)
    for each in range(26): 

        temp = np.roll(LLF,-each)
        diferenca_local = sum(abs(np.subtract(EN_LETTER_FREQUENCIES,temp)))
        print(chr(each + 97) , " - ", diferenca_local)
        if(diferenca_local < diferenca):
           
            diferenca = diferenca_local
            letra = each

    key.append(letra)

print("Key: ")
for each in key:
    print(chr(each+97),end = "")
