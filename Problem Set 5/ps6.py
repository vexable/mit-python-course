from distutils.command import build
from pydoc import text
from pyexpat.errors import messages
import re
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    # print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if shift > 25:
            shift -= 26
        returnList=[]
        low = []
        up = []
        for x in string.ascii_lowercase:
            low.append(x)
        for s in string.ascii_uppercase:
            up.append(s)
        endTrack = low[shift * -1:]
        upTrack = up[shift * -1:]
        for x in string.ascii_lowercase:
            endTrack.append(x)
        for s in string.ascii_uppercase:
            upTrack.append(s)
        for lower in string.ascii_lowercase:
            returnList.append(lower)
        for upper in string.ascii_uppercase:
            returnList.append(upper)
        returnDict = dict(zip(returnList, [None]*len(returnList)))
        try:
            for letter in low:
                returnDict[letter] = low[low.index(letter) + shift]
        except IndexError:
            for y in endTrack:
                if y == "a":
                    break
                returnDict[y] = endTrack[endTrack.index(y) + shift]
        try:
            for letter in up:
                returnDict[letter] = up[up.index(letter) + shift]
        except IndexError:
            for y in upTrack:
                if y == "A":
                    break
                returnDict[y] = upTrack[upTrack.index(y) + shift]
        return returnDict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        temp = Message(self.message_text).build_shift_dict(shift)
        result = ''
        for s in self.message_text:
            if s not in temp:
                result += s
            else:
                result += temp[s]
        return result

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shiftPossible = [i for i in range(27)]
        test = ''
        count = 0
        testList = []
        currentShift = ""
        bool = False
        for x in shiftPossible:
            count = 0
            if bool:
                break
            currentShift = x
            test = self.apply_shift(x)
            testList = test.split(" ")
            for y in testList:
                if is_word(load_words(WORDLIST_FILENAME), y):
                    count += 1
                    if count == len(testList):
                        bool = True
                        break
                else:
                    break
        self.message_text = test
        self.message_text_encrypted = test
        self.shift = currentShift
        value = (currentShift, str(test))
        return value
#Example test case (PlaintextMessage)
# plaintext = CiphertextMessage('bzs')1
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.decrypt_message())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('Hihmyhmy qilxm: jumm jlynns zohyluf mowb yrnlygy wliqx wuh iohwy jumnls juchn yfmy ginbyl qbcmjyl xyuzyh mnluj')

print(ciphertext.message_text)
# print('Expected Output:', (1, 'cat'))
print('Actual Output:', ciphertext.decrypt_message())
print(ciphertext.message_text)
print(ciphertext.shift)
