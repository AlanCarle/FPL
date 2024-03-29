import requests
import pandas as pd
import json
from pathlib import Path
from math import floor
from datetime import datetime


#filepath_to_use = r"C:\Users\name

'''
def fplAPI_FAKE_DONOTUSE([VARIABLE INPUTS], max_iterations, save_to_csv=None, func_filepath_save=None, [OUTNAMES=None]):
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, [VARIABLE INPUTS]))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        [OUTPATHS] = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, ([TUPLE OF OUTNAMES]))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_[ALL DATAFRAMES] = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type([INPUT]) == int: [INPUT] = ([INPUT],)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for [INPUT] in tuple([INPUT]):
    
        api_link = [WHATEVER THE API LINK IS]

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # get info via the following


            # add variable input of endpoint into the dataframes

            
            # concat them all
            df_MAIN = pd.concat([df_MAIN, df_MAIN_TEMP], axis=0)


    # export to csv
    if save_to_csv == True:
        df_MAIN.to_csv(OUTPATH_MAIN, index=False)


    return [TUPLE OF OUT_DFs]
'''

'''
def fplAPI_FAKE_USE_FOR_NON_VARAIBLE_INPUR_FUNCTION(save_to_csv=None, func_filepath_save=None, [OUTNAMES=None]):
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        [OUTPATHS] = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, ([TUPLE OF OUTNAMES]))
    
    api_link = [api link WITH NO VARIABLE INPUTS]

    # create the dataframes, s.t. all further additions can be concat onto these
    df_[ALL DATAFRAMES] = pd.DataFrame()

    # get the data from fpl api, check result is valid, if so then continue
    myData = requests.get(api_link)
    if myData.text != '{"detail":"Not found."}':
        myData = myData.json()

        # get info via the following




    # export to csv
    if save_to_csv == True:
        df_MAIN.to_csv(OUTPATH_MAIN, index=False)

    return [DATAFRAMES TO RETURN]
'''


'''
# basic format of all functions
def fplAPI_[rough endpoint suffix]
    (
    {SOMETIMES} variable_input1 [Array of numbers]
    {SOMETIMES} varaible_input2 [Array of numbers]
    ...
    {SOMETIMES} max_iterations [Number]
    save_to_csv [Boolean]
    filepath_to_save_to [String]
    output csv name 1 [String]
    {SOMETIMES} output csv name 2 [String]
    ...
    )
    - if there are any variable inputs, call fplAPI_specific_assertNumberInputs_checkMaxIter. If returns false then exit
    - assert isinstance for only save_to_csv
    - if save_to_csv is true, call fplAPI_specific_constructFilepathsAndTestExists
    
    - create empty dataframe/s
    - convert number variable inputs to tuples if necessary
    
    - loop through all variable combinations
        - get api link and produce the dataframe/s
        - concat individual files onto main
    
    - if save_to_csv is true, save the files
   
    - return the dataframes

'''



# The two below functions are used for general housekeeping with many further modules

def fplAPI_specific_constructFilepathsAndTestExists(userFilepath, userOutNames):
    # Function Code: 0001
    # Function Uses: None
    
    # inputs a filepath and set of filenames
    # check the filepaths/filenames are strings
    assert(isinstance(userFilepath, str))
    is_tuple = isinstance(userOutNames, tuple)
    is_str = isinstance(userOutNames, str)
    assert(is_tuple or is_str)
    # if tuple, check what is inside
    if is_tuple:
        for userOutNames_loop in userOutNames:
            assert(isinstance(userOutNames_loop, str))
    
    # check output folder exists
    assert(Path(userFilepath).exists())
    
    timePrefix = datetime.now().strftime("%Y.%m.%d..%H.%M.%S.%f")
    # if tuple, do testing with tuple input
    if is_tuple:
        # create all outpaths
        outPath_tuple = ()
        for userOutNames_loop in userOutNames:
            outPath_tuple = outPath_tuple + (userFilepath + r"\\" + timePrefix + " " + userOutNames_loop + ".csv",)
        # check that the files at the filepath do not exist
        for userOutPath_loop in outPath_tuple:
            assert(not Path(userOutPath_loop).exists())
        outPath_return = outPath_tuple
            
    # only other option is string (due to assert earlier)
    # now we do testing on string input
    else:
        outPath_str = userFilepath + r"\\" + timePrefix + " " + userOutNames + ".csv"
        assert(not Path(outPath_str).exists())
        outPath_return = outPath_str
    
    # return the outpaths
    return outPath_return

def fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, userAPIVar1, userAPIVar2=None, userAPIVar3=None, userAPIVar4=None):
    # Function Code: 0002
    # Function Uses: None
   
    assert(isinstance(max_iterations, int))
    # set value to count number of iterations
    current_iter = 1
    # assert that userAPIVar1 is either ints or tuples
    is_var1_int = isinstance(userAPIVar1, int)
    is_var1_tuple = isinstance(userAPIVar1, tuple)
    assert(is_var1_int or is_var1_tuple)
    # mult to current_iter if its a tuple
    # ALSO CHECK IF ITEMS INSIDE TUPLE ARE ALSO INTS
    if is_var1_tuple:
        current_iter = current_iter * len(userAPIVar1)
        for myNum in userAPIVar1:
            assert(isinstance(myNum, int))
    
    # do same as above for others, except open possibility for None inputs
    is_var2_int = isinstance(userAPIVar2, int)
    is_var2_tuple = isinstance(userAPIVar2, tuple)
    is_var2_None = userAPIVar2 == None
    is_var3_int = isinstance(userAPIVar3, int)
    is_var3_tuple = isinstance(userAPIVar3, tuple)
    is_var3_None = userAPIVar3 == None
    is_var4_int = isinstance(userAPIVar4, int)
    is_var4_tuple = isinstance(userAPIVar4, tuple)
    is_var4_None = userAPIVar4 == None  
    assert(is_var2_int or is_var2_tuple or is_var2_None)
    assert(is_var3_int or is_var3_tuple or is_var3_None)
    assert(is_var4_int or is_var4_tuple or is_var4_None)

    if is_var2_tuple:
        current_iter = current_iter * len(userAPIVar2)
        for myNum in userAPIVar2:
            assert(isinstance(myNum, int))
    if is_var3_tuple:
        current_iter = current_iter * len(userAPIVar3)
        for myNum in userAPIVar3:
            assert(isinstance(myNum, int))
    if is_var4_tuple:
        current_iter = current_iter * len(userAPIVar4)
        for myNum in userAPIVar4:
            assert(isinstance(myNum, int))
    
    # if number of iterations is more than what we have as max, return false. else, true
    # if false then don't run main function
    if max_iterations > current_iter: 
        return True
    else:
        return False

#----------------------------------------------

# The following functions allow a user to obtain all (most) info from the fpl api endpoints that I am aware of.
# Most endpoints have variable inputs for specific pages for players/managers/leagues/events.

def fplAPI_mostValuableTeams(save_to_csv=None, func_filepath_save=None, outName_mostValuableTeams=None):
    # Function Code: 0003
    # Function Uses: 0001
    
    # ensure all inputs are of correct type (or if optional and not included, that they are None)
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)

    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_mostValuableTeams = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, outName_mostValuableTeams)
    
    api_link = "https://fantasy.premierleague.com/api/stats/most-valuable-teams/"

    # get the data
    myData = requests.get(api_link).json()

    df_most_valuable_teams = pd.DataFrame.from_dict(myData)

    # export
    if save_to_csv == True:
        df_most_valuable_teams.to_csv(outPath_mostValuableTeams, index=False)

    return df_most_valuable_teams

def fplAPI_setPieceNotes(save_to_csv=None, func_filepath_save=None, outName_setPieceNotes=None, outName_lastUpdated=None):
    # Function Code: 0004
    # Function Uses: 0001    
    
    # ensure all inputs are of correct type, not including optional, however including save_to_csv
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_setPieceNotes, outPath_lastUpdated = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_setPieceNotes, outName_lastUpdated))
    
    api_link = "https://fantasy.premierleague.com/api/team/set-piece-notes/"
    
    # get the data
    myData = requests.get(api_link).json()

    # get main data and re-jig columns to make csv readable
    df_set_piece_notes = pd.json_normalize(myData, record_path=['teams', 'notes'], meta=[['teams','id']])
    df_set_piece_notes = df_set_piece_notes[['teams.id', 'info_message']]

    # get updated time info (annoying)
    fullString = str(myData)
    point1 = fullString.find(":",fullString.find("last_updated"))
    point2 = fullString.find(",",fullString.find("last_updated"))
    data = [[fullString[point1+2:point2]]]
    df_last_updated = pd.DataFrame(data, columns = ['last_updated'])

    # export them
    if save_to_csv == True:
        df_set_piece_notes.to_csv(outPath_setPieceNotes, index=False)
        df_last_updated.to_csv(outPath_lastUpdated, index=False)

    return df_set_piece_notes, df_last_updated

