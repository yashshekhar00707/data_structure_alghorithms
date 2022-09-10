# 1. Length of String
# Manual Method
x = "skdjskdjksdjksjd"
count = 0
for i in x:
    count += 1
print(count)

# Inbuilt method
x = "skdnshdsjdbdsssdnjsbj"
print(len(x))

# 2. Count the number of each character in the string
x = "skdskjdksjdksjksjd"
count_dict = {}
for i in x:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)

# 3. String slicing
x = "sdjksjdksjksjdkjs"
print(x[1:4])
print(x[::2])

# 4. Length of longest string in Python
# Method 1
x = "We will be visiting to Amsterdam Tomorrow."
split_line = x.split(" ")
len_list = []
for i in split_line:
    len_list.append(len(i))
max_index = len_list.index(max(len_list))
print(split_line[max_index])

# Method 2


def longest_word(sentence):
    split_line = sentence.split(" ")
    sorted_split_line = sorted(split_line, key = len)
    print(f"The string with highest length is : {split_line[-1]} and its length is {len(split_line[-1])}.")


x = "Please provide correct information."
longest_word(x)

# 4 First and last characters swapping

# Method 1
x = "Python"
resul_list = []
for i in x:
    resul_list.append(i)
resul_list[0], resul_list[-1] = resul_list[-1], resul_list[0]
result = "".join(resul_list)
print(result)

# Method 2
def swap(string):
    # storing the first character
    start = string[0]

    # storing the last character
    end = string[-1]

    swapped_string = end + string[1:-1] + start + end +end
    print(swapped_string)


# Driver Code
swap("Python")

# 5. Remove odd index value from a given string
x = "0123456789"
# x = input("Enter the string : ")
even_list = []
for i in x:
    if (x.index(i))%2 == 0:
        even_list.append(i)
odd_removed_string = "".join(even_list)
print(odd_removed_string)

# In above problem we are using numbers as string for checking the result
# if we put a string as input we will receive the characters of string at even values

# Count the number of words in a string

sentence = "Find the number of words in this sentence."
def count_words(sentence):
    words_list = sentence.split(' ')
    print(len(words_list))
count_words(sentence)

# 6. Given a string in lower case change it to upper case

string = "welcome"
def change_to_upper(string):
    upper_string = string.upper()
    print(upper_string)

change_to_upper(string)

# 7. Given a string in upper case change it to lower case.

string = "WELCOME"

def change_to_lower(string):
    lower_string = string.lower()
    print(lower_string)

change_to_lower(string)

# 8. Given a sting containing both upper and lower chars
# change the upper case chars to lower case and lower case chars to upper case

inp_string = "Virat"

def change_case(inp_string):
    case_changed_list = []
    for i in inp_string:
        if i.isupper():
            case_changed_list.append(i.lower())
        if i.islower():
            case_changed_list.append(i.upper())
    result_string = ''.join(case_changed_list)
    print(result_string)

change_case(inp_string)

# 9. Removing a new line character from the string in Python
# initialize list
test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']

# printing original list
print("The original list : " + str(test_list))

# Removing newline character from string
# using loop
res = []
for sub in test_list:
    res.append(sub.replace("\n", ""))

# printing result
print("List after newline character removal : " + str(res))

# 10. Program to check whether a string starts with specified characters

text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)

x = "I am learning Python."
print(x.startswith(("Rahul", "I")))
# If we wish to check whether the given string starts with "Rahul" or "I"
# we can use multiple strings inside the paranthesis like in example above.

# 11. Python program to set the indentation of the first line
import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()

# 12. program to print the given floating number to 2 decimal places

list_of_floating_numbers = [1.2334, 3.1121, 4.121212, 4.13121212, 2.121323]
def round_to_2(num):
    rounded_num = round(num, 2)
    return rounded_num

rounded_list = []
for i in list_of_floating_numbers:
    rounded_list.append(round_to_2(i))
print(rounded_list)

# 13. program to print the given floating numbers to 2 decimal places with a sign

list1 = [1.22122, 3.132322, 4.1323242, 4.2323232]
list2 = [3.324343, 4.23242233, 2.1132323, 10.212]
result_list = []
for (i,j) in zip(list1, list2):
    ans = i-j
    if ans >= 0:
        ans_with_sign = '+' + str(ans)
        result_list.append(ans_with_sign)
    else:
        result_list.append(ans)
print(result_list)


# 14. Program to print the numbers with comma separator
list3 = [1000000000,200000000000,30000000]
for i in list3:
    print(f"{i:,}")

# 15. To format a number with percentage in python
list4 = [1,2,3,4]
for i in list4:
    print(f"{i:.0%}")

# 16. To count occurrences of a substring in a string
# or count repeated characters in a string
def count_sub_string(string, sub_string):
    split_line = string.split(' ')
    count = 0
    for i in split_line:
        if i == sub_string:
            count += 1
    print(count)


inp_str = "the fox is considered to be the most clever animal amongst its class."
sub_string = "the"
count_sub_string(string, sub_string)


# In the given string find the number of occurrences of substring "gh"
inp_str2 = "ghkwhghswghedghrfgheddjdksjfhsdkjdkjgh"
count = 0
for i in inp_str2:
    if (i == 'g') and (inp_str2[(inp_str2.index(i) + 1)] == "h"):
        count += 1
print(f"The count of 'gh' in the given string is {count}")

# 17. print the index of character of the string
def get_index(string, char):
    print(string.index(char))
string = "Welcome to NASA"
char = "m"
get_index(string, char)

# 18 converting the string to list

def list_converter(string):
    list1 = []
    for i in string:
        list1.append(i)
    print(list1)
list_converter("Rakesh")

# 19 swap comma and dot in a string
def punc_swapper(string):
    string = string.replace(',','x')
    string = string.replace('.',',')
    string = string.replace('x','.')
    print(string)

string = "123,12,1.23.45"
punc_swapper(string)

# 20 count and display the vowels of a given string

def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
            print(i)
    print(count)

string = "Abhishek is a data scientist."
vowel_counter(string)

# 21 remove spaces from a given string

def remove_string(string):
    string = string.replace(' ','')
    print(string)

string = "We will be going to picnic tomorrow."
remove_string(string)

# 22 Move spaced to the front of a given string

def move_spaces(string):
    count = 0
    for i in string:
        if i == ' ':
            count += 1
    string.replace(' ','')
    string = string + " "*count
    print(string)

string = "We live in Mumbai."
move_spaces(string)

# 23 Capitalize first and last character of each word in a given string

def capitalize_first_and_last(string):
    string = string.split(' ')
    list1 = []
    for x in string:
        y = x[0].capitalize() + x[1:-1] + x[-1].capitalize()
        list1.append(y)
    result_string = ' '.join(list1)
    print(result_string)

string = "frpfrpl frplfprlf frplfprlf frplfpr frpflprlf lfprlf"
capitalize_first_and_last(string)

# 24 Removing leading zeros from an IP address

def remove_zeros(IP):
    print(IP.rstrip("0."))

IP = "208.80. 154.224.000."
remove_zeros(IP)


# OOP practice

class Item:
    pay_rate = 0.8 # after applying 20% discount
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        result = self.price * self.quantity
        print(result)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)









