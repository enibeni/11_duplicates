# Анти-дубликатор

Скрипт для поиска файлов дубликатов в указанной директории.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.
В качестве параметра нужно указать директорию в которой нужно найти дубликаты.

Пример выполнения скрипта, Python 3.5:

```bash
$ python3 duplicates.py dir_with_files/
Сканирую...dir_with_files/
Сканирую...dir_with_files/dir_2
Сканирую...dir_with_files/dir_2/dir_2_1
Сканирую...dir_with_files/dir_1
Сканирую...dir_with_files/dir_1/dir_1_2
Сканирую...dir_with_files/dir_1/dir_1_1
Сканирую...dir_with_files/dir_1/dir_1_1/dir_1_1_1

Найдены дубликаты:
Названия могут быть разными, но содержание одинаковым
___________________
dir_with_files/dir_1/file.txt
dir_with_files/dir_1/dir_1_2/filed.txt
dir_with_files/dir_1/dir_1_1/file.txt
dir_with_files/dir_1/dir_1_1/dir_1_1_1/file.txt
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
