### PROGRAM : Reverse Cipher program
### Coded By : Suman Gangopadhyay
### Email ID : linuxgurusuman@gmail.com
### Date : 23-Nov-2016

msg = input("Enter your Message to code # ")
cipher = ""
length_of_msg = len(msg)-1
while length_of_msg >=0:
    cipher = cipher + msg[length_of_msg]
    length_of_msg = length_of_msg - 1
print("Encypted Reverse Cipher # "+cipher)