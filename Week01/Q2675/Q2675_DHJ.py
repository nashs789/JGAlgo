T = int(input())
for i in range(T):
    R, S = input().split()
    list_S = list(S)
    answer_list = []
    for i in list_S:
      answer_list.append(i * int(R))
    answer = ''.join(answer_list)
    print(answer)
    
    #JS에서는 신경쓰지 않아도 되었던 자료형 (int(R) 부분)이 꼬여서 쓸데없이 시간이 걸렸음