#a=int(input("1-sonni kiriting: "))
#b=int(input("2-sonni kiriting: "))
#if a==b:
#	print(f"{a}={b}")
#if a>b:
#	print(f"{a}>{b}")
#else:
#	print(f"{a}<{b}")
#mahsulotlar=["olma", "tuxum", "sabzi", "sut", "kolbasa", "guruch", "yog'", "non", "piyoz", "tarvuz", "uzum"]
#savat=[]
#for n in range(5):
#	savat.append(input(f"{n+1}-mahsulotni kiriting: "))
#for mahsulot in savat:
#	if mahsulot in mahsulotlar:
#		print(f"dokonda {mahsulot} mahsuloti bor")
#	else:
#	#	print(f"dokonda {mahsulot} mahsuloti yoq")
#mahsulotlar=["olma", "tuxum", "sabzi", "sut", "kolbasa", "guruch", "yog'", "non", "piyoz", "tarvuz", "uzum"]
#savat=[]
#for n in range(5):
#	savat.append(input(f"{n+1}-mahsulotni kiriting: "))	
#bor_mahsulotlar=[]
#mavjud_emas=[]
#for mahsulot in savat:
#	if mahsulot in mahsulotlar:
#		bor_mahsulotlar.append(mahsulot)
#	else:
#		mavjud_emas.append(mahsulot)
#print(bor_mahsulotlar)
#print("siz so'ragan mahsulotlar do'konimizda bor")
#print(mavjud_emas)		
#print("quyidagi mahsulotlar do'konimizda yo'q")
#foydalanuvchi=["maqsud", "jayrona", "husan", "bekzod", "asliddin"]
#user=[]
#for n in range(6):
#	user.append(input(f"{n+1}-loginni kiriting: "))
#for login0 in user:
#	if login0 in foydalanuvchi:
#		print(f"{login0} logini band boshqa kiriting")
#	else:
#		print(f"xush kelibsiz {login0}")
#foydalanuvchilar=["maqsud", "jayrona", "husan", "bekzod", "asliddin"]
#user=input("yangi login tanlang: ")
#if user in foydalanuvchilar:
#print(f"{user} logini band, boshqa login tanlang")
#else:
#	print(f"xush kelibsiz {user} logini foydalanuvhchisi")
#butun_son=int(input("istalgan butun sonni kiriting"))
#n_j1=[]
#n_j2=[]
#for n in range(2,11):
#	if butun_son%n==0:
#		n_j1.append(n)
#	else:
#		n_j2.append(n)
#print(f"ushbu son {n_j1} sonlariga qoldiqsiz bo'linadi")
#print(f"ushbu son {n_j2} sonlariga qoldiqsiz bo'linmaydi")
#talaba={}
#talaba["ism"]="teshaboyev abdug'ani"
#talaba["kurs"]=3
#talaba["yosh"]=24
#print(talaba)
#print(f"Talaba {talaba["ism"].title()} {talaba["kurs"]}-kurs ")
#talaba={"ism":"teshaboyev abdug'ani", "kurs":3, "yosh":24, "t_yil":2002}
#print(talaba)
#del talaba["yosh"]	
#print(talaba)
#dustlar={
#	"Bekmurod":"samlung A20",
#	"Jasur":"honor x5",
#	"Maruf":"Iphone"   
#	}
#print(dustlar["Bekmurod"])
#phone=dustlar["Bekmurod"]
#print(f"Bekmurodni telefoni {phone}")
#print(dustlar.get("Sherzod", "bunday ism mavjud emas"))
#dada={"ism": "shirinov shahobiddin teshayevich", "yosh":51, "kasb":"jismoniy tarbiya o'qituvchisi", "qiziqishlari":"hunarmandlik"}
#print(f"Dadamning ismi {dada["ism"].title()} uning yoshi {dada["yosh"]} da, u {dada["kasb"]} bo'lib ishlaydi, u {dada["qiziqishlari"]}ga qiziqadi ") 
#print("salom dunyo")
#oila={"dada":"osh", "ona":"somsa", "opa":"shashlik", "aka":"manti", "uka":"lag'mon"}
#for k, q in oila.items():
#	print(f"{k}ning sevimli taomi {q}")
#lugatpython={"print":"yoz", "if":"agar", "else":"aks holda", "append":"qo'sh", "del":"o'chir", "title":"bosh harf", "lower":"kichik harf", "for":"uchun", "in":"ichida", "not":"uchun"}
#print(lugatpython)
#lugatpython={"print":"yoz", "if":"agar", "else":"aks holda", "append":"qo'sh", "del":"o'chir", "title":"bosh harf", "lower":"kichik harf", "for":"uchun", "in":"ichida", "not":"uchun"}
#kalit=input("biron kalit so'z ayting: ")
#if kalit in lugatpython:
#	print(lugatpython[kalit])
#else:
#	print(lugatpython.get(kalit, "bunday kalit mavjud emas"))
#lugatpython={"print":"yoz", "if":"agar", "else":"aks holda", "append":"qo'sh", "del":"o'chir", "title":"bosh harf", "lower":"kichik harf", "for":"uchun", "in":"ichida", "not":"emas"}
#print(lugatpython.items())
#for kalit, qiymat in lugatpython.items():
#	print(f"Kalit: {kalit}")
#	print(f"Qiymat: {qiymat}")
#talaba={"ism_f":"Teshaboyev Abdugani", "yosh":"24", "tugilgan_y":"2002", "kasb":"bojxonachi",}
#print(talaba.items())
#for kalit, qiymat in talaba.items():
#	print(f"Kalit: {kalit}")
#	print(f"Qiymat: {qiymat}")
#dustlar={"sherzod":"samsung A22", "jasur":"honor x4", "o'kir":"iphone 16", "maruf":"iphone 15"}
#for k, q in dustlar.items():
	#print(f"{k.title()}nig telefoni {q}")
	#	print(mahsulot)
