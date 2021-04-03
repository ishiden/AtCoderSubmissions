import sys
import bisect

input = sys.stdin.readline

def main():
    ans = 0
    N, M = map(int, input().split())
    points = [0] * (N + 1)
    for i in range(N):
        points[i + 1] = int(input())
    two = set()
    for i in range(N + 1):
        for j in range(N + 1):
            if points[i] + points[j] <= M:
                two.add(points[i] + points[j])
    two = sorted(two)

    for i in two:
        idx = bisect.bisect_left(two, M - i)
        ans = max(ans, i + two[idx])

    # for i in two:
    #     left, right, mid = 0, len(two) - 1, 0
    #     while right - left > 1:
    #         mid = (left + right) // 2
    #         if (i + two[mid] >= M):
    #             right = mid
    #         else:
    #             left = mid
    #     if i + two[left] > M:
    #         continue
    #     ans = max(ans, i + two[left])

    print(ans)

if __name__ == '__main__':
    main()