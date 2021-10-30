data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

sort_with_lambda = lambda lst: sorted(lst, key=abs, reverse=True)

if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print(result)

    print(sort_with_lambda(data))