#mevalar={"olma":18_000, "anor":25_000, "banan":35_000, "uzum":50_000}
#bozorlik=["olma", "anor", "banan", "uzum", "anjir"]
#print(mevalar.keys())
#for mahsulot in mevalar:
#	if mahsulot in bozorlik:
#		print(f"{mahsulot} narxi {mevalar[mahsulot]}")
#for mahsulot in bozorlik:
#	if mahsulot not in mevalar:
#		print(f"iltimos shu {mahsulot} mevasidan ham olib keling.")
#print("do'konimizdagi mahsulotlar")
#for mahsulot in sorted(mevalar):
	#print(mahsulot.title())
#print(dustlar.values())
#print("Foydalanuvchilar quyidagi telefonlarni ishlatadi")
#dustlar={"sherzod":"samsung A22", "jasur":"iphone 16", "o'kir":"iphone 16", "maruf":"iphone 16"}
#for tel in dustlar.values():
#	print(tel)
#print(dustlar.values())
#print("Foydalanuvchilar quyidagi telefonlarni ishlatadi")
#dustlar={"sherzod":"samsung A22", "jasur":"iphone 16", "o'kir":"iphone 16", "maruf":"iphone 16"}
#for tel in set(dustlar.values()):
#	print(tel)
#lugatpython={"print":"yoz", "if":"agar", "else":"aks holda", "append":"qo'sh", "del":"o'chir", "title":"bosh harf", "lower":"kichik harf", "for":"uchun", "in":"ichida", "not":"emas"}
#for k in sorted(lugatpython.keys()):
#	print(f"{k}")
#for q in sorted(lugatpython.values()):
#	print(f"{q}") 
#print(sorted(davlatp.items()))
#davlatp={"amerika":"vashington", "rossiya":"makva", "o'zbekiston":"toshkent", "afg'oniston":"kobul"}
#for k, q in sorted(davlatp.items()):
#	print(f"{k.title()}:{q.title()}")
#vapros=input("istalgan davlatni kiriting: ").lower()
#davlatp={"amerika":"vashington", "rossiya":"makva", "o'zbekiston":"toshkent", "afg'oniston":"kobul"}
#	if vapros==davlatp.keys():
#		print(davlatp[davlat])
#	else:
#		print("Bizda bunday davlat yo'q")
#restoran={"shashlik":10000, "dimlama":50000, "osh":30000, "manti":10000, "chuponcha":120000}
#zakazlar=[]
#for n in range(3):
#	zakaz=input(f"{n+1}-buyurtmani bering: ")
#	zakazlar.append(zakaz)
#	if zakaz.lower() in restoran.keys():
#		print(restoran[zakaz.lower()])
#	else:
#		print("bizda bunday taom yo'q")
#	print(zakazlar)
#car0={"model":"jip", "rang":"qora", "yil":"2025", "narxi":"5000 $"}
#car1={"model":"nexia", "rang":"oq", "yil":"2020", "narxi":"2000 $"}
#car2={"model":"tahoe", "rang":"kuk", "yil":"2022", "narxi":"62000 $"}
#cars=[car0, car1, car2]
#for car in cars:
	#print(f"{car["model"].title()}, "
	#	f"{car["rang"]} rang, "
	#	f"{car["narxi"]}")
