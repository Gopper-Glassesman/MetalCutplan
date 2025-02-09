import tkinter as tk
from Boxcreate import Box
from tkinter import ttk 

self = tk.Tk()
self.title("Program ตัดเหล็ก")

self.geometry("500x600")

font_set="TH SarabunPSK",12,"bold"


# Create a Canvas widget
canvas = tk.Canvas(self)
canvas.grid(row=0, column=0, sticky="nsew")

# Create vertical and horizontal scrollbars
vsb = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
hsb = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        
# Pack the scrollbars to the right and bottom
vsb.grid(row=0, column=1, sticky="ns")
hsb.grid(row=2, column=0, sticky="ew")
        
# Create a Frame inside the Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")
        
# Configure the Canvas scrollbars
canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
Top_frame=tk.LabelFrame(frame,text="Create Member")
Top_frame.grid(row=0,column=0,sticky="w")

Entry_box = tk.Entry(Top_frame,width=10)
Entry_box.grid(row=0,column=1)

Entry_box_Create=tk.Button(Top_frame,text="Create")
Entry_box_Create.grid(row=0,column=2)

Entry_1box_create=tk.Button(Top_frame,text="Create 1 Mem")
Entry_1box_create.grid(row=1,column=2)

Destroy_box=tk.Button(Top_frame,text="Delete All Member",fg="Blue")
Destroy_box.grid(row=0,column=3)

Monitor_Label=tk.Label(Top_frame,text="Create Entry",font=font_set)
Monitor_Label.grid(row=2,column=2)


frame_store_member=tk.Frame(frame)
frame_store_member.grid(row=1,column=0)

def On_frame_configure(event=None):
    # Update the scroll region of the Canvas
    canvas.configure(scrollregion=canvas.bbox("all"))


"""test_label=TK.Label(Frame_for_Entry,text="Testing")
test_label.grid(row=0,column=0)"""
main_frame=[]

def Create_Entry():
    if len(main_frame)>0:
        Monitor_Label.configure(text="<กด Delete ก่อน>",fg="red")
    
    else:
       
        for i in range(0,int(Entry_box.get())):
            E_Entry=Box(frame_store_member,1,i)
            main_frame.append(E_Entry)

    On_frame_configure()
        
def Add_1_Member():
    last=len(main_frame)
    E_Entry=Box(frame_store_member,1,last)
    main_frame.append(E_Entry)
    On_frame_configure()

def Destroy_Frame():
    w=0
    for widget in frame_store_member.winfo_children():
        widget.destroy()
        main_frame.clear()
    Monitor_Label.configure(text="<Create Entry>",fg="black")
    On_frame_configure()
       
# Bind the Frame resize event
frame_store_member.bind("<Configure>",On_frame_configure)
        
# Configure grid weights
self.grid_columnconfigure(0, weight=1)
self.grid_rowconfigure(0, weight=1)
self.grid_rowconfigure(1, weight=0)
self.grid_columnconfigure(1, weight=0)

Entry_box_Create.configure(command=Create_Entry)
Entry_1box_create.configure(command=Add_1_Member)
Destroy_box.configure(command=Destroy_Frame)


self.mainloop()

"""    
#.........................................................................

main_label=TK.LabelFrame(firstframe,text="Main")
main_label.grid(row=0,column=0,padx=5,pady=10)

#เซต ความยาวเหล็กเส้น......................................................................................
setting0_label=TK.Label(main_label,text="รูปทรง โลหะ",font=("AngsanaUPC",12))
setting0_label.grid(row=0,column=1)

setting0_type=TK.Label(main_label,text="ชนิดโลหะ",font=("AngsanaUPC",12))
setting0_type.grid(row=2,column=1)
"""
