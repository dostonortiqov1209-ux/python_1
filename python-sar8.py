try :
#      son=float(input('juf son kiriting:\n>>>>'))
#      if son%2==0:
#          print('ajoyib, rahmat')
#      else:
#          print('iltimos juf son kiriting')
# 
# 
#      yosh=int(input('yoshingiz nechida?\n>>>> '))
#      if yosh<=4:
#          narx=0
#      elif yosh<=18:
#          narx=5000
#      else:
#          narx=10000
#      print(f"siz uchun kirish bilet narxi {narx} so'm bo'ladi")
#     son1=int(input('1-sonni kiriting:\n>>>>'))
#     son2=int(input('2-sonni kiriting:\n>>>>'))
#     if son1<son2:
#         print('ikkinchi son katta')
#     elif son1>son2:
#         print('birinchi son katta')
#     else:
#         print('ikki son teng')
    # mahsulotlar=['choy','olma','anor','un','sovun','cola']
    # n=int(input('nechta mahsulot olishingiz kerak:\n>>>>'))
    # savat=[]
    # yuq=[]
    # for i in range(n):
    #     savat.append(input(f"{i+1}-mahsulotni tanlang:\n>>>>").lower())
    # if savat:
    #         for narsa in savat:
    #             if narsa in mahsulotlar :
    #                 print(f"do'konda siz tanlagan {narsa} mahsulotingiz mavjud")                                        
    #             else:
    #                 yuq.append(narsa)
    # else:
    #     print('siz mahsulot tanlamadingiz')
    # if yuq:
    #     print("bizning do'konda ushbu mahsulotlar yo'q:\n",yuq)
    # foydalanuvchilar=['asad','diyor','diyorbek','ilyor','abror','ahror','kamol']
    # login=input('loginingizni kiriting:\n>>>>').lower()
    # if login in foydalanuvchilar:
    #     print('iltimos boshqa loginni tanlang')
    # else:
    #     print(f"xush kelibsiz hurmatli {login}")
    # son=int(input('ixtiyoriy butun son kiriting biz siz uchun 1 dan 10 gacha bo\'luvchilarni chiqaramiz\n>>>>'))
    # for n in range(1,11):
    #     if son%n==0:
    #         print(f"siz tanlagan {son} soni {n} ga qoldiqsz bo'linadi natijasi:\n>>>>{int(son/n)}")       
    danger_zone=[]
    logs = ["LOGIN_SUCCESS:user1", "ERROR:db_fail", "LOGIN_FAILED:admin", "ATTACK:sql_inj", "LOGIN_FAILED:user2", "INFO:update"]
    for virus in logs:
        if 'LOGIN_FAILED' in virus or 'ATTACK' in virus:
            danger_zone.append(virus)
    print('bu xavf sabablari:')
    for zarar in danger_zone:
        sabab=zarar.split(':')[1].lower()
        print(sabab)
        if sabab=='sql_inj':
            print('>>>> bu kritik xavf 100%')
        elif sabab=='admin':
            print('>>>> bu yuqori xavfli 80%')
        else:
            print('>>>> bu o\'rtacha xavf 50%')
except IndexError:
    print('bu o\'rtacha xavf 50%')
except ValueError:
    print('iltimos faqat raqamlar bilan javob bering')
