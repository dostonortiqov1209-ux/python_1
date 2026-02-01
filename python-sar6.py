ismlar=['sardor', 'akbar', 'jamol']
print(f"{ismlar[0]} futbol borasanmi? {ismlar[1]} va  {ismlar[2]} bormoqda ular ham futbolga ")
sonlar=[1,-2,3.4,23,-4,-15,4.5,12.6]
sonlar.append(18)
sonlar.insert(2,15)
del sonlar[1]
raqam=sonlar.pop(4)
sonlar.remove(12.6)
t_shaxslar=['Amir Temur','Mirzo Ulug\'bek', 'jorj vashington', 'Beruniy']
z_shaxslar=['elon musk', 'Jahongir ortixo\'jayev', 'bill geyts']
t_1=t_shaxslar.pop(0)
t_2=t_shaxslar.pop(2)
matn='men buyuk siymolarimiz '+t_1+' va '+t_2+' larni bilaman, hozirgi zamon buyuklari esa '+z_shaxslar.pop(0)+' va '+z_shaxslar.pop(1)+' hisoblanishadi'
print(matn)
friends=[]
friends.append('sardor')
friends.append('asad')
friends.append('sanjar')
friends.append('samandar')
friends.append('akmal')
friends.insert(0, 'odil')
friends.insert(3,'akbar')
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(2))
print(f"bazmga do'stlarim {friends}  mehmonga kemadi bular mehmonga {mehmonlar} keldi ularga tashakkur")