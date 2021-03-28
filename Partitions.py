peas = {}
peas[0]=1

def third_seq(n):
    return [((i+2)*(i%2))+(int(0.5*i)+1)*((i+1)%2) for i in range(n)]

def second_seq(n):
    seq3 = third_seq(n-1)
    seq2 = [1]
    for val in seq3:
        seq2.append(seq2[-1]+val)
    return seq2

def p(n,seq2):
    plist = [n-i for i in seq2 if n-i >= 0]
    ans = 0
    for i, arg in enumerate(plist):
        try:
            val = peas[arg]
        except:
            peas[arg] = p(arg,seq2)
            val = peas[arg]
        if i%4<2:
            ans = ans + val
        else:
            ans = ans - val

    return ans


n=666
seq2 = second_seq(n)
answer = p(n,seq2)

print(seq2)
print(answer)
