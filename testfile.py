import sqlite3
import random
import tkinter as tk
from tkinter.constants import BOTTOM, TOP
from tkinter import *
from datetime import date

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
    
    def main(self):
        print()
        app=Wastage()
            
app=MainMenu()

class Wastage():
    def __init__(self):
        self.Product_ID=0
        self.Product_Name=""
        self.main()
    def main(self):
        print("Welcome to Wastage!")
        self.continue1=1
        while self.continue1==1:
            self.WastageDataInputs()
            if self.stringorint == 0:
                print("Your input was not valid")
                Lookupentry=input("Please enter the barcode number or the name of the product!")
            if self.stringorint == "string":
                self.Product_Name=self.stringorintegerans.lower()
                self.Product_Name="'"+self.Product_Name+"'"
                self.AllinColumnProduct("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence","Product_Name", self.Product_Name)
                self.ProductID=self.CheckString3i("Product_ID", "Product_Name", self.Product_Name)
                self.ProductID=self.ProductID[0]
                if self.Product_ID != None:
                    self.WastageReasonDecision()
                else:
                    print("Sorry this item doesn't exist! Please try again.")
            if self.stringorint == "integer":
                self.Product_ID=self.stringorintegerans                              
                self.ProductName=self.CheckNummber3i("Product_Name", "Product_ID", self.Product_ID)
                self.AllinColumnProdNo("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence","Product_ID", self.Product_ID)
                self.Product_Name="'"+self.Product_Name+"'"
                if self.ProductName != None:
                    self.WastageReasonDecision()

                else:
                    print("Sorry this item doesn't exist! Please try again.")
    def WastageDataInputs(self):
        self.Lookupentry=input("Please enter the barcode number or the name of the product!")
        self.stringorint=self.integerorstring()
        print(self.stringorint)      

    def WastageReasonDecision(self):
        self.WastageReasonInput=int(input("Please selct your Wastage Reason by typing it's corresponding number!\n\n1) Damaged Product\n\n 2) Out of Date\n\n3) Product Stolen\n\n"))
        valid1=0
        while valid1==0:
            if self.WastageReasonInput==1:
                self.WastageReason="Damaged Product"
            elif self.WastageReasonInput==2:
                self.WastageReason="Out of Date"
            elif self.WastageReasonInput==3:
                self.WastageReason=="Product Stolen"
            else: 
                print("Please enter a Valid Response!")
                self.WastageReasonInput=int(input("Please selct your Wastage Reason by typing it's corresponding number!\n\n1) Damaged Product\n\n 2) Out of Date\n\n3) Product Stolen\n\n"))
            valid1=1
        self.ConfirmWastage()
    
    def ConfirmWastage(self):
        self.WastageQuantity=input("Please enter the Number of items that need to be Wasted")
        print("Please check the validity of the data below before it's submitted!")
        self.Product_Name=self.Product_Name[0]                       
        print("ProductID: " + str(self.Product_ID))
        print("ProductName: " + self.Product_Name)
        print("Wastage Quantity: " + str(self.WastageQuantity))
        print("Wastage Reason: " + self.WastageReason)
        valid1=input("Is any of the above data incorrect? If yes please enter yes or y").lower()
        if valid1 == "yes" or valid1 == "y":
            self.WastageDataInputs()
        else:
            self.ItemReplaceNumber()
            self.continue1=0

    def ItemReplaceNumber(self):
        con=sqlite3.connect("Product.db")
        cur = con.cursor()
        print(self.CheckNummber3i("Stock_Total", "Product_ID", self.Product_ID))
        inputa=self.CheckNummber3i("Stock_Total", "Product_ID", self.Product_ID)
        inputa=int(inputa[0])-int(self.WastageQuantity)
        if inputa < 0:
            self.WastageQuantity=int(self.WastageQuantity)+inputa
            print("Wastage Quantity adjusted as Wastage Quantity is greater than remaining stock!")
            inputa=0                
        cur.execute(f''' UPDATE Users SET Stock_Total = {inputa} WHERE Product_ID = {self.Product_ID}''')
        con.commit()
        con.close()
        con=sqlite3.connect("Wastage.db")
        cur = con.cursor()
        #print(Product_Name)
        Stock_Total=self.CheckNummber3i("Stock_Total", "Product_ID", self.Product_ID)
        Stock_Total=int(Stock_Total[0])
        print(Stock_Total)
        print(self.Product_ID)
        Price=self.CheckNummber3i("Price", "Product_ID", self.Product_ID)
        Price=int(Price[0])
        print(Price)
        print(self.Username)
        print(self.WastageQuantity)
        print(self.WastageReason)        
        Product_Name="'"+self.Product_Name+"'"
        self.WastageReason="'"+self.WastageReason+"'"
        cur.execute(f''' INSERT INTO Products({"Product_ID"}, {"Product_Name"}, {"Price"}, {"Stock_Total"}, {"User_ID"}, {"Quantity_Wasted"}, {"Date_Wasted"}, {"Wastage_Reason"}) VALUES({self.Product_ID}, {Product_Name}, {Price}, {Stock_Total}, {self.Username}, {self.WastageQuantity}, {date.today()}, {self.WastageReason}) ''')
        con.commit()
        con.close()
        #cur.close()

