import random
import art
import word
print(art.logo)
pos = random.randint(0,212)
chosen_word=word.word_list[pos]
blank_list=[]
a=0
index2=6
for letter in chosen_word :
    blank_list.append("_")
while index2>=0 and a==0:
    a=1
    const=0
    guess=input("Which letter do you choose\n").lower()
    index=0
    for letter in chosen_word :
        if letter==guess :
            blank_list[index]=letter
            const=1
        index+=1
    if const==0 :
        print(art.stages[index2])
        index2-=1
    print(blank_list)
    for letter in blank_list :
        if letter=="_" :
            a=0
    if index2<0:
        a=1
    if a==1:
        index2=-1
if index2<0:
    print("You lost")
    print(f"The word was {chosen_word}")
else:
    print("You won")