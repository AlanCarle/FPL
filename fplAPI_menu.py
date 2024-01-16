# This py file contains code which largely runs the tkinter menu I use to access fpl API calls
# If this file is ran, the tkinter main menu will load
# There are also a series of functions that do various tasks

# One of these tasks is that if a button is pressed, then a new page in the tkinter menu will be shown

from fplAPI_allFunctions import *
import tkinter as tk
import json




# fplAPI_managerEventPicks(int(widgetsList[1][1].get()), int(widgetsList[2][1].get()), int(widgetsList[7][1].get()), True, settingsData['save_filepath'], widgetsList[3][1].get(), widgetsList[4][1].get(), widgetsList[5][1].get(), widgetsList[6][1].get())
def verifyNumbers(verify_elementID=None, verify_managerID=None, verify_eventID=None, verify_leagueID=None, verify_page_number=None, verify_max_iter=None):
    
    # verify main inputs first
    verifyList = [verify_elementID, verify_managerID, verify_eventID, verify_leagueID, verify_page_number]
    for i in range(0, 5):
        if verifyList[i] != "":
            # if dash is in the string, a tuple response must be given
            midVal = verifyList[i].find("-")
            if midVal != -1:
                verifyList[i] = tuple(range(int(verifyList[i][0:midVal]),int(verifyList[i][midVal+1:len(verifyList[i])])+1))
            else:
                verifyList[i] = int(verifyList[i])

    # verify max_iterations here, since there is less to be done
    if verify_max_iter != "":
        verify_max_iter = int(verify_max_iter)
    elif verify_max_iter == "":
        verify_max_iter = 9999999
        
    return verifyList[0], verifyList[1], verifyList[2], verifyList[3], verifyList[4], verify_max_iter



