def print_result(func_to_decorate):
    def decorated_func(*args):
        print(func_to_decorate.__name__)
        res = func_to_decorate(*args)
        if isinstance(res, list):
            for el in res:
                print(el)
            return res
        elif isinstance(res, dict):
            for el in res:
                print('{} = {}'.format(el, res.get(el)))
            return res
        else:
            print(res)
    return decorated_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
