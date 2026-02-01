ismlar=['Sardor','Asad', 'Abror', 'Ilhom', 'Jalol']
for ism in ismlar:
    print(f"qalaysan {ism}, do\'stim!!!")
print('ro\'yhat takrorlanishlar soni:', len(ismlar),'ta')

for son in list(range(11,100,2)):
    print(f"{son}ning kubi, teng:{son**3}")
print('sen yahshi ko\'rgan kinolar ro\'yhati:')
kinolar=[]
for n in range(5):
     kinolar.append(input(f"{n+1}-yahshi ko'rgan kinongiz=>").title())
print('siz yahshhi ko\'rgan kinolar jamlandi=>',kinolar)
xonadoshlar=[]
m=int(input('sening nechta xonadoshing bor?\n>>>>'))
print('xonada kimlar bilan turasan ismlari:')
for i in range(m):
    xonadoshlar.append(input(f"{i+1}-xonadoshing ismi:\n >>>>").title())
print(xonadoshlar)