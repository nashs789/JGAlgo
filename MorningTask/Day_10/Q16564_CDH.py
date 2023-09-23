# N개의 캐릭터
# 각 캐릭터의 레벨 xi, 총합 K
# 팀목표레벨 T

import sys
input = sys.stdin.readline

N, K = map(int,input().split()); # 3 10
levels = [(int(input())) for _ in range(N)];
levels.sort(); #[ 10, 15, 20 ]
# start, end , mid , while조건
T = 0;
# 5, 20, 7
# mid = 팀의 목표 레벨
# end = 레벨 리스트중 가장 큰수 +올릴 수 잇는 레벨의 총합

#mid 값보다 작은 level 차이의 총합
def get_diff(mid):
    diff = 0;
        for level in levels:
                if(level < mid):
                            diff += (mid - level);
                                    else:
                                                break;
                                                    return diff;



                                                                                start, end  = levels[0], levels[-1] + K
                                                                                mid = 0;
                                                                                while(start < end): # 10 < 20
                                                                                    mid = (start + end) // 2
                                                                                        if(get_diff(mid) < K):



                                                                                                                    print(levels);
                                                                                                                    print(min(T));
