from os import strerror

name = input("cual es el nombre del archivo? ")

try:
    file = open(name, 'r')
except IOError as e:
    print("No puede abrir el archivo.", strerror(e.errno))
    exit()
    
store = {}
count = 0

read = file.read()
for char in read:
    if char.isalpha() == True:
        if char not in store.keys():
            count = 1
            store.update({char.lower(): count})
        else:
            count += 1
            store.update({char.lower(): count})

clean_name = name.split('.')[0]
output = open(clean_name + '.hist', 'w+t')


newstore = {}

for key, value in sorted(store.items(), key=lambda x: x[1], reverse=True):
    output.write(str(key) + ' --> ' + str(value) + '\n')

file.close()
output.close()
