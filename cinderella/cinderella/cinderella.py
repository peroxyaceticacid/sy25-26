seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

amount_of_upsets = 0

for n in seeds:
    if n < 10:
        continue

    amount_of_upsets += 1
    print(f'Cinderella alert! {winners[n-1]} pulls the upset!')

print(f'\nUpsets: {amount_of_upsets}.')