#print(cars[0])
#print(cars[0]["model"])
#print(f"{cars[2]["rang"].title()}" 
#	f" {cars[2]["model"]}")
#malibus=[]
#for n in range(10):
#	new_car={
#	"model":"malibu", 
#	"rang":None, 
#	"narxi":None, 
#	"karobka":"avto"
#	}
#	malibus.append(new_car)
#for malibu in malibus[:3]:
#	malibu["rang"]="qora"
#for malibu in malibus[3:6]:
#	malibu["rang"]="qora"
#for malibu in malibus:
#	if malibu["karobka"]=="avto":
#		malibu["narxi"]=40000
#	else:
#		malibu["narxi"]=35000
#for malibu in malibus:
#		print(malibu)
#malibus = []

# 1. Yaratish
#for n in range(10):
    #new_car = {
      #  "model": "malibu",
     #   "rang": None,
    #    "narxi": None,
   #     "karobka": "avto"
  #  }
  #  malibus.append(new_car)

# 2. Rang berish
#for malibu in malibus[:3]:
 #   malibu["rang"] = "qora"

#for malibu in malibus[3:6]:
 #  malibu["rang"] = "oq"

# 3. Narx berish
#for malibu in malibus:
   # if malibu["karobka"] == "avto":
  #      malibu["narxi"] = 40000
 #   else:
#        malibu["narxi"] = 35000

# 4. Chiqarish
#for malibu in malibus:
#    print(malibu)
"""dasturchilar={"abdugani":["python", "c++"], "jasur":["java script", "c#", "css"], "bekmurod":["html", "php"]}
   for dasturchi, tillar in dasturchilar.items():
      print(f"\n{dasturchi.title()} quyidagi dasturlash tillarini biladi: ", end="" )
      for til in tillar:
         print(f"{til.upper()} ", end="")
   """   """
         hamkasblar={"ali":{"familya":"valiyev", "yosh":"24", "malumoti":"oliy", "dasturlar":["css","php", "js"]},
         "azim":{"familya":"choriyev", "yosh":30, "malumoti":"o'rta", "dasturlar":["python", "c++", "java", "c#"]},
         "alisher":{"familya":"ashurov", "yosh":"45", "malumoti":"oliy", "dasturlar":["javscript", "css"]}}
         for ism, info in hamkasblar.items():
            print(f"\n{ism.title()} {info["familya"].title()}, "
               f"{info["yosh"]} yoshda. " 
               f"malumoti: {info["malumoti"]}. \n"
               "quyidagi dasturlash tillarini biladi: ", end="")
            for dastur in info["dasturlar"]:
               print(f"{dastur.upper()} ", end="")""" 
