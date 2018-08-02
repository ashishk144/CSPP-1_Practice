"""Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5"""

def main():
	S = input("Enter the string")
	I = 0
	C = 0
	for I in range(S):
		if char(ord(I))='a' or char(ord(I))='e' 
		or char(ord(I))='i' or char(ord(I))='o' or char(ord(I))='u':
		C += 1
	I += 1
print(C)
if __name__== "__main__":
	main()