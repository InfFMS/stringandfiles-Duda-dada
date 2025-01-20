# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
with open("task3.txt", "r", encoding="utf-8") as f:
    task3 = f.read()
task3 = task3.lower()
import string

for punct in string.punctuation:
    task3 = task3.replace(punct, ' ')

words = task3.split()
word_nums = {}
for word in words:
    if word in word_nums:
        word_nums[word] += 1
    else:
        word_nums[word] = 1

words_sorted = sorted(word_nums.items())

with open("task3new.txt", "w", encoding="utf-8") as f_new:
    for word, count in words_sorted:
        f_new.write(f"{word}: {count}\n")
