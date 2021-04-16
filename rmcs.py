with open("touch.txt", "w") as i:
	i.write("")
from tkinter import *
from PIL import Image, ImageTk
import random
root = Tk()
root.geometry("1294x700")
root.title("Raja-Mantri-Chor-Sipahi")
root.config(bg="yellow")

def Main_Window():
	def scorecard():
		main_root = Tk()
		main_root.config(bg="yellow")
		main_root.title("Let's Play!!")
		main_root.geometry("1200x1000")
		f1 = Frame(main_root, relief=SUNKEN, borderwidth=10, bg="red")
		f1.grid(row=0, column=0, columnspan=4)
		heading = Label(f1, text="Scorecard", font="cailibri 40 bold", borderwidth=20, fg="red", bg="yellow")
		heading.grid(row=0, column=0, columnspan=4, padx=100, pady=13)
		name_1 = Label(main_root, text=Player1, font="Cailibri 20 bold", fg="red", bg="yellow")
		name_2 = Label(main_root, text=Player2, font="Cailibri 20 bold", fg="red", bg="yellow")
		name_3 = Label(main_root, text=Player3, font="Cailibri 20 bold", fg="red", bg="yellow")
		name_4 = Label(main_root, text=Player4, font="Cailibri 20 bold", fg="red", bg="yellow")
		name_1.grid(row=1, column=0, padx=100, pady=10)
		name_2.grid(row=1, column=1, padx=100, pady=10)
		name_3.grid(row=1, column=2, padx=100, pady=10)
		name_4.grid(row=1, column=3, padx=100, pady=10)
		submit_button = Button(main_root, text="Move to game!!", font="Cailibri 20 bold", fg="red", bg="yellow",
							   command=game)
		submit_button.grid(row=3, column=1, padx=20, pady=500, columnspan=2)
		main_root.mainloop()
		main_root.after(1000, scorecard)
	root.after(100, scorecard)
	Player1 = name1_val.get()
	Player2 = name2_val.get()
	Player3 = name3_val.get()
	Player4 = name4_val.get()
	def reveal():

		file = open("touch.txt", "r")
		chars = file.read(1)
		# print(chars)
		def final():
			def generation():
			    string_to_choose_from = "1234"
			    list_format = random.sample(string_to_choose_from, 4)
			    tarika = "".join(list_format)
			    if list_format[0] == "1":
			    	var1 = open("Player1.txt")
			    	value1 = var1.read()
			    	if value1 == "1":
			    		photo1 = f"{Player1} - King"
			    	var2 = open("Player2.txt")
			    	value2 = var1.read()
			    	if value2 == "1":
			    		photo1 = f"{Player2} - King"
			    	var3 = open("Player3.txt")
			    	value3 = var1.read()
			    	if value3 == "1":
			    		photo1 = f"{Player3} - King"
			    	var4 = open("Player4.txt")
			    	value4 = var1.read()
			    	if value4 == "1":
			    		photo1 = f"{Player4} - King"
			    	photo1 = "    king    "
			    if list_format[0] == "2":
			    	photo1 = "   minister   "
			    	tkinter.messagebox.askyesno(title=None, message="hey minister guess if player 1 is minister or not?", **options)
			    if list_format[0] == "3":
			    	photo1 = "????????"
			    	heading.config(text="Now Minister had to guess")
			    if list_format[0] == "4":
			    	photo1 = "????????"
			    if list_format[1] == "1":
			    	photo2 = "    king    "
			    if list_format[1] == "2":
			    	photo2 = "   minister   "
			    if list_format[1] == "3":
			    	photo2 = "????????"
			    	heading.config(text="Now Minister had to guess")
			    if list_format[1] == "4":
			    	photo2 = "????????"
			    if list_format[2] == "1":
			    	photo3 = "    king    "
			    	heading.config(text="Now Minister had to guess")
			    if list_format[2] == "2":
			    	photo3 = "   minister   "
			    if list_format[2] == "3":
			    	photo3 = "????????"
			    if list_format[2] == "4":
			    	photo3 = "????????"
			    	heading.config(text="Now Minister had to guess")
			    if list_format[3] == "1":
			    	photo4 = "    king    "
			    if list_format[3] == "2":
			    	photo4 = "   minister   "
			    if list_format[3] == "3":
			    	photo4 = "????????"
			    if list_format[3] == "4":
			    	photo4 = "????????"
			    	heading.config(text="Now Minister had to guess")
			    panl1 = Label(root, text=photo1, font="cailibri 24 bold", bg="red", fg="yellow")   # keep a reference
			    panl1.grid(row=4, column=0, padx=0, pady=12)
			    panl1 = Label(root, text=photo2, font="cailibri 24 bold", bg="red", fg="yellow")   # keep a reference
			    panl1.grid(row=4, column=1, padx=0, pady=12)
			    panl1 = Label(root, text=photo3, font="cailibri 24 bold", bg="red", fg="yellow")   # keep a reference
			    panl1.grid(row=4, column=2, padx=0, pady=12)
			    panl1 = Label(root, text=photo4, font="cailibri 24 bold", bg="red", fg="yellow")   # keep a reference
			    panl1.grid(row=4, column=3, padx=0, pady=12)
			    next_button = Button(root, text="    Next    ", font="Cailibri 20 bold", fg="red", bg="yellow", command=game)
			    next_button.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

			    

			submit_button.destroy()
			generate_button = Button(root, text=" generate ", font="Cailibri 20 bold", fg="red", bg="yellow", command=generation)


			generate_button.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
		if chars == "1":
			aaqqa = open("Player1.txt", "w")
			aaqqa.write("1")

			panl1 = Label(root, text=Player1, font="cailibri 24 bold", bg="red", fg="yellow")   # keep a reference
			panl1.grid(row=4, column=0, padx=0, pady=12)
		elif chars == "2":
			aaeeea = open("Player1.txt", "w")
			aaeeea.write("2")
			panl1 = Label(root, text=Player1, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=1, padx=0, pady=12)
		elif chars == "3":
			aaea = open("Player1.txt", "w")
			aaea.write("3")
			panl1 = Label(root, text=Player1, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=2, padx=0, pady=12)
		elif chars == "4":
			aassa = open("Player1.txt", "w")
			aassa.write("4")
			panl1 = Label(root, text=Player1, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=3, padx=0, pady=12)
		fil = open("touch.txt", "r")
		cars2 = list(fil.read(2))
		chars2 = cars2[1]
		# print(chars2)
		if chars2 == "1":
			aaar = open("Player2.txt", "w")
			aaar.write("1")
			panl1 = Label(root, text=Player2, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=0, padx=0, pady=12)
		elif chars2 == "2":
			aaay = open("Player2.txt", "w")
			aaay.write("2")
			panl1 = Label(root, text=Player2, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=1, padx=0, pady=12)
		elif chars2 == "3":
			aaai = open("Player2.txt", "w")
			aaai.write("3")
			panl1 = Label(root, text=Player2, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=2, padx=0, pady=12)
		elif chars2 == "4":
			aaal = open("Player2.txt", "w")
			aaal.write("4")
			panl1 = Label(root, text=Player2, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=3, padx=0, pady=12)
		fi = open("touch.txt", "r")
		chas3 = list(fi.read(3))
		chars3 = chas3[2]

		if chars3 == "1":
			aaak = open("Player3.txt", "w")
			aaak.write("1")
			panl1 = Label(root, text=Player3, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=0, padx=0, pady=12)
		elif chars3 == "2":
			aaaj = open("Player3.txt", "w")
			aaaj.write("2")
			panl1 = Label(root, text=Player3, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=1, padx=0, pady=12)
		elif chars3 == "3":
			aaah = open("Player3.txt", "w")
			aaah.write("3")
			panl1 = Label(root, text=Player3, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=2, padx=0, pady=12)
		elif chars3 == "4":
			aaag = open("Player3.txt", "w")
			aaag.write("4")
			panl1 = Label(root, text=Player3, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=3, padx=0, pady=12)
		fdd = open("touch.txt", "r")
		char4 = list(fdd.read(4))
		chars4 = char4[3]
		if chars4 == "1":
			aaaf = open("Player4.txt", "w")
			aaaf.write("1")
			panl1 = Label(root, text=Player4, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=0, padx=0, pady=12)
			final()
		elif chars4 == "2":
			aaad = open("Player4.txt", "w")
			aaad.write("2")
			panl1 = Label(root, text=Player4, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=1, padx=0, pady=12)
			final()
		elif chars4 == "3":
			aasa = open("Player4.txt", "w")
			aasa.write("3")
			panl1 = Label(root, text=Player4, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=2, padx=0, pady=12)
			final()
		elif chars4 == "4":
			aaaaa = open("Player4.txt", "w")
			aaaaa.write("4")
			panl1 = Label(root, text=Player4, font="cailibri 24 bold", bg="red", fg="yellow")  # keep a reference

			panl1.grid(row=4, column=3, padx=0, pady=12)
			final()

		# print(chars4)

			with open("touch.txt", "w") as aiii:
				aiii.write("")

	def click1():
		aa = open('touch.txt', 'a')
		aa.write('1')
		clickedphoto = Image.open("clicked.png")
		image1 = ImageTk.PhotoImage(clickedphoto)
		panl1 = Button(root, image=image1, borderwidth=0, command=reveal)
		panl1.image = image1  # keep a reference
		panl1.grid(row=4, column=0, padx=0, pady=12)
	def click2():
		aa = open('touch.txt', 'a')
		aa.write('2')
		clickedphoto = Image.open("clicked.png")
		image1 = ImageTk.PhotoImage(clickedphoto)
		panl1 = Button(root, image=image1, borderwidth=0, command=reveal)
		panl1.image = image1  # keep a reference
		panl1.grid(row=4, column=1, padx=0, pady=12)
	def click3():
		aa = open('touch.txt', 'a')
		aa.write('3')
		clickedphoto = Image.open("clicked.png")
		image1 = ImageTk.PhotoImage(clickedphoto)
		panl1 = Button(root, image=image1, borderwidth=0, command=reveal)
		panl1.image = image1  # keep a reference
		panl1.grid(row=4, column=2, padx=0, pady=12)
	def click4():
		aa = open('touch.txt', 'a')
		aa.write('4')
		clickedphoto = Image.open("clicked.png")
		image1 = ImageTk.PhotoImage(clickedphoto)
		panl1 = Button(root, image=image1, borderwidth=0, command=reveal)
		panl1.image = image1  # keep a reference
		panl1.grid(row=4, column=3, padx=0, pady=12)
	def game():
		heading.config(text="Welcome to Raja-Mantri-Chor-Sipahi")
		pathtophoto = Image.open("s.png")
		image1 = ImageTk.PhotoImage(pathtophoto)
		panel1 = Button(root, image=image1, borderwidth=0, command=click1)
		panel1.image = image1  # keep a reference
		panel1.grid(row=4, column=0, padx=0, pady=12)
		pathtophot = Image.open("s.png")
		image = ImageTk.PhotoImage(pathtophoto)
		panel = Button(root, image=image1, borderwidth=0, command=click2)
		panel.image = image1  # keep a reference
		panel.grid(row=4, column=1, padx=0, pady=12)
		pathtopho = Image.open("s.png")
		imag = ImageTk.PhotoImage(pathtophoto)
		pane = Button(root, image=image1, borderwidth=0, command=click3)
		pane.image = image1  # keep a reference
		pane.grid(row=4, column=2, padx=0, pady=12)
		pathtoph = Image.open("s.png")
		ima = ImageTk.PhotoImage(pathtophoto)
		pan = Button(root, image=image1, borderwidth=0, command=click4)
		pan.image = image1  # keep a reference
		pan.grid(row=4, column=3, padx=0, pady=12)
