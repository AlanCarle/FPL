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

def verifyOneNumber(myNum):
    if myNum != "":
        # if dash is in the string, a tuple response must be given
        midVal = myNum.find("-")
        if midVal != -1:
            myNum = tuple(range(int(myNum[0:midVal]),int(myNum[midVal+1:len(myNum)])+1))
        else:
            myNum = int(myNum)
    return myNum



# one function called by all basic downloads, will download that endpoint set
def func_basicDownloadEndpointExportCSV(endPointType, filepath_used, max_iter, elementID=None, managerID=None, eventID=None, leagueID=None, page_number=None, numVal_6=None, numVal_7=None, numVal_8=None, numVal_9=None, numVal_10=None, numVal_11=None, numVal_12=None, numVal_13=None, numVal_14=None, outname_1=None, outname_2=None, outname_3=None, outname_4=None, outname_5=None, outname_6=None, outname_7=None, outname_8=None, outname_9=None, outname_10=None, outname_11=None, outname_12=None, outname_13=None, outname_14=None, outname_15=None):
    # first ensure that elementID, managerID, eventID, leagueID, page_number AND MAX ITERATIONS are all in correct format
    # then go through each endPointType in an if elif elif... statement for each endpoint call
    # then give pop up or something to the user saying its done
    
    elementID, managerID, eventID, leagueID, page_number, max_iter = verifyNumbers(elementID, managerID, eventID, leagueID, page_number, max_iter)

    numVal_6 = verifyOneNumber(numVal_6)
    numVal_7 = verifyOneNumber(numVal_7)
    numVal_8 = verifyOneNumber(numVal_8)
    numVal_9 = verifyOneNumber(numVal_9)
    numVal_10 = verifyOneNumber(numVal_10)
    numVal_11 = verifyOneNumber(numVal_11)
    numVal_12 = verifyOneNumber(numVal_12)
    numVal_13 = verifyOneNumber(numVal_13)
    numVal_14 = verifyOneNumber(numVal_14)
    
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
    elif endPointType == "fplAPI_returnLastPageandRank":
        fplAPI_returnLastPageandRank(leagueID, numVal_6, max_iter, True, filepath_used, outname_1)




def num2activeInput(myNum):
    myTuple = ()
    for i in range(0,myNum):
        myTuple = myTuple + ("normal",)
    for i in range(myNum, 15):
        myTuple = myTuple + ("disabled",)
    return myTuple

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


# first set up func to save filepath if needed to external json file
def func_setFilepath(entryWidget):
    # change the thing you want to change
    settingsData['save_filepath'] = entryWidget.get()

    # open json file as write, put info in, close file
    with open("fplAPI_menu_JSON.json", "w") as json_data:
        json.dump(settingsData, json_data, indent=4)
        json_data.close()



# function to add start-up menu/main frames to tk_base
def func_pack_frmHome():
    
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menuHome = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menuHome)

    # insert button for basic downloads
    btn_basicDownloads = tk.Button(frm_menuHome, text='Basic' + "\n" + 'Downloads',font=('Bold',13), fg='black',bg='light pink',command=lambda: func_pack_frm_epButtons_choose("ep_basicDownloads"))
    btn_basicDownloads.place(relx=0.5, rely=0.18, anchor="center")
    frm_menuHome.pack(pady=20)
    
    # insert button for misc downloads
    btn_basicDownloads = tk.Button(frm_menuHome, text='Misc' + "\n" + 'Downloads',font=('Bold',13), fg='black',bg='light pink',command=lambda: func_pack_frm_epButtons_choose("ep_miscDownloads"))
    btn_basicDownloads.place(relx=0.5, rely=0.28, anchor="center")
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
    btnSetFilepath = tk.Button(frm_mainHome, text="Set current filepath.",command=lambda: func_setFilepath(entRequestFilepath))
    btnSetFilepath.pack(pady=2)
    
    frm_mainHome.pack(pady=20)





def func_pack_frm_epButtons_choose(endPointArrayLabel):
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

    func_pack_frm_epButtons_choooseMenu(frm_menu_BasicDownloadsHome, endPointArrayLabel)
    
    
def func_pack_frm_epButtons_choooseMenu(frame_to_pack, buttonArrayLabel):

    buttonArray = settingsData["btnLoads"][buttonArrayLabel].split(",")
    
    # pack buttons for each endpoint
    for i in range(0,len(buttonArray)):
        tk.Button(frame_to_pack, text=settingsData["loadInfo"][buttonArray[i]]["title"],font=('Bold',11), fg='black',bg='light pink',
            command=lambda i=i: func_pack_frm_epButtons_download(
                settingsData["loadInfo"][buttonArray[i]]["title"], 
                "Fill in the blue entires then select Download", 
                txt2activeInput(settingsData["loadInfo"][buttonArray[i]]["frmtNumEnt"]), 
                num2activeInput(settingsData["loadInfo"][buttonArray[i]]["frmtTxtEnt"]), 
                tuple(settingsData["loadInfo"][buttonArray[i]]["numEnt"].split(",")), 
                tuple(settingsData["loadInfo"][buttonArray[i]]["txtEnt"].split(",")), 
                buttonArray[i],
                buttonArrayLabel)
            ).place(relx=0.5, rely=0.12 + (i*0.055), anchor="center")




