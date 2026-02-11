ukam={'ismi':'Muhammadjon','t-yili':2019,'yoshi':7}
print(f"mening ukam ismi {ukam['ismi']} , u {ukam['t-yili']}-yil tug'ilgan,\
hozirda yoshi {ukam['yoshi']}da ")
food={'otam':'qaynatma','bobom':'sho\'rva','momom':'osh','onam':'osh','singlim':'manti'}
print(f"otam yahshi ko'radigan taom {food['otam']}")
print(f"onam yahshi ko'radigan taom {food['onam']}")
print(f"bobom yahshi ko'radigan taom {food['bobom']}")
dictionary={
    'print':'natiajni chop etadi',
    'integer':'butun qiymat qabul qiladi',
    'float':'haqiqiy sonlar qabul qiladi',
    'string':'matnlar bilan ishlaydi',
    'for':'takrorlanish sikli',
    'range(x,y,z)':'x dan boshlab y gacha z qadam bilan sanash',
    'list':'biror ma\'lumotlar yig\'indidi to\'plam',
    'sum':'elementlar yig\'indisi',
    'max':'eng katta elementini topish to\'plamdan',
    'min':'eng kichkina qiymatdagi elementni topish to\'plamdan',
    }
print('istalgan so\'zni tarjimasi topamiz pythonga oid')
word=input('pythonga oid termin kiriting men tarjima qilaman:\n>>>>').lower()
if word in dictionary:
    print(f"{word} so'zining tarjimasi pythonda \n{dictionary[word]}")
else:
    print(f"{word} so'zi tarjimasi bizni lug'atda yuq")

