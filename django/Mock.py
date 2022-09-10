# Question1. Check if the given string is palindrome or not using for loop

def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

#*****************************************************
# Question 2.

class Palindrome:

    def __init__(self,string):
        self.string = string

    def check_palindrome(self):
        for i in range(0, int(len(self.string) / 2)):
            if self.string[i] != self.string[len(self.string) - i - 1]:
                return False
        return True

s1 = Palindrome("malyalam")
print(s1.check_palindrome())
#
print("************Question 2***********************")
# 2. Sum of 2 digits into output
# 		n1 = 1234 # int(input("Enter number1 :" ))
# 		n2 = 9999 # int(input("Enter number2 :" ))
# 		Output: 9+1 2+9 3+9 4+9
# 		         10 + 11 + 12 + 13
# 				 46
n1 = 1234
n2 = 9999
def add_digits(n1,n2):
    l1 = []
    l2 = []
    result = []
    strn1 = str(n1)
    strn2 = str(n2)
    for i in strn1:
        l1.append(int(i))
    for j in strn2:
        l2.append(int(j))
    for (x,y) in zip(l1,l2):
        result.append((x+y))
    print(result)

add_digits(n1,n2)

print("***************Question 3*************")
#
# 3. st = "ab@#cd!ef"
#    Reverse string considering only alphabets. Symobls should not be reversed
#    # Output: fe@#dc!ba

# creating character array of size
# equal to length of string

def reve(s, l, r) :
    while l<r :
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1

def reverse(st):
    temp = [''] * len(st)
    x = 0

    for i in range(len(st)):
        if st[i] >= 'a' and st[i] <= 'z' or st[i] >= 'A' and st[i] <= 'Z':
            # storing elements in array
            temp[x] = st[i]
            x += 1

    # reversing the character array
    reve(temp, 0, x)

    lst = list(st)
    x = 0

    for i in range(len(st)):
        if st[i] >= 'a' and st[i] <= 'z' or st[i] >= 'A' and st[i] <= 'Z':
            # updating the origional string
            lst[i] = temp[x]
            x += 1

    revstring = ""
    for i in range(len(st)):
        revstring += lst[i]

    print("reverse string is :", revstring)

st = "ab@#cd!ef"
reverse(st)


print("************ Question 4*************")

# 4.
# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# findout elements duplicate count output in  dict format

def count_element(list1):
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(dict1)

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
count_element(some_list)

print("***********Question 5 ******************")
# t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
str_t1 = []
str_t2 = []
for i in t1:
    str_t1.append(str(i))
for i in t2:
    str_t2.append(str(i))
t1 = str_t1
t2 = str_t2
nt1 = []
st1 = []
nt2 = []
st2 = []
for i in t1:
    if i.isdigit():
        nt1.append(i)
    else:
        st1.append(i)
print(nt1,st1)

for i in t2:
    if i.isdigit():
        nt2.append(i)
    else:
        st2.append(i)
print(nt2,st2)

num_result = []
str_result = []

for (x,y) in zip(nt1,nt2):
    num_result.append((int(x) + int(y)))
print(num_result)

for (x,y) in zip(st1,st2):
    str_result.append((x+y))
print(str_result)

final_result = []
for i in num_result:
    final_result.append(i)
for i in str_result:
    final_result.append(i)

print(final_result)

print("\n")
print("********* Question 6 ************")
# Removing leading zeroes from the given IP address
def IP(ip):
  zeroip = ".".join([str(int(i)) for i in ip.split(".")])
  return zeroip
  # Driver code
  ip =input("Enter the IP address ::>")
  print("New Ip Address ::>",IP(ip))

inp = "216.08.094.196"
IP(inp)

print("**************** Question 7 ****************")
print("\n")
# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output= [1,2,3,4,5,6,7,8,9,10]

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(list(map(lambda x: int(x), str(l).replace("[", '').replace("]", '').split(","))))

print("\n")

print("**************** Question 8 **************")

Load sample content in text file.
  Read data and find
    1. No of lines in file
	2. No of words in each line
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total

content_in_text_file = """

 It is a general-purpose computer programming language. It is a high-level, 
object-oriented, dynamically typed, interpretted language which can run equally on different platforms such as Windows, 
Linux, UNIX, and Macintosh. Its high-level built-in data structures, combined with 
dynamic typing and dynamic binding. It is widely used in data science, machine learning 
and artificial intelligence domain. Also its very easy to learn.
 """

c = content_in_text_file

lines = 0
for i in c:
    if i == ".":
        lines += 1

print(f"The number of lines in the given content is : {lines}")

words = 0
split_c = c.split(" ")
print(f"The number of words in the given content is {len(split_c)}")

# checking the number of characters in each line
print("Printing the number of words in each line : ")
lines_list = c.split(".")
print(lines_list)

for i in lines_list:
    words_list = i.split(" ")
    words_count = len(words_list)
    print(f"the number of words is : {words_count}")

print("\n")
print("Printing the number of characters in each line ")

lines_list = c.split(".")
print(lines_list)
char_count = 0
for i in lines_list:
    for j in i:
        if j != " ":
            char_count += 1
    print(f"The number of characters in this line is : {char_count} ")

print("\n")
print("Checking the number of vowels and consonents in the given content")

v = ["a", "e", "i", "o", "u"]
v_count = 0
c_count = 0
for i in c:
    if i in v:
        v_count += 1
    else:
        c_count += 1
print(f"The vowel count in the given content is {v_count}")
print(f"The count of consonants in the given content is {c_count}")

print("\n")

print("Checking the count of special characters in the given content.")
print("\n")

symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', ':',
           ';', '"']
symbol_count = 0
for i in c:
    if i in symbols:
        symbol_count += 1
print(f"The number of special character in the given content is {symbol_count}")

print("\n")











