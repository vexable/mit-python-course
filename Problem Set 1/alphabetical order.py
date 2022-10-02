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