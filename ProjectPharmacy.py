from tkinter import *
from tkintermapview import TkinterMapView
abdo = Tk()

abdo.geometry('1000x600')

abdo.title('Pharmacie 7/7')
abdo.iconbitmap('livre.ico')

def find_sadaa():
        map = TkinterMapView(abdo,height=540,width=580)
        map.place(x=400,y=40)
        map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)

        map.set_position(30.355171, -9.538277)
        map.set_zoom(20)
        marker = map.set_marker(30.355171, -9.538277)
        
def find_Massdora():
        map =TkinterMapView(abdo,height=540,width=580)
        
        map.place(x=400,y=40)
        map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
        map.set_position(30.349991584008908, -9.539860928012011)
        map.set_zoom(20)
        marker = map.set_marker(30.349991584008908, -9.539860928012011)

def cu():
        country = en.get()
        map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
        map.set_address(country, marker=True)


#------------------Title------------------------

lb1 = Label(abdo,text='Pharmecie 7/7',bg='silver',fg='white',font=('Tajawal',18))
lb1.pack(fill=X)

#-----------------Logo-Medcine-----

logo = PhotoImage(file='51461.png')
lab_logo= Label(abdo,image=logo)
lab_logo.place(x=20,y=40)

#----------LABLE + ENTRY + BUTTON
#----label
l =  Label(abdo,text='Country:',fg='black',
            font = ('Tajawal',15)

                )
l.place(x=29,y= 400)

#------entry

en = Entry(abdo,
        font=('Tajawal',14),
        width=10,bd=2,relief=GROOVE
        )
en.place( x=122, y= 400 )

#--Button
b1 = Button(abdo,text='Check Country',
        relief=SOLID,
        bg='black'
        ,fg='white',
        width='12',
        cursor='hand2',command=cu
        
        )
b1.place(x= 240 , y = 400)

#---Pharmacy butoon

bb1 = Button(abdo , text='lmowadafin',font=(10),relief=GROOVE,width=10,cursor='hand2')
bb1.place(x=20,y=475)

bb2 = Button(abdo , text='Massdora',font=(10),relief=GROOVE,width=10,cursor='hand2',command=find_Massdora)
bb2.place(x=140,y=475)


bb3 = Button(abdo , text='Bozgar',font=(10),relief=GROOVE,width=10,cursor='hand2')
bb3.place(x=260,y=475)


bb4 = Button(abdo , text='Inzegan',font=(10),relief=GROOVE,width=10,cursor='hand2')
bb4.place(x=20,y=520)



bb5 = Button(abdo , text='saada',font=(10),relief=GROOVE,width=10,cursor='hand2',command=find_sadaa)
bb5.place(x=140,y=520)

bb6 = Button(abdo , text='Bozgar',font=(10),relief=GROOVE,width=10,cursor='hand2')
bb6.place(x=260,y=520)

#-------------Map----------------
map = TkinterMapView(abdo,width=580,height=540)
map.place(x=400,y=40)
#------------

abdo.mainloop()