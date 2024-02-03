import csv
with open('1.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile,delimiter=';',quotechar = '"')
    answer = sorted(list(reader)[1:])
    ans = dict()
    for g in answer:
        if g[0] not in ans:
            ans[g[0]] = [g[2]]
        else:
            ans[g[0]] += [g[2]]
    for key,values in ans.items():
        print(f'{key} - количество багов:{len(values)}')
    
    
        
