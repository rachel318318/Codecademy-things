def solution(t, r):
    answer = []
    lst = []
    i = 0
    
    zip_sort = sorted(zip(t,r))
    sorted_t = [i[0] for i in zip_sort]
    sorted_r = [i[1] for i in zip_sort]
    
    j = sorted_t[0]
    
    while i < len(sorted_t):
        if sorted_t[i] == j:
            lst.append(sorted_r[i])
            i += 1
        else:
            if len(lst) == 1:
                n = lst.pop()
                answer.append(n)
            elif len(lst) > 1:
                m = min(lst)
                lst.remove(m)
                answer.append(m)
            j += 1
        
    if lst:
        for i in lst:
            m = min(lst)
            lst.remove(m)
            answer.append(m)
    
    return answer