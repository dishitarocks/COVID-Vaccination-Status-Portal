from tkinter import* 
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import pymysql


class Register:
     def __init__(self,root):
         self.root=root
         self.root.title("DATA Input Window")
         self.root.geometry("1920x1080+0+0")
         #=======================================All Variables=====================================================================
         self.name_var=StringVar()
         self.PRN_var=StringVar()
         self.branch_var=StringVar()
         self.batch_var=StringVar()
         self.name_var=StringVar()
         self.search_by=StringVar()
         self.search_txt=StringVar()
          #-----------------------------------------------------------IMAGES--------------------------------------------------------
          #===========================================================BG image======================================================
         self.bg=ImageTk.PhotoImage(file="images/assets/bg vaccine.jpg")
         bg=Label(self.root,image=self.bg).place(x=300,y=0,relwidth=1,relheight=1)
         #======================================================Front left image===================================================
         self.left=ImageTk.PhotoImage(file="images/assets/left.jpg")
         left=Label(self.root,image=self.left).place(x=0,y=0,width=600,height=1080)
         #======================================================Front right image==================================================
         self.right=ImageTk.PhotoImage(file="images/assets/right.png")
         right=Label(self.root,image=self.right).place(x=600,y=50,width=973,height=900)
         #-------------------------------------------------------------------------------------------------------------------------


          #-----------------------------------------------------------INPUT FIELDS--------------------------------------------------
          #=============================================================name========================================================
         self.txt_name=Entry(right,textvariable=self.name_var,font=("times new roman",15),bg="lightgrey")
         self.txt_name.place(x=690,y=600,width=300)
          #==============================================================PRN========================================================
         self.txt_PRN=Entry(right,textvariable=self.PRN_var,font=("times new roman",15),bg="lightgrey")
         self.txt_PRN.place(x=1200,y=600,width=300)
          #=============================================================Branch======================================================
         self.cmb_branch=ttk.Combobox(right,textvariable=self.branch_var,font=("times new roman",15),state='readonly',justify=CENTER)
         self.cmb_branch['values']=("Select","CSE","IT","MECH","ENTC","CIVIL")
         self.cmb_branch.place(x=690,y=700,width=300)
         self.cmb_branch.current(0)
          #==============================================================batch======================================================
         self.cmb_batch=ttk.Combobox(right,textvariable=self.batch_var,font=("times new roman",15),state='readonly',justify=CENTER)
         self.cmb_batch['values']=("Select","2017-2021","2018-2022","2019-2023","2020-2024","2021-2025")
         self.cmb_batch.place(x=1200,y=700,width=300)
         self.cmb_batch.current(0)
          #=============================================================additional Date=============================================
         self.txt_password="123"
         self.txt_Dose1="not filled"
         self.txt_UVID="not filled"
         self.txt_age="not filled"
         self.txt_Vname="not filled"
         self.txt_Dose2="not filled"
          #=============================================================Buttons=====================================================
          #===========add============
         self.add_img=ImageTk.PhotoImage(file="images/assets/add button.png")
         add=Button(right,image=self.add_img,bd=0,cursor="hand2",command=self.add_students).place(x=700,y=765)
         #==========update==========
         self.upd_img=ImageTk.PhotoImage(file="images/assets/update button.png")
         upd=Button(right,image=self.upd_img,bd=0,cursor="hand2",command=self.update_data).place(x=1000,y=765)
         #==========delete==========
         self.dl_img=ImageTk.PhotoImage(file="images/assets/delete button.png")
         dl=Button(right,image=self.dl_img,bd=0,cursor="hand2",command=self.delete_data).place(x=1300,y=765)
         #=============================================Display frame=============================================================
         #==========ssearch by======       
         self.cmb_search=ttk.Combobox(right,textvariable=self.search_by,font=("times new roman",15),state='readonly',justify=CENTER)
         self.cmb_search['values']=("Select","name","PRN","branch","batch",)
         self.cmb_search.place(x=790,y=120,width=200)
         self.cmb_search.current(0)
         #=========Enter============
         self.txt_search=Entry(right,textvariable=self.search_txt,font=("times new roman",15),bg="lightgrey")
         self.txt_search.place(x=1110,y=120,width=200) 
         #========Search button===== 
         self.src_img=ImageTk.PhotoImage(file="images/assets/search button.png")
         src=Button(right,image=self.src_img,bd=0,cursor="hand2",command=self.search_data).place(x=1330,y=115)
         #========Show all==========
         self.vie_img=ImageTk.PhotoImage(file="images/assets/view all button.png")
         vie=Button(right,image=self.vie_img,bd=0,cursor="hand2",command=self.fetch_data).place(x=1420,y=115)
         #=============================================Table frame=================================================================
         Table_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
         Table_Frame.place(x=610,y=170,width=930,height=340)
         
         scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
         scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
         self.Register_table=ttk.Treeview(Table_Frame,columns=("name","PRN","branch","batch"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y) 
         scroll_x.config(command=self.Register_table.xview)
         scroll_y.config(command=self.Register_table.yview)
         self.Register_table.heading("name",text="Name")
         self.Register_table.heading("PRN",text="PRN")
         self.Register_table.heading("branch",text="BRANCH")
         self.Register_table.heading("batch",text="BATCH")
         self.Register_table['show']='headings'
         self.Register_table.column("name",width=300)
         self.Register_table.column("PRN",width=200)
         self.Register_table.column("branch",width=200)
         self.Register_table.column("batch",width=200)
         self.Register_table.pack(fill=BOTH,expand=1)
         self.Register_table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()
#================================Add function========================================================================================
     def add_students(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='student info')
        cur=con.cursor()
        if   self.txt_name.get()=="" or self.txt_PRN.get()=="" or self.cmb_branch.get()=="Select" or self.cmb_batch.get()=="Select":
             messagebox.showerror("Error","All fields Are Required",parent=self.root)
    
        elif cur.execute("SELECT * FROM `student data` WHERE PRN LIKE '%"+str(self.txt_PRN.get())+"%'"):
             messagebox.showerror("Error","Student with this PRN already Exists",parent=self.root)
             con.commit()
             self.fetch_data()
             con.close()
        else:
             cur.execute("INSERT INTO `student data`(`name`, `PRN`, `branch`, `batch`,`password`,`1st Dose Date`, `Unique Vaccine ID`, `age`, `Vaccine Name`, `2nd Dose Date`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (self.txt_name.get(),
                         self.txt_PRN.get(),
                         self.cmb_branch.get(),
                         self.cmb_batch.get(),
                         self.txt_password,
                         self.txt_Dose1,
                         self.txt_UVID,
                         self.txt_age,
                         self.txt_Vname,
                         self.txt_Dose2
                          ))
             con.commit()
             self.fetch_data()
             self.clear()
             con.close()
             messagebox.showinfo("Success","Added successfully",parent=self.root)

