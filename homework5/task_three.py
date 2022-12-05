with open(r"C:\Users\minke\pr_python\homeworks\homework5\opentext.txt") as f:
    file = str(f.read())
text = input('Введите букву:')
counter = 0
for i in file:
    if i.lower() == text.lower():
        counter += 1
f.close()
print(f'Результат: буква встречается {int(counter)} раза в тексте')
