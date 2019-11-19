#!/usr/bin/env python3

from tkinter import *
from .PlaceHolder import PlaceHolder

class PlaceHolderEntry(Entry, PlaceHolder):
    def __init__(self, parent, placeholder, **kw):
        Entry.__init__(self, parent, **kw)
        self.var = self["textvariable"] = StringVar()
        PlaceHolder.__init__(self, placeholder)