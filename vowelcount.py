#!/usr/bin/python
# Author Name : Suman Gangopadhyay
# Date : 10-May-2017

# Function to Count total number of Vowels and individual Vowels in a string
def VowelCount(string):
	a_count = 0;
	e_count = 0;
	i_count = 0;
	o_count = 0;
	u_count = 0;
	string_length = len(string);
	total_vowels = 0;
	for i  in string:
			if (i == "a"):
				a_count = a_count + 1;
			if (i == "e"):
				e_count = e_count + 1;
			if (i == "i"):
				i_count = i_count + 1;
			if (i == "o"):
				o_count = o_count + 1;
			if (i == "u"):
				u_count = u_count + 1;
	total_vowels = (a_count + e_count + i_count + o_count + u_count);
	total_consonents = (string_length - total_vowels);
	print("Total Number of Vowels     : ", total_vowels);
	print("Total Number of Consonents : ", total_consonents);
	print("No. of A Count : ", a_count);
	print("No. of E Count : ", e_count);
	print("No. of I Count : ",i_count);
	print("No. of O Count : ",o_count);
	print("No. of U Count : ",u_count);
