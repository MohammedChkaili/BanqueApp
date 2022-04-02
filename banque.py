import io
import time
import tkinter as tk
import os
import tkinter.messagebox as MessageBox
import webbrowser
from tkinter import ttk, filedialog
import mysql.connector as mysql
from bottle import url
from tkcalendar import DateEntry
from PIL import Image,ImageTk


def login():
    cin=e_cin.get()
    passwd=e_password.get()

    if (e_cin.get()=="" or e_password.get()==""):
        MessageBox.showwarning("warning!!!","All field are requried!!")
    else:

       con=mysql.connect(host="localhost",user="root",password="Mchkaili-18@23",database="bank")
       cursor=con.cursor()
       sql="select cin,password from register where cin=%s and password=%s"
       cursor.execute(sql,[(cin),(passwd)])
       result=cursor.fetchall()
       

       if result:

            window1=tk.Toplevel()
            window1.geometry('1200x500')
            window1.title("Bank system")
            window1.configure(bg="#4065A4")
            window1.iconbitmap("C:\\Users\\chkaili\\Desktop\\tkinter\\bank.ico")


            account=tk.Label(window1,text="Account information",font=('algerian',10),bg="#4065A4",fg="white")
            account.place(x=40,y=60)

            withdraw = tk.Button(window1, text="withdraw", font=('algerian', 10), bg="#4065A4", width=13, fg="white")
            withdraw.place(x=550, y=420)
            accountdepo = tk.Label(window1, text="Deposit", font=('algerian', 10), bg="#4065A4", fg="white")
            accountdepo.place(x=450, y=170)

            cin = tk.Label(window1, text="cin", font=('algerian', 10), bg="#4065A4", fg="white")
            cin.place(x=40, y=140)
            firstname = tk.Label(window1, text="Firstname", font=('algerian', 10), bg="#4065A4", fg="white")
            firstname.place(x=40, y=175)
            lastname = tk.Label(window1, text="Lastname", font=('algerian', 10), bg="#4065A4", fg="white")
            lastname.place(x=40, y=215)
            pays = tk.Label(window1, text="Pays", font=('algerian', 10), bg="#4065A4", fg="white")
            pays.place(x=42, y=250)
            card = tk.Label(window1, text="credit card", font=('algerian', 10), bg="#4065A4", fg="white")
            card.place(x=42, y=280)
            f_cin = tk.Entry(window1, width=26, bg="white")
            f_cin.place(x=190, y=140)
            e_firstname = tk.Entry(window1, width=26, bg="white")
            e_firstname.place(x=190, y=175)
            e_lastname = tk.Entry(window1, width=26, bg="white")
            e_lastname.place(x=190, y=216)
            e_card= tk.Entry(window1, width=26, bg="white")
            e_card.place(x=190, y=279)
            e_pays = tk.Entry(window1, width=26, bg="white")
            e_pays.place(x=190, y=250)
            balance = tk.Label(window1, text="Your Balance", font=('algerian', 10), bg="#4065A4", fg="white")
            balance.place(x=450, y=60)
            amount1 = tk.Label(window1, text="amount", font=('algerian', 10), bg="#4065A4", fg="white")
            amount1.place(x=490, y=110)
            e_amount1 = tk.Entry(window1, width=26, bg="white")
            e_amount1.place(x=580, y=110)
            amount2 = tk.Label(window1, text="amount", font=('algerian', 10), bg="#4065A4", fg="white")
            amount2.place(x=490, y=215)
            amount2=tk.Entry(window1, width=26, bg="white")
            amount2.place(x=580,y=215)
            amount3 = tk.Label(window1, text="withdraw", font=('algerian', 10), bg="#4065A4", fg="white")
            amount3.place(x=450, y=270)
            amount4 = tk.Label(window1, text="amount", font=('algerian', 10), bg="#4065A4", fg="white")
            amount4.place(x=490, y=320)
            amount4=tk.Entry(window1, width=26, bg="white")
            amount4.place(x=580,y=320)




            con = mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
            cursor = con.cursor()

            cursor.execute("select cin,firstname,lastname,card,pay,balance from register where cin='" + e_cin.get()+ "'")

            rows = cursor.fetchall()
            for row in rows:
                f_cin.insert(0,row[0])
                e_firstname.insert(0, row[1])
                e_lastname.insert(0, row[2])
                e_card.insert(0, row[3])
                e_pays.insert(0, row[4])
                e_amount1.insert(0, row[5])

            con.cursor() ;

            def withdraw():
                if(amount4.get()==""):
                    MessageBox.showwarning("warning","pls enter the amount")
                else:
                    insert="you can withdraw "+amount4.get()+" from your account "
                    MessageBox.showinfo("result",insert)

            withdraw = tk.Button(window1, text="withdraw", font=('algerian', 10), bg="#4065A4", width=13,
                                     fg="white",command=withdraw)
            withdraw.place(x=550, y=420)

            def check():

                window3 = tk.Toplevel()
                window3.geometry('1200x500')
                window3.title("Bank system")
                window3.configure(bg="#4065A4")
                window3.iconbitmap("C:\\Users\\chkaili\\Desktop\\tkinter\\bank.ico")
                tableau = ttk.Treeview(window3, columns=('cin', 'firstname', 'lastname', 'accountnumber', 'amount'))
                tableau.heading('cin', text='cin')

                tableau.heading('firstname', text='firstname')
                tableau.heading('lastname', text='lastname')
                tableau.heading('accountnumber', text='accountnumber')
                tableau.heading('amount', text='amount')
                tableau['show'] = 'headings'
                tableau.place(x=50, y=100)

                con = mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
                cursor = con.cursor()
                sql = "select cin,firstname,lastname,accountnumber,amount from transfer where cin='" + e_cin.get() + "'"
                cursor.execute(sql)

                rows = cursor.fetchall()
                for row in rows:
                    tableau.delete()
                    tableau.insert('', 'end', iid=row[0], values=(row[0], row[1], row[2], row[3], row[4]))

                con.close();

            transaction = tk.Button(window1, text="check transactions", font=('algerian', 10), fg="white", bg="#4065A4",
                                    command=check)
            transaction.place(x=60, y=410)

            def deposit():

                 if(amount2.get()==""):
                      MessageBox.showwarning("error","pls enter the amount!!")

                 else:

                     con=mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
                     cursor=con.cursor()
                     cursor.execute("insert into depos  values ('" + e_cin.get() +"','" +e_firstname.get()+"','" + e_lastname.get() +"','" + e_pays.get() +"','" + e_card.get() +"','" + amount2.get() +"')")
                     cursor.execute("commit");
                     insertdatas="transaction of "+amount2.get()+" was deposit in your account"
                     MessageBox.showinfo("result",insertdatas)

                     con.close();


            Deposit = tk.Button(window1, text="Deposit", font=('algerian', 10), bg="#4065A4", width=13, fg="white",
                                command=deposit)
            Deposit.place(x=670, y=420)



            def transfer():

                window2 = tk.Toplevel()
                window2.geometry('700x500')
                window2.title("Bank system")
                window2.configure(bg="#4065A4")
                window2.iconbitmap("C:\\Users\\chkaili\\Desktop\\tkinter\\bank.ico")
                labele = tk.Label(window2, text="Account number", fg="white", bg="#4065A4", font=('algerian', 10))
                labele.place(x=50, y=140)
                labele1 = tk.Label(window2, text="Amount in $", fg="white", bg="#4065A4", font=('algerian', 10))
                labele1.place(x=50, y=190)
                e_labele=tk.Entry(window2, width=26, bg="white")
                e_labele.place(x=190,y=140)
                e_labele1 = tk.Entry(window2, width=26, bg="white")
                e_labele1.place(x=190, y=190)
                instruction=tk.Label(window2,text="account reciever information",fg="white", bg="#4065A4", font=('algerian', 10))
                instruction.place(x=40,y=40)
                def done():
                    if (e_labele.get()=="" or e_labele1.get()==""):
                        MessageBox.showwarning("warning","empty filed!!")
                    else:


                         con = mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
                         cursor = con.cursor()
                         cursor.execute( "insert into transfer values('" + e_cin.get() + "','" +e_firstname.get()+"','" + e_lastname.get() +"','" + e_labele.get() + "','" + e_labele1.get() + "' )")
                         cursor.execute("commit");
                         insertdata=e_labele1.get()+" has been sent to "+e_labele.get()
                         MessageBox.showinfo("transfer",insertdata)
                         con.close();


                done = tk.Button(window2, text="transfer now", font=('algerian', 10), width=14, fg="white",
                                    bg="#4065A4", command=done)
                done.place(x=50,y=320)



            transfer = tk.Button(window1, text="transfer money", font=('algerian', 10), width=14, fg="white",
                                 bg="#4065A4",command=transfer)
            transfer.place(x=220, y=410)






       else:
           MessageBox.showerror("errror","invalid cin or password")


