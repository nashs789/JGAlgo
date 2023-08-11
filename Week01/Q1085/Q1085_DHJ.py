x, y, w, h = map(int,input().split()) #x축, y축 또는 직사각형의 변 중 어느값이 더 작은지

if (w-x) - x >= 0:
    x_minimum = x
else:
    x_minimum = w-x

if (h-y) - y >= 0:
    y_minimum = y
else:
    y_minimum = h-y
  
if(x_minimum - y_minimum) >= 0:
    print(y_minimum)
else:
    print(x_minimum) 