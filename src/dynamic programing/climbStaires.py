'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n):
    if n < 1:
        return 1
    solutions = {1: 1, 2: 2}
    for i in range(3, n + 1):
        solutions[i] = solutions[i - 1] + solutions[i - 2]

    return solutions[n]

print(climbStairs(10))
# 89



#time complextity O(n ) space complexity o(n)

def climbStairs3(n):
    dp=[-1]*(n+1)
    
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    dp[0]=0
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#time complexity O(n) space complexity O(1)

def climbStairs4(n):
    dp=[-1]*(n+1)
    
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    
    a=1
    b=2
    
    for i in range(3,n+1):
        c=b+a
        b,a=c,b
        
        
    return c
    

print("O(n)")
print(climbStairs3(10))
print("O(1)")
print(climbStairs4(10))