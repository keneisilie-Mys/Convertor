import tkinter as tkr
###############################################################################
#     CALCULATOR
def screen(entry,a):  #for claculator
    entry.insert("end",a)

def equal_to(entry):  #for claculator
    exp=entry.get()
    exp=exp.replace('x','*') #replacing * with x
    calc=eval(exp)
    entry.delete(0,"end")
    entry.insert(0,calc)

def clear(entry):  #for claculator
    entry.delete(0,"end")

def del_char(entry):   #for claculator
    size=len(entry.get())
    entry.delete(size-1, "end")

def delete():    
    for frames in frame.winfo_children():
        frames.destroy()

def calculator():
    delete()
    cal_frame=tkr.Frame(frame,height=300,width=300, bg="#EC5858")
    f1=tkr.Frame(cal_frame)
    f2=tkr.Frame(cal_frame,bg="#EC5858")
    f3=tkr.Frame(cal_frame)
    entry=tkr.Entry(f1, width=40,font=("Arial",12))
    entry.pack()
    butt0=tkr.Button(f2, text="0",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,0))
    butt1=tkr.Button(f2, text="1",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,1))
    butt2=tkr.Button(f2, text="2",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,2))
    butt3=tkr.Button(f2, text="3",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,3))
    butt4=tkr.Button(f2, text="4",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,4))
    butt5=tkr.Button(f2, text="5",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,5))
    butt6=tkr.Button(f2, text="6",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,6))
    butt7=tkr.Button(f2, text="7",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,7))
    butt8=tkr.Button(f2, text="8",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,8))
    butt9=tkr.Button(f2, text="9",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,9))
    butt_add=tkr.Button(f2, text="+",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,"+"))
    butt_sub=tkr.Button(f2, text="-",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,"-"))
    butt_mul=tkr.Button(f2, text="X",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,"x"))
    butt_div=tkr.Button(f2, text="/",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:screen(entry,"/"))
    buttdel=tkr.Button(f2, text="del",height=2,width=4, bg="#EC5858",font="Arial", command=lambda:del_char(entry))
    butteq=tkr.Button(f2, text="=",height=2,width=4,bg="#bee0ec",font="Arial", command=lambda:equal_to(entry))
    butt_clear=tkr.Button(cal_frame,text="AC", height=2, width=5,font="Arial", command=lambda:clear(entry))

    butt0.grid(row=3,column=0,padx=1,pady=1)
    butt_div.grid(row=3, column=3,padx=1,pady=1)
    butt1.grid(row=0,column=0,padx=1,pady=1)
    butt2.grid(row=0,column=1,padx=1,pady=1)
    butt3.grid(row=0,column=2,padx=1,pady=1)
    butt_add.grid(row=0, column=3,padx=1,pady=1)
    butt4.grid(row=1,column=0,padx=1,pady=1)
    butt5.grid(row=1,column=1,padx=1,pady=1)
    butt6.grid(row=1,column=2,padx=1,pady=1)
    butt_sub.grid(row=1, column=3,padx=1,pady=1)
    butt7.grid(row=2,column=0,padx=1,pady=1)
    butt8.grid(row=2,column=1,padx=1,pady=1)
    butt9.grid(row=2,column=2,padx=1,pady=1)
    butt_mul.grid(row=2, column=3,padx=1,pady=1)
    buttdel.grid(row=3, column=2,padx=1,pady=1)
    butteq.grid(row=3, column=1,padx=1,pady=1)
    butt_clear.place(x=300,y=53)

    f1.pack(pady=15)
    f2.pack()
    f3.pack()
    cal_frame.pack()

#######################################################################################################
def home():

    delete()
    home_page=tkr.Frame(frame,bg="#EC5858")
    label_h2=tkr.Label(home_page,bg="#EC5858",text="\n\n\n\n\nWelcome!\n\nClick the PROGRAM menu to perform \ndifferent operations.", font=("Arial",15))
    label_h2.pack()
    home_page.pack()
#####################################################################################################
#   GLOBAL FOR UNIT CONVERTERS
def clear_u(k_entry,m_label): 
    k_entry.delete(0,"end")
    m_label.config(text="")

def adjust_len(ans):
    stri="Answer's length exceeded"
    return stri

