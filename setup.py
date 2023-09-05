from distutils.core import setup
import py2exe

# Libraries inclusions
import configparser
import gettext
import locale
import os
import tkinter as tk
from tkinter import Tk, Label, Menu, Button, Text, Entry
from tkinter.messagebox import showinfo

# App import
import picture
import printing

setup(
    options={'py2exe': {'bundle_files': 0, 'compressed': True}},
    windows=[{'script': "main.py"}],
    zipfile=None,
)

# python setup.py py2exe