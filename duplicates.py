import os
import sys
import hashlib


def scan_directory(start_path):
    files_dict = {}
    for dir_name, subdir_list, file_list in os.walk(start_path):
        print("Сканирую...{}".format(dir_name))
        for filename in file_list:
            path_to_file = os.path.join(
                dir_name,
                filename
            )
            file_hash = hashfile(path_to_file)
            if file_hash in files_dict:
                files_dict[file_hash].append(path_to_file)
            else:
                files_dict[file_hash] = [path_to_file]
    return files_dict


def filter_dublicate_files(files_dict):
    duplicate_files = list(filter(
        lambda x: len(x) > 1,
        files_dict.values())
    )
    return duplicate_files


def hashfile(path, blocksize=65536):
    """https://www.pythoncentral.io/finding-duplicate-files-with-python/
    """
    hasher = hashlib.md5()
    afile = open(path, 'rb')
    buf = afile.read(blocksize)
    while buf:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
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
        duplicate_files = filter_dublicate_files(files_dict)
        print_duplicate_files(duplicate_files)
    else:
        sys.exit("Введено неверное имя директории")

