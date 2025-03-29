from tkinter import *
from yt_dlp import YoutubeDL
from tkinter import filedialog , messagebox

def start():

	download_window = Toplevel()
	download_window.title('Mp3 Downloader')
	download_window.resizable(False , False)
	download_window.iconbitmap(r'download_music.ico')
	download_window.geometry('763x229+200+200')
	download_window.config(bg = 'cyan')
	
	
	first_label = Label(download_window , text = 'Music Downloader' , bg = 'RoyalBlue2' , fg = 'black' , width = 38 , height = 2 , font = ('arial',25,'bold'))
	first_label.grid(row = 1 , column = 1 , columnspan = 2)
	
	
	second_label = Label(download_window , text = 'Enter the link of the song below :' , bg = 'cyan' , fg = 'black' , width = 44 , height = 1 , font = ('arial',20,'bold'))
	second_label.grid(row = 2 , column = 1 , columnspan = 2)
	
	

	# creating paste menu , to paste the link on the entry field
	the_menu = Menu(download_window, tearoff=0)
	the_menu.add_command(label="Paste")


	def show_paste_menu(parameter):
		download_window = parameter.widget
		the_menu.entryconfigure("Paste",command=lambda: download_window.event_generate("<<Paste>>"))
		the_menu.tk.call("tk_popup", the_menu, parameter.x_root, parameter.y_root)

	
	def activate_entry_field(parameter):
		entry_field.configure(state = NORMAL)

		
	entry_field = Entry(download_window , bg = 'white' , fg = 'darkred' , borderwidth = 12 , width = 49 , justify = LEFT , font = ('arial',20,'bold'))
	entry_field.grid(row = 3 , column = 1 ,  columnspan = 2)
	entry_field.configure(state = DISABLED)
	entry_field.bind('<Button-1>' , activate_entry_field)
	entry_field.bind('<Button-3>' , activate_entry_field)
	entry_field.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_paste_menu)
		
	
	
	def download():
		if str(entry_field.get()) == '':
			messagebox.showwarning('Warning' , 'Please enter a link on the field !')
		else:
			directory=filedialog.askdirectory()
			ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3','preferredquality': '192',}],'outtmpl':directory + '/%(title)s.%(ext)s',}
			with YoutubeDL(ydl_opts) as ydl:
				 ydl.download([entry_field.get()])
			
				
	
	download_button = Button(download_window , text = 'Download' , bg = 'seagreen2' , fg = 'black' , width = 15 , height = 1 ,  font = ('arial',18,'bold') , command = download)
	download_button.grid(row = 5 , column = 2)
	
	
	
	
	def clearing():
		entry_field.delete(0 , END)
		entry_field.configure(state = DISABLED)
		
	
	clear_button = Button(download_window , text = 'Clear' , bg = 'lime green' , fg = 'black' , width = 15 , height = 1 ,  font = ('arial',18,'bold') , command = clearing)
	clear_button.grid(row = 5 , column = 1)
	
