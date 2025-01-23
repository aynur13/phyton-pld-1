string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

str1 = string1.replace(" ", "").lower()
str2 = string2.replace(" ", "").lower()
    
if (sorted(str1) == sorted(str2)):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
