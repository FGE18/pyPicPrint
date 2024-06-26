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
from tkinter import ttk

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
    :Parameters: none
    :Returns: none
    """
    about_message = config.get('APPLICATION', 'APP_NAME') + "\n\n"
    about_message += _("This application gives you the appropriate size for the best printing.\n\n")
    about_message += _("Developer: ")
    about_message += config.get('APPLICATION', 'APP_AUTHOR') + "\n\n"
    about_message += config.get('APPLICATION', 'APP_VERSION')
    showinfo(_('About'), message=about_message)


class Menu(tk.Menu):
    """
    Menu Creation for main application window
    """
    def __init__(self, parent):
        super().__init__(parent)

        # Icons application loading
        # camera_icon = tk.PhotoImage(file="./pictures/camera.png")
        # printer_icon = tk.PhotoImage(file="./pictures/printer.png")

        # Icons menu loading
        # Variables containing icon need to be set as global to be shown in Tkinter menu.
        # global menu_conf_icon
        # global menu_help_icon
        # global menu_quit_icon
        # menu_conf_icon = tk.PhotoImage(file="./pictures/menu-conf.png")
        # menu_help_icon = tk.PhotoImage(file="./pictures/menu-help.png")
        # menu_quit_icon = tk.PhotoImage(file="./pictures/menu-quit.png")

        # Menu creation
        app_menu = tk.Menu(self)
        self.add_cascade(label=_('Application'), menu=app_menu)
        app_menu.add_command(label=_('Configuration'), compound='left', command=lambda: ConfWin(self))
        app_menu.add_separator()
        app_menu.add_command(label = _('Quit'), compound = 'left', command = self.quit)
        help_menu = tk.Menu(self)
        self.add_cascade(label=_('Help'), menu=help_menu)
        help_menu.add_command(label=_('About'), compound='left', command=about)

        # self.sAppMenu = tk.Menu(self.appMenu)
        # self.appMenu.add_cascade(label=_('Application'), menu=self.sAppMenu)
        # # self.sAppMenu.add_command(label=_('Configuration'), image=menu_conf_icon, compound='left', command=lambda: ConfWin(unit))
        # self.sAppMenu.add_command(label=_('Configuration'), compound='left', command=lambda: ConfWin(unit))
        # self.sAppMenu.add_separator()
        # # self.sAppMenu.add_command(label=_('Quit'), image=menu_quit_icon, compound='left', command=self.quit)
        # self.sAppMenu.add_command(label=_('Quit'), compound='left', command=self.quit)
        # self.sHelpMenu = tk.Menu(self.appMenu)
        # self.appMenu.add_cascade(label=_('Help'), menu=self.sHelpMenu)
        # # self.sHelpMenu.add_command(label=_('About'), image=menu_help_icon, compound='left', command=about)
        # self.sHelpMenu.add_command(label=_('About'), compound='left', command=about)


# Class for GUI
class Application(tk.Tk):

    def __init__(self):
        """
        Initialize application in a tkinter window.
        """
        super().__init__()
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        self.geometry("600x400")
        self.title(config.get('APPLICATION', 'APP_NAME'))
        self.iconbitmap('./pictures/camera.ico')

        # Variables definition
        self.definition = tk.IntVar()
        self.definition.set(printing.LOW_DEFINITION)
        self.error_msg_height = tk.StringVar()
        self.error_msg_width = tk.StringVar()
        self.my_pic_height = tk.StringVar()
        self.my_pic_width = tk.StringVar()
        self.result_msg = tk.StringVar()

        # Form creation
        frm_form=tk.Frame(self)
        tk.Label(frm_form, text=_("Original picture information"), font=("Arial Bold", 12), foreground="midnight blue").grid(row=1, column=2)
        tk.Label(frm_form, text=_("Height (pixel):"), font=("Arial Bold", 10), foreground="midnight blue").grid(row=3, column=1)
        tk.Label(frm_form, text=_("Width (pixel):"), font=("Arial Bold", 10), foreground="midnight blue").grid(row=5, column=1)
        tk.Entry(frm_form, width=10, textvariable=self.my_pic_height, validatecommand=self.height_validation, validate="focusout").grid(row=3, column=2)
        tk.Entry(frm_form, width=10, textvariable=self.my_pic_width, validatecommand=self.width_validation, validate="focusout").grid(row=5, column=2)
        tk.Label(frm_form, textvariable=self.error_msg_height, font=("Arial Bold", 10), foreground="red").grid(row=3, column=3)
        tk.Label(frm_form, textvariable=self.error_msg_width, font=("Arial Bold", 10), foreground="red").grid(row=5, column=3)
        tk.Label(frm_form, text=_("Printing definition"), font=("Arial Bold", 12), foreground="dark green").grid(row=6, column=2)
        tk.Radiobutton(frm_form, text=_("Low (") + str(printing.LOW_DEFINITION) + _(" dpi)"), foreground="dark green", variable=self.definition, value=printing.LOW_DEFINITION).grid(row=7, column=1, sticky=tk.W)
        tk.Radiobutton(frm_form, text=_("Standard (") + str(printing.STANDARD_DEFINITION) + _(" dpi)"), foreground="dark green", variable=self.definition, value=printing.STANDARD_DEFINITION).grid(row=8, column=1, sticky=tk.W)
        tk.Radiobutton(frm_form, text=_("High (") + str(printing.HIGH_DEFINITION) + _(" dpi)"), foreground="dark green", variable=self.definition, value=printing.HIGH_DEFINITION).grid(row=9, column=1, sticky=tk.W)
        tk.Button(frm_form, text=_('Submit'), command=lambda: self.display_optimal_print_size(self.my_pic_height.get(), self.my_pic_width.get(), self.definition.get(), config.get('USER', 'USER_UNIT'))).grid(row=15, column=2, sticky=tk.W)
        frm_form.grid(row=1, column=1)
        ttk.Separator(self, orient='horizontal').grid(row=17, sticky="ew", columnspan=3, pady=10)
        frm_result=tk.Frame(self, bd=1)
        tk.Label(frm_result, textvariable=self.result_msg).grid(row=1, column=1)
        frm_result.grid(row=20, column=1)

    def height_validation(self)->bool:
        """
        This function checks if height entry is valid (positive integer) or not.
        :return: bool True if entry is valid and False if entry is empty or not valid.
        """
        e_height = self.my_pic_height.get()
        if e_height:
            if e_height.isdigit() and int(e_height) > 0:
                self.error_msg_height.set("")
                return True
            else:
                self.error_msg_height.set(_("Invalid entry!"))
                return False
        else:
            self.error_msg_height.set(_("Entry is empty!"))
            return False


    def width_validation(self)->bool:
        """
        This function checks if width entry is valid (positive integer) or not.
        :return: bool True if entry is valid and False if entry is empty or not valid.
        """
        e_width = self.my_pic_width.get()
        if e_width:
            if e_width.isdigit() and int(e_width) > 0:
                self.error_msg_width.set("")
                return True
            else:
                self.error_msg_width.set(_("Invalid entry!"))
                return False
        else:
            self.error_msg_width.set(_("Entry is empty!"))
            return False


    def display_optimal_print_size(self, f_height: int, f_width: int, f_def: int, f_unit: str):
        """This method computes optimal print size with values entered in parameters and set result_msg value. This
        value is displayed in bottom of windows (in frm_result frame).
        :Parameters: f_height -- Integer containing image height
        :Parameters: f_width -- Integer containing image width
        :Parameters: f_def -- Integer containing printing definition
        :Parameters: f_unit -- String containing unit
        :Returns: None
        """
        my_pic = picture.Picture(f_height, f_width)
        info_msg = _("Optimal size printing at ") + str(f_def) + _(" dpi is:") + "\n\n"
        info_msg += str(my_pic.get_optimal_print_width(f_def, f_unit)) + f_unit + _(" x ") + str(
            my_pic.get_optimal_print_height(f_def, f_unit)) + f_unit
        self.result_msg.set(info_msg)


class ConfWin(tk.Toplevel):
    """
    This class displays a new window to manage configuration settings.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("320x200")
        self.title(_("Configuration page"))
        self.iconbitmap('./pictures/config.ico')
        self.c_unit = config.get('USER', 'USER_UNIT')
        self.grab_set()

        # Unit form creation
        radio_unit = tk.StringVar()
        radio_unit.set(self.c_unit)
        tk.Label(self, text=_("Unit configuration value"), font=("Arial Bold", 12), foreground="midnight blue").grid(row=1, column=2)
        tk.Radiobutton(self, text=_("Centimeter"), foreground="dark green", variable=radio_unit, value="CM").grid(row=7, column=1, sticky=tk.W)
        tk.Radiobutton(self, text=_("Inch"), foreground="dark green", variable=radio_unit, value="IN").grid(row=8, column=1, sticky=tk.W)
        tk.Button(self, text=_('Save'), command=lambda:self.save_unit_conf(radio_unit.get())).grid(row=15, column=1, sticky=tk.W)
        tk.Button(self, text=_('Cancel'), command=self.destroy).grid(row=15, column=2, sticky=tk.W)


    @staticmethod
    def save_unit_conf(val:str):
        """
        This method save unit value entered in parameter in application configuration in file in its section.
        :param val: String containing Unit (only CM/IN)
        :return: tkinter message box confirmation.
        """
        config.set('USER', 'USER_UNIT', val)
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
        change_msg=_("Parameter has been set to: ") + val
        showinfo(_('Result'), message=change_msg)
        config.read('config.cfg')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
