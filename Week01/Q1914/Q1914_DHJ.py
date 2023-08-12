move_list = []

def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)
 
    move_list.append(f'{no} {y}')

    if no > 1:
        move(no - 1, 6 -x -y, y)

N = int(input())
move_time = 2**N - 1

if move_time < 20:
  move(N, 1, 3)
  print(move_time)
  for move_ in move_time:
      print(move_)
else:
    print(move_time)


#방법은 맞았으나 시간이 초과하여 질문게시판에서 얻은 팁
#하노이의 탑 문제에서 이동횟수는 무조건 2**n - 1 번이므로 20번 이하로 나왔을 경우에만 함수를 실행시켜서 이동경로를 기록하면 통과할 수 있다.