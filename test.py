import random

val = []
for i in range(10):
    r = random.randint(0, 25)
    asciiCode = ord('a') + r # ord() でアルファベットをアスキーコードに変換
    ch = chr(asciiCode) # chr()でアスキーコードをアルファベットに変換
    val.append(ch)

print(val)
