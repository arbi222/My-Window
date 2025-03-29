from tkinter import *
from tkinter import filedialog , messagebox
import webbrowser
from PIL import ImageTk, Image
import os 
import pygame
import random
import math
from pygame import mixer


root = Tk()
root.geometry('925x400+20+20')
root.title('My Window')
root.resizable(width = False , height = False)
root.iconbitmap(r'window.ico')
root.grid()
root.config(bg = 'white')
#root.attributes("-toolwindow", 1)


import snake
def close_main_window():
			if messagebox.askyesno("My Window", "Are you sure you want to quit My Window ?"):
				root.destroy() 
				snake.bye()
						

root.protocol("WM_DELETE_WINDOW", close_main_window)

#===============================BUTTON COLORS===================================	
x = 'thistle3' #gray51	
y = 'gray51'   #sea green

#=================MUSIC FUNCTIONS============================================
Youtube_photo = ImageTk.PhotoImage(Image.open('youtube.png'))
Pc_photo = ImageTk.PhotoImage(Image.open('Pc.png'))
file_to_play = ''
active = 1
def music():
	global Youtube_photo
	global Pc_photo
	music_window = Toplevel()
	music_window.title('Music Folder')
	music_window.geometry('245x133+400+200')
	music_window.resizable(False , False)
	music_window.iconbitmap(r'music_icon.ico')
	music_window.config(bg = 'peach puff')

	# ======================YOUTUBE===========================================
	def open_youtube():
		webbrowser.open('https://www.youtube.com/')

	Youtube_button = Button(music_window , image = Youtube_photo , bg = 'red2' , command = open_youtube )
	Youtube_button.grid(row = 0 , column = 0 , pady = 20 , padx = 20)

	Youtube_label = Label(music_window , text = 'Youtube' , bg = 'red2' , font = 'Times 13 italic' , fg = 'black')
	Youtube_label.grid(row = 1 , column = 0 , pady = 0, padx = 30)

	
	#=================================COMPUTER================================
	def Pc_music():

		def selecting_song():
			global file_to_play
			fln = filedialog.askopenfilename(initialdir=os.getcwd(), title = 'Select song file' , filetypes = (('Music File', '*.mp3'), ('All Files', '*.*')))
			title_of_song.set(os.path.basename(fln[:-4]))
			file_to_play = fln
			pygame.mixer.music.load(file_to_play)
			pygame.mixer.music.play()
			selecting_button = Button(main_label, text = 'Select Other Song' , bg = 'skyblue' ,font = ('arial',19,'bold'),
							fg = 'black' , height = 1 , width = 26, command = selecting_song ).grid(row = 1 , column = 0, pady = 50 , padx = 1 ,  columnspan = 2)
			play_button = Button(main_label , text = 'Pause' , bg = 'skyblue' , fg = 'black', font = ('arial',10,'bold'), 
											height = 1 , width = 13 , command = play_song).grid(row = 2 , column = 0 , pady = 10 , padx = 1 ,columnspan = 2)
		
		
		def play_song():
			global active
			if file_to_play == '':
				messagebox.showerror(title='No Song Selected' , message = 'Please select a song to play ')
				return False	
			
			if active == 1:
				 pygame.mixer.music.pause()
				 play_button = Button(main_label , text = 'Resume' , bg = 'skyblue' , fg = 'black', font = ('arial',10,'bold'), 
											height = 1 , width = 13 , command = play_song).grid(row = 2 , column = 0 , pady = 10 , padx = 1 ,columnspan = 2)
			else:
				pygame.mixer.music.unpause()
				play_button = Button(main_label , text = 'Pause' , bg = 'skyblue' , fg = 'black', font = ('arial',10,'bold'), 
											height = 1 , width = 13 , command = play_song).grid(row = 2 , column = 0 , pady = 10 , padx = 1 ,columnspan = 2)
			active = 3 - active
		
		
		a_window = Toplevel()
		a_window.title('Mp3 Player')
		a_window.resizable(False , False)
		a_window.geometry('405x270+300+300')
		a_window.iconbitmap(r'mp3.ico')
		a_window.config(bg = 'cyan')
		
		pygame.init()
		
		title_of_song = StringVar()
		title_of_song.set("Song : No song selected")
		
		
		main_label = LabelFrame(a_window , bg = '#58F') 
		main_label.pack(fill = "both" , expand = 'yes' )
		
		listing = Frame(main_label)
		listing.grid()
		
		small_label = Label(main_label , textvariable = title_of_song , bg = 'black' , font = ('arial',9,'bold'), 
										fg = 'white' , height = 1 , width = 56).grid(row = 0 , column = 0 , pady = 1 , padx = 1 , columnspan = 2)	
		
		selecting_button = Button(main_label, text = 'Select Song' , bg = 'skyblue' ,font = ('arial',19,'bold'),
								fg = 'black' , height = 1 , width = 26, command = selecting_song ).grid(row = 1 , column = 0, pady = 50 , padx = 1 ,  columnspan = 2)
		
		play_button = Button(main_label , text = 'Play' , bg = 'skyblue' , fg = 'black', font = ('arial',10,'bold'), 
											height = 1 , width = 13 , command = play_song).grid(row = 2 , column = 0 , pady = 10 , padx = 1 ,columnspan = 2)
		
		def closing_music_window():
			if messagebox.askokcancel("Quit", "Do you want to quit?"):
				pygame.mixer.music.stop()
				a_window.destroy()
				music_window.destroy()
    		
		a_window.protocol("WM_DELETE_WINDOW",closing_music_window)

	
	Pc_button = Button(music_window , image = Pc_photo ,bg = 'skyblue' , command = Pc_music)
	Pc_button.grid(row = 0 , column = 1 , pady = 20 , padx = 20)

	Pc_label = Label(music_window , text = 'Computer' , bg = 'skyblue' , fg = 'black' , font = 'Times 12 italic')
	Pc_label.grid(row = 1 , column = 1 , pady = 0 , padx = 20)


