start_sentence = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."

question_sentence = "\"재귀함수가 뭔가요?\""

recursion_sentence_1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."  

recursion_sentence_2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."

recursion_sentence_3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"" 

answer ="\"재귀함수는 자기 자신을 호출하는 함수라네\""#파이썬에서 따옴표 표기하는 법

end_sentence = '라고 답변하였지.'

under_line = '____'

def recursion_bot(N, K):
  print(under_line * (K-1), end="")
  print(question_sentence)
  print(under_line * (K-1), end="")
  print(recursion_sentence_1)
  print(under_line * (K-1), end="")
  print(recursion_sentence_2)
  print(under_line * (K-1), end="")
  print(recursion_sentence_3)

  if N > K:
    recursion_bot(N, K + 1)
    print(under_line * K, end='')
    print(end_sentence)

  if K == N:
    print(under_line * (N), end='')
    print(question_sentence)
    print(under_line * (N), end='')
    print(answer)
    print(under_line * (N), end='')
    print(end_sentence)

N = int(input())
K = 1
print(start_sentence)
recursion_bot(N,K)
print(end_sentence)