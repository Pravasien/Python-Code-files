"""
Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
"""
Palindrome_OG=(1,2,3,3,2,1)
Palindrome_Rev=Palindrome_OG[::-1]
if Palindrome_OG == Palindrome_Rev:
    print("the number",Palindrome_OG,"is a palindrome")
else:
    print("The number",Palindrome_OG,"is not a palindrome")