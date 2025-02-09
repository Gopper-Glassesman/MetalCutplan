import tkinter as TK
from tkinter.ttk import *
from tkinter import font
import decimal as D
import new_function_ClearCoding as CAL
from PIL import Image, ImageTk

font_set="TH SarabunPSK",12,"bold"


class Box (TK.Frame):
    

    def __init__(self,root,x,y):

        super().__init__()

        self.RM=["Steel","Stainless 304","Stainless 316","Aluminum 1050"]
        self.Spec= {"RM":"","Type":"","Height":0,"Fin":0,"Width": 0,"Thickness 1": 0 ,"Thickness 2": 0,"Max":0 }

        self.Type=["SQ","REC","H-Beam",\
                    "Channel","L","C-Lip","Pipe","Flat Bar","Round Bar","Square Bar"]

        self.Mainframe = TK.Frame(root)
        self.Mainframe.grid(row=x,column=y)

        self.MainLabelF=TK.LabelFrame(self.Mainframe,text="Main")
        self.MainLabelF.grid(row=0,column=0,padx=5,pady=10)
        
        # ของในMain frame 

        self.setting0_label=TK.Label(self.MainLabelF,text="รูปทรง โลหะ",font=font_set)
        self.setting0_label.grid(row=0,column=1)

        self.setting0_RM=TK.Label(self.MainLabelF,text="ชนิดโลหะ",font=font_set)
        self.setting0_RM.grid(row=2,column=1)

        self.setting0_Max_Label=TK.Label(self.MainLabelF,text="ความยาวเต็มเส้น(Max)",font=font_set)
        self.setting0_Max_Label.grid(row=0 ,column=2)
        
        #เลือกว่าเปน steel stainless Aluminum... ....
        self.setting0_RM_box=Combobox(self.MainLabelF,width=15,values=self.RM)
        self.setting0_RM_box.grid(row=3,column=1)     
        bigfont = font.Font(family="AngsanaUPC",size=12)
        self.setting0_RM_box.option_add("*TCombobox*Listbox*Font", bigfont)
        self.setting0_RM_box.bind("<<ComboboxSelected>>",self.Register_RM)

        
        #เลือกว่าเปน L,SQ,H-Beam,C-lip ....
        self.setting0_Type_combo=Combobox(self.MainLabelF,width=15,values=self.Type)
        self.setting0_Type_combo.grid(row=1,column=1,padx=5)
        self.setting0_Type_combo.bind("<<ComboboxSelected>>",self.SelectSize)

        self.setting0_Max_box=TK.Entry(self.MainLabelF,width=15)
        self.setting0_Max_box.grid(row=1,column=2)


        self.test_Label=TK.Label(self.MainLabelF,text="result")
        self.test_Label.grid(row=4,column=1)

        
        #พอเลือกแล้วจะให้แสดงเฉพาะ ระยะ เหล็กทรงนั้นๆต้องใช้ 
        print("OK")
        #Set parameter spec ของRM

        self.size_frame=TK.LabelFrame(self.Mainframe,text="Size")
        self.size_frame.grid(row=1,column=0,padx=5,pady=10)
        self.require_size=[]
        self.require_size_box=[]
        self.require_thk=[]
        self.require_thk_box=[]

        self.Test_AnswerF=TK.LabelFrame(self.Mainframe,text="Result")
        self.Test_AnswerF.grid(row=2,column=0,padx=2,pady=3)

        #ตำแหน่งที่ตั้งรูปประกอบ

        """H_image = Image.open("images/H-BeamR1.png")
        H_image_tk=ImageTk.PhotoImage(H_image)
        Channel_image = Image.open("images/ChannelR1.png")
        Channel_image_tk=ImageTk.PhotoImage(Channel_image)
        L_image= Image.open("images/AngleR1.png")
        L_image_tk=ImageTk.PhotoImage(L_image)
        REC_image = Image.open("images/RectangularR1.png")
        REC_image_tk=ImageTk.PhotoImage(REC_image)
        SQ_image=Image.open("images/SquareR1.png")
        SQ_image_tk=ImageTk.PhotoImage(SQ_image)
        Pipe_image=Image.open("images/PipeR1.png")
        Pipe_image_tk=ImageTk.PhotoImage(Pipe_image)
        RB_image=Image.open("images/Round_barR1.png")
        RB_image_tk=ImageTk.PhotoImage(RB_image)
        C_Lip_image=Image.open("images/C-LipR1.png")
        C_Lip_image_tk=ImageTk.PhotoImage(C_Lip_image)
        FB_image=Image.open("images/Flat_bar.png")
        FB_image_tk=ImageTk.PhotoImage(FB_image)
        Square_bar_image=Image.open("images/Square_bar.png")
        Square_bar_image_tk=ImageTk.PhotoImage(Square_bar_image)


        self.image_library={"SQ":SQ_image_tk ,"H-Beam": H_image_tk,"REC":REC_image_tk,\
                    "Channel":Channel_image_tk,"L":L_image_tk,"C-Lip":C_Lip_image_tk\
                        ,"Pipe":Pipe_image_tk,"Flat Bar":FB_image_tk,"Round Bar":RB_image_tk\
                            ,"Square Bar":Square_bar_image_tk}"""
        
        
        
        
        self.Image=TK.Label(self.Test_AnswerF)
        self.Image.pack(padx=2,pady=3)

        self.Go_Button=TK.Button(self.Test_AnswerF,text="Calculate",fg="Green",command=self.Go_Cal)
        self.Go_Button.pack()

        self.Answer_Label=TK.Label(self.Test_AnswerF,text="Result",fg="Red",font=font_set)
        self.Answer_Label.pack()

        #รับความยาว +ปริมาณ
        self.frame_for_boxes = TK.LabelFrame(self.Mainframe,text="Set Quantity")
        self.frame_for_boxes.grid(row=3,column=0)
        self.canvas=TK.Canvas(self.frame_for_boxes,width="300")

        self.frame2=TK.LabelFrame(self.canvas,text="for Calculation")
        
        self.scroll=Scrollbar(self.frame_for_boxes,orient="vertical",command=self.canvas.yview)
        self.canvas.grid(row=3,column=0,sticky="e")

            
        self.scroll.grid(row=3,column=2,sticky="ns")
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.canvas.bind('<Configure>',lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        #Frame ไว้ใส่กล่อง Entry
            
        self.canvas.create_window((0,0),window=self.frame2) #ไว้เก็บค่า เพื่อรัย จำนวนmember ความยาวที่จะตัด
        self.NO_Loop=[]
        
        self.Cut_No=[]
        self.Cut_Length=[]
        self.Cut_Qty=[]


        self.Cut_Length_Qty()

    def Register_RM(self,L):
        self.Spec["RM"]= self.setting0_RM_box
        self.test_Label.configure(text=f"Selected Material : {self.setting0_RM_box.get()} ")
        print(f"ตรงนี้ก็work  นะ {L}")
  
    def Return_Normal(self):
        self.Answer_Label.configure(text="Result")

    def SelectSize (self,evemt):
        print("ตรงนี้workแล้ว")
        
        self.Image.configure(image="")
        
        self.require_size.clear()
        self.require_size_box.clear()
        self.require_thk.clear()
        self.require_thk_box.clear()

        for widget in self.size_frame.winfo_children():
            widget.destroy()
            print("Sizing Deleted")

        
        #Label .........................................

        Height_Label=TK.Label(self.size_frame,text="Height")
        Fin_Label=TK.Label(self.size_frame,text="Fin")
        Width_Label=TK.Label(self.size_frame,text="Width")

        Thk1_Label=TK.Label(self.size_frame,text="Thickness 1")
        Thk2_Label=TK.Label(self.size_frame,text="Thickness 2")
        
        self.require_size.append(Height_Label)
        #self.require_size.append(Fin_Label)
        self.require_size.append(Width_Label)
        self.require_thk.append(Thk1_Label)
        self.require_thk.append(Thk2_Label)

        #DWG label
        #DWG_Label=TK.Label(self.size_frame)
        #self.require_size.append(DWG_Label)

        #Box ..............................................

        Height_Box=TK.Entry(self.size_frame,width=10)
        Fin_Box=TK.Entry(self.size_frame,width=10)
        Width_Box=TK.Entry(self.size_frame,width=10)

        Thk1_Box=TK.Entry(self.size_frame,width=10)
        Thk2_Box=TK.Entry(self.size_frame,width=10)

        self.require_size_box.append(Height_Box)
        #self.require_size_box.append(Fin_Box)
        self.require_size_box.append(Width_Box)
        self.require_thk_box.append(Thk1_Box)
        self.require_thk_box.append(Thk2_Box)

        # แสดงเป็น Widget

        Type_set= self.setting0_Type_combo.get()
        sq_type=["SQ","REC","L","Flat Bar","C-Lip"]

        if any (b==Type_set for b in sq_type):

            self.require_thk.remove(Thk2_Label)
            self.require_thk_box.remove(Thk2_Box)
            
            if Type_set == "C-Lip":
                self.require_size.append(Fin_Label)
                self.require_size_box.append(Fin_Box)

            if Type_set != "REC" and Type_set!= "C-Lip":
                self.require_size.remove(Height_Label)
                self.require_size_box.remove(Height_Box)
            
        
        #elif Type_set=="H-Beam" or Type_set=="Channel" or :
           
        elif Type_set=="Pipe" or Type_set=="Round Bar" or Type_set=="Square Bar":

            if Type_set!="Square Bar":    
                Width_Label.configure(text="Diameter")

            self.require_thk.remove(Thk2_Label)
            self.require_thk_box.remove(Thk2_Box)
            self.require_size.remove(Height_Label)
            self.require_size_box.remove(Height_Box)
            
            if Type_set=="Round Bar" or Type_set=="Square Bar":
                self.require_thk.remove(Thk1_Label)
                self.require_thk_box.remove(Thk1_Box)

        

            
                
        for i in range (len(self.require_size)):
            self.require_size[i].grid(row=i,column=0)
        for j in range (len(self.require_size_box)):
            self.require_size_box[j].grid(row=j,column =1)
        for a in range (len(self.require_thk)):
            self.require_thk[a].grid(row=a,column=2)
        for b in range (len(self.require_thk_box)):
            self.require_thk_box[b].grid(row=b,column=3)

        
        """self.Image.configure(image=self.image_library[Type_set])"""
        
        
        self.Return_Normal()
        
    def recheck_box(self,Input):
        try:
            float(Input.get())>0

            print("No Error E")

        except ValueError:
            self.Answer_Label.configure(text="Error E ค่าความยาวเต็มเส้น หรือ ขนาดของเหล็ก ไม่ได้ใส่")
            print("Error E")
            system.exit()
    
    def Remember (self):
        
        Complete_Spec_label =self.require_size +self.require_thk
        Complete_Spec_box =self.require_size_box + self.require_thk_box

        for i in range(len(Complete_Spec_label)):

            name=Complete_Spec_label[i].cget("text")
            self.recheck_box(Complete_Spec_box[i]) # เช็คว่ากล่องว่างไหม

            size= float(Complete_Spec_box[i].get())
            print(f"name = {name}, size = {size}")

            for a in self.Spec:
                if name == a :
                    self.Spec[a]= size
                    print(f"remember OK ,now a = {a}" )
                if name=="Diameter":
                    self.Spec["Width"]=size

        RM_name = self.setting0_RM_box.get()
        self.Spec["RM"]=RM_name
        RM_Type = self.setting0_Type_combo.get()
        self.Spec["Type"] = RM_Type

        self.recheck_box(self.setting0_Max_box)

        RM_Max = D.Decimal(self.setting0_Max_box.get())
        self.Spec["Max"]= RM_Max
     
        print(self.Spec)
 
    def Cut_Length_Qty(self):
        Safe=0
        print(f"len {len(self.Cut_Length)}")

        if len(self.Cut_Length) >0:
            Safe=1
        print(f"Safe {Safe}")

        if  Safe==0:

            Add_frame=TK.Frame(self.frame_for_boxes)
            Add_frame.grid(row=0,column=0)

            Add_Loop_box=TK.Entry(Add_frame,width=10)
            Add_Loop_box.grid(row=0,column=0)

            self.NO_Loop.append(Add_Loop_box)

            Add_button=TK.Button(Add_frame,text="Add All",fg="red",command=self.Add_box_from_Entry)
            Add_button.grid(row=0,column=1)

            Delete_button=TK.Button(Add_frame,text="Delete All",fg="Blue",command=self.Delete_All)
            Delete_button.grid(row=0,column=2)

            Add_1=TK.Button(Add_frame,text="<Add 1>",fg="red",command=self.Add_by_Click)
            Add_1.grid(row=1,column=1)

            Del_1=TK.Button(Add_frame,text="<Delete 1>",fg="Blue",command=self.Delete_by_Click)
            Del_1.grid(row=1,column=2)

            Add_Qty_Label=TK.Label(self.frame_for_boxes, text="Qty Need")
            Add_Qty_Label.grid(row=5,column=0)

            self.Create_Canvas()

    
    def Create_Canvas (self):
        
        if len(self.Cut_Length)>0:
            print("Error-0")
        else:
            
            print("OK")

    def Add_box_from_Entry(self):
        
        loop=int(self.NO_Loop[0].get())

        if len(self.Cut_Length)>0:
            self.Answer_Label.configure(text="กด Delete ก่อน",font=font_set)
        
        else:
            Leng=TK.Label(self.frame2,text="ความยาวที่ต้องการตัด",font=("AngsanaUPC",12),fg="Blue")
            Leng.grid(row=0,column=1)
            QT=TK.Label(self.frame2,text="จำนวนชิ้นที่ใช้",font=("AngsanaUPC",12),fg="Blue")
            QT.grid(row=0,column=2)

            print(f"Loop={loop}")
            for x in range(loop):
                NO_Label=TK.Label(self.frame2,text=f"NO.{len(self.Cut_Length)+1}",width=10)
                self.Cut_No.append(NO_Label)
                Length_Entry=TK.Entry(self.frame2,width=15)
                self.Cut_Length.append(Length_Entry)
                Qty_Entry=TK.Entry(self.frame2,width=15)
                self.Cut_Qty.append(Qty_Entry)
                
            for y in range(len(self.Cut_Length)):
                self.Cut_No[y].grid(row=y+1,column=0,sticky="SE")
                self.Cut_Length[y].grid(row=y+1,column=1)
                self.Cut_Qty[y].grid(row=y+1,column=2)

            self.Config_Scroll()

    def Add_by_Click(self):
        
        NO_Label=TK.Label(self.frame2,text=f"NO.{len(self.Cut_Length)+1}",width=10)
        self.Cut_No.append(NO_Label)
        Length_Entry=TK.Entry(self.frame2,width=15)
        self.Cut_Length.append(Length_Entry)
        Qty_Entry=TK.Entry(self.frame2,width=15)
        self.Cut_Qty.append(Qty_Entry)

        next=len(self.Cut_Length)-1

        self.Cut_No[next].grid(row=next+1,column=0)  
        self.Cut_Length[next].grid(row=next+1,column=1)
        self.Cut_Qty[next].grid(row=next+1,column=2)

        self.Config_Scroll()

    def Delete_by_Click(self):

        if len(self.Cut_Length)>0:

            last=len(self.Cut_Length)-1

            self.Cut_No[last].destroy()
            self.Cut_Length[last].destroy()
            self.Cut_Qty[last].destroy()

            self.Cut_No.pop(last)
            self.Cut_Length.pop(last)
            self.Cut_Qty.pop(last)
        else:
            self.Answer_Label.configure(text="ไม่มีให้ลบแล้ว",font=font_set)

        self.Config_Scroll()


    def Config_Scroll(self):
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.frame2.bind('<Configure>',lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def Delete_All(self):
        
        self.Cut_No.clear()
        self.Cut_Length.clear()
        print(self.Cut_Length)
        print(f"len cut length = {len(self.Cut_Length)}")
        self.Cut_Qty.clear()
        self.Answer_Label.configure(text="Result",font=font_set)

        for widget in self.frame2.winfo_children():
            widget.destroy()
            print("For calculation Deleted")
        
        self.Config_Scroll()

    def Go_Cal(self):
        self.Remember()
        Length_for_cal=[]
        Qty_for_cal=[]
        check_a=0
        check_b=0

        for en in (self.Cut_Length):
            try:
                float(en.get())>0
                check_a +=1
            except ValueError:
                self.Answer_Label.configure(text="Error A ช่องความยาวตัด ใส่ตัวเลขไม่ใช่ตัวอักษร หรือมีเครื่องหมายติดมา?"\
                                    ,font=font_set)
                break
        for qty in (self.Cut_Qty):
            try:
                float(qty.get())>0
                check_b +=1
            except ValueError:
                self.Answer_Label.configure(text="Error B ช่องจำนวนตัด ใส่ตัวเลขไม่ใช่ตัวอักษร หรือมีเครื่องหมายติดมา?"\
                                    ,font=font_set)
                break
        

        print(f" Check a = {check_a}")
        print(f"Check b = {check_b}")

        if check_a>0 and check_b>0:
            for i in range(len(self.Cut_Length)):
                num_L=D.Decimal(self.Cut_Length[i].get())
                num_Q=int(self.Cut_Qty[i].get())
                Length_for_cal.append(num_L)
                Qty_for_cal.append(num_Q)
        

        if any (b> self.Spec["Max"] for b in Length_for_cal):
            self.Answer_Label.configure(text="Error D : มีค่าความยาวตัด มากกกว่า ค่าความยาวเต็มเส้น")
            print("Error D")
            return


        
        
        Final_ANS=CAL.Call(Length_for_cal,Qty_for_cal,self.Spec)
        Final_ANS.Calu()
        ANS = Final_ANS.Result()

        self.Answer_Label.configure(text=ANS,font=font_set)

"""root=TK.Tk()
root.title("Testing")

Test1=Box(root,0,0)



root.mainloop()"""