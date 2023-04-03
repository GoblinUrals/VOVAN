# Python program to explain os.lseek() method

# importing os module
import os

# path
path = 'C:/Users/Rajnish/Desktop/testfile.txt'

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# String to be written
s = 'GeeksforGeeks - A Computer Science portal'

# Convert the string to bytes
line = str.encode(s)

# Write the bytestring to the file
# associated with the file
# descriptor fd
os.write(fd, line)

# Seek the file from beginning
# using os.lseek() method
os.lseek(fd, 0, 0)

# Read the file
s = os.read(fd, 13)

# Print string
print(s)

# Close the file descriptor
os.close(fd)