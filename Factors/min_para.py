# Return the first pair from square root of N
# Super fast compare to go from 1 --> square root of N
import math
def solution(N):
    
    limit = int(math.sqrt(N))
    min_peri = (N + 1) * 2 
    for i in range(limit,0,-1):
        if N % i == 0:
            return int(N / i + i) * 2
    return min_peri