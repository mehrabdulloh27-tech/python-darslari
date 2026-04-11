"""print("hello")
mashhurlar={"mohirdev":{"ism":"anvar", "familya":"narzullayev", "kasbi":"dasturchi", "ijod namunalari":["python darslari", "java darslari"], "qiziqishlari":["yengil atletika", "suzish", "stol tenisi"]},
	"jaloliddin":{"ism":"jaloliddin", "familya":"ahmadaliyev", "kasbi":"qo'shiqchilik", "ijod namunalari":["sevgi", "ko'zmunchog'im"], "qiziqishlari":["sayohat", "shaxmat"]},
	"muhammadali":{"ism":"muhammadali", "familya":"eshonqulov", "kasbi":"moliyachi", "ijod namunalari":[""] "qiziqishlari":["kitob o'qish", "kamondan o'q uzish"]}
	}
for kalit, info in mashhurlar.items():
	print(f"{kalit.title()}: ismi {info['ism']} familyasi {info['familya']}, " 
		f"kasbi {info['kasbi']}, " 
		"quyidagi qiziqishlari bor: ")
	for qiziqish in info["qiziqishlari"]:
		print(qiziqish)"""
"""films_oshna=[]
films_dada=[]
films_opa=[]
for n in range(3):
		opa=input("3 ta sevimli filimingizni ayting: ")
		films_opa.append(opa)
		oshna=input("3 ta sevimli filmingizni ayting: ")
		films_oshna.append(oshna)
		dada=input("3 ta sevimli filimingizni ayting: ")
		films_dada.append(dada)
films_oila={"opa":films_opa, "oshna":films_oshna, "dada":films_dada}
print(films_oila)"""
"""davlatlar={
	"amerika":["dunyo iqtisodiyotida yetakchi", "dunyo top mamalakatlari amerikada", "dollarning vatani"],
	"xitoy":["aholisi soni bo'yicha dunyoda 2 chi o'rinda", "iqtisodiyoti amerikadan keyin rivojlanayotgan davlat"],
	"rossiya":["dunyodagi eng katta ega davlat", "oyga birinchi bo'lib raketa qo;ndira olgan davlat"]
	}
	for davlat, info in davlatlar.items():
	print(f"{davlat} -{info}")
	for i in info:
					print(f"{davlat}-{i}")
	print(f"n\n{davlat.title()}")
	for i in info:
		print(f"- {i}")"""
"""savol=input("biron davlat haqida so'rang: ")
davlatlar={
	"amerika":["dunyo iqtisodiyotida yetakchi", "dunyo top mamalakatlari amerikada", "dollarning vatani"],
	"xitoy":["aholisi soni bo'yicha dunyoda 2 chi o'rinda", "iqtisodiyoti amerikadan keyin rivojlanayotgan davlat"],
	"rossiya":["dunyodagi eng katta ega davlat", "oyga birinchi bo'lib raketa qo;ndira olgan davlat"]
	}
for davlat, info in davlatlar.items():
	if savol==davlat:
		print(f"\n{davlat.title()}")
		for i in info:
			print(f"-{i}")
	elif savol!=davlat:
		print("bizda bunday davlat haqida malumot yo'q")"""
"""savol=input("biron davlat haqida so'rang: ")
davlatlar={
	"amerika":["dunyo iqtisodiyotida yetakchi", "dunyo top mamalakatlari amerikada", "dollarning vatani"],
	"xitoy":["aholisi soni bo'yicha dunyoda 2 chi o'rinda", "iqtisodiyoti amerikadan keyin rivojlanayotgan davlat"],
	"rossiya":["dunyodagi eng katta ega davlat", "oyga birinchi bo'lib raketa qo;ndira olgan davlat"]
	}
if savol in davlatlar.keys():
	print(f"\n{savol.title()}")
	print(davlatlar[savol])
else:
	print("bizda bunday davlat haqida malumot yo'q")
"""
"""savol=input("biron davlat haqida so'rang: ").lower()
davlatlar={
	"amerika":["dunyo iqtisodiyotida yetakchi", "dunyo top mamalakatlari amerikada", "dollarning vatani"],
	"xitoy":["aholisi soni bo'yicha dunyoda 2 chi o'rinda", "iqtisodiyoti amerikadan keyin rivojlanayotgan davlat"],
	"rossiya":["dunyodagi eng katta ega davlat", "oyga birinchi bo'lib raketa qo;ndira olgan davlat"]
	}
if savol in davlatlar:
	print(f"\n{savol.title()}")
	for info in davlatlar[savol]:
		print(f"- {info}")
else:
	print("bizda bunday davlat haqida malumot yo'q")"""
