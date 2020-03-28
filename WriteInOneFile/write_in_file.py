import os
output = ''
for file in os.listdir('test_neg/'):
    with open('test_neg/'+file, "r",encoding="utf-8") as f:
        content = f.read()
    output += content + '\n'
output_bytes = bytes(output, encoding = 'utf-8')
with open('final.txt', 'wb') as f:
    f.write(output_bytes)