def fplAPI_managerTransfers(manager_id, max_iterations, save_to_csv=None, func_filepath_save=None, outName_transfersMain=None):
    # Function Code: 0005
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, manager_id))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_transfersMain = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, outName_transfersMain)
    
    # create the dataframe, taking tuple entries into consideration
    df_main = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(manager_id) == int: manager_id = (manager_id,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for manager_id_loop in tuple(manager_id):
    
        api_link = "https://fantasy.premierleague.com/api/entry/" + str(manager_id_loop) + "/transfers/"
        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()
        
            df_temp = pd.DataFrame.from_dict(myData)
            
            df_main = pd.concat([df_main, df_temp], axis=0)
        

    # export to csv
    if save_to_csv == True:
        df_main.to_csv(outPath_transfersMain, index=False)
    
    return df_main

def fplAPI_managerHistory(manager_id, max_iterations, save_to_csv=None, func_filepath_save=None, outName_currentSeason=None, outName_pastSeasons=None, outName_chips=None):
    # Function Code: 0006
    # Function Uses: 0001,0002    
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, manager_id))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_currentSeason, outPath_pastSeasons, outPath_chips = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_currentSeason, outName_pastSeasons, outName_chips))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_currentSeason = pd.DataFrame()
    df_pastSeason = pd.DataFrame()
    df_chips = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(manager_id) == int: manager_id = (manager_id,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for manager_id_loop in tuple(manager_id):
        api_link = "https://fantasy.premierleague.com/api/entry/" + str(manager_id_loop) + "/history/"

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # get info via the following
            df_currentSeason_temp = pd.json_normalize(myData, record_path=['current'])
            df_pastSeason_temp = pd.json_normalize(myData, record_path=['past'])
            df_chips_temp = pd.json_normalize(myData, record_path=['chips'])

            # add variable input of endpoint into the dataframes
            df_currentSeason_temp.insert(0, "FA_manager", manager_id_loop)
            df_pastSeason_temp.insert(0, "FA_manager", manager_id_loop)
            df_chips_temp.insert(0, "FA_manager", manager_id_loop)
            
            # concat them all
            df_currentSeason = pd.concat([df_currentSeason, df_currentSeason_temp], axis=0)
            df_pastSeason = pd.concat([df_pastSeason, df_pastSeason_temp], axis=0)
            df_chips = pd.concat([df_chips, df_chips_temp], axis=0)

    # export to csv
    if save_to_csv == True:
        df_currentSeason.to_csv(outPath_currentSeason, index=False)
        df_pastSeason.to_csv(outPath_pastSeasons, index=False)
        df_chips.to_csv(outPath_chips, index=False)

    return df_currentSeason, df_pastSeason, df_chips

def fplAPI_manager(manager_id, max_iterations, save_to_csv=None, func_filepath_save=None, outName_general=None, outName_leagueInfo=None):
    # Function Code: 0007
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, manager_id))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_general, outPath_leagueInfo = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_general, outName_leagueInfo))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_general = pd.DataFrame()
    df_leagueInfo = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(manager_id) == int: manager_id = (manager_id,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for manager_id_loop in tuple(manager_id):
    
        api_link = "https://fantasy.premierleague.com/api/entry/" + str(manager_id_loop) + "/"

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # get info via the following
            # get main, filter to only include normal stats (perhaps an oversight but for now I will allow it. Just remove the filter bit to change it back)
            df_general_temp = pd.DataFrame.from_dict(myData)
            df_general_temp = df_general_temp.filter(items=['classic'],axis=0)

            # get info for all leagues the manager is in
            df_leagueInfo_temp = pd.json_normalize(myData, record_path=['leagues','classic'])

            # add variable input of endpoint into the dataframes
            df_leagueInfo_temp.insert(0, "FA_manager", manager_id_loop)

            # concat them all
            df_general = pd.concat([df_general, df_general_temp], axis=0)
            df_leagueInfo = pd.concat([df_leagueInfo, df_leagueInfo_temp], axis=0)

    # export to csv
    if save_to_csv == True:
        df_general.to_csv(outPath_general, index=False)
        df_leagueInfo.to_csv(outPath_leagueInfo, index=False)

    return df_general, df_leagueInfo

def fplAPI_managerEventPicks(manager_id, event_id, max_iterations, save_to_csv=None, func_filepath_save=None, outName_picks=None, outName_subs=None, outName_entryHistory=None, outName_activeChips=None):
    # Function Code: 0008
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, manager_id, event_id))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_picks, outPath_subs, outPath_entryHistory, outPath_activeChips = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_picks, outName_subs, outName_entryHistory, outName_activeChips))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_picks = pd.DataFrame()
    df_subs = pd.DataFrame()
    df_entryHistory = pd.DataFrame()
    df_activeChips = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(manager_id) == int: manager_id = (manager_id,)
    if type(event_id) == int: event_id = (event_id,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for event_id_loop in tuple(event_id):
         for manager_id_loop in tuple(manager_id):
    
            api_link = "https://fantasy.premierleague.com/api/entry/" + str(manager_id_loop) + "/event/" + str(event_id_loop) + "/picks/"

            # get the data from fpl api, check result is valid, if so then continue
            myData = requests.get(api_link)
            if myData.text != '{"detail":"Not found."}':
                myData = myData.json()

                # get info via the following
                df_picks_temp = pd.json_normalize(myData, record_path=['picks'])
                df_subs_temp = pd.json_normalize(myData, record_path=['automatic_subs'])
                df_entryHistory_temp = pd.json_normalize(myData['entry_history'])
                
                # get wildcard info (annoying)
                fullString = str(myData)
                point1 = fullString.find(":",fullString.find("active_chip"))
                point2 = fullString.find(",",fullString.find("active_chip"))
                data = [[fullString[point1+2:point2], manager_id_loop, event_id_loop]]
                df_activeChips_temp = pd.DataFrame(data, columns = ['active_chip', 'manager_id', 'event_id'])

                # add variable input of endpoint into the dataframes
                df_entryHistory_temp.insert(0, "FA_manager", manager_id_loop)
                df_picks_temp.insert(0, "FA_manager", manager_id_loop)
                df_picks_temp.insert(0, "FA_event", event_id_loop)
                
                # concat them all
                df_picks = pd.concat([df_picks, df_picks_temp], axis=0)
                df_subs = pd.concat([df_subs, df_subs_temp], axis=0)
                df_entryHistory = pd.concat([df_entryHistory, df_entryHistory_temp], axis=0)
                df_activeChips = pd.concat([df_activeChips, df_activeChips_temp], axis=0)


    # export to csv
    if save_to_csv == True:
        df_picks.to_csv(outPath_picks, index=False)
        df_subs.to_csv(outPath_subs, index=False)
        df_entryHistory.to_csv(outPath_entryHistory, index=False)
        df_activeChips.to_csv(outPath_activeChips, index=False)


    return df_picks, df_subs, df_entryHistory, df_activeChips

def fplAPI_leagueStandings(leagueID, pageNumber, max_iterations, save_to_csv=None, func_filepath_save=None, outName_standings=None, outName_info=None, outName_lastUpdate=None, outName_meta=None):
    # Function Code: 0009
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, leagueID, pageNumber))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_standings, outPath_info, outPath_lastUpdate, outPath_meta = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_standings, outName_info, outName_lastUpdate, outName_meta))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_standings = pd.DataFrame()
    df_info = pd.DataFrame()
    df_lastUpdate = pd.DataFrame()
    df_meta = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(leagueID) == int: leagueID = (leagueID,)
    if type(pageNumber) == int: pageNumber = (pageNumber,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for leagueID_loop in tuple(leagueID):
        infoLastUpdate_forLeague = False
        for pageNumber_loop in tuple(pageNumber):
    
            api_link = "https://fantasy.premierleague.com/api/leagues-classic/" + str(leagueID_loop) + "/standings/?page_standings=" + str(pageNumber_loop)

            # get the data from fpl api, check result is valid, if so then continue
            myData = requests.get(api_link)
            if myData.text != '{"detail":"Not found."}':
                myData = myData.json()
                
                # get info and last_update for only the first page in the loop list (that works), and don't bother otherwise. It's the same in all page_nums
                if infoLastUpdate_forLeague == False:
                    infoLastUpdate_forLeague = True
                    df_info_temp = pd.json_normalize(myData['league'])

                    # get last update time info (annoying)
                    fullString = str(myData)
                    point1 = fullString.find(":",fullString.find("last_updated_data"))
                    point2 = fullString.find(",",fullString.find("last_updated_data"))
                    data = [[fullString[point1+2:point2], leagueID_loop, pageNumber_loop]]
                    df_lastUpdate_temp = pd.DataFrame(data, columns = ['last_update', 'league_id', 'page_num'])
                
                    # concat them
                    df_info = pd.concat([df_info, df_info_temp], axis=0)
                    df_lastUpdate = pd.concat([df_lastUpdate, df_lastUpdate_temp], axis=0)
                    
                # get info via the following
                df_standings_temp = pd.json_normalize(myData, record_path=['standings','results'])
                df_meta_temp = pd.json_normalize(myData['standings'])
                
                # add variable input of endpoint into the dataframes
                df_standings_temp.insert(0, "FA_league", leagueID_loop)
                df_standings_temp.insert(0, "FA_page", pageNumber_loop)
                df_meta_temp.insert(0, "FA_league", leagueID_loop)
                
                # concat them all
                df_standings = pd.concat([df_standings, df_standings_temp], axis=0)
                df_meta = pd.concat([df_meta, df_meta_temp], axis=0)


    # export to csv
    if save_to_csv == True:
        df_standings.to_csv(outPath_standings, index=False)
        df_info.to_csv(outPath_info, index=False)
        df_lastUpdate.to_csv(outPath_lastUpdate, index=False)
        df_meta.to_csv(outPath_meta, index=False)


    return df_standings, df_info, df_lastUpdate, df_meta

def fplAPI_liveGameweekEvent(gameweek, max_iterations, save_to_csv=None, func_filepath_save=None, outName_elementStats=None, outName_pointsDistribution=None):
    # Function Code: 0010
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, gameweek))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_elementStats, outPath_pointsDistribution = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_elementStats, outName_pointsDistribution))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_elementStats = pd.DataFrame()
    df_pointsDistribution = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(gameweek) == int: gameweek = (gameweek,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for gameweek_loop in tuple(gameweek):
    
        api_link = 'https://fantasy.premierleague.com/api/event/' + str(gameweek_loop) + '/live/'

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # normalise for the main bulk of stats
            df_elementStats_temp = pd.json_normalize(myData['elements'])

            # normalise for the points distribution
            df_pointsDistribution_temp = pd.json_normalize(myData, record_path=['elements', 'explain', 'stats'],
                meta=[['elements','id'],['elements', 'explain','fixture']])

            # add variable input of endpoint into the dataframes
            df_elementStats_temp.insert(0, "FA_gw", gameweek_loop)
            df_pointsDistribution_temp.insert(0, "FA_gw", gameweek_loop)
            
            # concat them all
            df_elementStats = pd.concat([df_elementStats, df_elementStats_temp], axis=0)
            df_pointsDistribution = pd.concat([df_pointsDistribution, df_pointsDistribution_temp], axis=0)


    # export to csv
    if save_to_csv == True:
        df_elementStats.to_csv(outPath_elementStats, index=False)
        df_pointsDistribution.to_csv(outPath_pointsDistribution, index=False)


    return df_elementStats, df_pointsDistribution

def fplAPI_fixtures(save_to_csv=None, func_filepath_save=None, outName_fixtures=None, outName_fixtureElementStats=None):
    # Function Code: 0011
    # Function Uses: 0001
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_fixtures, outPath_fixtureElementStats = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_fixtures, outName_fixtureElementStats))
    
    api_link = 'https://fantasy.premierleague.com/api/fixtures/'

    # create the dataframes, s.t. all further additions can be concat onto these
    df_fixtures = pd.DataFrame()
    df_fixtureElementStats = pd.DataFrame()

    # get the data from fpl api, check result is valid, if so then continue
    myData = requests.get(api_link)
    if myData.text != '{"detail":"Not found."}':
        myData = myData.json()

        # get info via the following
        # main bulk of stats
        df_fixtures = pd.json_normalize(myData)

        # normalise for the various stats included
        df_away = pd.json_normalize(myData, record_path=['stats', 'a'], meta=[['stats','identifier'],'event','id'])
        df_home = pd.json_normalize(myData, record_path=['stats', 'h'], meta=[['stats','identifier'],'event','id'])

        df_fixtureElementStats = pd.concat([df_away, df_home], axis=0)
        df_fixtureElementStats.sort_values(by=['id'], inplace=True)


    # export to csv
    if save_to_csv == True:
        df_fixtures.to_csv(outPath_fixtures, index=False)
        df_fixtureElementStats.to_csv(outPath_fixtureElementStats, index=False)

    return df_fixtures, df_fixtureElementStats

