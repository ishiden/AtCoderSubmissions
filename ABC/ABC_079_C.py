import sys

input = sys.stdin.readline

def main():
    ans,p,m = '','+','-'
    n = input().rstrip('\n')
    for i in range(2**3):
        ans = [n[0], p, n[1], p, n[2], p, n[3]]
        for j in range(3):
            if i>>j&1:
                ans[2*j+1] = m
        if eval(''.join(ans)) == 7:
            break
    ans = ''.join(ans) + '=7'
    print(ans)



# def main():
#     ans = ""
#     nums = list(map(int, list(input().rstrip("\n"))))

#     for i in range(2**3):
#         ts = sum(nums)
#         ops = ['+']*3
#         for j in range(3):
#             if i>>j&1:
#                 ts -= nums[j+1]*2
#                 ops[j]='-'
#         if ts == 7:
#             for i in range(3):
#                 ans += str(nums[i])+ops[i]
#             ans += str(nums[3])+"=7"
#             break
#     print(ans)

if __name__ == '__main__':
    main()