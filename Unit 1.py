# x = int(input("Enter an integer: "))
# if x%2 == 0:
#     print("Even")
# else:
#     print("Odd")
# print("Done with conditional"
# num = 10
# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#         print(char + str(numCons))

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 
# s = "aeiour"
# vowel = 0
# for char in s:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char =="u" :
#             vowel += 1
# print("Number of vowels: " + str(vowel))
# x=0
# count = 0
# for char in s:
#     if char == 'b' and x == 0:
#         x = 1
#     if char == 'o' and x ==1:
#         x = 2
#     if char == 'b' and x==2:
#         count += 1
#         x = 0
# print(count)
# s = "bobobobobbob"
# count = 0
# iter_count = 0
# for char in s:
#     if char != "b" and char != "o":
#         iter_count = 0
#     elif char == 'b' and iter_count == 0:
#         iter_count = 1
#     elif char == 'o' and (iter_count == 1):
#         iter_count = 2
#     elif char == 'b' and (iter_count == 2):
#         count += 1
# print(count)

# s = 'bobbboobobobaboboc'
# s1 = 'tibobbobbobbltwobobbooboboolm'
# s = 'cboobobfbobobb'
# s = 'tbofcy hobobobthehobowonder'
# count = 0
# iter_count = 0
# for char in s:
#     if char != 'b' and char != 'o':
#         iter_count = 0
#     elif char == 'b' and iter_count == 0:
#         iter_count = 1
#     elif char == 'o' and (iter_count == 1 or iter_count == 3):
#         iter_count = 2
#     elif char == 'o':
#         iter_count = 0
#     elif char == 'b' and iter_count == 2:
#         iter_count = 3
#         count += 1

# print("Number of times bob occurs is: " + str(count))
s = 'cjnjjnyabccjnxyzaaccddeeffgg'
s = "jdmkxcjngheqjjnyajpksowy"
count = []
streak = " "
big_streak = " "
previous_letter = 0
alphabet = ['1','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letter in s:
    if letter in alphabet and count != []:
        count.append(letter)
        count.append(alphabet.index(letter))
    if letter in alphabet and count == []:
        count = [letter, alphabet.index(letter)]
        streak = letter
    if len(count)>2:
        if alphabet.index(letter) >= alphabet.index(previous_letter):
            if streak == " ":
                streak = previous_letter
            streak += str(letter)
        else:
            streak = " "
    if big_streak == ' ':
        big_streak = streak
    if len(streak)>len(big_streak):
        big_streak = streak
    previous_letter = letter
if big_streak == " ":
    big_streak = count[0]
print("Longest substring in alphabetical order is: " + big_streak)

# count = a, 1,b , 3
# streak = ab
# previous_letter = a 
# letter = a
# bigstreak =
