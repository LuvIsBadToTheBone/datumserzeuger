#erzeugt datumsangaben für einen monat im format "Tag, dd.mm.yy"
#usage: python3 dingsbums.py

wochentage = ("Mo","Di","Mi","Do","Fr","Sa","So")


print("Erzeugt Datumsangaben fuer einen ganzen Monat in Form: Tag, dd,mm,yy, und speichert it Textdatei.\n\n")


jahr = int(input("Bitte Gib die letzten beiden Zahlen des Jahres ein:  "))
while jahr < 0 or jahr > 99:
	if jahr < 0:
		print("Zu klein.")
		jahr = int(input("Bitte Gib die letzten beiden Zahlen des Jahres ein:  "))
	elif jahr > 99:
		print("Zu groß.")
		jahr = int(input("Bitte Gib die letzten beiden Zahlen des Jahres ein:  "))
		
monat = int(input("Bitte Gib den Monat an, 1-12:  "))
while monat < 1 or monat > 12:
	if jahr < 1:
		print("Zu klein.")
		monat = int(input("Bitte Gib den Monat an:  "))
	elif jahr > 12:
		print("Zu groß.")
		monat = int(input("Bitte Gib den Monat an:  "))
		
gesamttage = int(input("Bitte gib die Anzahl der Monatstage an: "))
while gesamttage < 28 or gesamttage > 31:
	if gesamttage < 28:
		print("Zu klein.")
		gesamttage = int(input("Bitte gib die Anzahl der Monatstage an: "))
	elif gesamttage > 31:
		print("Zu groß.")
		gesamttage = int(input("Bitte gib die Anzahl der Monatstage an: "))


starttagint = int(input("Bitte gib den Tag ein an dem der Monat startet.\nMo = 1, Di = 2, Mi = 3, Do = 4, Fr = 5, Sa = 6, So = 7: "))
while starttagint < 1 or starttagint > 7:
	if starttagint < 1:
		print("Zu klein.")
		starttagint = int(input("Bitte gib den Tag ein an dem der Monat startet.\nMo = 1, Di = 2, Mi = 3, Do = 4, Fr = 5, Sa = 6, So = 7: "))
	elif starttagint > 7:
		print("Zo groß")
		starttagint = int(input("Bitte gib den Tag ein an dem der Monat startet.\nMo = 1, Di = 2, Mi = 3, Do = 4, Fr = 5, Sa = 6, So = 7: "))


wochentagscounter = starttagint



file = open("datumsdingens.txt","w")

for i in range(1,gesamttage+1):
	file.write(f"{wochentage[wochentagscounter-1]}, {i}.{monat}.{jahr}\n")
	if wochentagscounter == 7:
		wochentagscounter = 0
	wochentagscounter = wochentagscounter + 1
file.close()
print("In datumsdingens.txt gespeichert.")
