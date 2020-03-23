import nltk
from nltk.corpus import cmudict
from itertools import combinations, chain

arpabet = nltk.corpus.cmudict.dict()
d = cmudict.dict()
vowels=['AA2',
        'AE2',
        'AH2',
        'AO2',
        'AW2',
        'AY2',
        'EH2',
        'ER2',
        'EY2',
        'IH2',
        'IY2',
        'OW2',
        'OY2',
        'UH2',
        'UW2',
        'AA1',
        'AE1',
        'AH1',
        'AO1',
        'AW1',
        'AY1',
        'EH1',
        'ER1',
        'EY1',
        'IH1',
        'IY1',
        'OW1',
        'OY1',
        'UH1',
        'UW1',
        'AA0',
        'AE0',
        'AH0',
        'AO0',
        'AW0',
        'AY0',
        'EH0',
        'ER0',
        'EY0',
        'IH0',
        'IY0',
        'OW0',
        'OY0',
        'UH0',
        'UW0'   
        ]
rhymecount=0
text_file = open("2-2-syl.txt", "a")

# Count dem syllllyabamboozles
def nsyl(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except KeyError:
        #if word not found in cmudict trigger syllables def
        return syllables(word)
    
def sum_to_n(n):
    from operator import sub
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i)) 
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)

def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count

#def that returns every phoneme after last stressed vowel for given word
#Ex.: cakedays => EY1 + S
def getrhymepart(word):
    phonemes=arpabet[word]
    for phoneme in reversed(range(len(phonemes[0]))):
        for vowel in range(len(vowels)):
            if str(phonemes[0][phoneme]) == str(vowels[vowel]):
                phonemeoffset = 0-len(phonemes[0])+phoneme
                rhymepart=phonemes[0][phonemeoffset:]
                rhymepart[0]=rhymepart[0][:-1]
                return rhymepart

def getword(syllables):
    for word in cmudict.words():
        if nsyl(word) == [syllables]:
            print(word)



scheme = [[0],[1]]
dividedscheme = [[0],[1]]


#Note to self: Elegant coding is for purist bourgoisie snobs. Clarity is an illusion. Or i'm just lazy&stupid, you decide.