def Register():

    class Page(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)

        def show(self):
            self.lift()


    class Page1(Page):
        def __init__(self, *args, **kwargs):
            Page.__init__(self, *args, **kwargs)


            self.configure(bg="#4065A4")
            label = tk.Label(self, text="Registration form", font=('algerian', 15), bg="#4065A4", fg="white")
            label.place(x=100, y=60)
            cin = tk.Label(self, text="cin", font=('algerian', 10), bg="#4065A4", fg="white")
            cin.place(x=40, y=140)
            firstname = tk.Label(self, text="Firstname", font=('algerian', 10), bg="#4065A4", fg="white")
            firstname.place(x=40, y=175)
            lastname = tk.Label(self, text="Lastname", font=('algerian', 10), bg="#4065A4", fg="white")
            lastname.place(x=40, y=215)
            pays = tk.Label(self, text="Pays", font=('algerian', 10), bg="#4065A4", fg="white")
            pays.place(x=42, y=385)
            paysbox= ttk.Combobox(self,values=["morocco", "france", "germany", "usa","australie","GB","espagne","italy"])
            paysbox.place(x=190, y=383)
            paysbox['state']='readonly'

            contact = tk.Label(self, text="contact number", font=('algerian', 10), bg="#4065A4", fg="white")
            contact.place(x=40, y=298)
            password = tk.Label(self, text="password", font=('algerian', 10), bg="#4065A4", fg="white")
            password.place(x=40, y=338)
            dob=tk.Label(self,text="Date of birth",font=('algerian',10),bg="#4065A4",fg="white")
            dob.place(x=40,y=256)
            e_cin = tk.Entry(self, width=26, bg="white")
            e_cin.place(x=190, y=140)
            e_firstname = tk.Entry(self, width=26, bg="white")
            e_firstname.place(x=190, y=175)
            e_lastname = tk.Entry(self, width=26, bg="white")
            e_lastname.place(x=190, y=216)
            """e_dob=tk.Entry(self,width=26,bg="white")
            e_dob.place(x=190,y=255)"""
            cal = DateEntry(self, selectmode='day',width=20)
            cal.place(x=190,y=255)


            dt=cal.get_date()
            str_dt4=dt.strftime("%Y-%m-%d")

            e_contact = tk.Entry(self, width=26, bg="white")
            e_contact.place(x=190, y=298)
            e_password = tk.Entry(self, width=26, bg="white")
            e_password.place(x=190, y=338)
            dob=str_dt4

            pack1 = tk.Label(self, text="package", font=('algerian', 10), bg="#4065A4", fg="white")
            pack1.place(x=390, y=180)
            card = tk.Label(self, text="credit card", font=('algerian', 10), bg="#4065A4", fg="white")
            card.place(x=390, y=220)
            pic = tk.Label(self, text="Picture", font=('algerian', 10), bg="#4065A4", fg="white")
            pic.place(x=390, y=290)
            offre = tk.Label(self, text="Choix de l'offre", font=("algerian", 11), fg="white", bg="#4065A4")
            offre.place(x=490, y=120)
            packbox = ttk.Combobox(self, values=["pack jeune", "pack adultes", "pack étudiant", "pack e-commerce"])
            packbox.place(x=510, y=180)
            packbox['state'] = 'readonly'

            cardbox = ttk.Combobox(self, values=["Mastercard", "Visa", "skrill"])
            cardbox.place(x=510, y=220)
            cardbox['state'] = 'readonly'
            def browse():
                f_types = [('Jpg files', '*.jpg'), ('Png files', '*.png')]
                filename = filedialog.askopenfilename(initialdir="/", title="select image",
                                                      filetypes=(f_types))

                picture = Image.open(filename)

                picture = picture.resize((120, 120))

                picture = ImageTk.PhotoImage(picture)
                mycanvas = tk.Label(self, width=145, height=125, bg="#4065A4")
                mycanvas.place(x=485, y=320)

                mycanvas.image = picture
                mycanvas['image'] = picture

            browse = tk.Button(self, text="Browse", fg="white", font=('algerian', 10), bg="#4065A4",command=browse)
            browse.place(x=530, y=450)

            def submit():


                cin = e_cin.get()
                firstname = e_firstname.get()
                lastname = e_lastname.get()
                contact = e_contact.get()
                password = e_password.get()
                pay=paysbox.get()
                pack = packbox.get()
                card = cardbox.get()





                if (cin== "" or firstname=="" or lastname=="" or contact=="" or password=="" or pack=="" or card==""or dob==""or pay=="" ):
                    MessageBox.showwarning("Warning!!","All fields required!!")
                else:


                   con = mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
                   cursor = con.cursor()
                   cursor.execute(
                    "insert into register values('" + cin + "','" + firstname + "','" + lastname + "','" + contact + "','" + password + "','" + pack + "','" + card +"','" + dob +"','"+pay+ "')")


                   cursor.execute("commit");

                   con.close();

            submit = tk.Button(self, text="submit", fg="white", bg="#4065A4", width=16, relief="groove",
                               font=('algerian', 11), command=submit)
            submit.place(x=480, y=570)

    class Page2(Page):
        def __init__(self, *args, **kwargs):
            Page.__init__(self, *args, **kwargs)
            bi = tk.PhotoImage(file="C:/Users/chkaili/Desktop/tkinter/form2.gif")
            image = tk.Label(self, image=bi, bg="#4065A4")
            image.place(x=400, y=50)
            bg = tk.PhotoImage(file='C:/Users/chkaili/Desktop/tkinter/7.gif')

            self.configure(bg="#4065A4")

            vie=tk.Label(self,text="Documentation",font=('algerian',17),fg="white",bg="#4065A4")
            vie.place(x=30,y=30)
            text=tk.Label(self,text="Related website",bg="#4065A4",font=('algerian',11),fg="white")
            text1=tk.Label(self,text="Contacter nous",bg="#4065A4",font=('algerian',11),fg="white")
            text2=tk.Label(self,text="numéro de telephone: 06 06 29 43 40",bg="#4065A4",font=('bold',11),fg="white")
            text3 = tk.Label(self, text="Adresse mail : OTP_bank@gmail.com", bg="#4065A4", font=('bold', 11),
                             fg="white")
            text5 = tk.Label(self, text="A propos de OTP_Bank", bg="#4065A4", font=('algerian', 11), fg="white")
            text5.place(x=35,y=315)



            text2.place(x=350,y=145)
            text1.place(x=350,y=110)
            text.place(x=35,y=90)
            text3.place(x=350, y=180)
            text4 = tk.Label(self, text="Réclamation", bg="#4065A4", font=('algerian', 11),
                             fg="white")
            text4.place(x=350,y=230)
            text_4=tk.Entry(self,bg="white")

            text_4.place(x=350,y=270,height=150,width=350)

            def reclam():
                if(text_4.get()==""):
                    MessageBox.showerror("error","no reclamation entered")

                else:
                    con = mysql.connect(host="localhost", user="root", password="Mchkaili-18@23", database="bank")
                    cursor = con.cursor()
                    cursor.execute("insert into reclamation values('" + text_4.get() + "' )")
                    cursor.execute("commit");
                    time.sleep(0.2)
                    MessageBox.showinfo("info","seccessfull operation")
                    text_4.delete(0)




            recl=tk.Button(self,text="send",width=11,relief="groove",fg="white",bg="#4065A4",command=reclam)
            recl.place(x=350,y=430)


            def callback(event):

                webbrowser.open_new(event.widget.cget("text"))

            link=tk.Label(self,text="www.OTP_bank.com",bg="#4065A4",fg="orange",font=('italic',11),cursor="hand2")
            link.place(x=35,y=140)
            link.bind("<Button-1>", callback)
            link = tk.Label(self, text="www.cdi2way.com", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=180)
            link.bind("<Button-1>", callback)
            link = tk.Label(self, text="www.Blakcedraw.com", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=220)
            link.bind("<Button-1>", callback)
            link = tk.Label(self, text="www.Pornhub.com", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=260)
            link.bind("<Button-1>", callback)
            link = tk.Label(self, text="historique", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=360)
            link = tk.Label(self, text="CHiffres clés", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=400)
            link = tk.Label(self, text="Réseaux", bg="#4065A4", fg="orange", font=('italic', 11),
                            cursor="hand2")
            link.place(x=35, y=440)
            link.bind("<Button-1>", callback)

    class MainView(tk.Frame):

        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)

            p1 = Page1(self)
            p2 = Page2(self)




            window2.title("Bank system")
            window2.configure(bg="#4065A4")
            window2.iconbitmap("C:\\Users\\chkaili\\Desktop\\tkinter\\bank.ico")

            container = tk.Frame(self, bg="white")
            container.pack(fill="both", expand=True)

            p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1, height=600, width=700)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1, height=600, width=700)


            back = tk.Button(window2, text="Back", bg="#4065A4", width=16, relief="groove", fg="white",
                                font=('algerian', 11), command=p1.show)
            suivant1 = tk.Button(window2, text="suivant", bg="#4065A4", width=16, relief="groove", fg="white",
                                 font=('algerian', 11), command=p2.show)


            back.place(x=560, y=530)
            suivant1.place(x=400, y=530)

            p1.show()



    if __name__ == "__main__":
        window2 = tk.Toplevel()
        bi = tk.PhotoImage(file="C:/Users/chkaili/Desktop/tkinter/form2.gif")
        image = tk.Label(window2, image=bi, bg="#4065A4")
        image.place(x=40, y=50)
        main = MainView(window2)
        main.pack(fill="both", expand=True)
        window2.geometry("800x600")






        window2.mainloop()





    """def suivant():
        window2.destroy()
        window3 = tk.Toplevel()
        window3.geometry('600x500')
        window3.title("Bank system")
        window3.configure(bg="#4065A4")
        window3.iconbitmap("C:\\Users\\chkaili\\Desktop\\bank.ico")



        window3.mainloop()"""



