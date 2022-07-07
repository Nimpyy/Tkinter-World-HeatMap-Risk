# Import the library tkinter
from tkinter import *
import pandas as pd
import geopandas as gpd
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as colors
import country_converter as coco
matplotlib.use("TkAgg")

sources = pd.read_csv(r"path to 7sources.csv", encoding = 'ISO-8859-1')
colsource = list(sources.columns.values)
df = pd.read_csv('data.csv', encoding = 'ISO-8859-1')
cols = list(df.columns.values)
SHAPEFILE = r'path to shapefile'
geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
geo_df_columns = ['country', 'CODE', 'GEONMETRY']
geo_df = geo_df.drop(geo_df.loc[geo_df['ADMIN'] == 'Antarctica'].index)
iso3_codes = geo_df['ADMIN'].to_list()
iso2_codes_list = coco.convert(names=iso3_codes, to='ISO2', not_found='NULL')
geo_df['iso2_code'] = iso2_codes_list
geo_df = geo_df.drop(geo_df.loc[geo_df['iso2_code'] == 'NULL'].index)
df = df.sort_values('ADMIN') 
merged_df = pd.merge(left=geo_df.sort_values('ADMIN'), right=df.sort_values('ADMIN'), on="ADMIN")


# Create a GUI app
app = Tk()

# Give a title to your app
app.title("project CYBER")
app.geometry("400x800")
app.iconbitmap("Thresh.ico")

bounds = (0,1,7,14,21)

#button functions
def cyber():
    global R 
    global X 
    global bounds 
    bounds = (0,1,7,14,21)
    X = 0
    R = "CYBER"

    norm = colors.BoundaryNorm(bounds, len(bounds)-1)
    color_map1 = ['#ffffff','#59e300', '#fff20b','#e31900']
    color_map = colors.ListedColormap(color_map1)

    fig = plt.Figure()
    fig, ax1 = plt.subplots(1, figsize=(15,8))
    fig.subplots_adjust(left=0.03, bottom=0.07, right=0.98, top=0.97, wspace=0, hspace=0)
    # ax1 = fig.add_subplot(111)
    ax1.axis("off")
    canvas = FigureCanvasTkAgg(fig, app)
    canvas.get_tk_widget().place(x = 350, y = 150)
    merged_df.plot(column = "CYBER", edgecolor='0.8', linewidth=0.8,ax=ax1, cmap = color_map)
    ax1.annotate(xy = (0,21), xycoords='figure fraction', horizontalalignment='left', verticalalignment='bottom', fontsize=10, text=" ")
    ax1.set_title('HEATMAP')

    sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
    cbaxes = fig.add_axes([0.18, 0.25, 0.01, 0.3])
    cbar = fig.colorbar(sm, cax=cbaxes)

def phy():
    global R 
    global X 
    global bounds 
    bounds = (0,1,2,4,6)
    X = 0
    R = "PHYSICAL SECURITY"

    norm = colors.BoundaryNorm(bounds, len(bounds)-1)
    color_map1 = ['#ffffff','#59e300', '#fff20b','#e31900']
    color_map = colors.ListedColormap(color_map1)

    fig = plt.Figure()
    fig, ax1 = plt.subplots(1, figsize=(15,8))
    fig.subplots_adjust(left=0.03, bottom=0.07, right=0.98, top=0.97, wspace=0, hspace=0)
    # ax1 = fig.add_subplot(111)
    ax1.axis("off")
    canvas = FigureCanvasTkAgg(fig, app)
    canvas.get_tk_widget().place(x = 350, y = 150)
    merged_df.plot(column = "PHY SEQ", edgecolor='0.8', linewidth=0.8,ax=ax1, cmap = color_map)
    ax1.annotate(xy = (0,21), xycoords='figure fraction', horizontalalignment='left', verticalalignment='bottom', fontsize=10, text=" ")
    ax1.set_title('HEATMAP')

    sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
    cbaxes = fig.add_axes([0.18, 0.25, 0.01, 0.3])
    cbar = fig.colorbar(sm, cax=cbaxes)

