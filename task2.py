# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.

with open("task2.txt", "r", encoding="utf-8") as f:
    task2 = f.read()
python_count = task2.count("Python")
new_text = task2.replace("Python", " Питон")
with open("task2new.txt", "w", encoding="utf-8") as f_new:
    f_new.write(new_text)

print(" Количество замен:", python_count)
