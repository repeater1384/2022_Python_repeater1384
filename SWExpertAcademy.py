T = int(input())
for t in range(1, T + 1):
    N,D = map(int,input().split())
    answer = (N // (D * 2 + 1)) + (1 if N % (D*2+1) else 0)
    print(f'#{t} {answer}')