def fplAPI_eventStatus(save_to_csv=None, func_filepath_save=None, outName_status=None, outName_isUpdating=None):
    # Function Code: 0012
    # Function Uses: 0001
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_status, outPath_isUpdating = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_status, outName_isUpdating))
    
    api_link = "https://fantasy.premierleague.com/api/event-status/"

    # create the dataframes, s.t. all further additions can be concat onto these
    df_status = pd.DataFrame()
    df_isUpdating = pd.DataFrame()

    # get the data from fpl api, check result is valid, if so then continue
    myData = requests.get(api_link)
    if myData.text != '{"detail":"Not found."}':
        myData = myData.json()

        # get info via the following
        df_status = pd.json_normalize(myData['status'])

        # get 'whether updated' info (annoying)
        fullString = str(myData)
        point1 = fullString.find(":",fullString.find("leagues"))
        point2 = fullString.find("}",fullString.find("leagues"))
        data = [[fullString[point1+2:point2]]]
        df_isUpdating = pd.DataFrame(data, columns = ['leagues'])

    # export to csv
    if save_to_csv == True:
        df_status.to_csv(outPath_status, index=False)
        df_isUpdating.to_csv(outPath_isUpdating, index=False)

    return df_status, df_isUpdating

def fplAPI_elementSummary(elementID, max_iterations, save_to_csv=None, func_filepath_save=None, outName_fixtures=None, outName_history=None, outName_historyPast=None):
    # Function Code: 0013
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, elementID))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_fixtures, outPath_history, outPath_historyPast = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_fixtures, outName_history, outName_historyPast))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_fixtures = pd.DataFrame()
    df_history = pd.DataFrame()
    df_historyPast = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(elementID) == int: elementID = (elementID,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for elementID_loop in tuple(elementID):
    
        api_link = "https://fantasy.premierleague.com/api/element-summary/" + str(elementID_loop) + "/"

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # get info via the following
            df_fixtures_temp = pd.json_normalize(myData['fixtures'])
            df_history_temp = pd.json_normalize(myData['history'])
            df_historyPast_temp = pd.json_normalize(myData['history_past'])

            # add variable input of endpoint into the dataframes
            df_fixtures_temp.insert(0, "FA_element", elementID_loop)
            df_history_temp.insert(0, "FA_element", elementID_loop)
            df_historyPast_temp.insert(0, "FA_element", elementID_loop)
            
            # concat them all
            df_fixtures = pd.concat([df_fixtures, df_fixtures_temp], axis=0)
            df_history = pd.concat([df_history, df_history_temp], axis=0)
            df_historyPast = pd.concat([df_historyPast, df_historyPast_temp], axis=0)


    # export to csv
    if save_to_csv == True:
        df_fixtures.to_csv(outPath_fixtures, index=False)
        df_history.to_csv(outPath_history, index=False)
        df_historyPast.to_csv(outPath_historyPast, index=False)


    return df_fixtures, df_history, df_historyPast

def fplAPI_dreamTeam(gameweek, max_iterations, save_to_csv=None, func_filepath_save=None, outName_gameweekDreamTeam=None, outName_gameweekDreamPlayer=None):
    # Function Code: 0014
    # Function Uses: 0001,0002
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(max_iterations, gameweek))
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_gameweekDreamTeam, outPath_gameweekDreamPlayer = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_gameweekDreamTeam, outName_gameweekDreamPlayer))

    # create the dataframes, s.t. all further additions can be concat onto these
    df_gameweekDreamTeam = pd.DataFrame()
    df_gameweekDreamPlayer = pd.DataFrame()
    
    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(gameweek) == int: gameweek = (gameweek,)
    
    # loop over each manager id (iterate over a tuple of the input. If already a tuple, it will remain a tuple)
    for gameweek_loop in tuple(gameweek):
    
        api_link = "https://fantasy.premierleague.com/api/dream-team/" + str(gameweek_loop) + "/"

        # get the data from fpl api, check result is valid, if so then continue
        myData = requests.get(api_link)
        if myData.text != '{"detail":"Not found."}':
            myData = myData.json()

            # get info via the following
            df_gameweekDreamTeam_temp = pd.json_normalize(myData['team'])
            df_gameweekDreamPlayer_temp = pd.json_normalize(myData['top_player'])

            # add variable input of endpoint into the dataframes
            df_gameweekDreamTeam_temp.insert(0, "FA_gw", gameweek_loop)
            df_gameweekDreamPlayer_temp.insert(0, "FA_gw", gameweek_loop)
            
            # concat them all
            df_gameweekDreamTeam = pd.concat([df_gameweekDreamTeam, df_gameweekDreamTeam_temp], axis=0)
            df_gameweekDreamPlayer = pd.concat([df_gameweekDreamPlayer, df_gameweekDreamPlayer_temp], axis=0)

    # export to csv
    if save_to_csv == True:
        df_gameweekDreamTeam.to_csv(outPath_gameweekDreamTeam, index=False)
        df_gameweekDreamPlayer.to_csv(outPath_gameweekDreamPlayer, index=False)


    return df_gameweekDreamTeam, df_gameweekDreamPlayer