#=========================DOWNLOAD MUSIC FUNCTIONS===============================
def download_music():
	import download_music
	download_music.start()

#=============================GAMES SECTION====================================
Space_invader_photo = ImageTk.PhotoImage(Image.open('space_invader_photo.png'))
Tic_tac_toe_photo = ImageTk.PhotoImage(Image.open('tic_tac_toe_photo.png'))
Snake_photo = ImageTk.PhotoImage(Image.open('snake_photo.png'))
bullet_state = 'ready'
def games():
	games_window = Toplevel()
	games_window.title('Games folder')
	games_window.geometry('815x500+50+50')
	games_window.resizable(False , False)
	games_window.iconbitmap(r'games_folder_icon.ico')
	games_window.config(bg = 'cyan')


	welcome_label = Label(games_window , text = 'Welcome to Gaming' ,width = 45 , height = 2 ,   bg = 'red' , fg = 'black', font = 'Times 25')
	welcome_label.grid(row = 0 , column = 0 , columnspan = 120)

	def close_games_window():
			if messagebox.askyesno("My Window", "Do you really wish to quit playing ?"):
				games_window.destroy()
    		
	games_window.protocol("WM_DELETE_WINDOW", close_games_window)


	# ======================== SPACE INVADERS====================================
	def space_ivaders():
	
		# initialize the pygame 
		pygame.init()
		
		# creating the screen             w   h
		screen = pygame.display.set_mode((800,600))
		
		
		# background
		background = pygame.image.load('1234.jpg')
		
		# background sound 
		mixer.music.load('background.mp3')
		mixer.music.play(-1) # play the song all the time 
		
		# title and icon
		pygame.display.set_caption('Space invaders')
		icon = pygame.image.load('laser-gun.png')
		pygame.display.set_icon(icon)
		
		# Player
		playerImg = pygame.image.load('space-invaders.png')
		playerX = 370
		playerY = 500
		playerX_change = 0
		
		# Enemy
		enemyImg =[]
		enemyX = []
		
		enemyY = []
		enemyX_change = []
		enemyY_change = []
		num_of_enemys = 7
		
		for i in range(num_of_enemys):
			enemyImg.append(pygame.image.load('alien.png')) 
			enemyX.append(random.randint(0,735))
			enemyY.append(random.randint(50,150))
			enemyX_change.append(0.45)
			enemyY_change.append(40)
		
		
		# bullet
		bulletImg = pygame.image.load('bullet.png')
		bulletX = 0
		bulletY = 480
		bulletX_change = 0
		bulletY_change = 1
		
		
		# score
		score_value = 0
		font = pygame.font.Font('freesansbold.ttf', 32)
		
		textX = 10
		textY = 10
		
		# game over text 
		over_font = pygame.font.Font('freesansbold.ttf', 64)
		
		def show_score(x,y):
			score = font.render('Score : ' + str(score_value) , True, (255,255,255))
			screen.blit(score , (x , y))
		
		def game_over_text():
			over_text = over_font.render('GAME OVER' , True , (255, 255, 255))
			screen.blit(over_text , (200 , 250))
		
		
		def player(x,y):
			screen.blit(playerImg , (x , y))
		
		def enemy(x,y ,i):
			screen.blit(enemyImg[i], (x , y))
		
		def fire_bullet(x,y):
			global bullet_state
			bullet_state = 'fire'
			screen.blit(bulletImg, (x + 16, y + 10))
		
		def iscollision(enemyX , enemyY , bulletX , bulletY):
			distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
			if distance < 27:
				return True
			else:
				return False	
		
		running = True
		while running:
			global bullet_state
			# RGB = RED , GREEN , BLUE ,,  	255 the biggest value
			screen.fill((0,0,0))
			# background image
			screen.blit(background,(0,0))
		
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
			
				
				if event.type == pygame.KEYDOWN:
					# player
					if event.key == pygame.K_LEFT:
						playerX_change = -0.4
					if event.key == pygame.K_RIGHT:
						playerX_change = 0.4
		
					# multiple bullets
					if bulletY <= 0:
						bulletY = 480
						bullet_state = 'ready'	
					if event.key == pygame.K_SPACE:
						if bullet_state == 'ready':
							bullet_sound = mixer.Sound('laser.wav')
							bullet_sound.play()
							bulletX = playerX
							fire_bullet(bulletX , bulletY)
		
		
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						playerX_change = 0
			
			# checking for boundaries 
			playerX += playerX_change
		
			if playerX <= 0:
				playerX = 0
			elif playerX >= 736:
				playerX = 736	
		
			# enemy boundairies
			for i in range(num_of_enemys):
				
				# game over
				if enemyY[i] > 440:
					for j in range(num_of_enemys):
						enemyY[j] = 2000
					game_over_text()
					break
		
				enemyX[i] += enemyX_change[i]
				if enemyX[i] <= 0:
					enemyX_change[i] = 0.45
					enemyY[i] += enemyY_change[i]
				elif enemyX[i] >= 736:
					enemyX_change[i] = -0.45
					enemyY[i] += enemyY_change[i]	
		
		
				# collision
				collision = iscollision(enemyX[i] , enemyY[i] , bulletX , bulletY)
				if collision:
					explosion_sound = mixer.Sound('explosion.wav')
					explosion_sound.play()
					bulletY = 480
					bullet_state = 'ready'
					score_value += 1
					enemyX[i] = random.randint(0,735)
					enemyY[i] = random.randint(50,150)
		
				enemy(enemyX[i] , enemyY[i] , i)
			
		
			# bullet movement
			if bullet_state == 'fire':
				fire_bullet(bulletX , bulletY)
				bulletY -= bulletY_change		
		
		
			player(playerX,playerY)
			show_score(textX , textY)
			pygame.display.update()	
		
	global Space_invader_photo
	Space_invader_button = Button(games_window , image = Space_invader_photo , bg = x , activebackground = y , command = space_ivaders)
	Space_invader_button.grid(row = 1 , column = 0 , pady = 20 , padx = 30)

	Space_invader_label = Label(games_window , text = 'Space Invaders' , font = 'Times 16 italic' , bg = x , fg = 'white')
	Space_invader_label.grid(row = 2 , column = 0 , pady = 0 , padx = 30)

	#============================TIC TAC TOE========================================
	def Tic_tac_toe():
		import TicTacToe
		TicTacToe.RunProgram()

	global Tic_tac_toe_photo
	Tic_tac_toe_button = Button(games_window , image = Tic_tac_toe_photo , bg = x , activebackground = y , command = Tic_tac_toe)
	Tic_tac_toe_button.grid(row = 1 , column = 1 , pady = 20 , padx = 30)

	Tic_tac_toe_label = Label(games_window , text = 'Tic-Tac-Toe' , font = 'Times 16 italic' ,width = 12, bg = x , fg = 'white')
	Tic_tac_toe_label.grid(row = 2 , column = 1 , pady = 0 , padx = 30)

	#====================================SNAKE======================================
	def snake():
		import snake
		snake.run_game()

	global Snake_photo
	Snake_button = Button(games_window , image = Snake_photo , bg = x , activebackground = y , command = snake)
	Snake_button.grid(row = 1 , column = 2 , pady = 20 , padx = 30)

	Snake_label = Label(games_window , text = 'Snake' , font = 'Times 16 italic' ,width = 12, bg = x , fg = 'white')
	Snake_label.grid(row = 2 , column = 2 , pady = 0 , padx = 30)	
