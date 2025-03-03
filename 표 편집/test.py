def solution1(n, k, cmd):
    answer = ['O'] * n
    hist = []
    p = 0
    for i in cmd:
        if i[0] == 'D':
            p += int(i[2:])
        elif i[0] == 'U':
            p -= int(i[2:])
        else :
            while p > 0:
                k += 1
                if answer[k] == 'O':
                    p -= 1
            while p < 0:
                k -= 1
                if answer[k] == 'O':
                    p += 1
            if i[0] == 'C':
                answer[k] = 'X'
                hist.append(k)
                k2 = k - 1
                while k < n and answer[k] == 'X':
                    k += 1
                if k == n:
                    k = k2
                    while answer[k] == 'X':
                        k -= 1
            else :
                answer[hist.pop()] = 'O'

    return ''.join(answer)

def solution2(n, k, cmd):
    answer = {}
    for i in range(-1, n + 1):
        answer[i] = ['O', i - 1, i + 1]
    hist = []
    p = 0
    for i in cmd:
        if i[0] == 'D':
            p += int(i[2:])
        elif i[0] == 'U':
            p -= int(i[2:])
        else :
            while p > 0:
                k = answer[k][2]
                p -= 1
            while p < 0:
                k = answer[k][1]
                p += 1
            
            if i[0] == 'C':
                answer[k][0] = 'X'
                hist.append(k)
                answer[answer[k][1]][2] = answer[k][2]
                answer[answer[k][2]][1] = answer[k][1]
                if answer[k][2] == n :
                    k = answer[k][1]
                else :
                    k = answer[k][2]
                
            else :
                j = hist.pop()
                answer[j][0] = 'O'
                j2 = j - 1
                while answer[j2][0] == 'X':
                    j2 -= 1
                answer[j][1] = j2
                answer[j][2] = answer[j2][2]
                answer[j2][2] = j
                answer[answer[j][2]][1] = j

    ans = [answer[i][0] for i in range(n)]
    return ''.join(ans)

def solution(n, k, cmd):
    if n > 300000:
        return solution1(n, k, cmd) #효율성 8 실패
    else :
        return solution2(n, k, cmd) #효율성 6 실패
    #test6_n > 300000 > test8_n > 200000

n = 8; k = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd1))
print(solution(n, k, cmd2))
sol1 = "OOOOXOOO"
sol2 = "OOXOXOOO"