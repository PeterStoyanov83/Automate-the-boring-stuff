"""Bitmap Message, by Al Sweigart al@inventwithpython.com
 Displays a text message according to the provided bitmap image.
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: tiny, beginner, artistic"""
""" notes from P. Stoyanov - Fixed the formatting on the output in the console!"""

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """ 
...................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ....................................................................
 """
import sys

width = 69
print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message or a symbol to display with the bitmap.')

message = input('> ')
while message == '' or message == ' ':
    print("Please visible message or symbol")
    message = input('> ')
    if message != "" or message != " ":
        continue

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        elif i > 0 and i % width == 0:
            print()
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.
