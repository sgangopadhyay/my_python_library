### PROGRAM : Caesar Cipher program
### Coded By : Suman Gangopadhyay
### Email ID : linuxgurusuman@gmail.com
### Date : 23-Nov-2016

msg = input("Enter your Message : ")
key = 10
mode = 'encrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = msg.upper()
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
    if num >= len(LETTERS):
        num = num - len(LETTERS)
    elif num < 0:
        num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)
