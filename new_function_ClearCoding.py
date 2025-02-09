
"""Calculate part  update 20/8/24"""
import decimal
import math
Data={"Steel":{"Density":7850},
      "Stainless 304":{"Density": 7930 },
      "Stainless 316": {"Density": 7870 },
      "Aluminum 1050": {"Density": 2710}
      }

#Start Here........................................................
class Call ():
    def __init__(self,use,useqt,spec) :
        self.use_length=use
        self.use_qty=useqt
        self.Max_length=spec["Max"]
        self.arranged_length=[]
        self.arranged_qty=[]
        self.answer=0   #จำนวนเส้นที่ต้องซื้อ 
        self.RM=spec["RM"]
        self.RM_Type=spec["Type"]
        self.face_Height=decimal.Decimal(spec["Height"]/1000)
        self.face_Fin=decimal.Decimal(spec["Fin"]/1000)
        self.face_Width=decimal.Decimal(spec["Width"]/1000)
        self.face_Thick01= decimal.Decimal(spec["Thickness 1"]/1000)
        self.face_Thick02= decimal.Decimal(spec["Thickness 2"]/1000)
        self.Area = 0
        self.Volume=0
        self.Weight=0
        self.Final_Answer=""
    
    def Skin (self):
        total_Length=0
        H=self.face_Height
        F=self.face_Fin
        W=self.face_Width
        T=self.face_Thick01
        T2=self.face_Thick02
        Area=0
        Volume=0

        for i in range(len(self.use_qty)):
            total_Length+=decimal.Decimal(self.use_length[i]*self.use_qty[i])
            print(f"total_Length = {total_Length}")

        if self.RM_Type== "SQ" or self.RM_Type=="REC" or self.RM_Type=="L":
            print("Area SQ")
            if self.RM_Type =="SQ" or self.RM_Type=="L":
                H=W
            print(f"Height = {H}")
            print(f"Width = {W}")
            Area = decimal.Decimal((H*2+W*2)*total_Length)
            Volume= (T*(2*H+2*W-4*T))*total_Length

        if self.RM_Type=="Flat Bar":
            print("Area FB")
            Area=decimal.Decimal((W*2+T*2)*total_Length)
            Volume= W*T*total_Length

        if self.RM_Type=="Pipe"or self.RM_Type=="Round Bar":
            Area=decimal.Decimal(decimal.Decimal(math.pi)*W*total_Length)
            Volume=decimal.Decimal(1 / 4) *decimal.Decimal(math.pi)*(W**2)*total_Length
            if self.RM_Type=="Pipe":
                Volume = decimal.Decimal(math.pi) *(W*W/4 - (W-T*2)*(W-T*2)/4)*total_Length
        
        if self.RM_Type=="Square Bar":
            Area=decimal.Decimal((W*4)*total_Length)
            Volume=decimal.Decimal(W*W*total_Length)

        if self.RM_Type=="H-Beam" or self.RM_Type=="Channel":
            Area=decimal.Decimal((W*4 +H*2)*total_Length)
            Volume= (2*(W*T2)+(H-2*T2)*T)*total_Length

        if self.RM_Type== "C-Lip":
            Area=decimal.Decimal((W*4+H*2+F*4)*total_Length)
            Volume= (2*(W*T)+(H-2*T)*T+2*(F-T)*T)*total_Length

        self.Area=Area
        self.Volume= Volume
        
#*****************************************************

    def Weight_Cal (self):

        Weight = self.Volume*Data[self.RM]["Density"]
        
        self.Weight=Weight
        
#*****************************************************

    def Rearrange(self):
        #เรียงลำดับ ค่าความยาวจากมากไปน้อย.....................................................
        inputlist=self.use_length
        inputqty=self.use_qty
        Arranged_len=self.arranged_length
        Arranged_qty=self.arranged_qty
        while inputlist !=[]:
            Max=max(inputlist)
            Location= inputlist.index(Max)
            Arranged_len.append(inputlist[Location])
            Arranged_qty.append(inputqty[Location])
            inputlist.pop(Location)
            inputqty.pop(Location)
    
