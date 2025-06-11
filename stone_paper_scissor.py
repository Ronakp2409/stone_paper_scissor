import random

user = int (input("0 for stone,1 for paper and 2 for scissor: "))
comp = random.randint(0,2)
def check(comp,user):
  
  if (comp== user):
    return 0
  if ((comp ==0 and user ==1) or (comp==1 and user ==2) or (comp ==2 and user ==1)):
    return -1

  return 1

score = check(comp,user)
print ("you: ",user)
print("computer: ",comp)

if(score == 0):
  print("its a draw")
elif (score == -1):
  print("you lose")
else:
  print("you win")
 



