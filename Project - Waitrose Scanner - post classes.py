import sqlite3
import random
import tkinter as tk
from tkinter.constants import BOTTOM, TOP
from tkinter import *
import pandas as pd
from datetime import date
    # DataBase Creation Functions
def CreateUserDB():
    #only run once
    con = sqlite3.connect("Credentials.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Users
                (User_ID INTEGER PRIMARY KEY, PIN INTEGER, First_Name TEXT, Surname TEXT, Permissions TEXT, Locked_Out TEXT)
                ''')
    con.commit()
    print("DB CREATED!")

#def ProductSearch():    

def CreateProductDB():

    con = sqlite3.connect("Product.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Users
                (Product_ID INTEGER PRIMARY KEY, Product_Name TEXT, Price REAL, Stock_Total INTEGER, Aisle INTEGER, Block INTEGER, Shelf INTEGER, Sequence INTEGER)
                ''')
    con.commit()

def CreateRandomProducts():
    for i in range(500):
        location=random.randint(1,18)
        block=random.randint(1,6)
        shelf=random.randint(1,8)
        sequence=random.randint(1,5)
        stocktotal=random.randint(0,100)
        price=str(round(random.uniform(0.15,35.99),2))
        productint=str(i)
        Product_name="item"+productint
        SQLRandProd("Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence", Product_name, price, stocktotal, location, block, shelf, sequence)

def SQLRandProd(inputa, inputb, inputc, inputd, inpute, inputf, inputg, inputh, inputi, inputj, inputk, inputl, inputm, inputn):
    inputi=str("'"+(inputi)+"'")
    inputh=str("'"+(inputh)+"'")
    con = sqlite3.connect("Product.db")
    cur = con.cursor()
    cur.execute(f''' INSERT INTO Users({inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}) VALUES({inputh}, {inputi}, {inputj}, {inputk}, {inputl}, {inputm}, {inputn}) ''')
    con.commit()

def CreateWastageDB():
    con = sqlite3.connect("Wastage.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Products
                (Product_ID INTEGER PRIMARY KEY, Product_Name TEXT, Price REAL, Stock_Total INTEGER, User_ID INTEGER, Quantiy_Wasted INTEGER, Date_Wasted TEXT, Wastage_Reason TEXT)
                ''')
    con.commit()
    print("DB CREATED!")

def CreateLLDB():
    con = sqlite3.connect("LineLookup.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Users
                (User_ID INTEGER PRIMARY KEY, PIN INTEGER, First_Name TEXT, Surname TEXT)
                ''')
    con.commit()
    print("DB CREATED!")
#CreateUserDB()
#CreateProductDB()
#CreateRandomProducts()
#CreateWastageDB()


