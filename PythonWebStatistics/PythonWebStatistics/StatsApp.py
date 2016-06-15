import tkinter as tk
from tkinter import font

class StatsApp(object):
    """tkinter GUI for this application"""

    def __init__(self, window):
        #set up font
        self.app_font = font.Font(family="Helvetica", size=12)
        #header
        header = tk.Label(text = 'Lake Pend Oreille Statistics', borderwidth = 5)
        header.pack(fill = 'x')

        #small buttons to make font bigger/smaller
        font_buttons_frame = tk.Frame(window, height = 200)
        font_buttons_frame.pack(expand = False, side = 'top', anchor = 'ne')
        bigger = tk.Button(font_buttons_frame, text="+", width = 2, command = self.make_font_bigger)
        smaller = tk.Button(font_buttons_frame, text="-", width = 2, command = self.make_font_smaller)
        smaller.pack(side = 'right')
        bigger.pack(side = 'right')

        #side bar
        side_bar = tk.Frame(window, bg = 'white', height = 400, relief = 'sunken', borderwidth = 1)
        side_bar.pack(expand = False, fill = 'both', side = 'left', anchor = 'nw')

        #side_bar with data query set up
        year_label = tk.Label(side_bar, text = 'Year:', bg = 'white', font = self.app_font)
        year_entry = tk.Entry(side_bar, relief = 'sunken')
        month_label = tk.Label(side_bar, text = 'Month:', bg = 'white', font = self.app_font)
        month_entry = tk.Entry(side_bar, relief = 'sunken')
        day_label = tk.Label(side_bar, text = 'Day:', bg = 'white', font = self.app_font)
        day_entry = tk.Entry(side_bar, relief = 'sunken')
        year_label.grid(row = 0, column = 0, sticky = 'e')
        year_entry.grid(row = 0, column = 1)
        month_label.grid(row = 1, column = 0, sticky = 'e')
        month_entry.grid(row = 1, column = 1)
        day_label.grid(row = 2, column = 0, sticky = 'e')
        day_entry.grid(row = 2, column = 1)

    
        #main area
        main_area = tk.Frame(window, bg = 'grey', width = 600, height = 400)
        main_area.pack(expand = True, fill = 'both', side = 'right') 

        window.update_idletasks()
        #positioning window
        scrn_width = window.winfo_screenwidth()
        scrn_height = window.winfo_screenheight()
        win_width, win_height = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
        pos_x = scrn_width//2 - (win_width-200)
        pos_y = scrn_height//2 - win_height
        window.geometry('{}x{}+{}+{}'.format(win_width, win_height,pos_x,pos_y))

    def make_font_bigger(self):
        '''Make the font a point bigger'''
        size = self.app_font['size']
        self.app_font.configure(size = size+1)

    def make_font_smaller(self):
        '''Make the font 1 point smaller'''
        size = self.app_font['size']
        self.app_font.configure(size=size-1)