def fplAPI_bootstrap(save_to_csv=None, func_filepath_save=None, outName_events=None, outName_teams=None, outName_elements=None, outName_elementTypes=None, outName_phases=None, outName_elementStats=None, outName_gameSettings=None, outName_totalPlayers=None, outName_chipPlays=None):
    # Function Code: 0015
    # Function Uses: 0001
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_events, outPath_teams, outPath_elements, outPath_elementTypes, outPath_phases, outPath_elementStats, outPath_gameSettings, outPath_totalPlayers, outPath_chipPlays = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_events, outName_teams, outName_elements, outName_elementTypes, outName_phases, outName_elementStats, outName_gameSettings, outName_totalPlayers, outName_chipPlays))
    
    api_link = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    
    # get the data from fpl api
    myData = requests.get(api_link).json()

    # get info via the following
    # normalise for all stats
    df_events = pd.json_normalize(myData['events'])
    df_teams = pd.json_normalize(myData['teams'])
    df_elements = pd.json_normalize(myData['elements'])
    df_elementTypes = pd.json_normalize(myData['element_types'])

    df_phases = pd.json_normalize(myData['phases'])
    df_elementStats = pd.json_normalize(myData['element_stats'])
    df_gameSettings = pd.json_normalize(myData['game_settings'])

    # get total players
    # total players exists between a : and , after the text total_players. Just lift it straight out the text and put it in a dataframe
    fullString = str(myData)
    point1 = fullString.find(":",fullString.find("total_players"))
    point2 = fullString.find(",",fullString.find("total_players"))
    data = [[fullString[point1+2:point2]]]
    df_totalPlayers = pd.DataFrame(data, columns = ['total_players'])

    # get chip usage in (slightly) better format from events
    df_chipPlays = pd.json_normalize(myData, record_path=['events','chip_plays'], meta=[['events','id']])



    # export to csv
    if save_to_csv == True:
        df_events.to_csv(outPath_events, index=False)
        df_teams.to_csv(outPath_teams, index=False)
        df_elements.to_csv(outPath_elements, index=False)
        df_elementTypes.to_csv(outPath_elementTypes, index=False)
        
        df_phases.to_csv(outPath_phases, index=False)
        df_elementStats.to_csv(outPath_elementStats, index=False)
        df_gameSettings.to_csv(outPath_gameSettings, index=False)
        
        df_totalPlayers.to_csv(outPath_totalPlayers, index=False)
        df_chipPlays.to_csv(outPath_chipPlays, index=False)

    return df_events, df_teams, df_elements, df_elementTypes, df_phases, df_elementStats, df_gameSettings, df_totalPlayers, df_chipPlays

