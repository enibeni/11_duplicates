import os
import sys
import hashlib


def get_duplicate_files(start_path):
    duplicate_files = {}
    for dir_name, subdir_list, file_list in os.walk(start_path):
        print("Сканирую...{}".format(dir_name))
        for filename in file_list:
            path_to_file = os.path.join(
                dir_name,
                filename
            )
            file_hash = hashfile(path_to_file)
            if file_hash in duplicate_files:
                duplicate_files[file_hash].append(path_to_file)
            else:
                duplicate_files[file_hash] = [path_to_file]
    return duplicate_files


def hashfile(path, blocksize=65536):
    """https://www.pythoncentral.io/finding-duplicate-files-with-python/
    """
    hasher = hashlib.md5()
    afile = open(path, 'rb')
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def print_duplicate_files(duplicate_files):
    results = list(filter(
        lambda x: len(x) > 1,
        duplicate_files.values())
    )
    if len(results) > 0:
        print('\nНайдены дубликаты:')
        print('Названия могут быть разными,но содержание одинаковым')
        print('___________________')
        for result in results:
            for subresult in result:
                print(subresult)
            print('___________________')
    else:
        print('Дубликатов не найдено')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        sys.exit("Для работы программы введите имя директории")

    if os.path.exists(start_path):
        duplicate_files = get_duplicate_files(start_path)
        print_duplicate_files(duplicate_files)
    else:
        sys.exit("Введено неверное имя директории")

