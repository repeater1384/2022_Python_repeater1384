import itertools


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


def sol_2072():
    T = int(input())
    for t in range(1, T + 1):
        odd_list = [i for i in map(int, input().split()) if i % 2]
        print(f'#{t} {sum(odd_list)}')


def sol_14361():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        check = False
        for shaked_num in shake_number(N):
            if shaked_num % N == 0 and shaked_num > N:
                check = True
                break
        print(f'#{t} {"possible" if check else "impossible"}')


if __name__ == "__main__":
    sol_14361()
