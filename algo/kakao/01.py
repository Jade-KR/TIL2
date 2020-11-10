def solution(new_id):
    new_id = list(new_id)
    answer = []
    result = ''
    check = ['-', '_', '.']
    for i in new_id:
        if i.isdigit():
            answer.append(i)
        elif 65 <= ord(i) <= 90:
            answer.append(i.lower())
        elif 96 < ord(i) < 123:
            answer.append(i)
        else:
            if i in check:
                if len(answer) == 0:
                    answer.append(i)
                else:
                    if i == '.' and i != answer[-1]:
                        answer.append(i)
                    else:
                        if i != '.':
                            answer.append(i)



    while len(answer):
        if answer[0] == '.':
            answer.pop(0)
        else:
            break

    while len(answer):
        if answer[-1] == '.':
            answer.pop()
        else:
            break

    if len(answer) == 0:
        answer = ['a']

    if len(answer) >= 16:
        answer = answer[0:16]
        if answer[-1] == '.':
            answer.pop()

    if len(answer) <= 2:
        while len(answer) <= 2:
            answer.append(answer[-1])

    for k in answer:
        result += k
    return result

q = "...!@BaT#*..y.abcdefghijklm"
print(solution(q))