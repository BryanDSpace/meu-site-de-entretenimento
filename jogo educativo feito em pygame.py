caracter_zero = 0
barra = "-----"
linha = f"{caracter_zero}|{caracter_zero}|{caracter_zero}\n{barra}"

print(linha)

import pyttsx3
import os
import time 

engine = pyttsx3.init()

roteiro = "testo"

for i in range(len(roteiro)):
    print(f"{roteiro[:i]}")
    time.sleep(0.05)
    os.system("cls")
print(roteiro)