"""navoiy={"ism":"Alisher NAvoiy", "t_yil":1441, "t_joy":"Hirot", "v_yil":1501}
	erkin={"ism":"Erkin Vohidov", "t_yil":1960, "t_joy":"Toshkent", "v_yil":2005}
	qodiriy={"ism":"Abdulla Qodiriy", "t_yil":1936, "t_joy":"Toshkent", "v_yil":1960}
	shaxslar=[navoiy, erkin, qodiriy]
	for shaxs in shaxslar:
	"""	#print(f"""{shaxs["ism"]} {shaxs["t_yil"]}-yil {shaxs["t_joy"]}da tug'ilgan, {shaxs["v_yil"]-shaxs["t_yil"]} yil umr ko'rgan""")
"""enshteyn={"ism":"Albert Enshteyn", "yunalish":"ilm fan", 't_yil':1879, 't_joy':'Germaniya'}
nyuton={'ism':'Isak Nyuton', 'yunalish':'ilm fan', 't_yil':1643, 't_joy':'Angliya'}
tesla={'ism':'Nikola Tesla', 'yunalish':'ilm fan', 't_yil':1856, 't_joy':'Serbiya'}
davinchi={'ism':'Leanardo davinchi', 'yunalish':'san\'at', 't_yil':1452, 't_joy':'Italiya'}
shaxslar=[enshteyn, nyuton, tesla, davinchi]
for shaxs in shaxslar:
	print(f" {shaxs['ism']} {shaxs['t_yil']}-yil {shaxs['t_joy']}da tug\'ilgan, \n" 
	f"{shaxs['yunalish']} yo\'nalishida faoliyat yuritgan.")
"""

"""picasso={'ism':'Pablo Picasso', 'soha':'sanat', 't_yil':1881, 't_joy':'Ispaniya', 
'asar':['o	Guernica', 'o	Les Demoiselles dAvignon']}
gates={'ism':'Bill Gates', 'soha':'internet', 't_yil':1955, 't_joy':'AQSh'}
musk={'ism':'Elon Musk', 'soha':'internet', 't_yil':1971, 't_joy':'AQSh'}
shaxslar=[picasso, gates, musk]
for shaxs in shaxslar:
	print(f"{shaxs['ism']} {shaxs['t_yil']}-yil {shaxs['t_joy']}da tug'ilgan, {shaxs['soha']} sohasida faoliyat yuritgan")
"""
"""
print('istalgan sonni kvadartini hisoblaovchi dastur')
savol='istalgan sonni kiriting '
savol+='dasturni tuxtatish uchun exit deb yozing '
qiymat=' '
ishora=True
while ishora:
	qiymat=input(savol)
	if qiymat=='exit':
		ishora=False
	else:
		print(float(qiymat)**2)"""
"""print('foydalanuchining yoshini sorovchi dastur')
savol='yoshingiz nechida '
savol+='dasturni tuxtatish uchun exitni bosing '
yosh=' '
ishora=True
while ishora:
	yosh=input(savol)
	if yosh=='exit':
		ishora=False
	else:
		print(yosh)
"""
"""savol='seltsini frahfreitga otkazib haroratni aytuvchi dastur '
savol+='dasturni tuxtatish uchun tuxta deb yoz '
yosh=' '
ishora=True
while ishora:
	yosh=input(savol)
	if yosh=='tuxta':
		ishora=False
	else:
		print(f'bugun harorat {yosh} seltsiy, {float(yosh)*33.8} frahfreigt boladi')"""
"""talaba_baho={}
print("Talabaning bahosi haqida malumot")
while True:
	ism=input("Talaba ismini kiriting: ")
	if ism=="stop":
		break
	baho=input("Talaba bahosini kiriting: ")
	talaba_baho[ism]=baho
print("Talabalarning baholari:")
for ism, baho in talaba_baho.items():
	print(f"{ism}ning bahosi: {baho}")
"""
"""print("Kontaktlar")
kontaktlar={}
while True:
	kontakt=input("Kontakt nomini kiriting: ")
	if kontakt=="stop":
		break
	tel_raqam=input("Kontakt telefon raqamini kiriting: ")
	kontaktlar[kontakt]=tel_raqam
for kontakt, tel_raqam in kontaktlar.items():
	print(f"{kontakt}ning telefon raqami: {tel_raqam}")
"""
"""print("Davlatlar haqida ma'lumotlar")
davlat_poytaxt={}
while True:
	davlat=input("Davlat nomini kiriting: ")
	if davlat=="stop":
		break
	poytaxt=input("Poytaxt nomini kiritning: ")
	davlat_poytaxt[davlat]=poytaxt
for davlat, poytaxt in davlat_poytaxt.items():
	print(f"{davlat}ning poytaxti: {poytaxt}")
"""



