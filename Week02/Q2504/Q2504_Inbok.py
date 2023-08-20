# import sys
# from copy import copy

# if __name__ == "__main__":
#     stack = list(sys.stdin.readline().replace("()", "2").replace("[]", "3").strip('\n'))
#     chk_list = []
#     temp = 1
#     result = 0

#     for ch in stack: 
#         if ch.isnumeric():
#             continue

#         if len(chk_list) != 0:
#             if ch == ")" and chk_list[-1] == "(":
#                 chk_list.pop()
#                 continue
#             elif ch == "]" and chk_list[-1] == "[":
#                 chk_list.pop()
#                 continue

#         chk_list.append(ch)

#     if len(chk_list) != 0:
#         print(0)
#         sys.exit()

#     while len(stack) != 0:
#         ch = stack.pop()
        
#         if ch == ")":
#             temp *= 2
#         elif ch == "]":
#             temp *= 3
#         elif ch == "(":
#             temp /= 2
#         elif ch == "[":
#             temp /= 3
#         else:
#             result += int(ch) * int(temp)

#     print(result)

import sys
from copy import copy

if __name__ == "__main__":
    stack = list(sys.stdin.readline().replace("()", "2").replace("[]", "3").strip('\n'))
    chk_list = []
    temp = 1
    result = 0

    for ch in stack: 
        if ch == "(":
            temp *= 2
        elif ch == "[":
            temp *= 3
        elif ch == ")":
            temp /= 2
        elif ch == "]":
            temp /= 3
        else:
            result += int(ch) * int(temp)

        if ch.isnumeric():
             continue

        if len(chk_list) != 0:
            if ch == ")" and chk_list[-1] == "(":
                chk_list.pop()
                continue
            elif ch == "]" and chk_list[-1] == "[":
                chk_list.pop()
                continue

        chk_list.append(ch)

    if len(chk_list) != 0:
        print(0)
    else: 
        print(result)