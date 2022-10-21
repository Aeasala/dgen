#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:06:54 2022

@author: evan
"""
#this will be a dictionary showing each of the required and optional parameters for the .desktop file
import enum
class appinfo():
    required = {
        "Type": "Application",
        "Terminal": "false",
        "Exec": "echo 'Your Desktop file is not complete'",
        "Name": "Blank Desktop File",
        "Path": "~/"
        }
    optional = {
        "Icon": "",
        "Categories": ""
        }
    def appendToFile(self):
        newDFile = open("app.desktop","w")
        newDFile.write("[Desktop Entry]\n")
        for key, value in self.required.items() :
            newDFile.write(key+"="+value+"\n")
    def tellMeEverything(self):
        for key, value in self.required.items() :
            print(key+"="+value)