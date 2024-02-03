import csv
with open('1.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile,delimiter=';',quotechar = '"')
    answer = list(reader)[1:]
    ans = []
    for i in answer:
        if '55' in i[2]:
            print(f' У персонажа\t{i[1]} \t в игре\t{i[0]}\tнашлась ошибка с кодом:\t {i[2]}.\tДата фиксации:\t {i[3]}')
            i[2] = 'Done'
            i[3] = '0000-00-00'
with open('game_new.csv', 'w', newline = '', encoding="utf8") as file:
    w =csv.writer(file)
    w.writerow(['GameName','characters','nameError','date'])
    w.writerows(answer)
    
        
#    for GameName, characters, nameError, date in i.split(','):
#        print(GameName, characters, nameError, date)