#============================SOCIAL NETWORKS FUNCTIONS===========================
Facebook_photo = ImageTk.PhotoImage(Image.open('facebook.png'))
Instagram_photo = ImageTk.PhotoImage(Image.open('instagram.png'))
Twitter_photo = ImageTk.PhotoImage(Image.open('twitter.png'))
Linkedin_photo = ImageTk.PhotoImage(Image.open('linkedin.png'))
Vk_photo = ImageTk.PhotoImage(Image.open('vk.png'))
Tumblr_photo = ImageTk.PhotoImage(Image.open('tumblr.png'))
Pinterest_photo = ImageTk.PhotoImage(Image.open('pinterest.png'))

def social_network():
	social_network_window = Toplevel()
	social_network_window.title('Social Networks')
	social_network_window.geometry('784x160+200+200')
	social_network_window.resizable(False , False)
	social_network_window.iconbitmap(r'social_network_icon.ico')
	social_network_window.config(bg = 'light coral')

	def openFacebook():
		webbrowser.open('https://www.facebook.com/')

	def openInstagram():
		webbrowser.open('https://www.instagram.com/')

	def openTwitter():
		webbrowser.open('https://www.twitter.com/')

	def openLinkedin():
		webbrowser.open('https://www.linkedin.com/')

	def openTumblr():
		webbrowser.open('https://www.tumblr.com/')

	def openVk():
		webbrowser.open('https://www.vk.com/')

	def openPinterest():
		webbrowser.open('https://www.pinterest.com/')


	Facebook_button = Button(social_network_window , image = Facebook_photo ,command = openFacebook)
	Facebook_button.grid(row = 0 , column = 0 , pady = 30 , padx = 20)
	Facebook_label = Label(social_network_window,text = 'Facebook',font = ('Times 13 italic'), bg = '#3b5998' , fg = 'white')
	Facebook_label.grid(row = 1 , column = 0 , pady = 1 , padx = 20)

	Instagram_button = Button(social_network_window , image = Instagram_photo , command = openInstagram)
	Instagram_button.grid(row = 0 , column = 1 , pady = 30 , padx = 20)
	Instagram_label = Label(social_network_window,text = 'Instagram',font = ('Times 13 italic'), bg = '#fbad50' , fg = 'white')
	Instagram_label.grid(row = 1 , column = 1 , pady = 1 , padx = 20)

	Twitter_button = Button(social_network_window , image = Twitter_photo , command = openTwitter)
	Twitter_button.grid(row = 0 , column = 2 , pady = 30 , padx = 20)
	Twitter_label = Label(social_network_window,text = 'Twitter',font = ('Times 13 italic'),width = 7, bg = '#00acee' , fg = 'white')
	Twitter_label.grid(row = 1 , column = 2 , pady = 1 , padx = 20)

	Linkedin_button = Button(social_network_window , image = Linkedin_photo , command = openLinkedin )
	Linkedin_button.grid(row = 0 , column = 3 , pady = 30 , padx = 20)
	Linkedin_label = Label(social_network_window,text = 'Linkedin',font = ('Times 13 italic'), bg = '#0e76a8' , fg = 'white')
	Linkedin_label.grid(row = 1 , column = 3 , pady = 1 , padx = 20)

	Tumblr_button = Button(social_network_window , image = Tumblr_photo , command = openTumblr )
	Tumblr_button.grid(row = 0 , column = 4 , pady = 30 , padx = 20)
	Tumblr_label = Label(social_network_window,text = 'Tumblr',font = ('Times 13 italic'),width = 7, bg = '#34526f' , fg = 'white')
	Tumblr_label.grid(row = 1 , column = 4 , pady = 1 , padx = 20)

	Vk_button = Button(social_network_window , image = Vk_photo , command = openVk)
	Vk_button.grid(row = 0 , column = 5 , pady = 30 , padx = 20)
	Vk_label = Label(social_network_window,text = 'Vk',font = ('Times 13 italic'),width = 7, bg = '#0e76a8' , fg = 'white')
	Vk_label.grid(row = 1 , column = 5 , pady = 1 , padx = 20)

	Pinterest_button = Button(social_network_window , image = Pinterest_photo , command = openPinterest )
	Pinterest_button.grid(row = 0 , column = 6 , pady = 30 , padx = 20)
	Pinterest_label = Label(social_network_window,text = 'Pinterest',font = ('Times 13 italic'),width = 7, bg = '#c8232c' , fg = 'white')
	Pinterest_label.grid(row = 1 , column = 6 , pady = 1 , padx = 20)

