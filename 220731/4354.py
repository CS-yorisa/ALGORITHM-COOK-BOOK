while True:
    s = input()
    if s == '.':
        break
    s_len = len(s)
    p = [0 for _ in range(s_len)]
    
    j = 0
    for i in range(1, s_len):
        while j>0 and s[i]!=s[j]:
            j=p[j - 1]
        if s[i] == s[j]:
            j+=1
            p[i] = j
    p_len = s_len - p[s_len - 1]
    
    if s_len%p_len == 0:
        print(s_len//p_len)
    else:
        print(1)
