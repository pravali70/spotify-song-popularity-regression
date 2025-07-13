def solve(N):
    MOD = 10**9 + 7
    
    # Target sum for each player
    target = 2 * N
    
    # All possible permutations of [1, 2, 3]
    permutations = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    
    # dp[i][s1][s2] = number of ways to achieve sums s1, s2 for players 1, 2 after i turns
    # Player 3's sum is determined as 6*i - s1 - s2
    dp = {}
    
    # Base case: 0 turns, all sums are 0
    dp[0] = {(0, 0): 1}
    
    for turn in range(1, N + 1):
        dp[turn] = {}
        
        for (s1, s2), count in dp[turn - 1].items():
            s3 = 6 * (turn - 1) - s1 - s2
            
            # Try each permutation
            for perm in permutations:
                new_s1 = s1 + perm[0]
                new_s2 = s2 + perm[1]
                new_s3 = s3 + perm[2]
                
                # Check if new sums are valid (non-negative and within bounds)
                if new_s1 >= 0 and new_s2 >= 0 and new_s3 >= 0:
                    if new_s1 <= 3 * N and new_s2 <= 3 * N and new_s3 <= 3 * N:
                        key = (new_s1, new_s2)
                        if key not in dp[turn]:
                            dp[turn][key] = 0
                        dp[turn][key] = (dp[turn][key] + count) % MOD
    
    # Answer is the number of ways to achieve target sum for all players
    key = (target, target)
    return dp[N].get(key, 0)

if __name__ == "__main__":
    # Read input and solve
    N = int(input().strip())
    print(solve(N))