class SQLCommands():
    def __init__():
        print()
    
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
                        Aislenumber=self.GetAisleNumberSTR("Aisle", "Product_Name", string)                   
                        app = StoreMap(int(Aislenumber[0]))
            if stringorint == "integer":
                integer=self.stringorintegerans
                output=self.AllinColumnProdNo("Product_ID", "Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence", "Product_ID", integer)
                mapdisplay=input("Would you like to view this on the store map enter y or yes to view, or any key to continue.").lower()
                if mapdisplay =="yes" or mapdisplay == "y":
                    if __name__ == "__main__":    
                        print("Please close the window to continue!")
                        Aislenumber=self.GetAisleNumberINT("Aisle", "Product_Name", integer)                   
                        StoreMap.Main(int(Aislenumber[0]))
            stop=input("Do you want to stop looking up? Enter y or yes, or to continue press any key").lower()
            if stop == "y" or stop == "yes":
                print("Returning to main menu!")
                return       
    def GetAisleNumberINT(self,inputa, inputb, inputc):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        #inputc="'"+inputc+"'"    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output = cur.fetchone()
        return output
    def GetAisleNumberSTR(self,inputa, inputb, inputc):
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        inputc="'"+inputc+"'"    
        cur.execute(f'SELECT {inputa} FROM Users WHERE {inputb} = {inputc}')
        output = cur.fetchone()
        return output
    

class CreateDB():
    def __init__(self):
        self.CreateUserDB()
        self.CreateProductDB()
        self.CreateRandomProducts()
        self.CreateWastageDB()
        self.CreateLLDB()

    def CreateUserDB(self):
        #only run once
        con = sqlite3.connect("Credentials.db")
        cur = con.cursor()

        cur.execute('''CREATE TABLE Users
                    (User_ID INTEGER PRIMARY KEY, PIN INTEGER, First_Name TEXT, Surname TEXT, Permissions TEXT, Locked_Out TEXT)
                    ''')
        con.commit()
        print("DB CREATED!")

    def CreateProductDB(self):

        con = sqlite3.connect("Product.db")
        cur = con.cursor()

        cur.execute('''CREATE TABLE Users
                    (Product_ID INTEGER PRIMARY KEY, Product_Name TEXT, Price REAL, Stock_Total INTEGER, Aisle INTEGER, Block INTEGER, Shelf INTEGER, Sequence INTEGER)
                    ''')
        con.commit()

    def CreateRandomProducts(self):
        for i in range(500):
            location=random.randint(1,18)
            block=random.randint(1,6)
            shelf=random.randint(1,8)
            sequence=random.randint(1,5)
            stocktotal=random.randint(0,100)
            price=str(round(random.uniform(0.15,35.99),2))
            productint=str(i)
            Product_name="item"+productint
            self.SQLRandProd("Product_Name", "Price", "Stock_Total", "Aisle", "Block", "Shelf", "Sequence", Product_name, price, stocktotal, location, block, shelf, sequence)

    def SQLRandProd(self,inputa, inputb, inputc, inputd, inpute, inputf, inputg, inputh, inputi, inputj, inputk, inputl, inputm, inputn):
        inputi=str("'"+(inputi)+"'")
        inputh=str("'"+(inputh)+"'")
        con = sqlite3.connect("Product.db")
        cur = con.cursor()
        cur.execute(f''' INSERT INTO Users({inputa}, {inputb}, {inputc}, {inputd}, {inpute}, {inputf}, {inputg}) VALUES({inputh}, {inputi}, {inputj}, {inputk}, {inputl}, {inputm}, {inputn}) ''')
        con.commit()

    def CreateWastageDB(self):
        con = sqlite3.connect("Wastage.db")
        cur = con.cursor()

        cur.execute('''CREATE TABLE Products
                    (Wastage_ID INTEGER PRIMARY KEY, Product_ID INTEGER, Product_Name TEXT, Price REAL, Stock_Total INTEGER, User_ID INTEGER, Quantity_Wasted INTEGER, Date_Wasted TEXT, Wastage_Reason TEXT)
                    ''')
        con.commit()
        print("DB CREATED!")

    def CreateLLDB(self):
        con = sqlite3.connect("LineLookup.db")
        cur = con.cursor()

        cur.execute('''CREATE TABLE Users
                    (User_ID INTEGER PRIMARY KEY, PIN INTEGER, First_Name TEXT, Surname TEXT)
                    ''')
        con.commit()
        print("DB CREATED!")
                  
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
