a=[]
for i in range(9):
    a.append(int(input()))

sorted_a = sorted(a)

max = sorted_a[8]
#print(a) [3, 29, 38, 12, 57, 74, 40, 85, 61]
#print(sorted_a) [3, 12, 29, 38, 40, 57, 61, 74, 85]
print(max)
print(a.index(max)+1)

#JS와는 다르게 sorted_a = a.sort() 라고 정렬된 리스트를 다른 리스트를 선언해서 저장하려고 하면
#원래 리스트 a가 정렬되어서 저장되고 sorted_a는 아무것도 아니게 되어버려서 시간을 좀 썼음
#정렬한 리스트를 따로 저장하려면 b = sorted(a)라고 해야 함