#================================Display function====================================================================================          
     def fetch_data(self):
         con=pymysql.connect(host='localhost',user='root',password='',database='student info')
         cur=con.cursor()
         cur.execute("SELECT * FROM `student data` WHERE 1")
         rows=cur.fetchall()
         if len(rows)!=0:
                self.Register_table.delete(*self.Register_table.get_children())
                for row in rows:
                        self.Register_table.insert('',END,values=row)
                con.commit()
         con.close()
#================================Clear Function=======================================================================================
     def clear(self):
         self.name_var.set("")
         self.PRN_var.set("")
         self.branch_var.set("Select")
         self.batch_var.set("Select")
#================================Back fill event function=============================================================================
     def get_cursor(self,ev):
         cursor_row=self.Register_table.focus()
         contents=self.Register_table.item(cursor_row)
         row=contents['values']
         self.name_var.set(row[0])
         self.PRN_var.set(row[1])
         self.branch_var.set(row[2])
         self.batch_var.set(row[3])
#==================================Update function=====================================================================================
     def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='student info')
        cur=con.cursor()
        if   self.txt_name.get()=="" or self.txt_PRN.get()=="" or self.cmb_branch.get()=="Select" or self.cmb_batch.get()=="Select":
             messagebox.showerror("Error","All fields Are Required",parent=self.root)
    
        else:
             cur.execute("UPDATE `student data` SET `name`=%s,`branch`=%s,`batch`=%s,`password`=%s,`1st Dose Date`=%s,`Unique Vaccine ID`=%s,`age`=%s,`Vaccine Name`=%s,`2nd Dose Date`=%s WHERE `PRN`=%s",
                        (self.txt_name.get(),
                        self.cmb_branch.get(),
                        self.cmb_batch.get(),
                        self.txt_password,
                        self.txt_Dose1,
                        self.txt_UVID,
                        self.txt_age,
                        self.txt_Vname,
                        self.txt_Dose2,
                        self.txt_PRN.get()
                         ))
             con.commit()
             self.fetch_data()
             self.clear()
             con.close()
             messagebox.showinfo("Success","Updated successfully",parent=self.root)
#================================delete function=======================================================================================
     def delete_data(self):
         con=pymysql.connect(host='localhost',user='root',password='',database='student info')
         cur=con.cursor()
         cur.execute("DELETE FROM `student data` WHERE PRN=%s",self.PRN_var.get())
         con.commit()
         con.close()
         self.fetch_data()
         self.clear()
#==================================Search function=====================================================================================

     def search_data(self):
        if   self.search_by.get()=="Select":
             messagebox.showerror("Error","Search by field not selected",parent=self.root)
        elif  self.search_txt.get()=="":
              messagebox.showerror("Error","Search box is empty",parent=self.root)     
        else:
             con=pymysql.connect(host='localhost',user='root',password='',database='student info')
             cur=con.cursor()
             cur.execute("SELECT * FROM `student data` WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
             rows=cur.fetchall()
             if len(rows)!=0:
                self.Register_table.delete(*self.Register_table.get_children())
                for row in rows:
                        self.Register_table.insert('',END,values=row)
                con.commit()
             con.close()    

root=Tk()
obj=Register(root)
root.mainloop()