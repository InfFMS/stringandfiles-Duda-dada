# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

import string

with open("task5.txt", "r", encoding="utf-8") as f:
    task5 = f.read()
    file_line = f.readlines()

for punct in string.punctuation:
    words = task5.split()
    task5 = task5.replace(punct, ' ')
    the_longest_word = ''
    the_longest_word = max(words, key=len)
    the_len = len(the_longest_word)
    new_file5 = {}
    with open("new_file5", "w", encoding="utf-8") as f_new:
        f_new.write(f"{'Его длинна:', the_len}\n{'Самое длинное слово:', the_longest_word}\n")

print('Его длинна:', the_len, 'Самое длинное слово:', the_longest_word)