#=============================NOTES SECTION======================================
def notes():
	
	notes_window = Toplevel()
	notes_window.title('Notes')
	notes_window.iconbitmap(r'notes_icon.ico')
	
	text_scroll = Scrollbar(notes_window)
	text_scroll.pack(side = RIGHT , fill = Y)
	
	
	my_text = Text(notes_window , width = 97 , height = 25 , font = ('Times' , 15 , 'normal') , selectbackground = 'gray60' , selectforeground = 'black', undo = True , yscrollcommand = text_scroll.set)
	my_text.pack(expand=YES, fill= BOTH, pady = 10 )
	
	
	text_scroll.config(command = my_text.yview)
	
	# Functions
	#==================FISRT MENU=========================================
	def new_file():
		#checks if there is any word inside so it can save it , if it's not then directly quit
		written_text = my_text.get(1.0 , END)
		if len(written_text) > 1:
			#checks if you would like to save what's inside
			if messagebox.askyesno("Notes", "Do want to save it ?"):
				text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
				if text_file:
					text_file = open(text_file , 'w')
					text_file.write(my_text.get(1.0 , END))
					text_file.close()
					my_text.delete('1.0' , END)
					status_bar.config(text = 'New File')
			else:
				my_text.delete('1.0' , END)
				status_bar.config(text = 'New File')
		else:
			my_text.delete('1.0' , END)
			status_bar.config(text = 'New File')

	
	def open_file():
		#checks if there is any word inside so it can save it , if it's not then directly quit
		written_text = my_text.get(1.0 , END)
		if len(written_text) > 1:
			#checks if you would like to save what's inside
			if messagebox.askyesno("Notes", "Do want to save it ?"):
				text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
				if text_file:
					text_file = open(text_file , 'w')
					text_file.write(my_text.get(1.0 , END))
					text_file.close()
					
					my_text.delete('1.0' , END)
					text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
					name = text_file
					status_bar.config(text = name)
					
					text_file = open(text_file, 'r')
					stuff = text_file.read()
					my_text.insert(END , stuff)
					text_file.close()
			else:
				my_text.delete('1.0' , END)
				text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
				name = text_file
				status_bar.config(text = name)
			
				text_file = open(text_file, 'r')
				stuff = text_file.read()
				my_text.insert(END , stuff)
				text_file.close()		
		else:
			my_text.delete('1.0' , END)
			text_file = filedialog.askopenfilename(initialdir = 'C:/Desktop', title = 'Open file' , filetypes = (('Text Files', '*.txt') , ('All Files' , '*.*')))
			name = text_file
			status_bar.config(text = name)
		
			text_file = open(text_file, 'r')
			stuff = text_file.read()
			my_text.insert(END , stuff)
			text_file.close()	

	
	def save_file():
		text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
		if text_file:
			status_bar.config(text = 'File Saved')
	
			text_file = open(text_file , 'w')
			text_file.write(my_text.get(1.0 , END))
			text_file.close()
	
	def word_counter():
		words = my_text.get('1.0' , END)
		words_list = words.split()
		number_of_words = len(words_list)
		status_bar.config(text = '{x} words'.format(x = number_of_words))	
	
	
	def close_window():
		#checks if there is any word inside so it can save it , if it's not then directly quit
		written_text = my_text.get(1.0 , END)
		if len(written_text) > 1:
			#checks if you would like to save what's inside
			if messagebox.askyesno("Notes", "Do want to save it ?"):
				text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
				if text_file:
					text_file = open(text_file , 'w')
					text_file.write(my_text.get(1.0 , END))
					text_file.close()
					notes_window.destroy()	
			else:
				notes_window.destroy()
		else:
			notes_window.destroy()
	
	notes_window.protocol("WM_DELETE_WINDOW", close_window)
	
	
	def exit():
		#checks if there is any word inside so it can save it , if it's not then directly quit
		written_text = my_text.get(1.0 , END)
		if len(written_text) > 1:
			#checks if you would like to save what's inside
			if messagebox.askyesno("Notes", "Do want to save it ?"):
				text_file = filedialog.asksaveasfilename(defaultextension = '.txt' , initialdir = 'C:/Desktop' , title = 'Save File' , filetypes = (('Text Files' , '*.txt') , ('All Files' , '*.*')))
				if text_file:
					text_file = open(text_file , 'w')
					text_file.write(my_text.get(1.0 , END))
					text_file.close()
					notes_window.destroy()	
			else:
				notes_window.destroy()
		else:
			notes_window.destroy()
	
	
	#======================SECOND MENU==========================
	def cut_text(parameter):
		global selected
		if parameter:
			selected = notes_window.clipboard_get()
		else:
			if my_text.selection_get():
				#select text
				selected = my_text.selection_get()
				# delete text
				my_text.delete('sel.first' , 'sel.last')
				notes_window.clipboard_clear()
				notes_window.clipboard_append(selected)
	
	def copy_text(parameter):
		global selected
		# check to see if we used keyboard shortcuts
		if parameter:
			selected = notes_window.clipboard_get()
		
		if my_text.selection_get():
			selected = my_text.selection_get()
			notes_window.clipboard_clear()
			notes_window.clipboard_append(selected)
	
	def paste_text(parameter):
		global selected
		if parameter:
			selected = notes_window.clipboard_get()
		else:	
			if selected:
				position = my_text.index(INSERT)
				my_text.insert(position , selected)	
	
	# Menu
	my_menu = Menu(notes_window)
	notes_window.config(menu = my_menu)


	# Add file to menu
	file_menu = Menu(my_menu , tearoff = False)
	my_menu.add_cascade(label = 'File' , menu = file_menu)
	file_menu.add_command(label = 'New' , command = new_file)
	file_menu.add_command(label = 'Open' , command = open_file)
	file_menu.add_command(label = 'Save', command = save_file)
	file_menu.add_command(label = 'Count words', command = word_counter)
	file_menu.add_separator()
	file_menu.add_command(label = 'Exit' , command = exit)
	
	# Add edit menu
	edit_menu = Menu(my_menu , tearoff = False)
	my_menu.add_cascade(label = 'Edit' , menu = edit_menu)
	edit_menu.add_command(label = 'Cut' , command = lambda: cut_text(0) , accelerator = '(Ctrl+X)')
	edit_menu.add_command(label = 'Copy' , command = lambda: copy_text(0) , accelerator = '(Ctrl+C)')
	edit_menu.add_command(label = 'Paste' , command = lambda: paste_text(0) , accelerator = '(Ctrl+V)')
	edit_menu.add_separator()
	edit_menu.add_command(label = 'Undo' , command = my_text.edit_undo , accelerator = '(Ctrl+Z)')
	edit_menu.add_command(label = 'Redo', command = my_text.edit_redo , accelerator = '(Ctrl+Y)')
	
	
	# Add status bar
	status_bar = Label(notes_window , text = 'Ready  ', anchor = E )
	status_bar.pack(fill = X , side = BOTTOM )
	
	
	# edit bidings
	notes_window.bind('<Control-x>', cut_text)
	notes_window.bind('<Control-c>', copy_text)
	notes_window.bind('<Control-v>', paste_text)