while True:
    scheme[0][0]=int(scheme[0][0])+1
    for i in range(scheme[0][0]):
        scheme[1][0]=int(i+1)
        for p in sum_to_n(scheme[0][0]):
            for q in sum_to_n(scheme[1][0]):  
                dividedscheme[0]=p
                dividedscheme[1]=q
                print(dividedscheme)
                for word in cmudict.words():
                    if nsyl(word) == [dividedscheme[0][0]]:
                         l1w1=word
                         if len(dividedscheme[0])==1:                                                                                                                                                   #if line1=1
                             for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[1][0]]:                 
                                    l2w1=word
                                    if len(dividedscheme[1])==7:                                                                                                   
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                        l2w3=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                l2w4=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                        l2w5=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                l2w6=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][6]]:
                                                                                        l2w7=word
                                                                                        if getrhymepart(l1w1)==getrhymepart(l2w7):
                                                                                            print(l1w1+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n')                            #x,xxxxxxx
                                    if len(dividedscheme[1])==6:                                                                                                    
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                        l2w3=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                l2w4=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                        l2w5=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                l2w6=word
                                                                                if getrhymepart(l1w1)==getrhymepart(l2w6):
                                                                                    print(l1w1+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')                                             #x,xxxxxx
                                    if len(dividedscheme[1])==5:                                                                                                    
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                        l2w3=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                l2w4=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                        l2w5=word
                                                                        if getrhymepart(l1w1)==getrhymepart(l2w5):
                                                                            print(l1w1+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                                                              #x,xxxxx
                                    if len(dividedscheme[1])==4:                                                                                                    
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                        l2w3=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                l2w4=word
                                                                if getrhymepart(l1w1)==getrhymepart(l2w4):
                                                                    print(l1w1+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                                                               #x,xxxx
                                    if len(dividedscheme[1])==3:                                                                                                    
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                        l2w3=word
                                                        if getrhymepart(l1w1)==getrhymepart(l2w3):
                                                            print(l1w1+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                                                                #x,xxx
                                                
                                    if len(dividedscheme[1])==2:                                                                                                    
                                        for word in cmudict.words():
                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                l2w2=word
                                                if getrhymepart(l1w1)==getrhymepart(l2w2):
                                                    print(l1w1+'\n'+l2w1+' '+l2w2+'\n')                                                                                                                 #x,xx done
                                    else:                                               
                                        if getrhymepart(l1w1)==getrhymepart(l2w1):
                                            print(l1w1+'\n'+l2w1+'\n')                                                                                                                                  #x,x done
                         if len(dividedscheme[0])==2:                                                                                                                                                   #if line1=2                                                                                                                                    
                             for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[1][0]]:                 
                                            l2w1=word
                                            if len(dividedscheme[1])==7:                                                                                                    
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                l2w3=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                        l2w4=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                l2w5=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                        l2w6=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                l2w7=word
                                                                                                if getrhymepart(l1w2)==getrhymepart(l2w7):
                                                                                                    print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n')       #xx,xxxxxxx
                                            if len(dividedscheme[1])==6:                                                                                                    
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                l2w3=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                        l2w4=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                l2w5=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                        l2w6=word
                                                                                        if getrhymepart(l1w2)==getrhymepart(l2w6):
                                                                                            print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')                        #xx,xxxxxx
                                            if len(dividedscheme[1])==5:                                                                                                    
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                l2w3=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                        l2w4=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                l2w5=word
                                                                                if getrhymepart(l1w2)==getrhymepart(l2w5):
                                                                                    print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                                         #xx,xxxxx
                                            if len(dividedscheme[1])==4:                                                                                                    
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                l2w3=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                        l2w4=word
                                                                        if getrhymepart(l1w2)==getrhymepart(l2w4):
                                                                            print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                                          #xx,xxxx
                                            if len(dividedscheme[1])==3:                                                                                                   
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                l2w3=word
                                                                if getrhymepart(l1w2)==getrhymepart(l2w3):
                                                                    print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                                           #xx,xxx
                                                        
                                            if len(dividedscheme[1])==2:                                                                                                   
                                                for word in cmudict.words():
                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                        l2w2=word
                                                        if getrhymepart(l1w2)==getrhymepart(l2w2):
                                                            print(l1w1+' '+l1w2+'\n'+l2w1+' '+l2w2+'\n')                                                                                            #xx,xx done
                                            else:                                               
                                                if getrhymepart(l1w2)==getrhymepart(l2w1):
                                                    print(l1w1+' '+l1w2+'\n'+l2w1+'\n')                                                                                                             #xx,x
                         if len(dividedscheme[0])==3:                                                                                                                                               #if line1==3                          
                             for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[0][2]]:
                                            l1w3=word
                                            for word in cmudict.words():
                                                if nsyl(word) == [dividedscheme[1][0]]:                 
                                                    l2w1=word
                                                    if len(dividedscheme[1])==7:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                        l2w3=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                l2w4=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                        l2w5=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                l2w6=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                        l2w7=word
                                                                                                        if getrhymepart(l1w3)==getrhymepart(l2w7):
                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n') #xxx,xxxxxx
                                                    if len(dividedscheme[1])==6:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                        l2w3=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                l2w4=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                        l2w5=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                l2w6=word
                                                                                                if getrhymepart(l1w3)==getrhymepart(l2w6):
                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')         #xxx,xxxxxx
                                                    if len(dividedscheme[1])==5:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                        l2w3=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                l2w4=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                        l2w5=word
                                                                                        if getrhymepart(l1w3)==getrhymepart(l2w5):
                                                                                            print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                          #xxx,xxxxx
                                                    if len(dividedscheme[1])==4:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                        l2w3=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                l2w4=word
                                                                                if getrhymepart(l1w3)==getrhymepart(l2w4):
                                                                                    print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                           #xxx,xxxx
                                                    if len(dividedscheme[1])==3:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                        l2w3=word
                                                                        if getrhymepart(l1w3)==getrhymepart(l2w3):
                                                                            print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                            #xxx,xxx
                                                                
                                                    if len(dividedscheme[1])==2:                                                                                                    
                                                        for word in cmudict.words():
                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                l2w2=word
                                                                if getrhymepart(l1w3)==getrhymepart(l2w2):
                                                                    print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+' '+l2w2+'\n')                                                                             #xxx,xx
                                                    else:                                               
                                                        if getrhymepart(l1w3)==getrhymepart(l2w1):
                                                            print(l1w1+' '+l1w2+' '+l1w3+'\n'+l2w1+'\n')
                         if len(dividedscheme[0])==4:                                                                                                                                               #if line1==3                          
                             for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[0][2]]:
                                            l1w3=word
                                            for word in cmudict.words():
                                                if nsyl(word) == [dividedscheme[0][3]]:
                                                    l1w4=word
                                                    for word in cmudict.words():
                                                        if nsyl(word) == [dividedscheme[1][0]]:                 
                                                            l2w1=word
                                                            if len(dividedscheme[1])==7:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                l2w3=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                        l2w4=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                l2w5=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                        l2w6=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                                l2w7=word
                                                                                                                if getrhymepart(l1w4)==getrhymepart(l2w7):
                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n') #xxxx,xxxxxx
                                                            if len(dividedscheme[1])==6:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                l2w3=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                        l2w4=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                l2w5=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                        l2w6=word
                                                                                                        if getrhymepart(l1w4)==getrhymepart(l2w6):
                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')         #xxxx,xxxxxx
                                                            if len(dividedscheme[1])==5:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                l2w3=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                        l2w4=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                l2w5=word
                                                                                                if getrhymepart(l1w4)==getrhymepart(l2w5):
                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                          #xxxx,xxxxx
                                                            if len(dividedscheme[1])==4:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                l2w3=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                        l2w4=word
                                                                                        if getrhymepart(l1w4)==getrhymepart(l2w4):
                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                           #xxxx,xxxx
                                                            if len(dividedscheme[1])==3:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                l2w3=word
                                                                                if getrhymepart(l1w4)==getrhymepart(l2w3):
                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                            #xxxx,xxx
                                                                        
                                                            if len(dividedscheme[1])==2:                                                                                                    
                                                                for word in cmudict.words():
                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                        l2w2=word
                                                                        if getrhymepart(l1w4)==getrhymepart(l2w2):
                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+' '+l2w2+'\n')                                                                             #xxxx,xx
                                                            else:                                               
                                                                if getrhymepart(l1w4)==getrhymepart(l2w1):
                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+'\n'+l2w1+'\n')                                          
                         if len(dividedscheme[0])==5:                                                                                                                                               #if line1==3                          
                             for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[0][2]]:
                                            l1w3=word
                                            for word in cmudict.words():
                                                if nsyl(word) == [dividedscheme[0][3]]:
                                                    l1w4=word
                                                    for word in cmudict.words():
                                                        if nsyl(word) == [dividedscheme[0][4]]:
                                                            l1w5=word
                                                            for word in cmudict.words():
                                                                if nsyl(word) == [dividedscheme[1][0]]:                 
                                                                    l2w1=word
                                                                    if len(dividedscheme[1])==7:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                        l2w3=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                l2w4=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                        l2w5=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                l2w6=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                                        l2w7=word
                                                                                                                        if getrhymepart(l1w5)==getrhymepart(l2w7):
                                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n') #xxxx,xxxxxx
                                                                    if len(dividedscheme[1])==6:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                        l2w3=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                l2w4=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                        l2w5=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                l2w6=word
                                                                                                                if getrhymepart(l1w5)==getrhymepart(l2w6):
                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')         #xxxx,xxxxxx
                                                                    if len(dividedscheme[1])==5:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                        l2w3=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                l2w4=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                        l2w5=word
                                                                                                        if getrhymepart(l1w5)==getrhymepart(l2w5):
                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                          #xxxx,xxxxx
                                                                    if len(dividedscheme[1])==4:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                        l2w3=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                l2w4=word
                                                                                                if getrhymepart(l1w5)==getrhymepart(l2w4):
                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                           #xxxx,xxxx
                                                                    if len(dividedscheme[1])==3:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                        l2w3=word
                                                                                        if getrhymepart(l1w5)==getrhymepart(l2w3):
                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                            #xxxx,xxx
                                                                                
                                                                    if len(dividedscheme[1])==2:                                                                                                    
                                                                        for word in cmudict.words():
                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                l2w2=word
                                                                                if getrhymepart(l1w5)==getrhymepart(l2w2):
                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+' '+l2w2+'\n')                                                                             #xxxx,xx
                                                                    else:                                               
                                                                        if getrhymepart(l1w5)==getrhymepart(l2w1):
                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+'\n'+l2w1+'\n')         
                         if len(dividedscheme[0])==6:
                            for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[0][2]]:
                                            l1w3=word
                                            for word in cmudict.words():
                                                if nsyl(word) == [dividedscheme[0][3]]:
                                                    l1w4=word
                                                    for word in cmudict.words():
                                                        if nsyl(word) == [dividedscheme[0][4]]:
                                                            l1w5=word
                                                            for word in cmudict.words():
                                                                if nsyl(word) == [dividedscheme[0][5]]:
                                                                    l1w6=word
                                                                    for word in cmudict.words():
                                                                        if nsyl(word) == [dividedscheme[1][0]]:                 
                                                                            l2w1=word
                                                                            if len(dividedscheme[1])==7:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                l2w3=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                        l2w4=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                l2w5=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                        l2w6=word
                                                                                                                        for word in cmudict.words():
                                                                                                                           if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                                                l2w7=word
                                                                                                                                if getrhymepart(l1w6)==getrhymepart(l2w7):
                                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n') #xxxx,xxxxxx
                                                                            if len(dividedscheme[1])==6:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                l2w3=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                        l2w4=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                l2w5=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                        l2w6=word
                                                                                                                        if getrhymepart(l1w6)==getrhymepart(l2w6):
                                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')         #xxxx,xxxxxx
                                                                            if len(dividedscheme[1])==5:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                l2w3=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                        l2w4=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                l2w5=word
                                                                                                                if getrhymepart(l1w6)==getrhymepart(l2w5):
                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                          #xxxx,xxxxx
                                                                            if len(dividedscheme[1])==4:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                l2w3=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                        l2w4=word
                                                                                                        if getrhymepart(l1w6)==getrhymepart(l2w4):
                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                           #xxxx,xxxx
                                                                            if len(dividedscheme[1])==3:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                l2w3=word
                                                                                                if getrhymepart(l1w6)==getrhymepart(l2w3):
                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                            #xxxx,xxx
                                                                                        
                                                                            if len(dividedscheme[1])==2:                                                                                                    
                                                                                for word in cmudict.words():
                                                                                   if nsyl(word) == [dividedscheme[1][1]]:
                                                                                        l2w2=word
                                                                                        if getrhymepart(l1w6)==getrhymepart(l2w2):
                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+' '+l2w2+'\n')                                                                             #xxxx,xx
                                                                            else:                                               
                                                                                if getrhymepart(l1w6)==getrhymepart(l2w1):
                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+'\n'+l2w1+'\n')
                         if len(dividedscheme[0])==7:
                            for word in cmudict.words():
                                if nsyl(word) == [dividedscheme[0][1]]:
                                    l1w2=word
                                    for word in cmudict.words():
                                        if nsyl(word) == [dividedscheme[0][2]]:
                                            l1w3=word
                                            for word in cmudict.words():
                                                if nsyl(word) == [dividedscheme[0][3]]:
                                                    l1w4=word
                                                    for word in cmudict.words():
                                                        if nsyl(word) == [dividedscheme[0][4]]:
                                                            l1w5=word
                                                            for word in cmudict.words():
                                                                if nsyl(word) == [dividedscheme[0][5]]:
                                                                    l1w6=word
                                                                    for word in cmudict.words():
                                                                        if nsyl(word) == [dividedscheme[0][6]]:
                                                                            l1w7=word
                                                                            for word in cmudict.words():
                                                                                if nsyl(word) == [dividedscheme[1][0]]:                 
                                                                                    l2w1=word
                                                                                    if len(dividedscheme[1])==7:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                        l2w3=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                                l2w4=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                        l2w5=word
                                                                                                                        for word in cmudict.words():
                                                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                                l2w6=word
                                                                                                                                for word in cmudict.words():
                                                                                                                                   if nsyl(word) == [dividedscheme[1][6]]:
                                                                                                                                        l2w7=word
                                                                                                                                        if getrhymepart(l1w7)==getrhymepart(l2w7):
                                                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+' '+l2w7+'\n') #xxxx,xxxxxx
                                                                                    if len(dividedscheme[1])==6:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                        l2w3=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                                l2w4=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                        l2w5=word
                                                                                                                        for word in cmudict.words():
                                                                                                                           if nsyl(word) == [dividedscheme[1][5]]:
                                                                                                                                l2w6=word
                                                                                                                                if getrhymepart(l1w7)==getrhymepart(l2w6):
                                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+' '+l2w6+'\n')         #xxxx,xxxxxx
                                                                                    if len(dividedscheme[1])==5:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                        l2w3=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                                l2w4=word
                                                                                                                for word in cmudict.words():
                                                                                                                   if nsyl(word) == [dividedscheme[1][4]]:
                                                                                                                        l2w5=word
                                                                                                                        if getrhymepart(l1w7)==getrhymepart(l2w5):
                                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+' '+l2w5+'\n')                          #xxxx,xxxxx
                                                                                    if len(dividedscheme[1])==4:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                        l2w3=word
                                                                                                        for word in cmudict.words():
                                                                                                           if nsyl(word) == [dividedscheme[1][3]]:
                                                                                                                l2w4=word
                                                                                                                if getrhymepart(l1w7)==getrhymepart(l2w4):
                                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+' '+l2w3+' '+l2w4+'\n')                                           #xxxx,xxxx
                                                                                    if len(dividedscheme[1])==3:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                for word in cmudict.words():
                                                                                                   if nsyl(word) == [dividedscheme[1][2]]:
                                                                                                        l2w3=word
                                                                                                        if getrhymepart(l1w7)==getrhymepart(l2w3):
                                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+' '+l2w3+'\n')                                                            #xxxx,xxx
                                                                                                
                                                                                    if len(dividedscheme[1])==2:                                                                                                    
                                                                                        for word in cmudict.words():
                                                                                           if nsyl(word) == [dividedscheme[1][1]]:
                                                                                                l2w2=word
                                                                                                if getrhymepart(l1w7)==getrhymepart(l2w2):
                                                                                                    print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+' '+l2w2+'\n')                                                                             #xxxx,xx
                                                                                    else:                                               
                                                                                        if getrhymepart(l1w7)==getrhymepart(l2w1):
                                                                                            print(l1w1+' '+l1w2+' '+l1w3+' '+l1w4+' '+l1w5+' '+l1w6+' '+l1w7+'\n'+l2w1+'\n')       
                                        
                        