#*****************************************************

    def Calu (self):
        self.Skin()
        self.Weight_Cal()
        self.Rearrange()
        Arranged_len=self.arranged_length
        Arranged_qty=self.arranged_qty
        Final_Answer=""
        
        print("*****start****")

        print(Arranged_len)

        print(Arranged_qty)

        while Arranged_qty!=[]:
            Answer_len=[]
            Answer_qty=[]
            Present_Maxlength=self.Max_length
            Mark_Locate=[]
            Multipler=[] #ตัวคูณเพิ่ม เผื่อว่าเศาที่เหลือสามารถตัดค่าuse ได้มากกว่า 1 ครั้ง   มันจะเอาไปใช้*ตอนตัคค่า useqt
            for i in range(len(Arranged_len)):
                print(f"******ความยาวที่หยิบมา    +   {Arranged_len[i]} ")
                A=decimal.Decimal(Present_Maxlength/decimal.Decimal(Arranged_len[i]))#maxจำนวนชิ้นที่ตัดได้ เช่น max 6m/ ชิ้นละ 1.8m = 3.333ชิ้น =A
                AA=int(A)# ตัดเศษ กรณีมีเศษ
                print(f"AA = {AA}")

                if Arranged_qty[i]<=AA:
                    AA=Arranged_qty[i]
                    print(" RE AA = "+str(AA))
                
                if AA==0:
                    continue

                Present_Maxlength=decimal.Decimal(Present_Maxlength-(AA*decimal.Decimal(Arranged_len[i])))
                print("New_Maxlength = "+str(Present_Maxlength))
                Mark_Locate.append(i)
                Multipler.append(AA)
                print("Marked")
            print("Member of Mark")
            #Mark คือ ตำแหน่ง index ของ Arranged_qty ที่ เราจะเอาไปพิจารณา ตัดว่าตัวไหนน้อยสุด เช่น len=[2.5,1.5,1] qty= [2,5,3]
            #เมื่อพิจารณาตามcodeด้านบนแล้ว  จะได้Mark iที่ 0,2 ,Multiplier 2,1 เพราะ1/1.5=0.06 ตัดเศาเหลือ 0 ไม่เข้าเงื่อนไข AA      
            Find_min_b=[] #array ที่สร้างมาเพื่อเก็บค่า qty ที่มีส่วนเกี่วข้องกับloopนี้
            #เอาindex j เพื้อสร้าง ชุด Array qty ที่ถูกใช่ เพื่อหาค่า minimun qty ที่จะโดนตัด
            for j in Mark_Locate:
                Find_min_b.append(Arranged_qty[j])
            print("SetของFind min b")
            print(Find_min_b)  

            Find_min_b_divided=[]
            for m,n in zip (Find_min_b,Multipler):
                Devided=int(m/n)
                Find_min_b_divided.append(Devided) #ทำเพื่อหาจำนววนเส้นของmember ในuse ที่น้อยที่สุดที่จะหมดก่อน

            print("SetของFind min b Devided")
            print(Find_min_b_divided)
            
            Value_min_b=min(Find_min_b_divided)
            print("Value_min_b ="+str(Value_min_b))
            #Value_min_b  คือ ค่า useqt ที่น้อยที่สุด หรือก็คือ จำนวนเส้นที่เราจะใช้ในloop นี้

            min_b_index=Find_min_b_divided.index(Value_min_b) #หาตำแหน่งตัวที่หมดก่อนจากในlist
            print("min_b_index ="+str(min_b_index))
            #ค่า index สำหรับเป็นฐานแล้ว*multiply เพื่อ pop เอา A,B ใน use,useqt ออกทีหลัง
            #index_for_pop=useqt.index(Value_min_b)
            min_b_for_erase=[]
            
            for r in Multipler:
                f=Value_min_b*r
                min_b_for_erase.append(f)


       
            for a in Mark_Locate :
                Answer_len.append(Arranged_len[a])
            for b in range(len(Multipler)) :    
                Answer_qty.append(Multipler[b])
            row_detect=1
            Loop_Answer=""

            for f,g in zip(Answer_len,Answer_qty):
                if (row_detect % 4) == 0:
                    Loop_Answer = Loop_Answer + "\n"

                Loop_Answer= Loop_Answer + f"Len-{f}m.:Qty{g}  " 
                row_detect+=1
            Loop_Answer += f" จน.เส้น:{Value_min_b}"
            Final_Answer += f"{Loop_Answer} \n \t"
            self.answer += Value_min_b
            print(Loop_Answer) #  สรุปแผนตัด Loop นี้  1เส้ร ได้ความยาวเท่าไหร่ กี่ชิ้น  ทำตามนี้ได้กี่เส้น 
            

            for j,l in zip(Mark_Locate,min_b_for_erase):
                Arranged_qty[j]=Arranged_qty[j]-l #ตัดเหล็ก  เอาจำนวนตัวที่ตัดแล้วออก
                print("nowwwwwww useqt")
                print(Arranged_qty)
            
            while any (b==0 for b in Arranged_qty): #คัดเอา qt ที่เหลือ0 ออก แล้ว ตัด length ที่ qt หมดแล้วออก
                B=Arranged_qty.index(0)
                Arranged_len.pop(B)
                Arranged_qty.pop(B)
                print("Popแล้วเหลือ")
                print(Arranged_qty)

            print("Final useqt")
            print(Arranged_qty)
            self.Final_Answer=Final_Answer
            
