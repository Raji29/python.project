from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Combobox
from pymysql import *


class addSale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("adding a sale")
        self.geometry("500x300")
        self.head = Label(self, text="Sale", font=('Times New Roman', 30))
        self.head.pack(side=TOP, padx=10, pady=20)
        self.selectId = Label(self, text="dd-mm-yyyy")
        self.selectId.pack(padx=1, pady=8)
        box = Entry(self,width=20, bg="black", fg="white")
        box.pack(padx=1, pady=10)
        self.ids = Combobox(self)
        combo = Combobox(self,)
        combo['values'] = ("Avenger Cruise", "Avenger Street", "CT100")
        combo.pack(padx=2, pady=3)
        self.typeconsumerName = Label(self, text="enter the name of the consumer", font=('Times New Roman', 12))
        self.typeconsumerName.pack(padx=0, pady=3)
        self.consumerName = Entry(self,width=20, bg="black", fg="white")
        self.consumerName.pack(padx=0, pady=3)
        self.typeaddress = Label(self, text="enter the address of the consumer", font=('Times New Roman', 12))
        self.typeaddress.pack(padx=0, pady=4)
        self.address = Entry(self,width=20, bg="black", fg="white")
        self.address.pack(padx=0, pady=4)
        self.typepaymentMode = Label(self, text="payment mode", font=('Times New Roman', 12))
        self.typepaymentMode.pack(padx=0, pady=5)
        self.paymentMode = Entry(self,width=20, bg="black", fg="white")
        self.paymentMode.pack(padx=0, pady=5)
        self.typemobileNumber = Label(self, text="mobile number", font=('Times New Roman', 12))
        self.typemobileNumber.pack(padx=0, pady=6)
        self.mobileNumber = Entry(self,width=20, bg="black", fg="white")
        self.mobileNumber.pack(padx=0, pady=6)
        self.typepaid = Label(self, text="Amount paid", font=('Times New Roman', 12))
        self.typepaid.pack(padx=0, pady=7)
        self.paid = Entry(self,width=20, bg="black", fg="white")
        self.paid.pack(padx=0, pady=7)
        self.bt = Button(self, text="Sale",fg="yellow",bg="green", command=self.sale)
        self.bt.pack(padx=0, pady=8)
        self.clearbt = Button(self, text="clear",fg="yellow",bg="maroon", command=self.clear)
        self.clearbt.pack(padx=0, pady=10)

    def sale(self):
        try:
            con = connect('localhost', 'root', '', 'showroom')
            qry = "insert into sales set consumerName='%s', address='%s', paymentMode='%s', mobileNumber=%d, paid=%d" % (
            self.consumerName.get(), self.address.get(), self.paymentMode.get(), int(self.mobileNumber.get()),
            int(self.paid.get()))
            cur = con.cursor()
            cur.execute(qry)
            messagebox.showinfo("status", "event added to base")
            con.commit()
        except EXCEPTION as e:
            print(e)
        finally:
            con.close()


    def clear(self):
        con = connect('localhost', 'root', '', 'showroom')
        global addSale, root
        addSale.destroy(self)

a = addSale()
a.mainloop()