def fplAPI_bestLeagues(save_to_csv=None, func_filepath_save=None, outName_bestLeagues=None):
    # Function Code: 0016
    # Function Uses: 0001
    
    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_bestLeagues = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_bestLeagues))
    
    api_link = "https://fantasy.premierleague.com/api/stats/best-classic-private-leagues/"

    # get info via the following
    myData = requests.get(api_link).json()

    df_bestLeagues = pd.DataFrame.from_dict(myData)

    # export to csv
    if save_to_csv == True:
        df_bestLeagues.to_csv(outPath_bestLeagues, index=False)

    return df_bestLeagues


# The following functions rely on not only the basic #0001, #0002 functions, but also the other above functions

def fplAPI_returnLastPageandRank(leagueID, pageGuess, estimateMaxIterations, save_to_csv=None, func_filepath_save=None, outName_leagueStats=None):
    # Function Code: 0017
    # Function Uses: 0001,0002,0009
    
    # assert number inputs good, and max_iterations is not exceeded
    assert(fplAPI_specific_assertNumberInputs_checkMaxIter(round(estimateMaxIterations/25), leagueID))

    # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_leagueStats = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_leagueStats))

    # initialise results list
    resultsList = []
    
    # 'save' pageGuess such that on each loop, the program uses this value again
    pageGuessConst = pageGuess

    # if not a tuple, turn integer variable inputs into tuples so they can be iterated over
    if type(leagueID) == int: leagueID = (leagueID,)

    for leagueID_loop in tuple(leagueID):
        pageGuess = pageGuessConst

        df_league = fplAPI_leagueStandings(leagueID_loop, pageGuess, 100)
        # quick check if given answer is correct, if so then exit with page
        if df_league[3].loc[0, "has_next"] == False and len(df_league[3].loc[0, "results"]) > 0:
            for x in df_league[0].tail(1)["rank_sort"].values: myNum = x
            myRow_temp = (leagueID_loop, pageGuess, myNum)
        
        else:
            # while we are not in a page before an empty page, keep doubling the page number
            while df_league[3].loc[0, "has_next"] == True:
                pageGuess = pageGuess * 2
                df_league = fplAPI_leagueStandings(leagueID_loop, pageGuess, 100)

            # at this point we have either returned the correct answer, or pageGuess is a number larger than the answer
            maxPage = pageGuess
            minPage = 1
            
            pageGuess = floor((maxPage+minPage)/2)
            
            df_league = fplAPI_leagueStandings(leagueID_loop, pageGuess, 100)
            
            # while we still don't have the answer
            while not(df_league[3].loc[0, "has_next"] == False and len(df_league[3].loc[0, "results"]) > 0):
                
                # if the answer is smaller, adjust pageGuess accordingly
                if df_league[3].loc[0, "has_next"] == False:
                    maxPage = pageGuess
                # else answer is larger
                else:
                    minPage = pageGuess
                
                # adjust pageGuess
                pageGuess = floor((maxPage+minPage)/2)
                
                df_league = fplAPI_leagueStandings(leagueID_loop, pageGuess, 100)
            
            for x in df_league[0].tail(1)["rank_sort"].values: myNum = x
            myRow_temp = (leagueID_loop, pageGuess, myNum)
        
        resultsList.append(list(myRow_temp))
        
    df_leagueStats = pd.DataFrame(resultsList, columns = ['league ID', 'final page', 'final rank'])    
    
    # export to csv
    if save_to_csv == True:
        df_leagueStats.to_csv(outPath_leagueStats, index=False)

    return df_leagueStats