#=================================MAIN MENU======================================
#===============================MUSIC===========================================
Music_photo = ImageTk.PhotoImage(Image.open('music.png'))
Music_button = Button(root , image = Music_photo , bg = x ,activebackground = y, command = music)
Music_button.grid(row = 0 , column = 0 , pady = 20 , padx = 20)

Music_label = Label(root ,text = 'Listen Music',font = ('Times 18 italic'), bg = x , fg = 'white')
Music_label.grid(row = 1 , column = 0 , pady = 1 , padx = 20)

#=================================SONG DOWNLOADER===================================
Download_photo = ImageTk.PhotoImage(Image.open('download.png'))
Download_button = Button(root , image = Download_photo , bg = x , activebackground = y, command= download_music)
Download_button.grid(row = 0 , column = 1 , pady = 20 , padx = 20)

Download_label = Label(root ,text = 'Download Music',font = ('Times 17 italic'), width = 12, bg = x , fg = 'white')
Download_label.grid(row = 1 , column = 1 , pady = 1 , padx = 20)

#==============================GAMES===================================================
Games_photo = ImageTk.PhotoImage(Image.open('games.png'))
Games_button = Button(root , bg = x ,activebackground = y, image = Games_photo , command = games)
Games_button.grid(row = 0 , column = 2 , pady = 20 , padx = 20)

