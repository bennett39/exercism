def tally(rows):
    table = {}
    for row in rows:
        data = row.split(';')
        for i in range(2):
            table.setdefault(data[i], {'win': 0, 'loss': 0, 'draw': 0, 'total': 0})
        table[data[0]]['total'] += 1
        table[data[1]]['total'] += 1
        if data[2] == 'win':
            table[data[0]]['win'] += 1
            table[data[1]]['loss'] += 1
        elif data[2] == 'loss':
            table[data[0]]['loss'] += 1
            table[data[1]]['win'] += 1
        elif data[2] == 'draw':
            table[data[0]]['draw'] += 1
            table[data[1]]['draw'] += 1
    header = ['Team                           | MP |  W |  D |  L |  P']
    output = []
    for team, data in table.items():
        points = data['win'] * 3 + data['draw']
        output.append(f"{team}\t\t|{data['total']}|{data['win']}|{data['loss']}|{points}")
    return header + output
