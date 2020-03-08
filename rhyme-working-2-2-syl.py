import nltk
from nltk.corpus import cmudict

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





dividedscheme=[[2, 1], [2]]

#For-loop to do all the stuff
for word1 in cmudict.words():
    if nsyl(word1) == [2]:
        print(rhymecount)
        print(word1)
        text_file.close()
        rhymecount=0
        text_file = open("2-2-syl.txt", "a")
        rhymepart1 = getrhymepart(word1)
        for word2 in cmudict.words():
            if nsyl(word2) == [2]:
                rhymepart2 = getrhymepart(word2)
                if rhymepart1==rhymepart2:
                    n = text_file.write(word1+"\n"+word2+"\n"+"\n")
                    rhymecount=rhymecount+1
