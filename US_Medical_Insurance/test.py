def solution(n, k, cmd):
    tot = n - 1
    del_lst = []
    answer = ''
    
    for i in cmd:
        if 'U' in i:
            num = int(i[2:])
            k -= num
            if k < 0:
                k = 0
        elif 'D' in i:
            num = int(i[2:])
            k += num
            if k > tot:
                k = tot
        elif i == 'C':
            del_lst.append(k)
            if k == tot:
                k -= 1
            tot -= 1
        elif i == 'Z':
            tot += 1
            u = del_lst.pop()
            if u <= k:
                k += 1
        
    j = 0
    while j < n:
        if j in del_lst:
            answer += "X"
        else:
            answer += "O"
        j += 1
            
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))