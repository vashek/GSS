def save_output(data, outfile):
    with open(outfile, 'w+', encoding='utf-8') as file:
        file.write(data)

charset = []

for i in range(192, 382):
    charset += chr(i)


n = 5
lst1 = [charset[i:i+n] for i in range(0, len(charset), n)]
str1 = ''

for lst in lst1:
    word = ''

    for a in lst:
        word = word + a

    str1 = str1 + ', ' + word
    word = ''


output = 'input3.txt'
save_output(str1, output)
