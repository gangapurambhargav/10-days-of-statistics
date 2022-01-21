totalelements=int(input())
numeratorele=[int(ele) for ele in input().split()]
denomele=[int(ele) for ele in input().split()]

resnumerator=0

if len(numeratorele) == len(denomele):
    for i in range(totalelements):
        cal=numeratorele[i]*denomele[i]
        resnumerator+=cal
print(round(resnumerator/sum(denomele),1))
//weighted mean