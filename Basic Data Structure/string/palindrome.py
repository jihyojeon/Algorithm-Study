# Valid Palindrome Problem

# test case 1
# input: "A man, a plan, a canal: Panama"
# output: true
# test case 2
# input: "race a car"
# output: false
import pprint

def list_palindrome(input_strs):
    # preprocessing: consider only lower alphabet and numbers
    strs = []
    for str in input_strs:
        if str.isalnum():
            strs.append(str.lower())
    # compare
    while True:
        if len(strs) <= 1:
            print('True')
            break
        elif strs.pop(0) != strs.pop():
            print('False')
            break

def slicing_palindrome(input_strs):
    # preprocessing: consider only lower alphabet and numbers
    strs = []
    for str in input_strs:
        if str.isalnum():
            strs.append(str.lower())
    # flip the list
    srts = strs[::-1]
    if strs == srts:
        print("True")
    else:
        print("False")

list_palindrome("A man, a plan, a canal: Panama")
slicing_palindrome("A man, a plan, a canal: Panama")