def con(entry, label, type):
    if (type=="distance"):
        a=float(entry.get())
        ans=a*1000
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

    if (type=="length"):
        a=float(entry.get())
        ans=a/2.54
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

    if (type=="temperature"):
        a=float(entry.get())
        ans=(a*(9/5))+32
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

    if(type=="distance_rev"):
        a=float(entry.get())
        ans=a/1000
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

    if (type=="length_rev"):
        a=float(entry.get())
        ans=a*2.54
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

    if (type=="temperature_rev"):
        a=float(entry.get())
        ans=(a-32)*(5/9)
        ans=str(ans)
        if(len(ans)>20):
            ans=adjust_len(ans)
        label.config(text="")
        label.config(text=ans)

#####################################################################################################
#    FOR CECLIUS TO FARENHEIT
def temp_con(main_frame):
    temp_frame=tkr.Frame(main_frame)
    a="temperature"

    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    cl_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    cl_uni=tkr.Label(f1, text="CELSIUS",bg="#EC5858",font="Arial")
    f_label=tkr.Label(f2, width=20,font=("Arial",12))
    f_uni=tkr.Label(f2,text="FAHRENHEIT",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(cl_entry,f_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame, temp_con_rev))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(cl_entry,f_label))

    #packing contents
    cl_entry.pack()
    cl_uni.pack()
    f_label.pack()
    f_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    temp_frame.pack() #main
###################################################################3##################################
#    FOR LENGTH CONVERTER  CM TO INCHES
def len_con(main_frame):  #length converter
    len_frame=tkr.Frame(main_frame)
    a="length"

    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    c_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    c_uni=tkr.Label(f1, text="CM",bg="#EC5858",font="Arial")
    i_label=tkr.Label(f2, width=20,font=("Arial",12))
    i_uni=tkr.Label(f2,text="INCHES",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(c_entry,i_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame, len_con_rev))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(c_entry,i_label))

    #packing contents
    c_entry.pack()
    c_uni.pack()
    i_label.pack()
    i_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    len_frame.pack() #main
#####################################################################################################
#   FOR DISTANCE COVERT (KM TO METRES)
def dis_con(main_frame):  #Distance converter
    dis_frame=tkr.Frame(main_frame)
    a="distance"
    b="hehe"

    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    k_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    k_uni=tkr.Label(f1, text="KM",bg="#EC5858",font="Arial")
    m_label=tkr.Label(f2, width=20,font=("Arial",12))
    m_uni=tkr.Label(f2,text="Metre",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(k_entry,m_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame,dis_con_rev))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(k_entry,m_label))

    #packing contents
    k_entry.pack()
    k_uni.pack()
    m_label.pack()
    m_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    dis_frame.pack() #main
############################################################################################################
#   FOR CHANGE
def change(main_frame,frame_2pack):
    for frames in main_frame.winfo_children():
        frames.destroy()
    frame_2pack(main_frame)
############################################################################################################
#   FOR   REVERSE
def dis_con_rev(main_frame):

    dis_frame2=tkr.Frame(main_frame)
    a="distance_rev"
    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    k_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    k_uni=tkr.Label(f1, text="Metre",bg="#EC5858",font="Arial")
    m_label=tkr.Label(f2, width=20,font=("Arial",12))
    m_uni=tkr.Label(f2,text="KM",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(k_entry,m_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame, dis_con))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(k_entry,m_label))

    #packing contents
    k_entry.pack()
    k_uni.pack()
    m_label.pack()
    m_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    dis_frame2.pack() #main

def len_con_rev(main_frame):
    len_frame2=tkr.Frame(main_frame)
    a="length_rev"

    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    c_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    c_uni=tkr.Label(f1, text="INCHES",bg="#EC5858",font="Arial")
    i_label=tkr.Label(f2, width=20,font=("Arial",12))
    i_uni=tkr.Label(f2,text="CM",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(c_entry,i_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame, len_con))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(c_entry,i_label))

    #packing contents
    c_entry.pack()
    c_uni.pack()
    i_label.pack()
    i_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    len_frame2.pack() #main

