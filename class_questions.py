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





