import random 
crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze']
ll = []
for i in range(1,4):
    jj = random.choice(crew_leaders)
    ll.append(jj)
    crew_leaders.remove(jj)
    print('winner N',i,'is',jj)
    if jj in crew_leaders:
        print(random.choice(crew_leaders - ll))