import sqlite3
import random
import tkinter as tk
from tkinter.constants import BOTTOM, TOP
from tkinter import *

def Checkifxexists(inputa, inputb, inputc):
    con = sqlite3.connect("Credentials.db")
    cur = con.cursor()    
    output = cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
    return output

class MainMenu():
    def __init__(self):
        self.name=''          #Checkifxexists("First_Name", "User_ID", 1)
        self.Username=''
        self.Permissions=''
        self.Attempts=0
        self.main()
        #if self.Permissions == "Admin":
        #    self.AdminMainMenu()
        #else:
        #    self.UserMainMenu()
    
    def ExistsValuePIN(self,inputa, inputb, inputc, inputd, inpute):
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()
        inputc="'"+inputc+"'"
        output = cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc} AND {inputd} = {inpute}')
        return output   
    
    def ExistsValueUser(self,inputa, inputb, inputc):
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()
        inputc="'"+inputc+"'"
        output = cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        return output  
    
    def CalculateHash(self,item):
        total=0
        for character in range(len(item)):
            total=total+ord(item[character])
        return total % 5000000
    def InsertInto(inputa, inputb, inputc, inputd):
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()    
        output = cur.execute(f'INSERT INTO USERS {inputa} VALUES({inputb} WHERE {inputc} = {inputd}')
        return output

    def login(self):
        valid1=0
        while valid1==0:
            self.Username=input("Please enter your User ID!:\n\n")
            exists1=self.ExistsValueUser("User_ID","User_ID",self.Username)
            checker=""
            Locked_out=Checkifxexists("Locked_Out", "User_ID", self.Username)
            lockcheck=[]
            for i in Locked_out:
                lockcheck+=i
                #print(i)
            
            if lockcheck[0] == "Y" or lockcheck[0]== "Yes":
                print("Sorry! Your account is Locked Out - Please Contact a Manager!")
                self.attempts=5
                return 
            else:
                print()
            for i in exists1:   #exists 1 calls function Exists value that looks for all the User ID's within the DB
                checker+=str(i)
            if checker == "":
                print("Your User_ID was incorrect!")
            else:
                print("Your username was accepted!")
                valid1=1

        valid2=0
        self.attempts=0
        while self.attempts < 5:
            while valid2==0:
                PIN_input=input("Please enter your PIN!:\n\n")
                HashPIN=str(self.CalculateHash(PIN_input))
                exists1=self.ExistsValuePIN("PIN", "PIN", HashPIN, "User_ID", self.Username)
                checker1=""
                for i in exists1:
                    checker1+=str(i)
                if checker1 == "":
                    print("Your PIN was incorrect!")
                    self.attempts+=1
                    print("You have "+ str(5-self.attempts) + " attempts remaining")                
                    if self.attempts == 5:
                        self.InsertInto("Locked_Out", "Yes", "User_ID", self.Username)
                        return 
                else:
                    print("Your PIN was accepted!")
                    return
                    # valid2=1
                    # Permscheck=Checkifxexists("Permissions", "User_ID", self.Username)
                    # permans=[]
                    # for i in Permscheck:
                    #     permans+=i
                    # if permans[0] == "Admin":
                    #     attempts==0
                    #     AdminMainMenu(self.Username)
                    # else:
                    #     attempts==0
                    #     UserMainMenu(self.Username)
                    #     return attempts
        
    def main(self):
        self.login()
        if self.Attempts>=5:
            print("You're locked out!")
            return
        names=Checkifxexists("First_Name", "User_ID", self.Username)
        namesall=[]
        for i in names:
            namesall+=i
        self.name=namesall[0]        
        valid2=1
        Permscheck=Checkifxexists("Permissions", "User_ID", self.Username)
        permans=[]
        for i in Permscheck:
            permans+=i
        if permans[0] == "Admin":
            self.attempts==0
            self.AdminMainMenu()
            return
        else:
            self.attempts==0
            self.UserMainMenu(self.Username)
            return 

    def greeting(self):
        #for character in "(,')":
        #    finishname = finishname.replace(character, '')
        #finishname=name1[0].replace('(','',"'",'',',','')
        if self.Permissions == "Admin":
            print("Hello", self.name, "You're an Admin!")
        else:
            print("Hello", self.name, "You're a User!")

    def AdminMainMenu(self):
        self.greeting()
        selection=int(input("1) Line Lookup\n\n2) Wastage\n\n3) Offsales\n\n PLEASE PRESS THE CORRESPONDING NUMBER FOR YOUR MENU CHOICE!"))
        if selection == 1:
            print()


    def UserMainMenu(self):
        print("hello")

    def Startup(self):
        choicelorr=input("Would you like to login or quit? To quit please press any key").lower()
        if choicelorr == "login":
            self.main()
        else:
            return
            
app=MainMenu()