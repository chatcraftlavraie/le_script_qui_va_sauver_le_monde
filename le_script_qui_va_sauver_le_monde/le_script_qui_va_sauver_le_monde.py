alph = "abcdefghijklmnopqrstuvwxyz"
alph = list(alph.strip())
nums = input("Tape un nombre : ")
nums = list(nums.strip())
letters = ""
word = ""

for num in nums:
	letters += num

letters = list(letters.split(" "))

for letter in letters:
	word += alph[int(letter)]

print(word)