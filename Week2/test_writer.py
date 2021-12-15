
line = 'This is a test line to write to "test.txt"\n'

f = open('test.txt', 'w')
f.write(line)
f.close()

f = open('test.txt')
print(f.readlines())
f.close()

f = open('test.txt', 'a')
lines = ['This is one line\n', 'This is a second line\n']
f.writelines(lines)
f.close()
