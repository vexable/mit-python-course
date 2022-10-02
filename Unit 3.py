x = [1, 2, [3, 'John', 4], 'Hi']
print(x[0:1])
#     secretWord = secretWord.lower()
#     status = ""
#     count = []
#     for s in range(len(secretWord)):
#       count.append("_ ")
#     for s in range(len(lettersGuessed)):
#       if lettersGuessed[s] in count:
#         count[spot + 1] = lettersGuessed[s]
#         s += 1
#       elif lettersGuessed[s] in secretWord:
#         spot = secretWord.index(lettersGuessed[s])
#         count[spot] = lettersGuessed[s]
#     for x in range(len(count)):
#       status += count[x]
#     return status


def lyrics_to_frequencies(lyrics):
    '''
    code to find how many times a word occurs in a song
    lyrics = all words in a song in order
    myDic = dictionary for all lyrics in the song
    word = current word in current iteration
    '''
    myDic = {}
    for word in lyrics:
        if word in lyrics:
            myDic[word] += 1
        else:
            myDic[word] = 1
    return myDic

def most_common_words(freqs):
    '''
    finds out what the most common words are in a song
    freqs = [word : how many times it occurs]
    values = all the occurence values
    words = all very frequent words
    '''
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words = words.append(k)
    return (words,best)