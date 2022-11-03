from os import strerror

conter = {chr(ch): 0 for ch in range(ord('a'), ord('z')+1)}
name =input("Ingrese el nombre: ")

try:
    h =open(name)
    for linea in h:
        for char in linea:
            if char.isalpha():
                conter[char.lower()]+=1
    h.close()
    for char in sorted(conter.keys(),
            key=lambda x: conter[x]):
            cnt = conter[char]
            if cnt > 0:
                print(char, '->', cnt)
                
except IOError as e:
    print("Error",strerror(e.errno))