def FPLAPI_managerPicksPlayers(df_IN_managerPicks, playerID_Tuple, save_to_csv=None, func_filepath_save=None, outName_managerPickPlayers=None):
    # Function Code: #0018
    # Function Uses: #0001
    
    # check inputs are good
    assert(isinstance(df_IN_managerPicks, pd.core.frame.DataFrame))
    assert(isinstance(playerID_Tuple, tuple))
    for playerID in playerID_Tuple:
        assert(isinstance(playerID, int))
    
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_managerPickPlayers = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, outName_managerPickPlayers)
    
    # make new dataframe with all unique manager IDs (from manager list)
    ar_managerIDs = df_IN_managerPicks[['FA_manager']]['FA_manager'].unique()
    df_managerPickCount = pd.DataFrame(ar_managerIDs, columns=['FA_manager'])
    
    
    # go through each manager, count number of instances of player ID for that manager
    managerCountList = []
    for managerID in ar_managerIDs:
        # make smaller df for just that manager
        df_picksFilter = df_IN_managerPicks[df_IN_managerPicks.FA_manager == managerID]
        pickCount = 0
        for playerID in playerID_Tuple:
            # if player id in smaller df, add 1 to the pickcount
            if (playerID in df_picksFilter['element'].unique()) == True:
                pickCount = pickCount + 1
        managerCountList.append(pickCount)

    # add column to manager list, sort by total count
    df_managerPickCount['total_count'] = managerCountList
    df_managerPickCount = df_managerPickCount.sort_values(by=['total_count'], ascending=False)
    
    # export them
    if save_to_csv == True:
        df_managerPickCount.to_csv(outPath_managerPickPlayers, index=False)
    
    return df_managerPickCount

