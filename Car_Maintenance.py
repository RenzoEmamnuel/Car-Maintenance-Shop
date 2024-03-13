from tkinter import *
from datetime import datetime
import pytz

root = Tk()
root.geometry("740x400")
root.config(bg="#EEEEEE")
root.title("mid_LA2")

def submit():
    total = 0
    lbl_shopname.config(text="Car Maintenance")
    lbl_time_and_date.config(text="")
    datetime_in_ph = datetime.now(pytz.timezone("Asia/Manila"))
    formated_date_time = datetime_in_ph.strftime("%B %d, %Y , %I:%M:%S %p")
    lbl_time_and_date.config(text=formated_date_time)

    lbl_line.config(text="--------------------------------------------------------")
    #######################################################
    if option_car.get()==1:
        lbl_cartype.config(text = " Car Type    : BMW                 ----  P 5,000.00")
        total += 5000
    elif option_car.get()==2:
        lbl_cartype.config(text = " Car Type    : Subaru              ----  P 2,500.00")
        total += 2500
    elif  option_car.get()==3:
        lbl_cartype.config(text=" Car Type    : Chevrolet           ----  P 4,100.00")
        total += 4100
    else:
        pass
    #######################################################
    if interior_option1.get() == 1 and interior_option2.get() == 1:
        lbl_interior_option.config(text=" Interior  : Leather             ----  P 550.00\n             : GPS                 ----  P 1,000.00")
        total += 1550

    elif interior_option1.get() == 1:
        lbl_interior_option.config(text=" Interior    : Leather             ----  P 550.00")
        total += 550

    elif interior_option2.get() == 1:
        lbl_interior_option.config(text=" Interior    : GPS                 ----  P 1,000.00")
        total += 1000

    else:
        pass
    #######################################################
    if option_exterior.get() == 1:
        lbl_exterior_frame2.config(text=" Exterior(F) : Hard Top            ----   ")
    if option_exterior.get() == 2:
        lbl_exterior_frame2.config(text=" Exterior(F) : Convertible         ----   ")
    else:
        pass
    #######################################################
    if checkbox_wheel1.get() == 1 and checkbox_wheel2.get() == 1:
        lbl_exterior_finish_frame_2.config(text=" Exterior(O) : Wheel Upgrade       ----  P 1,000.00\n"
                                                "             : Performance Package ----  P 2,000.00")
        total+= 3000
    elif checkbox_wheel1.get() == 1:
        lbl_exterior_finish_frame_2.config(text=" Exterior(O) : Wheel Upgrade       ----  P 1,000.00")
        total += 1000
    elif checkbox_wheel2.get() == 1:
        lbl_exterior_finish_frame_2.config(text=" Exterior(O) : Performance Package ----  P 2,000.00")
        total += 2000
    else:
        pass


    lbl_space1.config(text="--------------------------------------------------------")
    lbl_space2.config(text=" ")
    lbl_space3.config(text="")
    lbl_total.config(text=f"Total Amount: {total}      ")
    lbl_space4.config(text="")
    lbl_space5.config(text="")
    lbl_thankyou.config(text="Thankyou!")
# Frame_1
frame_1 = Frame(root, width=210, height=390, bg="#76ABAE")
frame_1.pack(side="left", padx=5)
frame_1.pack_propagate(False)
####################################################################################################################
lbl_car = Label(frame_1,text="Car Type",font=("corier",15,"bold"),bg="#76ABAE")
lbl_car.pack(anchor="w")

option_car= IntVar()

BMW_radiobutton = Radiobutton(frame_1,text= "BMW",value=1,variable=option_car,bg="#76ABAE")
BMW_radiobutton.pack(anchor="w")
Subaru_radiobutton = Radiobutton(frame_1,text= "Subaru",value=2,variable=option_car,bg="#76ABAE")
Subaru_radiobutton.pack(anchor="w")
Chevrolet_radiobutton = Radiobutton(frame_1,text= "Chevrolet",value=3,variable=option_car,bg="#76ABAE")
Chevrolet_radiobutton.pack(anchor="w")