window=tk.Tk()
window.geometry("800x500")
window.title("WELCOME")
window.configure(bg="#4065A4")
window.iconbitmap("C:\\Users\\chkaili\\Desktop\\tkinter\\bank.ico")

bg=tk.PhotoImage(file="C:/Users/chkaili/Desktop/tkinter/k.gif")
mylabel= tk.Label(window, image=bg,bg="#4065A4")
mylabel.place(x=160,y=120)
mytitle=tk.Label(window,text="Welcome to the Bank system",bg="#4065A4",font=('algerian',16),fg="white")
mytitle.place(x=190,y=40)
cin=tk.Label(window,text="Cin",bg="#4065A4",fg="white",font=('algerian',12))
cin.place(x=300,y=154)
password=tk.Label(window,text="Password",bg="#4065A4",fg="white",font=('algerian',12))
password.place(x=270,y=214)
e_cin=tk.Entry(window,bg="white",width=26)
e_cin.place(x=380,y=155)
e_password=tk.Entry(window,bg="white",width=26)
e_password.place(x=380,y=215)
myregister=tk.Label(window,text="Register if you don't have an account ",fg="white",font=('algerian',10),bg="#4065A4")
myregister.place(x=130,y=400)
login=tk.Button(window,text="Login",bg="#4065A4",fg="white",font=('algerian',11),width=11,relief="groove",command=login)
login.place(x=260,y=290)
register=tk.Button(window,text="Register",bg="#4065A4",fg="white",font=('algerian',11),width=11,relief="groove",command=Register)
register.place(x=400,y=289)




window.mainloop()