Games_label = Label(root ,text = 'Play Games',font = ('Times 18 italic'), width = 10, bg = x , fg = 'white')
Games_label.grid(row = 1 , column = 2 , pady = 1 , padx = 20)

#===============================SOCIAL NETWORKS BUTTON========================================
Social_network_photo = ImageTk.PhotoImage(Image.open('social_network.png'))
Social_network_button = Button(root , bg = x , activebackground = y , image = Social_network_photo , command = social_network)
Social_network_button.grid(row = 0 , column = 3 , pady = 20 , padx = 20)

Social_network_label = Label(root ,text = 'Social Networks',font = ('Times 18 italic'), width = 12, bg = x , fg = 'white')
Social_network_label.grid(row = 1 , column = 3 , pady = 1 , padx = 20)

#=====================================NOTES===================================================
Notes_photo = ImageTk.PhotoImage(Image.open('notes.png'))
Notes_button = Button(root , bg = x , activebackground = y , image = Notes_photo , command = notes)
Notes_button.grid(row = 0 , column = 4 , pady = 20 , padx = 20)

Notes_label = Label(root ,text = 'Notes',font = ('Times 18 italic'), width = 10, bg = x , fg = 'white')
Notes_label.grid(row = 1 , column = 4 , pady = 1 , padx = 20)

