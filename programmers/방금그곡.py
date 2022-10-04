m = "CDEFGAC"
musicinfos =  ["12:00,12:06,HELLO,CDEFGA"]
def solution(m, musicinfos):
    m_list = []
    i = 0
    # 리스트로 전부 만들어 줌 ex)[C#, C, B]
    while i < len(m):
        if m[i] != '#':
            m_list.append(m[i])
        else:
            a = m_list.pop()
            m_list.append(a+m[i])
        i += 1

    ans = ''
    max_t = 0
    for k in range(len(musicinfos)):
        st, ed, title, melody = musicinfos[k].split(',')
        st_h, st_m = map(int, st.split(':'))
        ed_h, ed_m = map(int, ed.split(':'))
        # 시간을 계산
        time = (ed_h - st_h)*60
        if ed_m - st_m < 0:
            time -= 60
            time += 60 + ed_m - st_m
        else:
            time += ed_m - st_m
            
        # 노래의 멜로디도 똑같이 리스트로 만들어 줌
        melody_list = []
        i = 0
        while i < len(melody):
            if melody[i] == '#':
                a = melody_list.pop()
                melody_list.append(a+melody[i])
            else:
                melody_list.append(melody[i])
            i += 1

        # 시간만큼 멜로디를 반복할테니 그 안에 내가 찾는 멜로디가 있다면 비교후 갱신시켜줌
        for i in range(time-len(m_list)+1):
            for j in range(len(m_list)):
                if melody_list[(i+j)%len(melody_list)] != m_list[j]:
                    break
            else:
                if time > max_t:
                    max_t = time
                    ans = title

    return ans if ans else "(None)"
print(solution(m, musicinfos))