#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:59:32 2022

@author: evan
"""
import sys,shutil,cmd
from helpers.appinfo import appinfo

app = appinfo()

print("What is the name of your application?\n")

lastuserin = input("app.Name > ")
app.required["Name"]=lastuserin
print("_____________")
print("What is the path of your application? (use as short of an arg as possible, using ~ or ./ if preferred)\n")

lastuserin = input("app.Path > ")
app.required["Path"]=lastuserin

print("Inside that path, what command do you want to run? (quotes are safe)")

lastuserin = input("app.Exec > ")
app.required["Exec"]=lastuserin

app.tellMeEverything()
app.appendToFile()
input()
#shutil.copyfile("./template.desktop","./new.desktop")
