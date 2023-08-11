def A():
    print('A')

def B():
    print('B')

def C():
    print('C')

def D():
    print('D')

score = int(input())
result = str(int(score / 10))

functions = {
    '10': A,
    '9' : A,
    '8' : B,
    '7' : C,
    '6' : D
}

fun = functions.get(result)

if fun == None:
    print('F')
else:
    functions[result]()