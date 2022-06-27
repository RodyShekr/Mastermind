# --- MASTERMIND --- #

import random


print (" --- MASTERMIND --- \n")
name=input("Willkommen bei Mastermind. Gib bitte deinen Namen ein:\n")
print("Hey "  + name +"! Freut mich, dass du hier bist.\n\n\n")
print ("Rate die geheimen Farben. \n")
print ("Gib bitte die Farben ein.\nDu kannst rot(R), grün(G), blau(B), orange(O), weiß(W) oder pink(P) wählen.")

colors = ["R", "G", "B", "O", "W", "P"]
trys = 0
game = True

#Computer nimmt durch Zufall Farben.
color_code = random.sample(colors,4)	
print (color_code)

#Spieler wählt die Farben aus.	
while game:
	correct_color = ""
	guessed_color = ""
	player_guess = input().upper()
	trys += 1
	
	#Hier wird geprüft ob die Farben richtig sind.
	if len(player_guess) != len(color_code):
		print ("\nDu kannst vier Farben wählen. Versuche nochmal!")
		continue
	for i in range(4):
		if player_guess[i] not in colors:
			print ("\nSchaue bitte nach, welche Farben du wählen kannst.")
			continue
			
	#Vergleich zwischen den geheimen Zahlen und die die eingegeben worden
	if correct_color != "++++":
		for i in range(4):
			if player_guess[i] == color_code[i]:
				correct_color += "+"
			if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
				guessed_color += "-"
		print (correct_color +  guessed_color + "\n")		
		
	if correct_color == "++++":
		if trys == 1:
			print ("Glückwunsch! Du hast es beim ersten Mal geschafft!")
		else:
			print ("Sehr gut! Du hast  " + str(trys) + " Versuche gebraucht, um es zu raten.")
		game = False
		
	if trys >= 1 and trys <6 and correct_color != "++++":
		print ("Nächster Versuch: ")
	elif trys >= 6:
		print ("Du hast leider verloren. Die Farben waren: " + str(color_code))	

	#Nochmal spielen?
	while game == False:
		finish_game = input("\nMöchtest du nochmal spielen (J oder N)?").upper()
		trys = 0
		if finish_game =="N":
			exit("\nDanke dir " +name+ " fürs Spielen! Auf Wiedersehen!\n")
		elif finish_game =="J":
			game = True
			print ("Also lass uns noch eine Runde spielen. Rate die geheimen Farben: ")
   
   # --- End Mastermind--- #