def fplAPI_findSameEventTeam(leagueID, playerIDtuple, captainPlayerID, currentGW, maxIter_leaguePages, maxIter_managerList, filepathToSave=None, outName_playerCountList=None, ifLeagueIsDownload=None, downloadedLeague=None):
    # Function Code: #0019
    # Function Uses: #0001, #0010, #0017, #0009, #0008, #0018
    
    
    # check ifLeagueIsDownload is all good
    assert(isinstance(ifLeagueIsDownload, bool) or ifLeagueIsDownload == None)
    if ifLeagueIsDownload == None: ifLeagueIsDownload = False
    assert(isinstance(downloadedLeague, pd.core.frame.DataFrame) or downloadedLeague == None)

    
    outPath_playerCountList = fplAPI_specific_constructFilepathsAndTestExists(filepathToSave, outName_playerCountList)
       
    
    # download gameweek summary, sum gameweek scores of players in playerIDtuple (taking captain into account)
    df_gwSummary = fplAPI_liveGameweekEvent(currentGW, 100,True,filepathToSave, "gw stats", "gw pointsdist")[0]
    pointsSum = 0
    for playerID in playerIDtuple:
        indexNum = df_gwSummary.index.get_loc(df_gwSummary.query('id == ' + str(playerID)).index[0])
        if playerID == captainPlayerID:
            pointsSum = pointsSum + (2* df_gwSummary.loc[indexNum, "stats.total_points"])
        else:
            pointsSum = pointsSum + df_gwSummary.loc[indexNum, "stats.total_points"]
    # the variable "pointsSum" now holds the total points for that team
    print("Total points of team given is " + str(pointsSum))
    
    
    # if, ifLeagueIsDownload = False, run following to get the league download through API
    if ifLeagueIsDownload == False:
    
        # check length of league. If longer than limit set, exit, else continue.
        numLeaguePages = fplAPI_returnLastPageandRank(leagueID, 7, 100).loc[0, "final page"]
        if numLeaguePages >= maxIter_leaguePages:
            print("page limit is " + str(maxIter_leaguePages) + ", league pages is " + str(numLeaguePages) + ", therefore exit")
            exit()
        print("page limit is " + str(maxIter_leaguePages) + ", league pages is " + str(numLeaguePages) + ", therefore continue") 
        
        
        # get tuple of manager IDs in the league with their gameweek total = pointsSum
        df_leagueToFilter = fplAPI_leagueStandings(leagueID, tuple(range(1,numLeaguePages+1)), maxIter_leaguePages+10, True, filepathToSave, str(leagueID) + " standings", str(leagueID) + " info", str(leagueID) + " lastupdate", str(leagueID) + " meta")[0]
        
    # if league already downloaded, get it from
    else:
        df_leagueToFilter = downloadedLeague
        print("League obtained from downloaded files")
        
        
        
    df_leagueToFilter = df_leagueToFilter[df_leagueToFilter.event_total == pointsSum]
    managerIDList = tuple(list(df_leagueToFilter['entry']))
    # if manager list too long, print warning and exit
    if len(managerIDList) >= maxIter_managerList:
        print("manager limit is " + str(maxIter_managerList) + ", number of managers matching points total is " + str(len(managerIDList)) + ", therefore exit")
        exit()
    print("manager limit is " + str(maxIter_managerList) + ", number of managers matching points total is " + str(len(managerIDList)) + ", therefore continue") 
        
    
    
    # for each manager in managerIDList, get their picks
    df_managerPicks = fplAPI_managerEventPicks(managerIDList,currentGW,100000000,True,filepathToSave,"manager picks","manager subs", "manager history", "manager chips")[0]
    
    # for each manager find how many of their picks are in the player list
    df_playerCounts = FPLAPI_managerPicksPlayers(df_managerPicks, playerIDtuple)
    

    df_playerCounts.to_csv(outPath_playerCountList, index=False)

    
    return df_playerCounts

def fplAPI_allPlayersElementSummary(save_to_csv=None, func_filepath_save=None, outName_fixtures=None, outName_history=None, outName_historyPast=None):
    # Function Code: #0020
    # Function Uses: #0001, #0013

    # find the highest id that covers a player
    df_latestGW = fplAPI_liveGameweekEvent(15,1000)[0]
    max_id = df_latestGW['id'].max()
    
   # check save_to_csv is bool or none
    assert(isinstance(save_to_csv, bool) or save_to_csv == None)
    # check filepath and filenames are all in order
    if save_to_csv == True:
        outPath_fixtures, outPath_history, outPath_historyPast = fplAPI_specific_constructFilepathsAndTestExists(func_filepath_save, (outName_fixtures, outName_history, outName_historyPast))

    df_fixtures, df_history, df_historyPast = fplAPI_elementSummary(tuple(range(1,max_id+1)),100000)
    
    # export to csv
    if save_to_csv == True:
        df_fixtures.to_csv(outPath_fixtures, index=False)
        df_history.to_csv(outPath_history, index=False)
        df_historyPast.to_csv(outPath_historyPast, index=False)


    return df_fixtures, df_history, df_historyPast



