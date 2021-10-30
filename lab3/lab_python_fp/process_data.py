import json
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

path = 'data_light.json'

with open('data_light.json', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(Unique(sorted(field(arg, 'job-name')), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda str: str.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda job: job + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary_list = [x for x in gen_random(len(arg), 100_000, 200_000)]
    return ['{}, зарплата {} руб.'.format(x, y) for x, y in zip(arg, salary_list)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
