#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries inclusions
import configparser
import gettext
import locale
import os
import sys
import tkinter as tk
from tkinter.messagebox import showinfo

# App import
import picture
import printing

# Read configuration
config = configparser.ConfigParser()
config.read('config.cfg')

# Internationalization
gettext.bindtextdomain('ppp', './languages/')
gettext.textdomain('ppp')
_ = gettext.gettext
lang = locale.getdefaultlocale()

# Needed to use Gettext on a Windows environment
if sys.platform.startswith('win'):
    import locale
    if os.getenv('LANG') is None:
        lang, enc = locale.getdefaultlocale()
        os.environ['LANG'] = lang

def about():
    """This function displays information from "About menu entry
    Parameters: none
    Returns: void
    """
    about_message = config.get('APPLICATION', 'APP_NAME') + "\n\n"
    about_message += _("This application gives you the appropriate size for the best printing.\n\n")
    about_message += _("Developer: ")
    about_message += config.get('APPLICATION', 'APP_AUTHOR') + "\n\n"
    about_message += config.get('APPLICATION', 'APP_VERSION')
    showinfo(_('About'), message=about_message)


def configure():
    """This function displays configuration from "Configuration" menu entry
    Parameters: none
    Returns: void
    """
    config_message = _("Configuration page") +"\n\n"
    config_message += _("Unit of length: ") + config.get('USER', 'USER_UNIT') + "\n"
    config_message += _("Coming soon...")
    showinfo(_('Configuration page'), message=config_message)


def show_optimal_print_size(f_height, f_width, f_def, f_unit):
    """This function displays information about optimal size printing in an infobox.
    Parameters: f_height -- Integer containing image height
    Parameters: f_width -- Integer containing image width
    Parameters: f_def -- Integer containing printing definition
    Parameters: f_unit -- String containing unit
    Returns: void
    """
    my_pic = picture.Picture(f_height, f_width)
    info_msg = _("Optimal size printing at ") + str(f_def) + _(" dpi is:") + "\n\n"
    info_msg += str(my_pic.get_optimal_print_width(f_def, f_unit)) + f_unit + _(" x ") + str(my_pic.get_optimal_print_height(f_def, f_unit)) + f_unit
    showinfo(_('Optimal size printing'), message=info_msg)


# Class for GUI
class Application(tk.Tk):




    def __init__(self):
        tk.Tk.__init__(self)
        self.sAppMenu = None
        self.sHelpMenu = None
        self.appMenu = None
        self.create_window()

    def create_window(self):
        # Variables definition
        my_pic_height = tk.StringVar()
        my_pic_width = tk.StringVar()
        definition = tk.IntVar()
        unit = config.get('USER', 'USER_UNIT')

        # Icons application loading
        camera_icon = tk.PhotoImage(file="./pictures/camera.png")
        printer_icon = tk.PhotoImage(file="./pictures/printer.png")

        # Icons menu loading
        # Variables containing icon need to be set as global to be shown in Tkinter menu.
        global menu_conf_icon
        global menu_help_icon
        global menu_quit_icon
        menu_conf_icon = tk.PhotoImage(file="./pictures/menu-conf.png")
        menu_help_icon = tk.PhotoImage(file="./pictures/menu-help.png")
        menu_quit_icon = tk.PhotoImage(file="./pictures/menu-quit.png")

        # Titlebar icon
        self.iconphoto(False, printer_icon)

        # Menu creation
        self.appMenu = tk.Menu(self)
        self['menu'] = self.appMenu

        self.sAppMenu = tk.Menu(self.appMenu)
        self.appMenu.add_cascade(label=_('Application'), menu=self.sAppMenu)
        self.sAppMenu.add_command(label=_('Configuration'), image=menu_conf_icon, compound='left', command=configure)
        self.sAppMenu.add_separator()
        self.sAppMenu.add_command(label=_('Quit'), image=menu_quit_icon, compound='left', command=self.quit)
        self.sHelpMenu = tk.Menu(self.appMenu)
        self.appMenu.add_cascade(label=_('Help'), menu=self.sHelpMenu)
        self.sHelpMenu.add_command(label=_('About'), image=menu_help_icon, compound='left', command=about)

        # Form creation
        tk.Label(self, text=_("Original picture information"), font=("Arial Bold", 12), foreground="midnight blue").grid(row=1, column=2)
        tk.Label(self, text=_("Height (pixel):"), font=("Arial Bold", 10), foreground="midnight blue").grid(row=3, column=1)
        tk.Label(self, text=_("Width (pixel):"), font=("Arial Bold", 10), foreground="midnight blue").grid(row=5, column=1)
        tk.Entry(self, width=10, textvariable=my_pic_height).grid(row=3, column=2)
        tk.Entry(self, width=10, textvariable=my_pic_width).grid(row=5, column=2)
        tk.Label(self, text=_("Printing definition"), font=("Arial Bold", 12), foreground="dark green").grid(row=6, column=2)
        tk.Radiobutton(self, text=_("Low (") + str(printing.LOW_DEFINITION) + _(" dpi)"), foreground="dark green", variable=definition, value=printing.LOW_DEFINITION).grid(row=7, column=1, sticky=tk.W)
        tk.Radiobutton(self, text=_("Standard (") + str(printing.STANDARD_DEFINITION) + _(" dpi)"), foreground="dark green", variable=definition, value=printing.STANDARD_DEFINITION).grid(row=8, column=1, sticky=tk.W)
        tk.Radiobutton(self, text=_("High (") + str(printing.HIGH_DEFINITION) + _(" dpi)"), foreground="dark green", variable=definition, value=printing.HIGH_DEFINITION).grid(row=9, column=1, sticky=tk.W)
        tk.Button(self, text=_('Submit'), command=lambda: show_optimal_print_size(my_pic_height.get(), my_pic_width.get(), definition.get(), unit)).grid(row=15, column=2, sticky=tk.W)


if __name__ == "__main__":
    app = Application()
    app.geometry("600x400")
    # app.configure(bg="light salmon")
    app.title(config.get('APPLICATION', 'APP_NAME'))
    app.mainloop()