# one function called by all basic downloads, will download that endpoint set
def func_basicDownloadEndpointExportCSV(endPointType, filepath_used, max_iter, elementID=None, managerID=None, eventID=None, leagueID=None, page_number=None, outname_1=None, outname_2=None, outname_3=None, outname_4=None, outname_5=None, outname_6=None, outname_7=None, outname_8=None, outname_9=None):
    # first ensure that elementID, managerID, eventID, leagueID, page_number AND MAX ITERATIONS are all in correct format
    # then go through each endPointType in an if elif elif... statement for each endpoint call
    # then give pop up or something to the user saying its done
    
    
    elementID, managerID, eventID, leagueID, page_number, max_iter = verifyNumbers(elementID, managerID, eventID, leagueID, page_number, max_iter)

    
    if endPointType == "fplAPI_bestLeagues":
        fplAPI_bestLeagues(True, filepath_used, outname_1)
    elif endPointType == "fplAPI_bootstrap":
        fplAPI_bootstrap(True, filepath_used, outname_1, outname_2, outname_3, outname_4, outname_5, outname_6, outname_7, outname_8, outname_9)
    elif endPointType == "fplAPI_dreamTeam":
        fplAPI_dreamTeam(eventID, max_iter, True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_elementSummary":
        fplAPI_elementSummary(elementID, max_iter, True, filepath_used, outname_1, outname_2, outname_3)
    elif endPointType == "fplAPI_eventStatus":
        fplAPI_eventStatus(True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_fixtures":
        fplAPI_fixtures(True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_liveGameweekEvent":
        fplAPI_liveGameweekEvent(eventID, max_iter, True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_leagueStandings":
        fplAPI_leagueStandings(leagueID, page_number, max_iter, True, filepath_used, outname_1, outname_2, outname_3, outname_4)
    elif endPointType == "fplAPI_managerEventPicks":
        fplAPI_managerEventPicks(managerID, eventID, max_iter, True, filepath_used, outname_1, outname_2, outname_3, outname_4)
    elif endPointType == "fplAPI_manager":
        fplAPI_manager(managerID, max_iter, True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_managerHistory":
        fplAPI_managerHistory(managerID, max_iter, True, filepath_used, outname_1, outname_2, outname_3)
    elif endPointType == "fplAPI_managerTransfers":
        fplAPI_managerTransfers(managerID, max_iter, True, filepath_used, outname_1)
    elif endPointType == "fplAPI_setPieceNotes":
        fplAPI_setPieceNotes(True, filepath_used, outname_1, outname_2)
    elif endPointType == "fplAPI_mostValuableTeams":
        fplAPI_mostValuableTeams(True, filepath_used, outname_1)





# create activeInput strings with ease
def txt2activeInput(myTxt):
    
    
    # create the strings to use
    midVal = myTxt.find(" ")
    str1 = myTxt[0:midVal]
    str2 = myTxt[midVal:len(myTxt)]

    # apply n/d with first 5 inputs
    constructTuple = ()
    for i in range(1,6):
        if str1.find(str(i)) != -1:
            constructTuple = constructTuple + ("n",)
        else:
            constructTuple = constructTuple + ("d",)

    # apply n/d with next 9 inputs
    for i in range(0,int(str2)):
        constructTuple = constructTuple + ("n",)
    for i in range(int(str2),9):
        constructTuple = constructTuple + ("d",)

    # last input is always n
    constructTuple = constructTuple + ("n",)

    return constructTuple


# delete all frames existing in main slots (main and menu). this is run before loading any frames
def func_deleteFrames():
    for myFrame in frm_menu_const.winfo_children():
        myFrame.destroy()
    for myFrame in frm_main_const.winfo_children():
        myFrame.destroy()

# add buttons (to go on (left) options frame) (these buttons will always be on the screen so can be called here)
def func_pack_MenuConstButtons(from_toCall):
    btn_home = tk.Button(from_toCall, text='Home',font=('Bold',15), fg='black',bg='light pink',command=lambda: func_pack_frmHome())
    btn_home.place(relx=0.5, rely=0.05, anchor="center")
    btn_exit = tk.Button(from_toCall, text='Exit',font=('Bold',15), fg='black',bg='light pink',command=tk_base.quit)
    btn_exit.place(relx=0.5, rely=0.95, anchor="center")


# function to add start-up menu/main frames to tk_base
def func_pack_frmHome():
    
    # first set up func to save filepath if needed to external json file
    def func_setFilepath():
        # change the thing you want to change
        settingsData['save_filepath'] = entRequestFilepath.get()

        # open json file as write, put info in, close file
        with open("fplAPI_menu_JSON.json", "w") as json_data:
            json.dump(settingsData, json_data, indent=4)
            json_data.close()
    
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menuHome = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menuHome)
    btn_basicDownloads_false = tk.Button(frm_menuHome, text='NO BAS' + "\n" + 'Downloads',font=('Bold',13), fg='black',bg='light pink',command=lambda: func_pack_frmBasicDownloads())
    btn_basicDownloads_false.place(relx=0.5, rely=0.18, anchor="center")
    frm_menuHome.pack(pady=20)
    
    btn_basicDownloads = tk.Button(frm_menuHome, text='Basic' + "\n" + 'Downloads',font=('Bold',13), fg='black',bg='light pink',command=lambda: func_pack_frmBasicDownloadsHome())
    btn_basicDownloads.place(relx=0.5, rely=0.27, anchor="center")
    frm_menuHome.pack(pady=20)
    
    # pack main
    frm_mainHome = tk.Frame(frm_main_const, bg="light grey")
    lblTitle = tk.Label(frm_mainHome, text="Welcome to the fpl API download hub",font=('Bold',30),bg="light grey")
    lblTitle.pack()
    # include section where the user can change their filepath that files are saved to
    lblRequestFilepath = tk.Label(frm_mainHome, text="Please ensure that the filepath to have your files saved to is correctly entered in the following textbox.\n Press save after making any changes.",font=('Bold',10),bg="light grey")
    lblRequestFilepath.pack(pady=5)
    entRequestFilepath = tk.Entry(frm_mainHome,width=150)
    entRequestFilepath.insert(0,settingsData['save_filepath'])
    entRequestFilepath.pack(pady=10)
    btnSetFilepath = tk.Button(frm_mainHome, text="Set current filepath.",command=lambda: func_setFilepath())
    btnSetFilepath.pack(pady=2)
    
    frm_mainHome.pack(pady=20)





def func_pack_frmBasicDownloadsHome():
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menu_BasicDownloadsHome = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menu_BasicDownloadsHome)
    frm_menu_BasicDownloadsHome.pack(pady=20)

    # pack main
    frm_main_BasicDownloadsHome = tk.Frame(frm_main_const, bg="light grey")
    frm_main_BasicDownloadsHome.pack()
    lblTitle = tk.Label(frm_main_BasicDownloadsHome, text="Select which endpoint to download",font=('Bold',30),bg="light grey")
    lblTitle.pack()

    func_pack_frmBasicDownloadsEndpointButtons(frm_menu_BasicDownloadsHome)



def func_pack_frmBasicDownloadsEndpointButtons(frame_to_pack):
    constNumEntries = ("elementID", "managerID", "eventID", "leagueID", "page_number")
    buttonArray = (("Best Leagues",txt2activeInput(" 1"),("Best Leagues","---","---","---","---","---","---","---","---"),"fplAPI_bestLeagues"), 
                   ("Bootstrap",txt2activeInput(" 9"),("Events","Teams","Elements","Element Types","Phases","Element Stats","Game Settings","Total Players","Chip Settings"),"fplAPI_bootstrap"), 
                   ("Dream Team",txt2activeInput("3 2"),("GW Dream Team","GW Dream Player","---","---","---","---","---","---","---"),"fplAPI_dreamTeam"), 
                   ("Element Summary",txt2activeInput("1 3"),("Fixtures","History","History Past","---","---","---","---","---","---"),"fplAPI_elementSummary"), 
                   ("Event Status",txt2activeInput(" 2"),("Status","Is Updating","---","---","---","---","---","---","---"),"fplAPI_eventStatus"), 
                   ("Fixtures",txt2activeInput(" 2"),("Fixtures","Fixture Element Stats","---","---","---","---","---","---","---"),"fplAPI_fixtures"), 
                   ("Live GW Event",txt2activeInput("3 2"),("Element Stats","Points Distribution","---","---","---","---","---","---","---"),"fplAPI_liveGameweekEvent"), 
                   ("League Standings",txt2activeInput("45 4"),("Standings","Info","Last Update","Meta","---","---","---","---","---"),"fplAPI_leagueStandings"), 
                   ("Manager Picks",txt2activeInput("23 4"),("Manager Picks","Subs","Entry History","Active Chips","---","---","---","---","---"),"fplAPI_managerEventPicks"), 
                   ("doNotUse-Manager Info",txt2activeInput("2 2"),("General","League Info","---","---","---","---","---","---","---"),"fplAPI_manager"), 
                   ("Manager History",txt2activeInput("2 3"),("Current Season","Past Seasons","Chips","---","---","---","---","---","---"),"fplAPI_managerHistory"), 
                   ("Manager Transfers",txt2activeInput("2 1"),("Transfers","---","---","---","---","---","---","---","---"),"fplAPI_managerTransfers"), 
                   ("Set Piece Notes",txt2activeInput(" 2"),("Set Piece Notes","Last Updated","---","---","---","---","---","---","---"),"fplAPI_setPieceNotes"), 
                   ("Most Valuable Teams",txt2activeInput(" 1"),("Most Valuable Teams","---","---","---","---","---","---","---","---"),"fplAPI_mostValuableTeams"))
    
    # pack buttons for each endpoint
    for i in range(0,len(buttonArray)):
        tk.Button(frame_to_pack, text=buttonArray[i][0],font=('Bold',11), fg='black',bg='light pink',command=lambda i=i: func_pack_frmBasicDownloadsTest(buttonArray[i][0], "Fill in the blue entires then select Download", buttonArray[i][1], constNumEntries, buttonArray[i][2], buttonArray[i][3])).place(relx=0.5, rely=0.12 + (i*0.055), anchor="center")







# pack the menu and main frames for the basic downloads page
def func_pack_frmBasicDownloads():
    
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menu_BasicDownloads = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menu_BasicDownloads)
    frm_menu_BasicDownloads.pack(pady=20)
    
    
    # pack main
    frm_main_BasicDownloads = tk.Frame(frm_main_const, height=base_height, width=base_width-150,bg="light grey")
    frm_main_BasicDownloads.pack(pady=20)
    # pack header text
    lblBasicDownloadsTitle = tk.Label(frm_main_BasicDownloads, text="Basic Downloads",font=('Bold',30),bg="light grey")
    lblBasicDownloadsTitle.grid(column=0,row=0,columnspan=2)
    lblBasicDownloadsExplain = tk.Label(frm_main_BasicDownloads, text="Ensure cells highlighted blue match what you want to download, then select the download button.",font=('Bold',15),bg="light grey")
    lblBasicDownloadsExplain.grid(column=0,row=1,pady=(0,30),columnspan=2)

    # create tuple statiung which inputs are active
    activeInputs = ("disabled", "normal", "normal", "disabled", "disabled", "normal", "normal", "normal", "normal", "disabled", "disabled", "disabled", "disabled", "disabled", "normal")

    # define list of entries for the specific download page
    numEntries = ("elementID", "managerID", "eventID", "leagueID", "page_number")
    txtEntries = ("Manager Picks", "Subs", "Entry History", "Active Chips", "-----", "-----", "-----", "-----", "-----")
    assert(len(activeInputs) == len(numEntries) + len(txtEntries) + 1)
    fullEntries = ()
    for i in range(0, len(numEntries)):
        fullEntries = fullEntries + (("Choose numerical endpoint variable:           " + numEntries[i], ""),)
    for i in range(0, len(txtEntries)):
        fullEntries = fullEntries + (("Choose text csv filename:                           " + txtEntries[i], txtEntries[i]),)
    fullEntries = fullEntries + (("[OPTIONAL] Choose numerical max download iterations", ""),)

    # define array to hold widgets, allows for easier creation/editing
    # length is number of "specific" entries, plus 1 line for headers at top, and 1 for run code
    num_cols = 2; num_rows = len(fullEntries) + 2
    widgetsList = [[0] * num_cols for i in range(num_rows)]
    
    # pack header of widget table
    widgetsList[0][1] = tk.Label(frm_main_BasicDownloads, text="Entry", font=('Arial',13),bg="light grey")
    widgetsList[0][1].grid(row=2,column=1)
    
    # set up widgets
    for i in range(0,len(fullEntries)):
        widgetsList[i+1][0] = tk.Label(frm_main_BasicDownloads, text=fullEntries[i][0], font=('Arial',13),bg="light grey", state=activeInputs[i])
        widgetsList[i+1][0].grid(row=i+3,column=0, sticky="w")
        widgetsList[i+1][1] = tk.Entry(frm_main_BasicDownloads, text="", bg="light blue", font=('Arial',13), state=activeInputs[i])
        widgetsList[i+1][1].grid(row=i+3,column=1)
        widgetsList[i+1][1].insert(0,fullEntries[i][1])


    # add button to run the appropriate code
    widgetsList[len(fullEntries) + 1][1] = tk.Button(frm_main_BasicDownloads,text="Download File", font=('Arial',13), bg="light grey", command=lambda: func_basicDownloadEndpointExportCSV("fplAPI_managerEventPicks",settingsData['save_filepath'],widgetsList[15][1].get(), elementID=widgetsList[1][1].get(), managerID=widgetsList[2][1].get(), eventID=widgetsList[3][1].get(), leagueID=widgetsList[4][1].get(), page_number=widgetsList[5][1].get(), outname_1=widgetsList[6][1].get(), outname_2=widgetsList[7][1].get(), outname_3=widgetsList[8][1].get(), outname_4=widgetsList[9][1].get(), outname_5=widgetsList[10][1].get(), outname_6=widgetsList[11][1].get(), outname_7=widgetsList[12][1].get(), outname_8=widgetsList[13][1].get(), outname_9=widgetsList[14][1].get()))
    widgetsList[len(fullEntries) + 1][1].grid(row=len(fullEntries)+3,column=1,pady=(20,0))




# pack the menu and main frames for the basic downloads page
def func_pack_frmBasicDownloadsTest(headerText, subheaderText, activeInputs, numEntries, txtEntries, fpl_type):
    
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menu_BasicDownloads = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menu_BasicDownloads)
    frm_menu_BasicDownloads.pack(pady=20)
    func_pack_frmBasicDownloadsEndpointButtons(frm_menu_BasicDownloads)
    
    # pack main
    frm_main_BasicDownloads = tk.Frame(frm_main_const, height=base_height, width=base_width-150,bg="light grey")
    frm_main_BasicDownloads.pack(pady=20)
    # pack header text
    lblBasicDownloadsTitle = tk.Label(frm_main_BasicDownloads, text=headerText,font=('Bold',30),bg="light grey")
    lblBasicDownloadsTitle.grid(column=0,row=0,columnspan=2)
    lblBasicDownloadsExplain = tk.Label(frm_main_BasicDownloads, text=subheaderText,font=('Bold',15),bg="light grey")
    lblBasicDownloadsExplain.grid(column=0,row=1,pady=(0,30),columnspan=2)

    # create tuple statiung which inputs are active
    #activeInputs = ("disabled", "normal", "normal", "disabled", "disabled", "normal", "normal", "normal", "normal", "disabled", "disabled", "disabled", "disabled", "disabled", "normal")

    # define list of entries for the specific download page
    #numEntries = ("elementID", "managerID", "eventID", "leagueID", "page_number")
    #txtEntries = ("Manager Picks", "Subs", "Entry History", "Active Chips", "-----", "-----", "-----", "-----", "-----")
    assert(len(activeInputs) == len(numEntries) + len(txtEntries) + 1)
    fullEntries = ()
    for i in range(0, len(numEntries)):
        fullEntries = fullEntries + (("Choose numerical endpoint variable:           " + numEntries[i], ""),)
    for i in range(0, len(txtEntries)):
        fullEntries = fullEntries + (("Choose text csv filename:                           " + txtEntries[i], txtEntries[i]),)
    fullEntries = fullEntries + (("[OPTIONAL] Choose numerical max download iterations", ""),)

    # define array to hold widgets, allows for easier creation/editing
    # length is number of "specific" entries, plus 1 line for headers at top, and 1 for run code
    num_cols = 2; num_rows = len(fullEntries) + 2
    widgetsList = [[0] * num_cols for i in range(num_rows)]
    
    # pack header of widget table
    widgetsList[0][1] = tk.Label(frm_main_BasicDownloads, text="Entry", font=('Arial',13),bg="light grey")
    widgetsList[0][1].grid(row=2,column=1)
    
    # set up widgets
    for i in range(0,len(fullEntries)):
        widgetsList[i+1][0] = tk.Label(frm_main_BasicDownloads, text=fullEntries[i][0], font=('Arial',13),bg="light grey", state=activeInputs[i])
        widgetsList[i+1][0].grid(row=i+3,column=0, sticky="w")
        widgetsList[i+1][1] = tk.Entry(frm_main_BasicDownloads, text="", bg="light blue", font=('Arial',13), state=activeInputs[i])
        widgetsList[i+1][1].grid(row=i+3,column=1)
        widgetsList[i+1][1].insert(0,fullEntries[i][1])


    # add button to run the appropriate code
    widgetsList[len(fullEntries) + 1][1] = tk.Button(frm_main_BasicDownloads,text="Download File", font=('Arial',13), bg="light grey", command=lambda: func_basicDownloadEndpointExportCSV(fpl_type,settingsData['save_filepath'],widgetsList[15][1].get(), elementID=widgetsList[1][1].get(), managerID=widgetsList[2][1].get(), eventID=widgetsList[3][1].get(), leagueID=widgetsList[4][1].get(), page_number=widgetsList[5][1].get(), outname_1=widgetsList[6][1].get(), outname_2=widgetsList[7][1].get(), outname_3=widgetsList[8][1].get(), outname_4=widgetsList[9][1].get(), outname_5=widgetsList[10][1].get(), outname_6=widgetsList[11][1].get(), outname_7=widgetsList[12][1].get(), outname_8=widgetsList[13][1].get(), outname_9=widgetsList[14][1].get()))
    widgetsList[len(fullEntries) + 1][1].grid(row=len(fullEntries)+3,column=1,pady=(20,0))







##########################################################################################################
####    Start of main code    ############################################################################
##########################################################################################################

# initialise tkinter pop up window and characteristics
tk_base = tk.Tk()
#tk_base.geometry('1100x700')
base_width = 1300
base_height = 700
tk_base.geometry('%dx%d+%d+%d' % (base_width, base_height, 10, 10))
tk_base.title('fpl API Menu')

# open json settings file as read, get info, close file
with open('fplAPI_menu_JSON.json','r') as json_data:
    settingsData = json.load(json_data)
    json_data.close()

# initialise constant menu frame (on left of screen). Individual menu frames will be inserted into the const frame.
frm_menu_const = tk.Frame(tk_base, bg='light pink')
frm_menu_const.pack(side=tk.LEFT)
frm_menu_const.pack_propagate(False)
frm_menu_const.configure(width=150, height=base_height)


# initialise constant contents frame (on right of screen). Individual main frames will be inserted into the const frame.
frm_main_const = tk.Frame(tk_base, highlightbackground='black', highlightthickness=2, bg='light grey')
frm_main_const.pack(side=tk.LEFT)
frm_main_const.pack_propagate(False)
frm_main_const.configure(width=base_width-150, height=base_height)

# pack home frames on startup
func_pack_frmHome()





tk_base.mainloop()