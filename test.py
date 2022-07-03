import re
import math
from collections import Counter



stringu = "atkoicpjqssjaqmsohaqksihaqqithatpfbtticppurbrsphjbqskhapufbrothhvcpphesvjhuppfgpkriisgcsgcsgfsgiagidgjdgjdgiwfvwfcsecsecsecsecsecsecsecsetgtffhudgurryesyesudgudgudshwftsehwftsehsehwrgrtfftfrxgrxgrxhsbfgeufit"
stringu1 = "WEXBINGWEXHUAAWEX"



def divisors(n):
    divs = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    divs.extend([n])
    return list(set(divs))

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


print(sorted(Counter(temp), key=lambda i: -Counter(temp)[i]))
