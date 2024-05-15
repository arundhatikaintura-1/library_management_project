from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
class LibraryManagementSystem:
    def __init__(self,root):
      self.root = root
      self.root.title("Library Management System")
      self.root.geometry("1500x750+0+0")


      #varuables#
      self.member_var=StringVar()
      self.prnno_var=StringVar()
      self.Idno_var=StringVar()
      self.Name_var=StringVar()
      self.Address_var=StringVar()
      self.Postcode_var=StringVar()
      self.Mobile_var=StringVar()

      self.Bookid_var=StringVar()
      self.Booktitle_var=StringVar()
      self.Dateborrowed_var=StringVar()
      self.Datedue_var=StringVar()
      self.Daysonbook_var=StringVar()
      self.Latereturnfine_var=StringVar()
      self.Actualprice_var=StringVar()




      lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="Blue",fg="green",bd=20,relief=RIDGE,font=("times new roman", 50,"bold"),padx=2,pady=6)
      lbltitle.pack(side=TOP,fill=X)

      frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="blue")
      frame.place(x=0,y=130,width=1500,height=350)
#dataframeleft
      DataFrameLeft=LabelFrame(frame,text="Library Member Information",bg="Blue",fg="red",bd=12,relief=RIDGE,font=("times new roman", 12,"bold"))
      DataFrameLeft.place(x=0,y=5,width=870,height=300)

      lblMember=Label(DataFrameLeft,bg="blue", text="Member Type",font=("times new roman", 15,"bold"),textvariable=self.member_var,padx=2,pady=6)
      lblMember.grid(row=0,column=0,sticky=W)

      comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman", 12,"bold"),width=27,state="readonly")
      comMember["value"]=("Admin staf","Student","Lacturer")
      comMember.grid(row=0,column=1)

      lblPRN_No= Label(DataFrameLeft, bg="blue", text="PRN NO", font=("times new roman", 15, "bold"), padx=2,pady=6)
      lblPRN_No.grid(row=1, column=0, sticky=W)
      txtPRN_NO=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.prnno_var,width=24)
      txtPRN_NO.grid(row=1,column=1)

      lblID_No = Label(DataFrameLeft, bg="blue", text="ID NO", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lblID_No.grid(row=2, column=0, sticky=W)
      txtID_NO = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Idno_var, width=24)
      txtID_NO.grid(row=2, column=1)

      lblname = Label(DataFrameLeft, bg="blue", text="Name", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lblname.grid(row=3, column=0, sticky=W)
      txtName = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Name_var,width=24)
      txtName.grid(row=3, column=1)

      lbladdress = Label(DataFrameLeft, bg="blue", text="Address", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lbladdress.grid(row=4, column=0, sticky=W)
      txtAddress = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.Address_var,width=24)
      txtAddress.grid(row=4, column=1)

      lblpostcode = Label(DataFrameLeft, bg="blue", text="Post Code", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lblpostcode.grid(row=5, column=0, sticky=W)
      txtpostcode= Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Postcode_var, width=24)
      txtpostcode.grid(row=5, column=1)

      lblmobile = Label(DataFrameLeft, bg="blue", text="Mobile", font=("times new roman", 15, "bold"), padx=2,pady=6)
      lblmobile.grid(row=6, column=0, sticky=W)
      txtMobile = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Mobile_var, width=24)
      txtMobile.grid(row=6, column=1)

      lblbookid = Label(DataFrameLeft, bg="blue", text="Book id", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lblbookid.grid(row=0, column=2, sticky=W)
      txtBookid = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Bookid_var,width=24)
      txtBookid.grid(row=0, column=3)

      lblbooktitle = Label(DataFrameLeft, bg="blue", text="Book title", font=("times new roman", 15, "bold"), padx=2, pady=6)
      lblbooktitle.grid(row=1, column=2, sticky=W)
      txtBooktitle = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Booktitle_var,width=24)
      txtBooktitle.grid(row=1, column=3)

      lblDateBorrowed = Label(DataFrameLeft, bg="blue", text="Date Borrowed", font=("times new roman", 15, "bold"), padx=2,pady=6)
      lblDateBorrowed.grid(row=2, column=2, sticky=W)
      txtdatebrowed = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.Dateborrowed_var,width=24)
      txtdatebrowed.grid(row=2, column=3)

      lblDatedue = Label(DataFrameLeft, bg="blue", text="Date Due", font=("times new roman", 15, "bold"),padx=2, pady=6)
      lblDatedue.grid(row=3, column=2, sticky=W)
      txtdatedue = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Datedue_var, width=24)
      txtdatedue.grid(row=3, column=3)

      lblDaysonbook = Label(DataFrameLeft, bg="blue", text="Days on book", font=("times new roman", 15, "bold"), padx=2,pady=6)
      lblDaysonbook.grid(row=4, column=2, sticky=W)
      txtdaysonbook = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Daysonbook_var,width=24)
      txtdaysonbook.grid(row=4, column=3)

      lbllatereturnfine = Label(DataFrameLeft, bg="blue", text="Late Return Fine", font=("times new roman", 15, "bold"), padx=2,pady=6)
      lbllatereturnfine.grid(row=5, column=2, sticky=W)
      txtlatereturnfine = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Latereturnfine_var, width=24)
      txtlatereturnfine.grid(row=5, column=3)

      lblactualprice = Label(DataFrameLeft, bg="blue", text="Actual price", font=("times new roman", 15, "bold"),padx=2, pady=6)
      lblactualprice.grid(row=6, column=2, sticky=W)
      txtactualprice = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.Actualprice_var, width=24)
      txtactualprice.grid(row=6, column=3)
