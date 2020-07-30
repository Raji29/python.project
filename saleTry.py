from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from pymysql import *

class addSale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("adding a sale")
        self.geometry("500x300")
        self.head = Label(self, text="Sale", font=('Times New Roman', 30))
        self.head.pack(side=TOP,padx=10,pady=20)
        self.ids = Combobox(self)
        combo=Combobox(self)
        combo['values']=("Avenger Cruise","Avenger Street","CT100")
        combo.pack(padx=2,pady=3)
        self.typedate = Label(self, text="enter date in dd-mm-yyyy", font=('Times New Roman', 12))
        self.typedate.pack(padx=0, pady=5)
        self.date = Entry(self)
        self.date.pack(padx=0, pady=5)
        self.typeconsumerName = Label(self, text="enter the name of the consumer", font=('Times New Roman',12))
        self.typeconsumerName.pack(padx=0,pady=3)
        self.consumerName=Entry(self)
        self.consumerName.pack(padx=0,pady=3)
        self.typeaddress = Label(self, text="enter the address of the consumer", font=('Times New Roman', 12))
        self.typeaddress.pack(padx=0, pady=4)
        self.address = Entry(self)
        self.address.pack(padx=0, pady=4)
        self.typepaymentMode = Label(self, text="payment mode", font=('Times New Roman', 12))
        self.typepaymentMode.pack(padx=0, pady=5)
        self.paymentMode = Entry(self)
        self.paymentMode.pack(padx=0, pady=5)
        self.typemobileNumber= Label(self, text="mobile number", font=('Times New Roman', 12))
        self.typemobileNumber.pack(padx=0, pady=6)
        self.mobileNumber = Entry(self)
        self.mobileNumber.pack(padx=0, pady=6)
        self.typepaid = Label(self, text="Amount paid", font=('Times New Roman', 12))
        self.typepaid.pack(padx=0, pady=7)
        self.paid= Entry(self)
        self.paid.pack(padx=0, pady=7)
        self.bt=Button(self,text="Sale",command=self.sale)
        self.bt.pack(padx=0,pady=8)
    def sale(self):
        try:
            con = connect('localhost', 'root', '', 'showroom')
            qry="insert into sales set date='%s', modelName='%s', onRoadPrice=%d, consumerName='%s', address='%s', paymentMode='%s', mobileNumber=%d, paid=%d" %(self.date.get(), self.modelName.get(),int(self.onRoadPrice.get()),self.consumerName.get(),self.address.get(),self.paymentMode.get(),int(self.mobileNumber.get()),int(self.paid.get()))
            cur = con.cursor()
            cur.execute(qry)
            pack=cur.fetchall()

            messagebox.showinfo("status", "event added to base")
            con.commit()
        except EXCEPTION as e:print(e)
        finally:
            con.close()
a=addSale()
a.mainloop()