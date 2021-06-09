# 두개의 배열 A와 B를 가지고 두 배열은 N개의 원소로 구성되어
# 배열의 원소는 모두 자연수
# N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수
# 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램
# 모든 원소는 천만보다 작다
# 1<=N<= 100,000, 0<= K <= N

# input
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
