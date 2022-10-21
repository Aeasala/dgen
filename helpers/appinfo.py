#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:06:54 2022

@author: evan
"""
#this will be a dictionary showing each of the required and optional parameters for the .desktop file
import enum
class appinfo():
    file = {
        "Filename": "app"
        }
    required = {
        "Name": "Blank Desktop File",
        "Path": "~/",
        "Exec": "echo 'Your Desktop file is not complete'",
        "Type": "Application",
        "Terminal": "false"
        }
    optional = {
        "Comment": "Application",
        "Keywords": "Application"
        }
    manual = {
        "Categories": "Utility",
        "Icon": ""
        }
    def appendToFile(self):
        newDFile = open(self.file["Filename"]+".desktop","w")
        newDFile.write("[Desktop Entry]\n")
        for key, value in self.required.items() :
            newDFile.write(key+"="+value+"\n")
        for key, value in self.optional.items() :
            newDFile.write(key+"="+value+"\n")
        for key, value in self.manual.items() :
            newDFile.write(key+"="+value+"\n")
        newDFile.close()
    def tellMeEverything(self):
        for key, value in self.file.items() :
            print(key+"="+value)
        for key, value in self.required.items() :
            print(key+"="+value)
        for key, value in self.optional.items() :
            print(key+"="+value)
        for key, value in self.manual.items() :
            print(key+"="+value)
        