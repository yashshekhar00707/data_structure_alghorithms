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









