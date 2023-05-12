# numbers_set = {1, 2, 3, 4, 3} #duplicate values removed
# print(numbers_set)

#numbers_set = {1, 2, [3, 4]} # cannot use mutable data types

numbers_set = {1, 2, 3, 4, (5, 6)} # tuples can be part of set as it is immutable
print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""

for word in words_set:
    abcd += word

print(abcd)

if "Alpha" in words_set:
    print("Alpha is in set")

else:
    print("Alpha is not in set")

words_set.add("Delta")
print(words_set)

words_set.discard("Bravo")
print(words_set)