# pack the menu and main frames for the basic downloads page
def func_pack_frm_epButtons_download(headerText, subheaderText, numSideActiveInputs, txtSideActiveInputs, numEntries, txtEntries, fpl_type, buttonArrayLabel):
    
    
    # ensure no frames exist in const frames
    func_deleteFrames()
    
    # pack menu
    frm_menu_BasicDownloads = tk.Frame(frm_menu_const, height=base_height, width=150, bg="light pink")
    func_pack_MenuConstButtons(frm_menu_BasicDownloads)
    frm_menu_BasicDownloads.pack(pady=20)
    func_pack_frm_epButtons_choooseMenu(frm_menu_BasicDownloads, buttonArrayLabel)
    
    # pack main
    frm_main_BasicDownloads = tk.Frame(frm_main_const, height=base_height, width=base_width-150,bg="light grey")
    frm_main_BasicDownloads.pack(pady=20)
    # pack header text
    lblBasicDownloadsTitle = tk.Label(frm_main_BasicDownloads, text=headerText,font=('Bold',30),bg="light grey")
    lblBasicDownloadsTitle.grid(column=0,row=0,columnspan=4)
    lblBasicDownloadsExplain = tk.Label(frm_main_BasicDownloads, text=subheaderText,font=('Bold',15),bg="light grey")
    lblBasicDownloadsExplain.grid(column=0,row=1,pady=(0,30),columnspan=4)

    
    # pack header of widget table
    tk.Label(frm_main_BasicDownloads, text="Entry", font=('Arial',13),bg="light grey").grid(row=2,column=1)
    
    
    numWidgetsList = setupMyWidgets(True, numEntries, frm_main_BasicDownloads, numSideActiveInputs, 3,0)
    
    txtWidgetsList = setupMyWidgets(False, txtEntries, frm_main_BasicDownloads, txtSideActiveInputs, 3,2)
    
    
    # add button to run the appropriate code
    tk.Button(frm_main_BasicDownloads,text="Download File", font=('Arial',13), bg="light grey", command=lambda: func_basicDownloadEndpointExportCSV(fpl_type,settingsData['save_filepath'],numWidgetsList[15][1].get(), elementID=numWidgetsList[1][1].get(), managerID=numWidgetsList[2][1].get(), eventID=numWidgetsList[3][1].get(), leagueID=numWidgetsList[4][1].get(), page_number=numWidgetsList[5][1].get(), numVal_6=numWidgetsList[6][1].get(), numVal_7=numWidgetsList[7][1].get(), numVal_8=numWidgetsList[8][1].get(), numVal_9=numWidgetsList[9][1].get(), numVal_10=numWidgetsList[10][1].get(), numVal_11=numWidgetsList[11][1].get(), numVal_12=numWidgetsList[12][1].get(), numVal_13=numWidgetsList[13][1].get(), numVal_14=numWidgetsList[14][1].get(), outname_1=txtWidgetsList[1][1].get(), outname_2=txtWidgetsList[2][1].get(), outname_3=txtWidgetsList[3][1].get(), outname_4=txtWidgetsList[4][1].get(), outname_5=txtWidgetsList[5][1].get(), outname_6=txtWidgetsList[6][1].get(), outname_7=txtWidgetsList[7][1].get(), outname_8=txtWidgetsList[8][1].get(), outname_9=txtWidgetsList[9][1].get(), outname_10=txtWidgetsList[10][1].get(), outname_11=txtWidgetsList[11][1].get(), outname_12=txtWidgetsList[12][1].get(), outname_13=txtWidgetsList[13][1].get(), outname_14=txtWidgetsList[14][1].get(), outname_15=txtWidgetsList[15][1].get())).grid(row=len(txtEntries)+3,column=1,pady=(20,0))


def setupMyWidgets(isNum, labelList, frm_to_pack, activeList, startRow, startCol):
    num_cols = 2; num_rows = len(labelList)+1
    setupWidgetList = [[0] * num_cols for i in range(num_rows)]
    
    padVal = 150 if isNum == False else 0
    
    for i in range(len(labelList)):
        setupWidgetList[i+1][0] = tk.Label(frm_to_pack, text=labelList[i], font=('Arial',13),bg="light grey", state=activeList[i])
        setupWidgetList[i+1][0].grid(row=i+startRow, column=startCol, sticky="w", padx=(padVal,0))
        setupWidgetList[i+1][1] = tk.Entry(frm_to_pack, text="", bg="light blue", font=('Arial',13), state=activeList[i])
        setupWidgetList[i+1][1].grid(row=i+startRow, column=startCol+1)
        if not isNum:
            setupWidgetList[i+1][1].insert(0,labelList[i])

    return setupWidgetList



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