f1 = Frame(root, relief=SUNKEN, borderwidth=10, bg="red")
f1.grid(row=0, column=0, columnspan=4)
heading = Label(f1, text="Welcome to Raja-Mantri-Chor-Sipahi", font="Cailibri 38 bold", fg="red", bg="yellow")
heading.grid(row=0, column=0, padx=50, pady=8)
f2 = Frame(root, relief=SUNKEN, borderwidth=10, bg="red").grid(row=1, column=1)
name_1 = Label(f2, text="Player 1", font="Cailibri 20 bold", fg="red", bg="yellow")
name_1.grid(row=1, column=0, padx=5, pady=10)
name_2 = Label(f2, text="Player 2", font="Cailibri 20 bold", fg="red", bg="yellow")
name_2.grid(row=1, column=1, padx=5, pady=10)
name_3 = Label(f2, text="Player 3", font="Cailibri 20 bold", fg="red", bg="yellow")
name_3.grid(row=1, column=2, padx=5, pady=10)
name_4 = Label(f2, text="Player 4", font="Cailibri 20 bold", fg="red", bg="yellow")
name_4.grid(row=1, column=3, padx=5, pady=10)
name1_val = StringVar()
name2_val = StringVar()
name3_val = StringVar()
name4_val = StringVar()
name1_entry = Entry(root, font="Cailibri 20 bold", fg="red", bg="yellow", textvariable=name1_val)
name2_entry = Entry(root, font="Cailibri 20 bold", fg="red", bg="yellow", textvariable=name2_val)
name3_entry = Entry(root, font="Cailibri 20 bold", fg="red", bg="yellow", textvariable=name3_val)
name4_entry = Entry(root, font="Cailibri 20 bold", fg="red", bg="yellow", textvariable=name4_val)
name1_entry.grid(row=2, column=0, padx=10, pady=10)
name2_entry.grid(row=2, column=1, padx=10, pady=10)
name3_entry.grid(row=2, column=2, padx=10, pady=10)
name4_entry.grid(row=2, column=3, padx=10, pady=10)
name1_entry.insert(0, "Player 1")
name2_entry.insert(0, "Player 2")
name3_entry.insert(0, "Player 3")
name4_entry.insert(0, "Player 4")
submit_button = Button(root, text="Submit", font="Cailibri 20 bold", fg="red", bg="yellow", command=Main_Window)
submit_button.grid(row=3, column = 1, padx=20, pady=20, columnspan=2)

root.mainloop()