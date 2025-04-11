def remember_args():
    out_list = []
    def inner(*args):
        out_list.append(args)
        return out_list
    return inner



save = remember_args()
save(1, 2, 3)
save("a", "b")
print(save(4, 6, 8))  # [(1, 2, 3), ('a', 'b')]