#*****************************************************

    def Result (self):

        Answer=f"""
        XXX    Result   XXX
        {self.Final_Answer}
        ต้องซื้อ {self.answer} เส้น
        พท.ผิวรวม = {round(self.Area,3)} sq.m.
        นน.รวม = {round(self.Weight,3)} Kg
        """
        print(Answer)

        return Answer

        """print("XXX    Result   XXX")
        print(self.Final_Answer)
        print(f"ต้องซื้อ {self.answer} เส้น")
        print(f"พท.ผิวรวม = {round(self.Area,3)} sq.m.")
        print(f"Volume {self.Volume}")
        print(f"นน.รวม = {round(self.Weight,3)} Kg")"""

#*****************************************************


"""
    Answer=0
    while useqt!=[]:

        Cut=M
        Mark=[]
        Multipler=[] #ตัวคูณเพิ่ม เผื่อว่าเศาที่เหลือสามารถตัดค่าuse ได้มากกว่า 1 ครั้ง   มันจะเอาไปใช้*ตอนตัคค่า useqt
        for i in range(len(use)):
            
            A=Decimal(Cut/Decimal(use[i]))
            AA=int(A)
            print("AA = "+str(AA))

            if useqt[i]<=AA:
                AA=useqt[i]
                print(" RE AA = "+str(AA))

            elif AA>=1:
                Cut=Decimal(Cut-(AA*Decimal(use[i])))
                print("Cut = "+str(Cut))
                Mark.append(i)
                Multipler.append(AA)
            print(Mark)

        print("Member of Mark")
        print(Mark)
        #Mark คือ ตำแหน่ง index ของ useqt ที่ คู่กับ use  ที่จะต้องเอาไปลดจำนวน 
        Find_min_b=[] #array ที่สร้างมาเพื่อเก็บค่า qt ที่มีส่วนเกี่วข้องกับloopนี้
        #เอาindex j เพื้อสร้าง ชุด Array qty ที่ถูกใช่ เพื่อหาค่า minimun qty ที่จะโดนตัด
        for j in Mark:
            Find_min_b.append(useqt[j])
        print("SetของFind min b")
        print(Find_min_b)

        Find_min_b_divided=[]
        for m,n in zip (Find_min_b,Multipler):
            Devided=int(m/n)
            Find_min_b_divided.append(int(Devided)) #ทำเพื่อหาจำนววนเส้นของmember ในuse ที่น้อยที่สุดที่จะหมดก่อน

        print("SetของFind min b Devided")
        print(Find_min_b_divided)



        Value_min_b=min(Find_min_b_divided)
        print("Value_min_b ="+str(Value_min_b))
        #Value_min_b  คือ ค่า useqt ที่น้อยที่สุด หรือก็คือ จำนวนเส้นที่เราจะใช้ในloop นี้
        min_b_index=Find_min_b_divided.index(Value_min_b)
        print("min_b_index ="+str(min_b_index))

        #ค่า index สำหรับ pop เอา A,B ใน use,useqt ออก
        #index_for_pop=useqt.index(Value_min_b)
        min_b_for_erase=[]
        for r in Multipler:
            f=Value_min_b*r
            min_b_for_erase.append(f)
            
        print("min_b = "+str(Value_min_b))
        #คำตอบของลูปนี้
        Answer=Answer+Value_min_b

        for j,l in zip(Mark,min_b_for_erase):
            useqt[j]=useqt[j]-l
            print("nowwwwwww useqt")
            print(useqt)
        
        while any (b==0 for b in useqt):
            B=useqt.index(0)
            use.pop(B)
            useqt.pop(B)
            print("Popแล้วเหลือ")
            print(useqt)
            
        """
"""

        for p in for_pop:
            use.pop(p)
            useqt.pop(p)

             
        print("new useqt")
        print(useqt)

    #End here.............................................................

    print("final Array Valur for this loop")
    print(use)
    print(useqt)
    print("Final Answer == " +str(Answer))
    return Answer"""


#test syntax

"""AA =[ 5,1,2.6 ]
XXuseqt=[1,30,15]
F=6
spec={"RM":"Aluminum 1050","Type":"SQ","Height":50,
      "Height2":0,"Width": 50,"Thickness 1": 2.3,"Thickness 2": 0,"Max":6 }

P=Call(AA, XXuseqt ,spec)

P.Calu()
P.Result()"""
