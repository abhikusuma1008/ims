from tkinter import *
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math

class Application():
    def __init__(self,master,*args,**kwargs):
        self.master=master

        self.left=Frame(master,width=750,height=768,bg='SkyBlue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=500, height=500, bg='white')
        self.right.pack(side=RIGHT)


        #components
        self.heading=Label(self.left,text="NEEDS AND DEEDS STORE",font=('ALGERIAN 40 bold'),fg='Black')
        self.heading.place(x=100,y=10)
        
        self.date_l=Label(self.right,text="Date: "+str(datetime),font=('Calibri 18 bold'),fg='black')
        self.date_l.place(x=140,y=0)

        #table invoice=======================================================
        self.tproduct=Label(self.right,text="Products",font=('Calibri 20 bold'),fg='Black')
        self.tproduct.place(x=0,y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('Calibri 20 bold'),fg='Black')
        self.tquantity.place(x=150, y=60)

        self.tamount = Label(self.right, text="Price", font=('Calibri 20 bold'), fg='Black')
        self.tamount.place(x=300, y=60)

        #enter stuff
        self.enterid=Label(self.left,text="ID Number",font=('calibri 20 bold'),fg='black')
        self.enterid.place(x=50,y=80)


        self.enteride=Entry(self.left,width=25,font=('Calibri 18 bold'),bg='lightblue')
        self.enteride.place(x=220,y=80)
        self.enteride.focus()

        #button
        self.search_btn=Button(self.left,text="Find",width=18,height=2,bg='green',command=self.ajax)
        self.search_btn.place(x=580,y=70)
        #fill it later by the fuction ajax

        self.productname=Label(self.left,text="",font=('Calibri 27 bold'),bg='white',fg='steelblue')
        self.productname.place(x=0,y=200)

        self.pprice = Label(self.left, text="", font=('Calibri 27 bold'), bg='white', fg='steelblue')
        self.pprice.place(x=0, y=250)

        #total label
        self.total_l=Label(self.right,text="",font=('arial 40 bold'),bg='lightblue',fg='white')
        self.total_l.place(x=0,y=400)
    def ajax(self,*args,**kwargs):
        self.conn = mysql.connector.connect(host='localhost',user='root',password='Sreethu@12345',database='inventory_system',port=3306)
        self.get_id=self.enteride.get()
    #get the product info with that id and fill i the labels above
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("SELECT * FROM inventory WHERE id= %s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        if self.pc:
            for self.r in self.pc:
                self.get_id=self.r[0]
                self.get_name=self.r[1]
                self.get_price=self.r[3]
                self.get_stock=self.r[2]
                
            self.productname.configure(text="Product's Name: " +str(self.get_name),fg='black',bg='white',font=('calibri,20,bold'))
            self.productname.place(x=50,y=200)
            #self.pprice.configure(text="Cost of the product:"+str(self.get_price),fg='black')


    #craete the quantity and the discount label
            self.quantityl=Label(self.left,text="Enter the qty ",font=('Calibri 18 bold'),fg='black',bg='white')
            self.quantityl.place(x=0,y=300)

            self.quantity_e=Entry(self.left,width=10,font=('Calibri 18 bold'),bg='lightblue')
            self.quantity_e.place(x=170,y=300)
            self.quantity_e.focus()

    #discount
            self.discount_l = Label(self.left, text="Discount offered", font=('Calibri 20 bold'),fg='black',bg='white')
            self.discount_l.place(x=320, y=300)


            self.discount_e = Entry(self.left, width=10, font=('Calibri 20 bold'), bg='lightblue')
            self.discount_e.place(x=530, y=300)
            self.discount_e.insert(END,0)


    #add to cart button
            self.add_to_cart_btn = Button(self.left, text="Display on the bill receipt", width=40, height=2, bg='green',command=self.add_to_cart)
            self.add_to_cart_btn.place(x=200, y=370)

    #genrate bill and change
            self.change_l=Label(self.left,text="Enter the amount paid",font=('Calibri 20 bold'),fg='black',bg='white')
            self.change_l.place(x=0,y=450)

            self.change_e=Entry(self.left,width=10,font=('Calibri 18 bold'),bg='lightblue')
            self.change_e.place(x=280,y=450)

            self.change_btn= Button(self.left, text="Calculate the difference", width=22, height=2, bg='green',command=self.change_func)
            self.change_btn.place(x=430, y=450)

    #geneerate bill button
            self.bill_btn = Button(self.left, text="Creat a bill of the items purchased", width=30, height=2, bg='Purple',fg='white',command=self.generate_bill)
            self.bill_btn.place(x=0, y=550)
        else:
            messagebox.showinfo("successfully completed")
    def add_to_cart(self,*args,**kwargs):

        self.quantity_value=int(self.quantity_e.get())

        if  self .quantity_value >int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Not that any products in our stock.")
        else:
        #calculate the price first
            self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
            product_price=self.final_price.get()
            products_list=products_list.append(self.ajax)
            product_quantity=product_quantity.append(self.ajax)
            product_id=product_id.append(self.get_id)
            
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in products_list:
                self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('arial 18 bold'),bg='gray',fg='white')
                self.tempname.place(x=0,y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
                self.tempqt.place(x=150, y=self.y_index)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
                self.tempprice.place(x=300, y=self.y_index)

                self.y_index+=40
                self.counter+=1


            #total confugure
                self.total_l.configure(text="Final amount=Rs. "+str(sum(product_price)),bg='gray',fg='white',font=('20'))
                self.total_l.place(x=180,y=450)
            #delete
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()
            #autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0,END)

    def change_func(self,*args,**kwargs):
        self.amount_given=float(self.change_e.get())
        product_price=product_price.append(self.final_price)
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given-self.our_total

    #label change
        self.c_amount=Label(self.left,text="Change is Rs. "+str(self.to_give),font=('Calibri 20 bold'),fg='Black',bg='white')
        self.c_amount.place(x=0 ,y=500)

    def generate_bill(self,*args,**kwargs):
        self.mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        products_list=products_list.append(self.get_name)
        for r in self.pc:
            self.old_stock=r[2]
        for i in products_list:
            for r in self.pc:
                self.old_stock = r[2]
            self.new_stock=int(self.old_stock) - int(self.quantity_value)
        #updating the stock
            self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s",[self.new_stock,self.get_id])
            self.conn.commit()

        #inster into transcation
            self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.get_price,datetime])
            self.conn.commit()
            print("Decreased")

        tkinter.messagebox.showinfo("successfully done")
master=Tk()

ob=Application(master)

master.mainloop()