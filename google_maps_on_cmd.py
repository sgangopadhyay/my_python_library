# Program : Program to see a place on the Google Maps from Command Line
# Coded By : Suman Gangopadhyay
# Date : 22-Nov-2017

#! /usr/bin/python3.
#! python3.
import sys
import webbrowser
import pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
webbrowser.open("https://www.google.com/maps/place/"+address)