def gov():
    global R1
    global R2
    global R3 
    global X 
    global bounds 
    bounds = (0,0.9,1,2,3)
    X = 1
    R1 = "GEOPOLITIC"
    R2 = "ESPIONNAGE"
    R3 = "GOVERNANCE SURVEILLANCE"

    norm = colors.BoundaryNorm(bounds, len(bounds)-1)
    color_map1 = ['#ffffff','#59e300', '#fff20b','#e31900']
    color_map = colors.ListedColormap(color_map1)

    fig = plt.Figure()
    fig, ax1 = plt.subplots(1, figsize=(15,8))
    fig.subplots_adjust(left=0.03, bottom=0.07, right=0.98, top=0.97, wspace=0, hspace=0)
    # ax1 = fig.add_subplot(111)
    ax1.axis("off")
    canvas = FigureCanvasTkAgg(fig, app)
    canvas.get_tk_widget().place(x = 350, y = 150)
    merged_df.plot(column = "GEOPOL & ESPIONNAGE", edgecolor='0.8', linewidth=0.8,ax=ax1, cmap = color_map)
    ax1.annotate(xy = (0,21), xycoords='figure fraction', horizontalalignment='left', verticalalignment='bottom', fontsize=10, text=" ")
    ax1.set_title('HEATMAP')

    sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
    cbaxes = fig.add_axes([0.18, 0.25, 0.01, 0.3])
    cbar = fig.colorbar(sm, cax=cbaxes)


def comparaison():
    if var.get() == 1 :
        global clicked2
        clicked2 = StringVar()
        clicked2.set("Select a country")
        global drop2
        drop2 = OptionMenu(frame2, clicked2, *countries, command = ShowTwo)
        drop2.grid(row = 1, column = 1)
    if var.get() == 0 :
        drop2.grid_forget()

#function compare button
def ShowTwo(pays):
    t2.delete(1.0, END)
    pays2 = clicked2.get()
    t2.insert(END, pays2.upper())
    t2.insert(END, "\n")

    class PrintTot2(object): 
        def write(self, s): 
            t2.insert(END, s) 
                    

# Display countries' stats
    sys.stdout = PrintTot2() 
    for i in range(len(sources[colsource[0]])):
        if sources[colsource[0]][i] == clicked2.get().upper():
            if X != 1:
                if R == "CYBER":
                    if sources[colsource[1]][i] == R:
                        t2.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                        t2.insert(END, "\n")
                if R == "PHYSICAL SECURITY":
                    if sources[colsource[1]][i] == R:
                        t2.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                        t2.insert(END, "\n")
            if X == 1:
                if sources[colsource[1]][i] == R1 or sources[colsource[1]][i] == R2 or sources[colsource[1]][i] == R3:
                    t2.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                    t2.insert(END, "\n")


def ShowOne(pays):
    t1.delete(1.0, END)
    pays = clicked.get()
    print(pays.upper())
    t1.insert(END, pays.upper())
    t1.insert(END, "\n")

    class PrintToT1(object): 
        def write(self, s): 
            t1.insert(END, s) 
                    

# Display country's stats
    sys.stdout = PrintToT1() 
    for i in range(len(sources[colsource[0]])):
        if sources[colsource[0]][i] == clicked.get().upper():
            if X != 1:
                if R == "CYBER":
                    if sources[colsource[1]][i] == R:
                        t1.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                        t1.insert(END, "\n")
                if R == "PHYSICAL SECURITY":
                    if sources[colsource[1]][i] == R:
                        t1.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                        t1.insert(END, "\n")
            if X == 1:
                if sources[colsource[1]][i] == R1 or sources[colsource[1]][i] == R2 or sources[colsource[1]][i] == R3:
                    t1.insert(END, sources.loc[i, ["SOURCE", 'SCORE']])
                    t1.insert(END, "\n")
        

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

countries = [ "Select a country",'Afghanistan','Algeria','Australia','Bangladesh','Belarus','Belgium','Benin','Bolivia','Bosnia and Herzegovina',
             'Brazil','Bulgaria','Burundi','Cameroon','Canada', 'Central African Republic','China','Colombia','Croatia','Cuba', 'Czechia',
             'Democratic Republic of the Congo', 'Denmark','Ecuador','Egypt', 'El Salvador','Eritrea', 'Estonia', 'Falkland Islands', 'Finland',
             'France','Georgia', 'Germany', 'Greece','Haiti','Honduras', 'Hong Kong S.A.R.','Indonesia','Iran','Iraq','Israel','Italy','Japan',
             'Kosovo','Lithuania','Malaysia', 'Mongolia', 'Myanmar' 'Netherlands','New Zealand', 'Nicaragua', 'Niger', 'Nigeria','Norway','Pakistan',
             'Peru','Philippines','Poland', 'Portugal','Republic of Serbia', 'Romania', 'Russia','Saudi Arabia','Senegal','Singapore','Slovakia',
             'Spain','Sweden','Switzerland','Tchad','Thailand','Turkey','Ukraine','United Kingdom','United Republic of Tanzania','United States of America',
             'Uzbekistan','Vietnam','Zimbabwe']
clicked = StringVar()
clicked.set("Select a country")
drop = OptionMenu(frame2, clicked, *countries, command = ShowOne)
drop.grid(row=1, column = 0)

var = IntVar()
c = Checkbutton(frame2, text="Comparaison", variable=var, command=comparaison)
c.grid(row=0, columnspan = 2 )

app.mainloop()
