weight = int(input('What is the weight of your potato? '))
# line 1 inconsistent with paper because i was writing in pen, it does the same thing just cleaner imo
grade = 'Large'

if weight < 100:
    grade = 'Small'
elif weight <= 200:
    grade = 'Medium'

print(f'This is a {grade} potato.')

blemish_counts = []

for i in range(5):
    potato = input('Enter blemishes for potato [number]: ')
    blemish_counts.append(int(potato))

print(f'Total: {sum(blemish_counts)} | Average: {sum(blemish_counts)/5}')

all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []

for p in all_potatoes:
    if p != 0: continue
    perfect_potatoes.append(p)

print(f'% perfect: {(len(perfect_potatoes)/len(all_potatoes))*100}%')
# line 26 inconsistent with paper because on the paper i forgot to *100, cuz u need the percentage.