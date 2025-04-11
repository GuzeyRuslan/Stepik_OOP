def takes_positive(func):
    def inner(*args, **kwargs):
        out_list = []
        out_dict = {}
        for num in args:
            if not isinstance(num, int):
                raise TypeError
            elif isinstance(num, int) and num <= 0:
                raise ValueError
            else:
                out_list.append(num)
        for key, val in kwargs.items():
            if not isinstance(kwargs[key], int):
                raise TypeError
            elif isinstance(kwargs[key], int) and kwargs[key] <= 0:
                raise ValueError
            else:
                out_dict[key] = val
        return func(*out_list, **out_dict)
    return inner


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))