#=====================MENU FILE OPTIONS=================================================
def exit():
	exit = messagebox.askyesno("My Window",'Are you sure you want to exit ?')
	if exit > 0:
		root.destroy()
		snake.bye()
		

def darkmode():
	root.config(bg = 'Black')


def darkmodeOff():
	root.config(bg = 'white')
	

menubar = Menu(root)

filemenu1 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File" , menu = filemenu1)
filemenu1.add_command(label = 'Turn On Dark Mode' , command = darkmode)
filemenu1.add_command(label = 'Turn Off Dark Mode' , command = darkmodeOff)
filemenu1.add_separator()
filemenu1.add_command(label = "Exit" , command = exit)

'''
def red():
	root.config(bg = 'red')

def cyan():
	root.config(bg = 'cyan')

def blue():
	root.config(bg = 'blue')

def green():
	root.config(bg = 'green')

def orange():
	root.config(bg = 'orange')

def yellow():
	root.config(bg = 'yellow')

def purple():
	root.config(bg = 'purple')

def violet():
	root.config(bg = 'violet')


filemenu2 = Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'Background color' , menu = filemenu2)
filemenu2.add_command(label = 'Red' , command = red)
filemenu2.add_command(label = 'Blue', command = blue)
filemenu2.add_command(label = 'Cyan', command = cyan)
filemenu2.add_command(label = 'Green', command = green)
filemenu2.add_command(label = 'Orange', command = orange)
filemenu2.add_command(label = 'Yellow', command = yellow)
filemenu2.add_command(label = 'Purple', command = purple)
filemenu2.add_command(label = 'Violet', command = violet)
'''

def Github():
	webbrowser.open('https://github.com/arbi222/')

def Instagram():
	webbrowser.open('https://www.instagram.com/arbi.hamolli/')	


filemenu3 = Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'Contact Developer' , menu = filemenu3)
filemenu3.add_command(label = 'Github' , command = Github)
filemenu3.add_command(label = 'Instagram' , command = Instagram)


root.config(menu = menubar)

root.mainloop()