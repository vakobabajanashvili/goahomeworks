for i in range(1, 100, 2,):
    print(str(i) + " " + 'კენტი')
for q in range(2, 100, 2,):
    print(str(q) + " " +'ლუწი')


ასაკი = int(input("შენი ასაკი: "))
მამის_ასაკი = int(input("მამაშენის ასაკი: "))

if მამის_ასაკი == ასაკი * 2:
    print("ბინგო")
else:
    print("ვირთხა")


წლის = int(input("რამდენი წლის ხარ?: "))
სქესი = input("სქესი: ")

if წლის >= 65 and სქესი == "კაცი":
    print("კაცი ხარ და გეკუთვნით პენსია")
if წლის >= 60 and სქესი == "ქალი":
    print("ქალი ხარ და გეკუთვნით პენსია")
if სქესი == "ნონ ბაინარი":
    print("არ გეკუთვნით პენსია")
    print("გაეთრიე აქედან პანჩურის კვრით")

განათლება = input("სად სწავლობთ/სწავლობდით?: ")

if განათლება == "goa-ში":
    print("ძალიან კარგი!")
else:
    print("ხოდა შემოდი goa-ში")