#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:59:32 2022

@author: evan
"""
import sys,shutil,cmd
from helpers.appinfo import appinfo

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Did not understand response -")

app = appinfo()

print("[Required Parameters]")

###

print("Preferred <filename>.desktop? ")
print("<< don't append '.desktop' >>")
lastuserin = input("app.filename > ")
if not (lastuserin==''):
    app.file["Filename"]=lastuserin


print("What is the name of your application?\n")
lastuserin = input("app.Name > ")
app.required["Name"]=lastuserin
print("_____________")


print("What is the path of your application? (use as short of an arg as possible, using ~ or ./ if preferred)\n")
lastuserin = input("app.Path > ")
if not (lastuserin[-1] == '/'):
    lastuserin = lastuserin + '/'
if (lastuserin == "/"):
    print("FYI, this is pointing to root ( / )")
app.required["Path"]=lastuserin

print("Inside that path, what command do you want to run? (quotes are safe)")
print(" >< " + app.required["Path"] + "%%%%%")
lastuserin = input("app.Exec > ")
if not (lastuserin==''):
    app.required["Exec"]=lastuserin

if yes_or_no("Execute inside a terminal?"):
    app.required["Terminal"] = "true"
else:
    app.required["Terminal"] = "false"    

print("\n[Optional Parameters]")
print("Keep a blank input to use default\n")

print("Comment/Short Descriptor? (def = "+app.optional["Comment"]+")")
lastuserin = input("app.Comment > ")
if not (lastuserin==''):
    app.optional["Comment"]=lastuserin

print("Keyword? (def = "+app.optional["Keywords"]+")")
lastuserin = input("app.Comment > ")
if not (lastuserin==''):
    app.optional["Keywords"]=lastuserin



app.tellMeEverything()
app.appendToFile()
input()
#shutil.copyfile("./template.desktop","./new.desktop")

