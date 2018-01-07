import os
import sys
import hashlib
from collections import defaultdict


def get_files_dict(start_path):
    files_dict = defaultdict(list)
    for dir_name, subdir_list, file_list in os.walk(start_path):
        print_current_dir_name(dir_name)
        for filename in file_list:
            path_to_file = os.path.join(
                dir_name,
                filename
            )
            file_hash = hashfile(path_to_file)
            files_dict[file_hash].append(path_to_file)
    return files_dict


def print_current_dir_name(dir_name):
    print("Сканирую...{}".format(dir_name))


def get_dublicate_files(files_dict):
    duplicate_files = list(filter(
        lambda x: len(x) > 1,
        files_dict.values())
    )
    return duplicate_files


def hashfile(path_to_file, blocksize=65536):
    hasher = hashlib.md5()
    with open(path_to_file, 'rb') as file:
        buf = file.read(blocksize)
        hasher.update(buf)
    return hasher.hexdigest()


def print_duplicate_files(duplicate_files):
    if duplicate_files:
        print('\nНайдены дубликаты:')
        print('Названия могут быть разными, но содержание одинаковым')
        print('___________________')
        for duplicate_list in duplicate_files:
            for file_name in duplicate_list:
                print(file_name)
            print('___________________')
    else:
        print('Дубликатов не найдено')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        sys.exit("Для работы программы введите имя директории")

    if os.path.exists(start_path):
        files_dict = scan_directory(start_path)
        duplicate_files = get_dublicate_files(files_dict)
        print_duplicate_files(duplicate_files)
    else:
        sys.exit("Введено неверное имя директории")

