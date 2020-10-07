"""Ricky Tran - 1832920"""
word = input()

word1 = word.replace(' ', '')

word2 = word1[::-1]

if word1 == word2:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')
