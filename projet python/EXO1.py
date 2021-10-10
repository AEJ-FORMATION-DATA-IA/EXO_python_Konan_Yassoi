A=15
B=4
C=A+B
D=A*B
E=A**B
F=A/B
G=A//B
H=A%B


#******* LES DICTIONNAIRES *******
dico ={
      "A":15,
      "B":4,
      "C":19,
      "D":60,
      "E":50625,
      "F":3.75,
      "G":3,
      "H":3
      }
print(dico)

dico["I"]=154
print(dico)


del dico["I"]
print(dico)

for i in dico.items():
    print(i)
    
# ******** les tuples ***********

tpl=(15,4,60)
print(type(tpl))

#pour ajouter faudrait je convertisse mon tuple en list
l=list(tpl)
print(l)
l.append(3.75)# ajout de list

#ensuite ma list en tuple
tpl=tuple(l)
print(tpl)


# pour modifier en va convertir en list ensuite en tuple

l=list(tpl)
l[0]=16
print(l)

# convertir la valeur modidifer dans la list  en tuple
tpl=tuple(l)
print(tpl)

# Suprimer la valeur de B dans le Tuple

l=list(tpl)
del l[1]
print(l)
tpl=tuple(l)
print(tpl)


#****** LES LISTES **********
#creation d'une liste1 contenant les lettres de a,b,d
liste1=["A", "B","C","D"]

#creons une seconde liste2 contenant les valeurs de A,B,C,D
liste2=[15,4,19,60]

#creons une troisièeme contenant les listes 1 et 2

liste3=[liste1,liste2]
print(liste3)

# Ajout E et F  la liste 1
liste1.append("E") 
liste1.append("F") 
print(liste1)


#supprimer B dans la liste1
del liste1[1]
print(liste1)

#Remplacer la lette de A par G

liste1[0]="G"
print(liste1)
