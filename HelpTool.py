import itertools


# Help Tools

def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def shake_number(num):
    len_num = len(str(num))
    shaked_number_list = []
    for indiv in itertools.permutations(range(len_num)):
        temp = ''
        if str(num)[indiv[0]] == '0': continue
        for idx in indiv:
            temp += str(num)[idx]
        shaked_number_list.append(int(temp))
    return shaked_number_list