def temp_con_rev(main_frame):
    temp_frame2=tkr.Frame(main_frame)
    a="temperature_rev"

    f1=tkr.Frame(main_frame,bg="#EC5858")
    f2=tkr.Frame(main_frame,bg="#EC5858")
    f3=tkr.Frame(main_frame,bg="#EC5858")

    #Creating contents
    cl_entry=tkr.Entry(f1, width=20,font=("Arial",12))
    cl_uni=tkr.Label(f1, text="FAHRENHEIT",bg="#EC5858",font="Arial")
    f_label=tkr.Label(f2, width=20,font=("Arial",12))
    f_uni=tkr.Label(f2,text="CELSIUS",bg="#EC5858",font="Arial")
    butt_con=tkr.Button(f3, text="Convert",bg="#bee0ec",font="Arial",command=lambda:con(cl_entry,f_label, a))
    butt_change=tkr.Button(f3, text="Change Unit",bg="#bee0ec",font="Arial",command=lambda:change(main_frame, temp_con))
    butt_clear=tkr.Button(main_frame, text="Clear",font="Arial",bg="#bee0ec",command=lambda:clear_u(cl_entry,f_label))

    #packing contents
    cl_entry.pack()
    cl_uni.pack()
    f_label.pack()
    f_uni.pack()
    butt_con.grid(row=0,column=0)
    butt_change.grid(row=0,column=1)

    #packing frames
    f1.pack(pady=14)
    f2.pack()
    f3.pack(pady=14)
    butt_clear.pack()

    temp_frame2.pack() #main
############################################################################################################
#   UNIT CONVERTER MAIN FRAME
def show_ind(bg,bgs,bgt,fun,main_frame):
    hide_ind(bg,bgs,bgt)
    bg.config(bg="#EC5858")
    for frames in main_frame.winfo_children():
        frames.destroy()
    fun(main_frame)  #this willl go to any frame

def hide_ind(bg,bgs,bgt):
    bg.config(bg="#bee0ec")
    bgs.config(bg="#bee0ec")
    bgt.config(bg="#bee0ec")

def main_con():   
    delete()
    main_frame=tkr.Frame(frame, bg="#EC5858", height=400, width=250)
    nav_frame=tkr.Frame(frame, bg="#bee0ec", height=400, width=150)
    
    bg1=tkr.Label(nav_frame, text="",bg="#EC5858", width=1, font=("Arial",19))
    bg2=tkr.Label(nav_frame, text="",bg="#bee0ec", width=1, font=("Arial",19))
    bg3=tkr.Label(nav_frame, text="",bg="#bee0ec", width=1, font=("Arial",19))

    distance=tkr.Button(nav_frame, text="Distance", bd=0,font="Arial", bg="#bee0ec", command=lambda:show_ind(bg1,bg2,bg3,dis_con,main_frame))
    temp=tkr.Button(nav_frame, text="Temperature", bd=0, font="Arial", bg="#bee0ec",command=lambda:show_ind(bg2,bg1,bg3,temp_con, main_frame))
    cent=tkr.Button(nav_frame, text="Length", bd=0, font="Arial", bg="#bee0ec", command=lambda:show_ind(bg3,bg2,bg1,len_con,main_frame))

    bg1.place(x=5, y=85)
    bg2.place(x=5, y=135)
    bg3.place(x=5, y=185)

    distance.place(x=13, y=85)
    temp.place(x=13, y=135)
    cent.place(x=13, y=185)

    nav_frame.pack(side=tkr.LEFT)
    nav_frame.pack_propagate(False)
    main_frame.pack(side=tkr.RIGHT)
    main_frame.pack_propagate(False)

    dis_con(main_frame)

############################################################################################  
root=tkr.Tk()
root.title("TKINTER")
root.geometry("400x400")
root.config(bg="#EC5858")

frame=tkr.Frame(root, height=400, width=400, bg="#EC5858", highlightthickness=2)

menu1 = tkr.Menu(root, font="Arial")
menu_in = tkr.Menu(menu1,tearoff=0, font=("Arial",10)) #tearoff removes the dottlines in menu
menu_in.add_command(label="Home", command=lambda:home())
menu_in.add_separator() #adds a line
menu_in.add_command(label="Calculator", command=lambda:calculator())
menu_in.add_command(label="Unit Converter",command=lambda:main_con())
menu_in.add_command(label="Exit", command=lambda:root.destroy())
menu1.add_cascade(label="PROGRAMS", menu=menu_in)
root.config(menu=menu1)

home() #initial frame

frame.pack(expand=True)#expand rezizes the paddings according to screen size
frame.pack_propagate(False) #prevents the frame from resizing to wrap the widgets

root.mainloop()