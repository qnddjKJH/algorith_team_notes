

# 병사 배치하기
# n명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유
# 병사를 배치 할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도
# 남아있는 병사의 수가 최대가 외었으면 합니다.
# 정렬로 위치시키는 것이 아닌 열외시켜서 정렬 시키는 것
# 15 11 4 8 5 2 4 -> 4와 2를 열외 -> 15 11 8 5 4

# n 입력 (1<=n<=2000)
# 전투력 <= 10,000,000 자연수
# 출력은 열외 시켜야하는 병사의 수

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n
# 지금 문제 해결은 => 정렬하는 병사의 수를 구하는 중
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:  # 앞의 병사가 다음 병사보다 작을 경우
            # 이렇게 계산하면 다음 병사가 작으면 dp 의 값은 변하지 않는다
            dp[i] = max(dp[i], dp[j] + 1)

# 병사의 수를 구했으므로 전체 병사 수 - 정렬된 병사 수 하여 결과값 도출
print(n - max(dp))
