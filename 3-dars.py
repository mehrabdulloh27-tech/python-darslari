hamkasblar={"ali":{"familya":"valiyev", "yosh":"24", "malumoti":"oliy", "dasturlar":["css","php", "js"]},
"azim":{"familya":"choriyev", "yosh":30, "malumoti":"o'rta", "dasturlar":["python", "c++", "java", "c#"]},
"alisher":{"familya":"ashurov", "yosh":"45", "malumoti":"oliy", "dasturlar":["javscript", "css"]}}
for ism, info in hamkasblar.items():
   print(f"\n{ism.title()}" {info["familya"].title()}, 
      f"{info["yosh"]} yoshda". 
      f"malumoti: {info["malumoti"]}. \n"
      "quyidagi dasturlash tillarini biladi: ")
   for dastur in info["dasturlar"]:
      print(dastur.upper())


print('Yaqin dustlaringizni ruyhatini tuzamiz')
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
   print(ismlar.sort())