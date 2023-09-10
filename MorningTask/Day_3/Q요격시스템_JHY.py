def solution(targets):
    answer = 0
    targets.sort(key = lambda x:[x[1],x[0]])
    
    s,e = 0,0 
    for x in targets:
        if(x[0]>=e):
            e = x[1]
            answer += 1
    return answer