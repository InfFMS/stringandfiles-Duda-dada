# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

import string


with open("task1.txt", "r", encoding="utf-8") as f:
    file_line = f.read()
print(file_line)
a_nums=0
for char in file_line:
    if char == "—":
        a_nums+=1
with open("task1.txt", "r", encoding="utf-8") as f:
    file_line = f.readlines()
line_count = len(file_line)
word_count = 0
for line in file_line:
    words = line.split()
    word_count += len(words)
symbol_count = 0
for line in file_line:
    symbol_count += len(line)

print("Общее количество строк:", line_count)
print("Общее количество слов:", word_count- a_nums)
print("Общее количество символов (включая пробелы):", symbol_count)
