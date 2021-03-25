# https://www.youtube.com/watch?v=Uh2ebFW8OYM

# f = open("test.txt", "r")
#f = open("test.txt", "w")
#f = open("test.txt", "a")
#f = open("test.txt", "r+")

# print(f.name)
# print(f.mode)

# f.close()

#! READING A FILE
# with open("test.txt", "r") as f:
# f_contents = f.read()
# print(f_contents)
# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line
# 6) Sixth line
# 7) Seventh line
# 8) Eighth line
# 9) Ninth line
# 10) Tenth line

# f_contents = f.readline()
# print(f_contents, end="")
# 1) This is a test file

# f_contents = f.readline()
# print(f_contents, end="")
# 2) With multiple lines of data...

# f_contents = f.readlines()
# print(f_contents, end="")
# ['3) Third line\n', '4) Fourth line\n', '5) Fifth line\n', '6) Sixth line\n', '7) Seventh line\n', '8) Eighth line\n', '9) Ninth line\n', '10) Tenth line']

# for line in f:
#     print(line, end="")

# f_contents = f.read(sizeToRead)  # pass no of chars
# print(f_contents)

# f_contents = f.read(sizeToRead)  # pass no of chars
# print(f_contents)

# f_contents = f.read(sizeToRead)  # pass no of chars
# print(f_contents)

# sizeToRead = 10
# f_contents = f.read(sizeToRead)  # pass no of chars

# while len(f_contents) > 0:
#     print(f_contents, end="")
#     f_contents = f.read(sizeToRead)

# f_contents = f.read(sizeToRead)  # pass no of chars
# print(f_contents)

# f.seek(0)

# f_contents = f.read(sizeToRead)  # pass no of chars
# print(f_contents)

# pass

#! WRITE
# with open("test2.txt", 'w') as f:
#     f.write("Test")
#     f.seek(0)
#     f.write("R")
#     pass

#! Make a copy of file
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('unsplash.jpg', 'rb') as rf:
    with open('unsplash_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
