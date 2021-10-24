# используется для сортировки
from operator import itemgetter


class Disk:
    """CD-диск"""

    def __init__(self, id, name, size, lib_id):
        self.id = id
        self.name = name
        self.size = size
        self.lib_id = lib_id


class Library:
    """Библиотека"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DiskLib:
    """
    'Диски библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, lib_id, disk_id):
        self.lib_id = lib_id
        self.disk_id = disk_id


# Библиотеки
libs = [
    Library(1, 'музыка'),
    Library(2, 'аниме'),
    Library(3, 'игры'),

    Library(41, 'архив фотографий'),
    Library(42, 'фотографии выпускной'),

    Library(51, 'архив видео'),
    Library(52, 'видео анапа 2012'),
]

# Диски
disks = [
    Disk(1, 'КиШ', 300, 1),
    Disk(2, 'Наутилус Помпилиус', 250, 1),
    Disk(3, 'Linkin Park', 231, 1),

    Disk(4, 'K-On', 165, 2),
    Disk(5, 'Evangelion', 50, 2),

    Disk(6, 'Minecraft', 30, 3),
    Disk(7, 'Охота: Разборка', 60, 3),
    Disk(8, 'Тетрис', 10, 3),

    Disk(9, 'Выпускной', 1, 41),
    Disk(10, 'Зоопарк', 2, 41),
    Disk(11, 'Обои', 1, 41),

    Disk(12, 'Отпуск 2012', 8, 51),
    Disk(13, 'Запись концерта', 6, 51),
    Disk(14, 'летсплей маинкрафт', 4, 51),
    Disk(15, 'Огурцы', 100, 51)
]

disks_libs = [
    DiskLib(3, 7),
    DiskLib(41, 9),
    DiskLib(41, 10),
    DiskLib(51, 11),
    DiskLib(51, 12),
    DiskLib(51, 15),

    DiskLib(42, 9),
    DiskLib(52, 11),
    DiskLib(52, 15)
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(l.name, d.name, d.size)
                    for l in libs
                    for d in disks
                    if d.lib_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, dl.lib_id, dl.disk_id)
                         for l in libs
                         for dl in disks_libs
                         if l.id == dl.lib_id]

    many_to_many = [(d.name, d.size, lib_name)
                    for lib_name, lib_id, disk_id in many_to_many_temp
                    for d in disks if d.id == disk_id]

    print('Задание E1')
    res_11 = {}
    for l in libs:
        if 'архив' in l.name:
            l_disks = [rec[1] for rec in one_to_many if rec[0] == l.name]
            res_11[l.name] = l_disks

    print(res_11)

    print('Задание E2')
    res_12 = []
    for lib in libs:
        lib_disks = list(filter(lambda i: i[0]==lib.name, one_to_many))
        if len(lib_disks) > 0:
            lib_size = [size for _,_,size in lib_disks]
            lib_size_avg = sum(lib_size) / len(lib_disks)
            res_12.append((lib.name, round(lib_size_avg, 2)))

    print(sorted(res_12, key=itemgetter(1), reverse=True))

    print('Задание E3')
    res_13 = {}
    for d in disks:
        if d.name.lower()[0] == 'о':
            d_libs = [rec[2] for rec in many_to_many if d.name == rec[0]]
            res_13[d.name] = d_libs

    print(res_13)


if __name__ == '__main__':
    main()
