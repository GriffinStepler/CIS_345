# Two ways to open a file

# open file and write to it. Terms File connection, stream, pointer
# file paths: c:\\ requires two backslashes due to escape sequences
# OR c:/users/ single forward slashes

# files that you read from have to be in your project folder if not given an explicit path
# open('file name', 'w - write, r - read, a - append', )
file = open('file1.txt', 'w')  # file path: need to include file name and extension
file.write('line 1\n')
file.write('line 2\nline 3\n')
file.close()  # when opening using the open function, you must close it

lines = ['a\n', 'b\n', 'c\n']
file = open('file1.txt', 'a')
file.writelines(lines)
file.close()

# opening a file using a with statement - fp stands for file "pointer"
# with open('file1.txt', 'r') as fp:
#     word = fp.read(4)  # argument = number of characters to read
#     fp.seek(0)  # moves read cursor to this index
#     line = fp.readline()
#     fp.seek(0)
#     content = fp.readlines()  # reads everything in the file
#     print(word)
#     print(line)
#     print(content)
#     # with statements automatically closes the file

with open('file1.txt', 'r') as fp:
    for line in fp:
        line = line.strip()  # trims any leading or following empty characters
        print(line)  # end=''
