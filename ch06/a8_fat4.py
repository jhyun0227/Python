def fat1(num):
    # fat1(3) : fat1(2) * 3 => fat1(1) * 2 * 3 => 1 * 2 * 3
    # fat1(5) : fat1(4) * 5 => fat1(3) * 4 * 5 => fat1(2) * 3 * 4 * 5 => fat1(1) * 2 * 3 * 4 * 5 => 1 * 2 * 3 * 4 * 5
    if num > 1:
        print(num, "* ", end="")
        return fat1(num-1) * num
    else:
        print('1 = ', end="")
        return 1



print(fat1(3))
print(fat1(5))