class MainMenu():
    def __init__(self):
        self.name=''          
        self.Username=''
        self.Permissions=''
        self.Attempts=0
        self.Startup()
        #output=self.GetAisleNumber("Product_ID", "Product_Name", "9520")
        #print(output)    
        #if self.Permissions == "Admin":
        #    self.AdminMainMenu()
        #else:
        #    self.UserMainMenu()
    
    def Checkifxexists(self,inputa, inputb, inputc):
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output=cur.fetchone()
        return output
    
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
    def LineLookup(self):
        print("Welcome to LineLookup!")
        #integerorstring=[int(product), str(product)]
        #for i in integerorstring:
        continue1=1
        while continue1==1:
            self.Lookupentry=input("Please enter the barcode number or the name of the product!")
            stringorint=self.integerorstring()
            if stringorint == 0:
                print("Your input was not valid")
                Lookupentry=input("Please enter the barcode number or the name of the product!")
            if stringorint == "string":
                string=self.stringorintegerans.lower()
                output=self.AllinColumnProduct("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence", "Product_Name", string)
                mapdisplay=input("Would you like to view this on the store map enter y or yes to view, or any key to continue.").lower()
                if mapdisplay =="yes" or mapdisplay == "y":
                    if __name__ == "__main__":    
                        print("Please close the window to continue!")
                        Aislenumber=self.GetAisleNumber("Aisle", "Product_Name", string)                   
                        app = StoreMap(int(Aislenumber[0]))
            if stringorint == "integer":
                integer=self.stringorintegerans
                output=self.AllinColumnProduct("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence", "Product_ID", integer)
            stop=input("Do you want to stop looking up? Enter y or yes, or to continue press any key").lower()
            if stop == "y" or stop == "yes":
                print("Returning to main menu!")
                return       
    def GetAisleNumber(self,inputa, inputb, inputc):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        #inputc="'"+inputc+"'"    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output = cur.fetchone()
        return output
    def integerorstring(self):
        integer=-1
        string="hey"
        valid=0
        while valid==0:
            try:
                val=int(self.Lookupentry)
                integer=val
            except ValueError:
                integer=0
            
            try:
                val=str(self.Lookupentry)
                string=val
            except ValueError:
                string=""
                
            if integer==0 and string=="":
                print("Input isn't Integer or String!")
                return 0
            if integer>0:
                self.stringorintegerans=integer
                valid=1
                return "integer"

            if string != "":
                self.stringorintegerans=string
                valid=1
                return "string"

        
        
            #print("That's not a string or an integer.")
    #This function is used by the Register Function when creating a new user to input them into the Credentials Database
    def InsertDataRegister(inputa,inputb,inputc,inputd,inpute,inputf, inputg, inputh):
        #inputd="'"+inputd+"'"
        inpute="'"+inpute+"'"
        inputf="'"+inputf+"'"
        inputg="'"+inputg+"'"
        inputh="'"+inputh+"'"
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()
        cur.execute(f''' INSERT INTO Users({inputa}, {inputb}, {inputc}, {inputd}) VALUES({inpute}, {inputf}, {inputg}, {inputh}) ''')
        con.commit()
    def Register(self,input21):
        print("PLEASE ADMIN/MANAGER, NOW HAND OVER TO USER!\n\n")
        F_Name=input("Please enter your First Name:\n\n")
        S_Name=input("Please enter your Surname:\n\n")
        PIN1=input("Please enter your PIN:\n\n")
        PIN2=input("Please enter your PIN\n\n")
        valid2=0
        while valid2==0:
            if PIN1==PIN2:
                valid2=1
            else:
                print("Your PINs did not match!")
                PIN1=input("Please enter your PIN:\n\n")
                PIN2=input("Please enter your PIN\n\n")
        continue1=0
        #check=input("Please confirm entered Details:\n\n First Name - " + F_Name + "\n\n Surname - " + S_Name + "\n\n PIN - " + str(PIN1) + "\n\n - Please press yes to change these or press any key to continue!").lower()
        while continue1==0:
            check=input("Please confirm entered Details:\n\n First Name - " + F_Name + "\n\n Surname - " + S_Name + "\n\n PIN - " + str(PIN1) + "\n\n - Please press yes to change these or press any other key to quit!").lower()
            correct=0
            if check=="y" or check=="yes":
                F_Name=input("Please enter your First Name:\n\n")
                S_Name=input("Please enter your Surname:\n\n")
                PIN1=(input("Please enter your PIN:\n\n"))
                PIN2=(input("Please enter your PIN\n\n"))
                valid2=0
                while valid2==0:
                    if PIN1==PIN2:
                        valid2=1
                    else:
                        print("Your PINs did not match!")
                        PIN1=(input("Please enter your PIN:\n\n"))
                        PIN2=(input("Please enter your PIN\n\n"))
            else:
                continue1=1
        print("PLEASE HAND BACK OVER TO THE ADMIN/MANAGER")
        adorus=input("Please enter a for admin or u for User to set the permissions for this user!")
        hashedpin=str(self.CalculateHash(PIN1))
        self.login()
        isadmin=0
        while isadmin==0:    
            if adorus == "a" or adorus == "A":
                valid1=0
                while valid1==0:
                    Username=input("Please enter your User ID!:\n\n")
                    exists1=self.ExistsValueUser("User_ID","User_ID",Username)
                    checker=""
                    Locked_out=self.Checkifxexists("Locked_Out", "User_ID", Username)
                    lockcheck=[]
                    for i in Locked_out:
                        lockcheck+=i
                        #print(i)
                    
                    if lockcheck[0] == "Y":
                        print("Sorry! Your account is Locked Out - Please Contact a Manager!")
                        return
                    for i in exists1:   #exists 1 calls function Exists value that looks for all the User ID's within the DB
                        checker+=str(i)
                    if checker == "":
                        print("Your User_ID was incorrect!")
                    else:
                        print("Your username was accepted!")
                        valid1=1
            
                valid2=0
                attempts=0
                while attempts < 5:
                    while valid2==0:
                        PIN_input=input("Please enter your PIN!:\n\n")
                        HashPIN=str(self.CalculateHash(PIN_input))
                        exists1=self.ExistsValuePIN("PIN", "PIN", HashPIN, "User_ID", Username)
                        checker1=""
                        for i in exists1:
                            checker1+=str(i)
                        if checker1 == "":
                            print("Your PIN was incorrect!")
                            attempts+=1
                            print("You have "+ str(5-attempts) + " attempts remaining")                
                            if attempts == 5:
                                print("You have exceeded the maxmum number of attempts!")
                                self.InsertInto("Locked_Out", "Yes", "User_ID", Username)
                        else:
                            print("Your PIN was accepted!")
                            valid2=1
                            Permscheck=self.Checkifxexists("Permissions", "User_ID", Username)
                            permans=[]
                            for i in Permscheck:
                                permans+=i
                            if permans[0] == "Admin":
                                print("Success!")
                                self.greeting(Username)
                            else:
                                print("Sorry you don't have the Sufficient Privilidges.")
                                
                            attempts==0
                            return attempts
        
        #    InsertDataRegister("PIN","First_Name", "Surname", "Permissions",hashedpin, F_Name, S_Name, "Admin")

        
        ID=self.ExistsValueUser("User_ID", "First_Name", "Ryan")
        output1=[]
        for row in ID:
            output1+=row
        length=len(output1)-1
        print("Your User ID is " + str(output1[length]))

    def AllinColumn(self,inputa, inputb, inputc, inputd):
        con = sqlite3.connect("Credentials.db")
        #cur = con.cursor()
        inputd="'"+inputd+"'"
        df=pd.read_sql_query(f'SELECT {inputa}, {inputb} FROM Users WHERE {inputc} = {inputd}', con)
        print(df)
        return

    def AllinColumnProduct(self, inputa, inputb, inputc, inputd, inpute, inputf, inputg, inputh, inputi, inputj):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        inputj="'"+inputj+"'"
        #cur.execute(f'SELECT {inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}, {inputh} FROM Users WHERE {inputi} = {inputj}')
        #output = cur.fetchone()
        df=pd.read_sql_query(f'SELECT {inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}, {inputh} FROM Users WHERE {inputi} = {inputj}', con)
        print(df)
        cur.close()
        return
    
    def CheckAllLockedOut(self):
        print("ATTENTION! These Users are Locked Out!")
        self.AllinColumn("User_ID", "First_Name", "Locked_Out", "Yes")

    #User Functions - Line Lookup, Wastage, Offsales

    def Wastage(self):
        print("Welcome to Wastage!")
        continue1=1
        while continue1==1:
            self.Lookupentry=input("Please enter the barcode number or the name of the product!")
            stringorint=self.integerorstring()
            if stringorint == 0:
                print("Your input was not valid")
                Lookupentry=input("Please enter the barcode number or the name of the product!")
            if stringorint == "string":
                string=self.stringorintegerans.lower()                                
                output=self.CheckString3i("Product_ID", "Product_Name", string)
                self.AllinColumnProduct("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence","Product_Name", string)
                if output != None:
                    continue1=0
                else:
                    print("Sorry this item doesn't exist! Please try again.")
            if stringorint == "integer":
                integer=self.stringorintegerans                              
                output=self.CheckNummber3i("Product_Name", "Product_ID", integer)
                self.AllinColumnProdNo("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence","Product_ID", integer)
                if output != None:
                    continue1=0
                    self.Wastage_Reason=input("Please selct your Wastage Reason by typing it's corresponding number!\n\n1) Damaged Product\n\n 2) Out of Date\n\n3) Product Stolen\n\n")
                    if self.Wastage_Reason==1:
                        self.WastageReason="Damaged Product"
                        self.WastageQuantity=input("Please enter the Number of items that need to be Wasted")
                        self.ItemReplaceNumber()
                else:
                    print("Sorry this item doesn't exist! Please try again.")

        
    def ItemReplaceNumber(self, inputa, inputb,):
        con=sqlite3.connect("Product.db")
        cur = con.cursor()
        inputa=inputa-self.WastageQuantity
        cur.execute(f''' UPDATE Users SET Stock_Total = {inputa} WHERE Product_ID = {inputb}''')
        cur.close()
        con=sqlite3.connect("Wastage.db")
        cur = con.cursor()
        cur.execute(f''' INSERT Users Users({"Product_ID"},{"Product_Name"}, {"Price"}, {"Stock_Total"}, {"User_ID"},{"Quantity_Wasted"}, {"Date_Wasted"}, {"Wastage_Reason"} VALUES({inputb}, {self.CheckNummber3i("Product_Name", "Product_ID", inputb)}, {self.CheckNummber3i("Price", "Product_ID", inputb)}, {self.CheckNummber3i("Stock_Total", "Product_ID", inputb)}, {self.Username}, {self.WastageQuantity}, {date.today()}, {self.WastageReason} ''')
        cur.close()
            
    # def AllinColumnWastage(self, inputa, inputb):
    #     con = sqlite3.connect("Product.db")
    #     cur = con.cursor()
    #     inputa="'"+inputa+"'"
    #     inputb="'"+inputb+"'"
    #     #cur.execute(f'SELECT {inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}, {inputh} FROM Users WHERE {inputi} = {inputj}')
    #     #output = cur.fetchone()
    #     df=pd.read_sql_query(f'SELECT {"Product_ID"}, {"Product_Name"}, {"Price"}, {"Stock_Total"}, {"User_ID"}, {"Quantity_Wasted"} FROM Users WHERE {inputa} = {inputb}', con)
    #     print(df)
    #     cur.close()
    #     return
    def CheckNummber3i(self,inputa, inputb, inputc):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output = cur.fetchone()
        return output
    def CheckString3i(self,inputa, inputb, inputc):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        inputc="'"+inputc+"'"    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output = cur.fetchone()
        return output
    def Offsales(self):
        print()
    def AllinColumnProdNo(self, inputa, inputb, inputc, inputd, inpute, inputf, inputg, inputh, inputi, inputj):
            con = sqlite3.connect("Product.db")
            cur = con.cursor()
            #cur.execute(f'SELECT {inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}, {inputh} FROM Users WHERE {inputi} = {inputj}')
            #output = cur.fetchone()
            df=pd.read_sql_query(f'SELECT {inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}, {inputh} FROM Users WHERE {inputi} = {inputj}', con)
            print(df)
            cur.close()
            return
    #def Wastage_Input(self, inputa, )
    #Admin Functions - Edit Product Database, Review Wastages, View Offsales

    def menu(self, Username):
        print("Hello")
        Username=input("Please enter your Username")
        if self.Checkifxexists("Permissions", "User_ID", Username) == "Admin":
            self.AdminMainMenu()
        else:
            self.UserMainMenu()


    def login(self):
        #self.Username=Username
        valid1=0
        while valid1==0:
            self.Username=input("Please enter your User ID!:\n\n")
            exists1=self.ExistsValueUser("User_ID","User_ID",self.Username)
            checker=""
            Locked_out=self.Checkifxexists("Locked_Out", "User_ID", self.Username)
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
        print(self.Permissions)
        if self.Attempts>=5:
            print("You're locked out!")
            return
        names=self.Checkifxexists("First_Name", "User_ID", self.Username)
        self.name=names[0]        
        valid2=1
        Permscheck=self.Checkifxexists("Permissions", "User_ID", self.Username)
        self.Permissions=Permscheck[0]
        if self.Permissions == "Admin":
            self.attempts==0
            self.AdminMainMenu()
            return
        else:
            self.attempts==0
            self.UserMainMenu()
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
        continue1=1
        while continue1==1:
            self.greeting()
            self.CheckAllLockedOut()
            selection=int(input("1) Line Lookup\n\n2) Wastage\n\n3) Offsales\n\n4) Logout\n\n5) Quit \n\n PLEASE PRESS THE CORRESPONDING NUMBER FOR YOUR MENU CHOICE!"))
            if selection == 1:
                self.LineLookup()
            if selection == 2:
                self.Wastage()
            if selection == 4:
                continue1=0
                print("Goodbye "+ self.name+"!")
                self.name=''          
                self.Username=''
                self.Permissions=''
                self.Attempts=0
            if selection == 5:
                exit()

    def UserMainMenu(self):
        print("hello")

    def Startup(self):
        continue1=1
        while continue1==1:
            self.main()
            choicelorr=input("Would you like to login or quit? To login please press any key or enter q or quit to quit.").lower()
            if choicelorr == "q" or choicelorr =="quit":
                return
            else:
                self.main()