#dataframeright
      DataFrameRight=LabelFrame(frame, text="Book Deatails", bg="Blue", fg="red", bd=12, relief=RIDGE,font=("times new roman", 12, "bold"))
      DataFrameRight.place(x=880, y=5, width=540, height=300)

      self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=13,padx=2,pady=6)
      self.txtBox.grid(row=0,column=2)

      listScrollbar=Scrollbar(DataFrameRight)
      listScrollbar.grid(row=0,column=1,sticky="ns")

      listBooks=["programming in c","java basics","python programming",
                 "DSA", "DBMS",".net", "machine python","python cookbook",
                 "Advance python","fluent python","think python",
                 "learning python","yellow dragan","pune python",
                 "red python","the tecnich python","inton python","Catcher in the Rye"]

      def selectbook(event=""):
        value=str(listBox.get(listBox.curselection()))
        x=value
        if (x=="programming in c"):
         self.Bookid_var.set("BKID5454")
         self.Booktitle_var.set(" concepts of c programming")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:500")

        elif (x=="java basics"):
         self.Bookid_var.set("BKID1234")
         self.Booktitle_var.set(" concepts of java")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:600")

        elif (x=="python programming"):
         self.Bookid_var.set("BKID1235")
         self.Booktitle_var.set(" concepts of python")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:700")

        elif (x=="DSA"):
         self.Bookid_var.set("BKID1236")
         self.Booktitle_var.set(" concepts of DSA")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:650")

        elif (x=="DBMS"):
         self.Bookid_var.set("BKID1237")
         self.Booktitle_var.set(" concepts of DBMS")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:450")

        elif (x == ".net"):
         self.Bookid_var.set("BKID1237")
         self.Booktitle_var.set(" concepts of .net technology")

         d1 = datetime.datetime.today()
         d2 = datetime.timedelta(days=15)
         d3 = d1 + d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:750")

        elif (x == "machine python"):
         self.Bookid_var.set("BKID1230")
         self.Booktitle_var.set(" concepts of machine python")

         d1 = datetime.datetime.today()
         d2 = datetime.timedelta(days=15)
         d3 = d1 + d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:1080")

        elif (x=="python cookbook"):
         self.Bookid_var.set("BKID1231")
         self.Booktitle_var.set(" cookbook")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:890")

        elif (x=="Advance python"):
         self.Bookid_var.set("BKID1232")
         self.Booktitle_var.set(" learn advance python")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:1500")

        elif (x == "fluent python"):
         self.Bookid_var.set("BKID1271")
         self.Booktitle_var.set(" learn fluent python")

         d1 = datetime.datetime.today()
         d2 = datetime.timedelta(days=15)
         d3 = d1 + d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:1650")

        elif (x=="think python"):
         self.Bookid_var.set("BKID1031")
         self.Booktitle_var.set(" python basics")

         d1=datetime.datetime.today()
         d2=datetime.timedelta(days=15)
         d3=d1+d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:670")

        elif (x == "learning python "):
         self.Bookid_var.set("BKID1265")
         self.Booktitle_var.set(" the  python course ")

         d1 = datetime.datetime.today()
         d2 = datetime.timedelta(days=15)
         d3 = d1 + d2
         self.Dateborrowed_var.set(d1)
         self.Datedue_var.set(d3)
         self.Daysonbook_var.set(15)
         self.Latereturnfine_var.set("Rs:50")
         self.Actualprice_var.set("Rs:896")

      listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=13)
      listBox.bind("<<ListboxSelect>>",selectbook)
      listBox.grid(row=0,column=0,padx=4)
      listScrollbar.config(command=listBox.yview)

      for item in listBooks:
        listBox.insert(END,item)
     #bottons/fram"e
      framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="blue")
      framebutton.place(x=0, y=480, width=1500, height=70)

      btnAddData=Button(framebutton, command=self.add_data, text="Add Data",font=("arial",12,"bold"),width=23,bg="green",fg="white")
      btnAddData.grid(row=0,column=0)

      btnshowData = Button(framebutton,command=self.show_data, text="Show Data", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
      btnshowData.grid(row=0, column=1)

      btnupdate = Button(framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
      btnupdate.grid(row=0, column=2)

      btndelete = Button(framebutton,command=self.delete, text="Delete", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
      btndelete.grid(row=0, column=3)

      btnreset = Button(framebutton,command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
      btnreset.grid(row=0, column=4)

      btnexit = Button(framebutton,  command=self.Exit, text="Exit", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
      btnexit.grid(row=0, column=5)

      #information frame
      frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="blue")
      frameDetails.place(x=0, y=550, width=1500, height=195)

      table_frame = Frame(frameDetails, bd=12, relief=RIDGE,  bg="blue")
      table_frame.place(x=0, y=2, width=1410, height=180)

      xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

      self.library_table=ttk.Treeview(table_frame,column=("membertype", "prnno", "idno","name","address","postcode", "mobileno","bookid", "title","DateBorrowed","datedue","days","latereturnfee", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

      xscroll.pack(side=BOTTOM,fill=X)
      yscroll.pack(side=RIGHT,fill=Y)

      xscroll.config(command=self.library_table.xview)
      yscroll.config(command=self.library_table.yview)

      self.library_table.heading("membertype",text="Member Type")
      self.library_table.heading("prnno", text="PRN No")
      self.library_table.heading("idno", text="ID NO")
      self.library_table.heading("name", text="Name")
      self.library_table.heading("address", text="Address")
      self.library_table.heading("postcode", text="Post Code")
      self.library_table.heading("mobileno", text="Mobile")
      self.library_table.heading("bookid", text="Book id")
      self.library_table.heading("title", text=" Book title")
      self.library_table.heading("DateBorrowed", text="Date Borrowed")
      self.library_table.heading("datedue", text="Date Due")
      self.library_table.heading("days", text="Days")
      self.library_table.heading("latereturnfee", text="Late Return Fine")
      self.library_table.heading("finalprice", text=" Actual price")

      self.library_table["show"]=["headings"]
      self.library_table.pack(fill=BOTH,expand=1)

      self.library_table.column("membertype", width=100)
      self.library_table.column("prnno", width=100)
      self.library_table.column("idno", width=100)
      self.library_table.column("name", width=100)
      self.library_table.column("address", width=100)
      self.library_table.column("postcode", width=100)
      self.library_table.column("mobileno", width=100)
      self.library_table.column("bookid", width=100)
      self.library_table.column("title", width=100)
      self.library_table.column("DateBorrowed", width=100)
      self.library_table.column("datedue", width=100)
      self.library_table.column("days", width=100)
      self.library_table.column("latereturnfee", width=100)
      self.library_table.column("finalprice", width=100)

      self.fatch_data()
      self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    def add_data(self):
      conn=mysql.connector.connect(host='localhost',username='root',port='3306',password='aruniannu',database='mydata')
      my_cursor= conn.cursor()
      my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.member_var.get(),
                                                                                                   self.prnno_var.get(),
                                                                                                   self.Idno_var.get(),
                                                                                                   self.Name_var.get(),
                                                                                                   self.Address_var.get(),
                                                                                                   self.Postcode_var.get(),
                                                                                                   self.Mobile_var.get(),
                                                                                                   self.Bookid_var.get(),
                                                                                                   self.Booktitle_var.get(),
                                                                                                   self.Dateborrowed_var.get(),
                                                                                                   self.Datedue_var.get(),
                                                                                                   self.Daysonbook_var.get(),
                                                                                                   self.Latereturnfine_var.get(),
                                                                                                   self.Actualprice_var.get()
                                                                                                 ))
      conn.commit()
      self.fatch_data()
      conn.close()

      messagebox.showinfo("Success", "Member has been inserted successfully")


    def update(self):
      conn = mysql.connector.connect(host='localhost', username='root', port='3306', password='aruniannu', database='mydata')
      my_cursor = conn.cursor()
      my_cursor.execute("update library set member=%s,ID=%s,Name=%s,Address=%s,Postcode=%s,Mobile=%s,bookid=%s,booktitle=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,actualprice=%s where PNR_NO=%s ",(
                                                                                                      self.member_var.get(),
                                                                                                      self.Idno_var.get(),
                                                                                                      self.Name_var.get(),
                                                                                                      self.Address_var.get(),
                                                                                                      self.Postcode_var.get(),
                                                                                                      self.Mobile_var.get(),
                                                                                                      self.Bookid_var.get(),
                                                                                                      self.Booktitle_var.get(),
                                                                                                      self.Dateborrowed_var.get(),
                                                                                                      self.Datedue_var.get(),
                                                                                                      self.Daysonbook_var.get(),
                                                                                                      self.Latereturnfine_var.get(),
                                                                                                      self.Actualprice_var.get(),
                                                                                                      self.prnno_var.get()
                                                                                                       ))
      conn.commit()
      self.fatch_data()
      self.reset()
      conn.close()
      messagebox.showinfo("Susccess", "Member has been updated")

    def  fatch_data(self):
      conn = mysql.connector.connect(host='localhost', username='root', port='3306', password='aruniannu', database='mydata')
      my_cursor = conn.cursor()
      my_cursor.execute("select * from library")
      rows=my_cursor.fetchall()

      if len(rows)!=0:
        self.library_table.delete(*self.library_table.get_children())
        for i in rows:
            self.library_table.insert("",END,values=i)
      conn.commit()
      conn.close()

    def get_cursor(self, event=""):
       cursor_row=self.library_table.focus()
       content=self.library_table.item(cursor_row)
       row=content['values']

       self.member_var.set(row[0]),
       self.prnno_var.set(row[1]),
       self.Idno_var.set(row[2]),
       self.Name_var.set(row[3]),
       self.Address_var.set(row[4]),
       self.Postcode_var.set(row[5]),
       self.Mobile_var.set(row[6]),
       self.Bookid_var.set(row[7]),
       self.Booktitle_var.set(row[8]),
       self.Dateborrowed_var.set(row[9]),
       self.Datedue_var.set(row[10]),
       self.Daysonbook_var.set(row[11]),
       self.Latereturnfine_var.set(row[12]),
       self.Actualprice_var.set(row[13])

    def show_data(self):
      self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
      self.txtBox.insert(END, "PRN NO\t\t" +self.prnno_var.get()+"\n")
      self.txtBox.insert(END, "ID NO \t\t" + self.Idno_var.get() + "\n")
      self.txtBox.insert(END, "Name\t\t" + self.Name_var.get() + "\n")
      self.txtBox.insert(END, "Address\t\t" + self.Address_var.get() + "\n")
      self.txtBox.insert(END, "Post code\t\t" + self.Mobile_var.get() + "\n")
      self.txtBox.insert(END, "Mobile\t\t" + self.Mobile_var.get() + "\n")
      self.txtBox.insert(END, "Book id\t\t" + self.Bookid_var.get() + "\n")
      self.txtBox.insert(END, "Book title\t\t" + self.Booktitle_var.get() + "\n")
      self.txtBox.insert(END, "Date Borrowed\t\t" + self.Dateborrowed_var.get() + "\n")
      self.txtBox.insert(END, "Date Due\t\t" + self.Datedue_var.get() + "\n")
      self.txtBox.insert(END, "Days on book\t\t" + self.Daysonbook_var.get() + "\n")
      self.txtBox.insert(END, "Late Return Fine\t\t" + self.Latereturnfine_var.get() + "\n")
      self.txtBox.insert(END, "Actual price\t\t" + self.Actualprice_var.get() + "\n")


    def reset(self):
      self.member_var.set(""),
      self.prnno_var.set(""),
      self.Idno_var.set(""),
      self.Name_var.set(""),
      self.Address_var.set(""),
      self.Postcode_var.set(""),
      self.Mobile_var.set(""),
      self.Bookid_var.set(""),
      self.Booktitle_var.set(""),
      self.Dateborrowed_var.set(""),

      self.Datedue_var .set(""),
      self.Daysonbook_var.set(""),
      self.Latereturnfine_var.set(""),
      self.Actualprice_var.set(""),
      self.txtBox.delete("1.0",END)

    def Exit(self):
      Exit=tkinter.messagebox.askyesno("Library management  System", "Do you want to exit?")
      if Exit>0:
        self.root.destroy()
        return

    def delete(self,):
       if self.prnno_var.get()=="" or self.Idno_var.get()=="":
         messagebox.showerror("Error", "first select the member")
       else:
         conn = mysql.connector.connect(host='localhost', username='root', port='3306', password='aruniannu', database='mydata')
         my_cursor = conn.cursor()
         query="delete from library where PNR_NO=%s"
         value=(self.prnno_var.get(),)
         my_cursor.execute(query , value)

         conn.commit()
         self.fatch_data()
         self.reset()
         conn.close()
         messagebox.showinfo("success", "Member has been deleted")

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
















