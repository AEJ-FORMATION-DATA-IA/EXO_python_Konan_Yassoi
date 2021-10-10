
A=input("veuiilez saisir une valeur :")
if(A.isnumeric()):
     B=input("veuillez saisir un entier:")
     if(B.isnumeric()):
         if(A>B):
             print("A est  est supérieur à B")
         elif (A<B): 
             print("A est inférieur à B")
         else: 
              print("A est egal à B")
     else:
            print("erreur vous n'avez pas saisi un entier") 
else:
    print("erreur vous avez pas saisi un entier")


  