"""print("sonning kvadratini hisoblovchi dastur")
savol='istalgan sonni kiriting'
savol +='dasturni tuxtatish uchun exit ni yozing'
qiymat=' '
while qiymat!='exit':
   qiymat=input(savol)
   if qiymat!='exit':
      print(float(qiymat)**2)"""
"""qiymat=' '
while qiymat!='0':
   qiymat=input('istalgan sonni kiriting: ')
   if qiymat!='0':
      print(float(qiymat)**3)
""""""
son=' '
while son!='0':
   son=input("sonni juft yoki toq ekanligini aniqla: ")
   if float(son)%2==0:
      print('juf')
   else:
      print("toq")
"""
"""son=' '
while son!='tuxta':
   son=input('sonni ishorasini aniqla: ')
   if son=='tuxta':
      break

   son=float(son)
   if son>0:
      print('musbat')
   elif son==0:
      print('musbat ham manfiy ham emas')
   else:
      print('manfiy')
"""
"""print('istalgan ikkita son kiriting')
while True:
   a=input('1-sonni kiriting: ')
   if a=='tuxta':
      break
   b=input('2-sonni kiriting: ')
   a=float(a)
   b=float(b)
   print(f'yigindi: {a+b}')
"""
"""print("3 ta sonnni qiymatini taqqoslash")
while True:
   a=input('birinchi sonni kiriting: ')
   if a=='tuxta':
      break
   b=input('ikkinchi sonni kiriting: ')
   c=input('uchinchi sonni kiriting: ')
   a=float(a)
   b=float(b)
   c=float(c)
   print('eng katta son:', max(a,b,c))   
"""
"""
print('istalgan sonni kv ildizini hisoblovchi dastur'
)
while True:
   son=input('istalgan sonni kiriting')
   if son=='exit':
      break
   elif float(son)<0:
      print('manfiy sonni kv ildizini hisoblab bolmaydi')
   else:
      ildiz=float(son)**0.5
      print(ildiz)"""
"""ismlar=[]
print('yaqin dustlaringiz ruyhatini tuzamiz')
n=1
while True:
   savol=f'{n}-dustingizni ismini kiriting: '
   ism=input(savol)
   ismlar.append(ism)
   javob=input('Yana ism qushasizmi? (ha/yuq)')
   if javob=='ha':
      n+=1
      continue
   else:
      break
print('dustlaringiz ruyhati: ')
for ism in ismlar:
   print(ism.title())
"""
"""print('Dustlaringizni yoshini saqlaymiz')
dustlar={}
ishora=True
while ishora:
   ism=input('dustingizni ismini kiriting: ')
   yosh=input(f'{ism.title()}ning yoshini kiriting: ')
   dustlar[ism]=int(yosh)
   javob=input('Yana malumot qushasizmi? (ha/yuq)')
   if javob=='yuq':
      ishora=False
print(dustlar.values())"""
"""print(dustlar.items())"""
"""for ism, yosh in dustlar.items():
   print(f'{ism.title()} {yosh} yoshda')"""
"""cars=['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars:
   cars.remove('nexia')
"""
"""print(cars)
"""
"""
cars.append('nexia')
print(cars)
"""
"""print('Yaqin dustlaringizni ruyhatini tuzamiz')
ismlar=[]
n=1
while True:
   savol=f'{n}-dustingizni ismini kiriting: '
   ism=input(savol)
   ismlar.append(ism)
   javob=input('Yana ism qushasizmi? (ha/yuq)')
   if javob=='ha':
      n+=1
      continue
   else: 
      break
   ismlar.sort()
print(ismlar)
   """