class StoreMap(tk.Tk):
    def __init__(self, input1):
        super().__init__()
        self.title("Store Map")
        self.minsize(810, 520)
        self.resizable(width=False, height=False)
        self.topbar = tk.Frame(self, bg="green")
        self.text = tk.Label(self.topbar, text="Store Map", bg="green")
        self.window = tk.Frame(self, bg="white")
        self.topbar.pack(side=TOP, fill="x")
        self.text.pack(pady=(10, 5))
        #self.buttons(self.window)
        self.Back(self.window)
        self.StoreMap(self.window, input1)
        self.Front(self.window)
        self.mainloop()

    def buttons(self, root):
        root.columnconfigure(0, weight=3)
        root.columnconfigure(1, weight=1)
        self.button1 = tk.Button(root, text="button 1", command=self.command1)
        self.button2 = tk.Button(root, text="button 2")
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=2)
        
    def StoreMap(self,root, input1):
        self.canvas = Canvas(self,height=520,width=810,bg="#fff")            
        self.canvas.pack()
        aislenumber=input1
        for i in range(1,9):
            if i == aislenumber:
                self.canvas.create_rectangle(30+((i-1)*100),30,((i-1)*100)+80,240, outline="black", fill="#fb0")
            else:
                self.canvas.create_rectangle((((i-1)*100)+30),30,((((i-1)*100)+80)),240, outline="black")
        
        for i in range(10,18):
            if i == aislenumber:
                self.canvas.create_rectangle((30+((i-10)*100)),280,(((i-10)*100)+80),490, outline="black", fill="red")
            else:
                self.canvas.create_rectangle((30+((i-10)*100)),280,(((i-10)*100)+80),490, outline="black")
    def Back(self,root):
        self.resizable(width=False, height=False)
        self.topbar = tk.Frame(self)
        self.text = tk.Label(self.topbar, text="Back of Store")
        #self.window = tk.Frame(self, bg="white")
        self.topbar.pack(side=TOP, fill="x")
        self.text.pack(pady=(10, 5))
    def Front(self,root):
        self.resizable(width=False, height=False)
        self.topbar = tk.Frame(self)
        self.text = tk.Label(self.topbar, text="Front of Store")
        #self.window = tk.Frame(self, bg="white")
        self.topbar.pack(side=TOP, fill="x")
        self.text.pack(pady=(10, 5))  

    def command1(self):
        print("comand1")

app=MainMenu()

