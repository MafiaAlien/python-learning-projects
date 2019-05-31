# #excersice page 38
#
invitation = []
invitation.append('Beffet')
invitation.append('Newton')
invitation.append('Edison')
print(invitation)
print('Beffet cannot come for dinner')
del invitation[0]
print('So we invite LZH to our party')
invitation.insert(0,'LZH')
print(invitation)
print('However , we found a bigger table than before ,so we want to invite 3 more people to our dinner')
invitation.insert(0,'WY')
invitation.insert(2,'NK')
invitation.insert(5,'James')
print('We invite WY,NK,and James to our party')
print(invitation)
print('unfortunately, the table cannot be delivered on time ,so we have to decrease our invitation to two customers ')
canceled_customers = invitation.pop()
print('Dear ' + canceled_customers.title()+', sorry to notice you that balblablablab')
canceled_customers = invitation.pop()
print('Dear ' + canceled_customers.title()+', sorry to notice you that balblablablab')
canceled_customers = invitation.pop()
print('Dear ' + canceled_customers.title()+', sorry to notice you that balblablablab')
canceled_customers = invitation.pop()
print('Dear ' + canceled_customers.title()+', sorry to notice you that balblablablab')

print(invitation)
print(len(invitation))

#excercise page 41
# places = ['Roma','Turkey','Japan','Israel','Egypt']
# print(places)
# print(sorted(places))
# places.reverse()
# print(places)