"""print('kitob nomlarimi kiritish')
kitoblar=[]

while True:
   nom=input('kitob nomini kiriting: ')
   if len(nom)<3:
      continue
   kitoblar.append(nom)
   if len(kitoblar)==5:
      break
print(kitoblar)
"""
"""print('musbat sonlarni urtachaqiymatini aniqlash')
musbat_sonlar=[]
while True:
   son=float(input('son kiriting: '))
   if float(son)>0:
      musbat_sonlar.append(son)
   else:
      break
jam=sum(musbat_sonlar)
dona=len(musbat_sonlar)
urta_son=float(jam)/float(dona)
print(urta_son)
"""                             
"""print('xaridingizni kiriting: ')
mahsulotlar={}
while True:         
   mahsulot=input("xarid qilgan mahsulotni kiriting ")
   if mahsulot=='0':
      break
   narx_mahsulot=float(input(f"{mahsulot}ning narxini kiriting: "))
   mahsulotlar[mahsulot]=narx_mahsulot
print(mahsulotlar.items())
jam_sum=sum(mahsulotlar.values())
print(f'jami mahsulot narxi: {jam_sum}')
"""
"""
mahsulotlar=[]
print('Mahsulot nomini kiriting: ')
while True:
   mahsulot=input('mahsulot buyuring: ')
   mahsulotlar.append(mahsulot)
   if mahsulot=="tuxta":
      break
print(f'Quyidagi mahsulotlar: \n{mahsulotlar} \nMahsulotlar soni: {len(mahsulotlar)} dona')"""
"""print('Mahsulotlar va ularning narxlari')
mahsulotlar={}
while True:
   mahsulot=input('mahsulot nomini kiriting: ')
   if mahsulot=='stop':
      break
   narx=float(input('mahsulot narxini kiriting: '))
   mahsulotlar[mahsulot]=narx
mahsulotlar1=[]
mahsulotlar1=list(mahsulotlar.keys())
narxlar=sum(mahsulotlar.values())
print(mahsulotlar1)
print(narxlar)
mahsulotlar_a=[]
for tovar in mahsulotlar1:
   if 'a' in tovar:
      mahsulotlar_a.append(tovar)
print(mahsulotlar_a)
for tovar in set(mahsulotlar1):
   print(f'{tovar} mahsuloti soni {mahsulotlar1.count(tovar)}')"""
"""print("Kassa")
jami=0
menyu={'osh':30000, 'manti':10000, 'qiyma shashlik':35000, 'kuskavoy shashlik':25000, 'chuponcha':180000}
while True:
   for taom, narx in menyu.items():
      narx=menyu[taom]
      taom=input('Buyurtma qilingan taom: ').lower()
      miqdor=float(input(f'{taom}ni miqdorini kiriting(1 kg/dona): '))
   if taom=='x':
      break
print(f'\n{taom}: \nsoni: {miqdor} \n(1 kg/dona) narxi: {narx} \njami summa(sum): {miqdor*narx} ')"""
"""menyu={'osh':30000, 
'manti':10000, 
'qiyma shashlik':35000, 
'kuskavoy shashlik':25000, 
'chuponcha':180000}
jami=0
while True:
   taom=input("Buyurtmani kiriting(1 kg/dona): ")
   if taom=='x':
      break
   if taom not in menyu:
      print("Bizda bunday taom yo'q")
      continue
   miqdor=float(input(f"{taom} miqdorini kiriting(kg/dona): "))
   narx=menyu[taom]
   summa=miqdor*narx
   jami+=summa
   print(f"{taom}: {miqdor} x {miqdor}={summa} so'm")
print(f"\njami summa: {jami} so'm")"""
menyu={'osh':30000, 
'manti':10000, 
'qiyma shashlik':35000, 
'kuskavoy shashlik':25000, 
'chuponcha':180000}
#jami=0
jami_s=[]
while True:
   taom=input("Buyurtmani kiriting(1 kg/dona): ")
   if taom=='x':
      break
   if taom not in menyu:
      print("Bizda bunday taom yo'q")
      continue
   miqdor=float(input(f"{taom} miqdorini kiriting(kg/dona): "))
   narx=menyu[taom]
   summa=miqdor*narx
   jami_s.append(summa)
   #jami+=summa
   print(f"{taom}: {miqdor} x {miqdor}={summa} so'm")
print(f"\njami summa: {sum(jami_s)} so'm")








