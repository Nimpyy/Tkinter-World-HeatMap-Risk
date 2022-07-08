#This piece of code contains all the functions to the various buttons, optionMenus, etc ... as well as the displaying function 

#score thresholds for the colormap
bounds = (0,1,7,14,21)

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


def ShowTwo(pays):
    t2.delete(1.0, END)
    pays2 = clicked2.get()
    t2.insert(END, pays2.upper())
    t2.insert(END, "\n")

    class PrintTot2(object): 
        def write(self, s): 
            t2.insert(END, s) 
                    


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
