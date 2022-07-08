#This piece of code contains all the functions to the various buttons, optionMenus, etc ... as well as the displaying fuction 

from tkinter import *

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("project CYBER")
app.geometry("400x800")
app.iconbitmap("Thresh.ico")

t1 = Text(app) 
t1.place(x = 10, y = 150, width=325)

t2 = Text(app)
t2.place(x = 10, y = 550, width=325)


# SELECT RISK FEATURE
frame1 = LabelFrame(app, text="Please Select a Risk:",  padx=200, pady=5)
frame1.place(x= 700, y = 10)

b1 = Button(frame1, text="Cyber",padx=50,pady=25, command = cyber).grid(row=0,column=0)
b2 = Button(frame1, text="Physical Security",padx=50, pady=25, command = phy).grid(row=0,column=1)
b3 = Button(frame1, text="Gouvernment Surveillance", padx=40, pady=25, command = gov).grid(row=0,column=2)


# COMPARAISON FEATURE
frame2 = LabelFrame(app, text="Comparaison",  padx=5, pady=20)

frame2.place(x = 100, y = 10)

countries = [ "Select a country",'Afghanistan','Algeria','Australia','Bangladesh','Belarus','Belgium','Benin','Bolivia','Bosnia and Herzegovina','Brazil','Bulgaria','Burundi','Cameroon','Canada', 'Central African Republic','China','Colombia','Croatia','Cuba', 'Czechia','Democratic Republic of the Congo', 'Denmark','Ecuador','Egypt', 'El Salvador','Eritrea', 'Estonia', 'Falkland Islands', 'Finland', 'France','Georgia', 'Germany', 'Greece','Haiti','Honduras', 'Hong Kong S.A.R.','Indonesia','Iran','Iraq','Israel','Italy','Japan','Kosovo','Lithuania','Malaysia', 'Mongolia', 'Myanmar' 'Netherlands','New Zealand', 'Nicaragua', 'Niger', 'Nigeria','Norway','Pakistan','Peru','Philippines','Poland', 'Portugal','Republic of Serbia', 'Romania', 'Russia','Saudi Arabia','Senegal','Singapore','Slovakia','Spain','Sweden','Switzerland','Tchad','Thailand','Turkey','Ukraine','United Kingdom','United Republic of Tanzania','United States of America','Uzbekistan','Vietnam','Zimbabwe']
clicked = StringVar()
clicked.set("Select a country")
drop = OptionMenu(frame2, clicked, *countries, command = ShowOne)
drop.grid(row=1, column = 0)

var = IntVar()
c = Checkbutton(frame2, text="Comparaison", variable=var, command=comparaison)
c.grid(row=0, columnspan = 2 )


app.mainloop()