####################################################################################################################
interior_option1 = IntVar()
interior_option2 = IntVar()

lbl_interior = Label(frame_1,text="Interior Option",font=("corier",15,"bold"),bg="#76ABAE")
lbl_interior.pack(anchor="w")
checkbox_lether = Checkbutton(frame_1, text="Leather", variable = interior_option1,offvalue=0,onvalue=1,bg="#76ABAE")
checkbox_lether.pack(anchor="w")
checkbox_gps = Checkbutton(frame_1, text="GPS", variable = interior_option2,offvalue=0,onvalue=1,bg="#76ABAE")
checkbox_gps.pack(anchor="w")

####################################################################################################################
option_exterior = IntVar()

lbl_exterior_finish  = Label(frame_1,text="Exterior Finish",font=("corier",15,"bold"),bg="#76ABAE")
lbl_exterior_finish.pack(anchor="w")
rdb_hardtop = Radiobutton(frame_1,text= "Hard Top",value=1,variable=option_exterior,bg="#76ABAE")
rdb_hardtop.pack(anchor="w")
rdb_covertible = Radiobutton(frame_1,text= "Convertible",value=2,variable=option_exterior,bg="#76ABAE")
rdb_covertible.pack(anchor="w")

####################################################################################################################
checkbox_wheel1= IntVar()
checkbox_wheel2 =IntVar()

lbl_exterior_option  = Label(frame_1,text="Exterior Option",font=("corier",15,"bold"),bg="#76ABAE")
lbl_exterior_option.pack(anchor="w")
checkbox_wheel = Checkbutton(frame_1, text="Wheel Upgrade", variable = checkbox_wheel1,offvalue=0,onvalue=1,bg="#76ABAE")
checkbox_wheel.pack(anchor="w")
checkbox_performance = Checkbutton(frame_1, text="Performance Package", variable = checkbox_wheel2,offvalue=0,onvalue=1,bg="#76ABAE")
checkbox_performance.pack(anchor="w")

btn_submit = Button(frame_1,text="Submit",command=submit,width=20,height=2,font=("Ariel",10,"bold"))
btn_submit.pack(pady=3)

####################################################################################################################

# Frame_2
frame_2 = Frame(root, width=510, height=390, bg="#76ABAE")
frame_2.pack(side="right", padx=5)
frame_2.pack_propagate(False)

lbl_shopname = Label(frame_2,text="",font=("courier",15,"bold"),bg="#76ABAE")
lbl_shopname.pack()
lbl_time_and_date = Label(frame_2,text="",font=("courier",11,"bold"),bg="#76ABAE")
lbl_time_and_date.pack()
lbl_line = Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_line.pack()
lbl_cartype = Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_cartype.pack(anchor="w")
lbl_interior_option =Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_interior_option.pack(anchor="w")
lbl_exterior_frame2 = Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_exterior_frame2.pack(anchor="w")
lbl_exterior_finish_frame_2 = Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_exterior_finish_frame_2.pack(anchor="w")
lbl_space1 = Label(frame_2,text="",bg="#76ABAE",font=("courier",11,"bold"))
lbl_space1.pack()
lbl_space2 = Label(frame_2, text="", bg="#76ABAE")
lbl_space2.pack()
lbl_space3 = Label(frame_2, text="", bg="#76ABAE")
lbl_space3.pack()
lbl_total = Label(frame_2,text="",font=("courier",11,),bg="#76ABAE")
lbl_total.pack(anchor="se")
lbl_space4 = Label(frame_2, text="", bg="#76ABAE")
lbl_space4.pack()
lbl_space5 = Label(frame_2, text="", bg="#76ABAE")
lbl_space5.pack()
lbl_thankyou = Label(frame_2, text="", font=("courier", 15, "bold"), bg="#76ABAE")
lbl_thankyou.pack()

root.mainloop()
