import csv
with open('1.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile,delimiter=';',quotechar = '"')
    answer = sorted(list(reader)[1:])
    ans = dict()
    for g in answer:
        if g[1] not in ans:
            ans[g[1]] = [g[0]]
        else:
            ans[g[1]] += [g[0]]
while True:
    a = input()
    if a == 'game':
        break
    if a in ans:
        print(f'Персонаж {a} встречается в играх:')
        for key,value in ans.items():
            if key == a:
                k = 0
                while len(ans[a])>k and k<5:
                    print(ans[a][k])
                    k+=1
                    if k == 5: print('и др.')
    else: print('Этого персонажа не существует')
    
    
    
    
        
