import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    leftMax, rightMax = 0, 0
    leftIdx, rightIdx = 0, 0
    rightStartIdx = int(2**N/2)
    for i in range(rightStartIdx):
        if A[i] > leftMax:
            leftIdx = i
            leftMax = A[i]
        if A[rightStartIdx + i] > rightMax:
            rightIdx = rightStartIdx + i
            rightMax = A[rightStartIdx + i]
    if leftMax > rightMax:
        ans = rightIdx
    else:
        ans = leftIdx
    print(ans+1)

if __name__ == '__main__':
    main()