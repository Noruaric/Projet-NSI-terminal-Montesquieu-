from random import *
'''initialisation'''
toutes_les_notes=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
tonique_chiffre=randint(0,11)
tonique=toutes_les_notes[tonique_chiffre]
gamme_liste=[[2,2,1,2,2,2,1],[2,1,2,2,1,2,2]]
gamme_liste_deux=[[2,4,5,7,9,11,12],[2,3,5,7,8,10,12]]
gamme_rand=randint(0,1)
gamme_chiffre=gamme_liste[gamme_rand]
gamme=[tonique]
if gamme_rand==0:
    maj_min='majeure'
else:
    maj_min='mineure'
for i in range(6):
    j=gamme_liste_deux[gamme_rand][i]+tonique_chiffre
    gamme.append(toutes_les_notes[j])
bpm=randint(75,140)
'''creation de l'intro'''

'''création clé de sol'''
temps_tourne_intro_rand_sol=[4,8]
compteur=temps_tourne_intro=choice(temps_tourne_intro_rand_sol)
couleurs_possibles_intro_sol=[1,0.5,0.25]
notes_intro_couleur_sol=[]
while compteur>=1:
    temp=choice(couleurs_possibles_intro_sol)
    notes_intro_couleur_sol.append(temp)
    compteur-=temp
if compteur != 0:
    if compteur != 0.75:
        notes_intro_couleur_sol.append(compteur)
    else:
        temp = randint(1,3)
        if temp == 1:
            notes_intro_couleur_sol.append(0.5)
            notes_intro_couleur_sol.append(0.25)
        elif temp == 2:
            notes_intro_couleur_sol.append(0.25)
            notes_intro_couleur_sol.append(0.5)
        else:
            notes_intro_couleur_sol.append(0.25)
            notes_intro_couleur_sol.append(0.25)
            notes_intro_couleur_sol.append(0.25)
notes_intro_sol=[]
for i in range (len(notes_intro_couleur_sol)):
    notes_intro_sol.append(choice(gamme))

tourne_intro_sol=[]
for i in range (len(notes_intro_couleur_sol)):
    tourne_intro_sol.append((notes_intro_sol[i],notes_intro_couleur_sol[i]))

'''création clé de fa'''
compteur=4
couleurs_possibles_intro_fa=[2,1.5,1,0.5,0.25]
notes_intro_couleur_fa=[]
while compteur>=2:
    temp=choice(couleurs_possibles_intro_fa)
    notes_intro_couleur_fa.append(temp)
    compteur-=temp
couleurs_possibles_intro_fa2=[1,0.5,0.25]
while compteur>=1:
    temp=choice(couleurs_possibles_intro_fa2)
    notes_intro_couleur_fa.append(temp)
    compteur-=temp
if compteur != 0:
    if compteur != 0.75:
        notes_intro_couleur_fa.append(compteur)
    else:
        temp = randint(1,3)
        if temp == 1:
            notes_intro_couleur_fa.append(0.5)
            notes_intro_couleur_fa.append(0.25)
        elif temp == 2:
            notes_intro_couleur_fa.append(0.25)
            notes_intro_couleur_fa.append(0.5)
        else:
            notes_intro_couleur_fa.append(0.25)
            notes_intro_couleur_fa.append(0.25)
            notes_intro_couleur_fa.append(0.25)
notes_intro_fa=[]
for i in range (len(notes_intro_couleur_fa)):
    notes_intro_fa.append(choice(gamme))

tourne_intro_fa=[]
for i in range (len(notes_intro_couleur_fa)):
    tourne_intro_fa.append((notes_intro_fa[i],notes_intro_couleur_fa[i]))

print(maj_min,'tonique = ',tonique,'gamme =',gamme, 'bpm = ',bpm,'tourne intro sol = ', tourne_intro_sol,'tourne intro fa = ', tourne_intro_fa)
