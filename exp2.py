import sys
with open('file.txt', 'w') as f:
    print(format('Hello, my friend, I am new here', '>20.5'), file=f)