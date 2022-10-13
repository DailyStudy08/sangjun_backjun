record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
chat_room = dict()
answer = []
result = []
first = ''
for i in record:
    console, *id_name = i.split()
    if console == 'Enter' or console == 'Leave':
        if console == 'Enter':
            chat_room[id_name[0]] = id_name[1]
            if id_name[0] == first:
                chat_room[id_name[0]] = id_name[1]
        result.append((console, id_name[0]))
    else:
        chat_room[id_name[0]] = id_name[1]
for j in result:
    if j[0] == 'Enter':
        answer.append(f'{chat_room[j[1]]}님이 들어왔습니다.')
    elif j[0] == 'Leave':
        answer.append(f'{chat_room[j[1]]}님이 나갔습니다.')
print(answer)