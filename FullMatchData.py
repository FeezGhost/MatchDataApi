### THIS API SEEKS TO CAPTURE LATEST MATCH DATA BY INPUTTING PLAYER'S RIOT ID AND TAGLINE. THEN, IT WILL CREATE TWO TABLES AND SAVE IT ON THE DIVERGENET MEDIA MYSQL DATABASE. ONE TABLE PER TEAM.

### SETUP:
#   - Add in whitelisted IP address on lines 793, 831 and 891 



#Imports
import requests
import json
import codecs
# API Key = RGAPI-cfc7e7fe-9ac5-48ae-8802-49f534119acf

###DELETE FILES###

for y in range(5):

#RED DELETE FILES
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/playerName/red"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/acs/acsRed"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/agentName/agentRed"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/kda/kdaRed"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/resultBlue.txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/wlBlue.txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()

        
#BLUE DELETE FILES
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/playerName/blue"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/acs/acsBlue"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/agentName/agentBlue"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/kda/kdaBlue"+str(y+1)+".txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/resultRed.txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/wlRed.txt", "r+") as f:
        same = f.read() #Read everything in the file
        f.seek(0) #Rewind
        f.truncate(0) #Erase file
        f.close()

######################################   
############# GRAB PUUID #############
######################################    

#Enter API Key and load in to API URL   
name = input('Enter Riot Name ')
tagline = input('Enter Tagline ')
response1 = requests.get('https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+name+'/'+tagline+'?api_key=RGAPI-977cb3bf-a83f-4bc4-9f02-3d7ed39b537c')

#Check Error
status = response1.status_code
if status > 200:
    print ('Error PUUID')

#Loads PUUID
content1 = response1.json()
puuid = content1[("puuid")]


######################################   
############ GET MATCH ID ############
######################################   


#API URL
response2 = requests.get("https://na.api.riotgames.com/val/match/v1/matchlists/by-puuid/"+puuid+"?api_key=RGAPI-977cb3bf-a83f-4bc4-9f02-3d7ed39b537c")

#Check Error
status = response2.status_code
if status > 200:
    print ('Error MatchID')

#Recent Match ID
content2 = response2.json()
matchList = content2["history"][0]
matchId = matchList["matchId"]


######################################   
############# LOAD INFO ##############
######################################  


#API URL
response3 = requests.get("https://na.api.riotgames.com/val/match/v1/matches/"+matchId+"?api_key=RGAPI-977cb3bf-a83f-4bc4-9f02-3d7ed39b537c")

#Load Match Info
data = response3.text
json = json.loads(data)
players = json["players"]
result = json["teams"]
resultRed = result[0]["won"]
resultRoundsRed = result[0]["roundsWon"]
resultBlue = result[1]["won"]
resultRoundsBlue = result[1]["roundsWon"]

######################################   
########### SORTING INFO #############
###################################### 

## APPENDS ##

#BLUE
teamBlue = []
agentBlue = []
scoreBlue = []
killsBlue = []
deathsBlue = []
assistsBlue = []
roundsBlue = []
acsBlue = []
kdaBlue = []

#RED
teamRed = []
agentRed = []
scoreRed = []
killsRed = []
deathsRed = []
assistsRed = []
roundsRed = []
acsRed = []
kdaRed = []


####### LOADING ALL PLAYER INFO #######

########## Player 1 info ##########
try:
    player1 = players[0]["stats"]
    score1 = player1["score"]

except (TypeError,IndexError):
            pass
    
else:
        player1 = players[0]["stats"]
        name1 = (players[0]["gameName"]).encode("utf-8")
        characterID1 = players[0]["characterId"]
        score1 = player1["score"]
        kills1 = player1["kills"]
        deaths1 = player1["deaths"]
        assists1 = player1["assists"]
        rounds1 = player1["roundsPlayed"]
        
#### CHARACTER1 CODING ####
        if characterID1 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
            agent1 = ("Breach")
        elif characterID1 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
            agent1 = ("Raze")
        elif characterID1 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
            agent1 = ("Chamber")
        elif characterID1 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
            agent1 = ("Kay/O")
        elif characterID1 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
            agent1 = ("Skye")
        elif characterID1 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
            agent1 = ("Cypher")
        elif characterID1 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
            agent1 = ("Sova")
        elif characterID1 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
            agent1 = ("Killjoy")
        elif characterID1 == ("707eab51-4836-f488-046a-cda6bf494859"):
            agent1 = ("Viper")
        elif characterID1 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
            agent1 = ("Phoenix")
        elif characterID1 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
            agent1 = ("Astra")
        elif characterID1 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
            agent1 = ("Brimstone")
        elif characterID1 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
            agent1 = ("Neon")
        elif characterID1 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
            agent1 = ("Yoru")
        elif characterID1 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
            agent1 = ("Sage")
        elif characterID1 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
            agent1 = ("Reyna")
        elif characterID1 == ("8e253930-4c05-31dd-1b6c-968525494517"):
            agent1 = ("Omen")
        elif characterID1 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
            agent1 = ("Jett")
        elif characterID1 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
            agent1 = ("Sova")
        elif characterID1 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
            agent1 = ("Fade")
        
### SORT TEAMS
        if players[0]["teamId"] == ('Blue'): 
            teamBlue.append(name1)
            agentBlue.append(agent1)
            scoreBlue.append(score1)
            killsBlue.append(kills1)
            deathsBlue.append(deaths1)
            assistsBlue.append(assists1)
            roundsBlue.append(rounds1)
            
        if players[0]["teamId"] == ('Red'): 
            teamRed.append(name1)
            agentRed.append(agent1)
            scoreRed.append(score1)
            killsRed.append(kills1)
            deathsRed.append(deaths1)
            assistsRed.append(assists1)
            roundsRed.append(rounds1)
########## Player 2 info ##########
try:
    player2 = players[1]["stats"]
    score2 = player2["score"]
except (TypeError,IndexError):
            pass
        
else:
        player2 = players[1]["stats"]
        name2 = (players[1]["gameName"]).encode("utf-8")
        characterID2 = players[1]["characterId"]
        score2 = player2["score"]
        kills2 = player2["kills"]
        deaths2 = player2["deaths"]
        assists2 = player2["assists"]
        rounds2 = player2["roundsPlayed"]
        
#### CHARACTER2 CODING ####
        if characterID2 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
            agent2 = ("Breach")
        elif characterID2 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
            agent2 = ("Raze")
        elif characterID2 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
            agent2 = ("Chamber")
        elif characterID2 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
            agent2 = ("Kay/O")
        elif characterID2 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
            agent2 = ("Skye")
        elif characterID2 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
            agent2 = ("Cypher")
        elif characterID2 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
            agent2 = ("Sova")
        elif characterID2 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
            agent2 = ("Killjoy")
        elif characterID2 == ("707eab51-4836-f488-046a-cda6bf494859"):
            agent2 = ("Viper")
        elif characterID2 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
            agent2 = ("Phoenix")
        elif characterID2 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
            agent2 = ("Astra")
        elif characterID2 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
            agent2 = ("Brimstone")
        elif characterID2 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
            agent2 = ("Neon")
        elif characterID2 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
            agent2 = ("Yoru")
        elif characterID2 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
            agent2 = ("Sage")
        elif characterID2 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
            agent2 = ("Reyna")
        elif characterID2 == ("8e253930-4c05-31dd-1b6c-968525494517"):
            agent2 = ("Omen")
        elif characterID2 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
            agent2 = ("Jett")
        elif characterID2 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
            agent2 = ("Sova")
        elif characterID2 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
            agent2 = ("Fade")

### SORT TEAMS

#RED
        if players[1]["teamId"] == ('Red'): 
            teamRed.append(name2)
            agentRed.append(agent2)
            scoreRed.append(score2)
            killsRed.append(kills2)
            deathsRed.append(deaths2)
            assistsRed.append(assists2)
            roundsRed.append(rounds2)
#BLUE
        if players[1]["teamId"] == ('Blue'): 
            teamBlue.append(name2)
            agentBlue.append(agent2)
            scoreBlue.append(score2)
            killsBlue.append(kills2)
            deathsBlue.append(deaths2)
            assistsBlue.append(assists2)
            roundsBlue.append(rounds2)
            
########## Player 3 info ##########
try:
    player3 = players[2]["stats"]
    score3 = player3["score"]
except (TypeError,IndexError):
    pass
    
else:
        player3 = players[2]["stats"]
        name3 = (players[2]["gameName"]).encode("utf-8")
        characterID3 = players[2]["characterId"]
        score3 = player3["score"]
        kills3 = player3["kills"]
        deaths3 = player3["deaths"]
        assists3 = player3["assists"]
        rounds3 = player3["roundsPlayed"]
        
#### CHARACTER3 CODING ####
        if characterID3 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
            agent3 = ("Breach")
        elif characterID3 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
            agent3 = ("Raze")
        elif characterID3 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
            agent3 = ("Chamber")
        elif characterID3 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
            agent3 = ("Kay/O")
        elif characterID3 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
            agent3 = ("Skye")
        elif characterID3 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
            agent3 = ("Cypher")
        elif characterID3 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
            agent3 = ("Sova")
        elif characterID3 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
            agent3 = ("Killjoy")
        elif characterID3 == ("707eab51-4836-f488-046a-cda6bf494859"):
            agent3 = ("Viper")
        elif characterID3 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
            agent3 = ("Phoenix")
        elif characterID3 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
            agent3 = ("Astra")
        elif characterID3 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
            agent3 = ("Brimstone")
        elif characterID3 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
            agent3 = ("Neon")
        elif characterID3 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
            agent3 = ("Yoru")
        elif characterID3 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
            agent3 = ("Sage")
        elif characterID3 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
            agent3 = ("Reyna")
        elif characterID3 == ("8e253930-4c05-31dd-1b6c-968525494517"):
            agent3 = ("Omen")
        elif characterID3 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
            agent3 = ("Jett")
        elif characterID3 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
            agent3 = ("Sova")
        elif characterID3 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
            agent3 = ("Fade")

### SORT TEAMS

#RED
        if players[2]["teamId"] == ('Red'): 
            teamRed.append(name3)
            agentRed.append(agent3)
            scoreRed.append(score3)
            killsRed.append(kills3)
            deathsRed.append(deaths3)
            assistsRed.append(assists3)
            roundsRed.append(rounds3)
#BLUE
        if players[2]["teamId"] == ('Blue'): 
            teamBlue.append(name3)
            agentBlue.append(agent3)
            scoreBlue.append(score3)
            killsBlue.append(kills3)
            deathsBlue.append(deaths3)
            assistsBlue.append(assists3)
            roundsBlue.append(rounds3)

########## Player 4 info ##########
try:
    player4 = players[3]["stats"]
    score4 = player4["score"]      
except (TypeError,IndexError):
    pass
            
else:
    player4 = players[3]["stats"]
    name4 = (players[3]["gameName"]).encode("utf-8")
    characterID4 = players[3]["characterId"]
    score4 = player4["score"]
    kills4 = player4["kills"]
    deaths4 = player4["deaths"]
    assists4 = player4["assists"]
    rounds4 = player4["roundsPlayed"]
    
#### CHARACTER4 CODING ####
    if characterID4 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent4 = ("Breach")
    elif characterID4 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent4 = ("Raze")
    elif characterID4 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent4 = ("Chamber")
    elif characterID4 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent4 = ("Kay/O")
    elif characterID4 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent4 = ("Skye")
    elif characterID4 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent4 = ("Cypher")
    elif characterID4 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent4 = ("Sova")
    elif characterID4 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent4 = ("Killjoy")
    elif characterID4 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent4 = ("Viper")
    elif characterID4 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent4 = ("Phoenix")
    elif characterID4 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent4 = ("Astra")
    elif characterID4 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent4 = ("Brimstone")
    elif characterID4 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent4 = ("Neon")
    elif characterID4 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent4 = ("Yoru")
    elif characterID4 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent4 = ("Sage")
    elif characterID4 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent4 = ("Reyna")
    elif characterID4 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent4 = ("Omen")
    elif characterID4 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent4 = ("Jett")
    elif characterID4 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent4 = ("Sova")
    elif characterID4 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent4 = ("Fade")

### SORT TEAMS

#BLUE
    if players[3]["teamId"] == ('Blue'): 
        teamBlue.append(name4)
        agentBlue.append(agent4)
        scoreBlue.append(score4)
        killsBlue.append(kills4)
        deathsBlue.append(deaths4)
        assistsBlue.append(assists4)
        roundsBlue.append(rounds4)
#RED
    if players[3]["teamId"] == ('Red'): 
        teamRed.append(name4)
        agentRed.append(agent4)
        scoreRed.append(score4)
        killsRed.append(kills4)
        deathsRed.append(deaths4)
        assistsRed.append(assists4)
        roundsRed.append(rounds4)

########## Player 5 info ##########
try:
    player5 = players[4]["stats"]
    score5 = player5["score"]           
except (TypeError,IndexError):
    pass
                
else:
    player5 = players[4]["stats"]
    name5 = (players[4]["gameName"]).encode("utf-8")
    characterID5 = players[4]["characterId"]
    score5 = player5["score"]
    kills5 = player5["kills"]
    deaths5 = player5["deaths"]
    assists5 = player5["assists"]
    rounds5 = player5["roundsPlayed"]
    
#### CHARACTER5 CODING ####
    if characterID5 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent5 = ("Breach")
    elif characterID5 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent5 = ("Raze")
    elif characterID5 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent5 = ("Chamber")
    elif characterID5 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent5 = ("Kay/O")
    elif characterID5 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent5 = ("Skye")
    elif characterID5 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent5 = ("Cypher")
    elif characterID5 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent5 = ("Sova")
    elif characterID5 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent5 = ("Killjoy")
    elif characterID5 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent5 = ("Viper")
    elif characterID5 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent5 = ("Phoenix")
    elif characterID5 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent5 = ("Astra")
    elif characterID5 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent5 = ("Brimstone")
    elif characterID5 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent5 = ("Neon")
    elif characterID5 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent5 = ("Yoru")
    elif characterID5 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent5 = ("Sage")
    elif characterID5 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent5 = ("Reyna")
    elif characterID5 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent5 = ("Omen")
    elif characterID5 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent5 = ("Jett")
    elif characterID5 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent5 = ("Sova")
    elif characterID5 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent5 = ("Fade")

### SORT TEAMS
#RED
    if players[4]["teamId"] == ('Red'): 
        teamRed.append(name5)
        agentRed.append(agent5)
        scoreRed.append(score5)
        killsRed.append(kills5)
        deathsRed.append(deaths5)
        assistsRed.append(assists5)
        roundsRed.append(rounds5)
#BLUE
    if players[4]["teamId"] == ('Blue'): 
        teamBlue.append(name5)
        agentBlue.append(agent5)
        scoreBlue.append(score5)
        killsBlue.append(kills5)
        deathsBlue.append(deaths5)
        assistsBlue.append(assists5)
        roundsBlue.append(rounds5)
    
########## Player 6 info ##########
try:
    player6 = players[5]["stats"]
    score6 = player6["score"]               
except (TypeError,IndexError):
    pass
                    
else:
    player6 = players[5]["stats"]
    name6 = (players[5]["gameName"]).encode("utf-8")
    characterID6 = players[5]["characterId"]
    score6 = player6["score"]
    kills6 = player6["kills"]
    deaths6 = player6["deaths"]
    assists6 = player6["assists"]
    rounds6 = player6["roundsPlayed"]
    
#### CHARACTER6 CODING ####
    if characterID6 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent6 = ("Breach")
    elif characterID6 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent6 = ("Raze")
    elif characterID6 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent6 = ("Chamber")
    elif characterID6 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent6 = ("Kay/O")
    elif characterID6 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent6 = ("Skye")
    elif characterID6 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent6 = ("Cypher")
    elif characterID6 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent6 = ("Sova")
    elif characterID6 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent6 = ("Killjoy")
    elif characterID6 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent6 = ("Viper")
    elif characterID6 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent6 = ("Phoenix")
    elif characterID6 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent6 = ("Astra")
    elif characterID6 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent6 = ("Brimstone")
    elif characterID6 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent6 = ("Neon")
    elif characterID6 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent6 = ("Yoru")
    elif characterID6 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent6 = ("Sage")
    elif characterID6 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent6 = ("Reyna")
    elif characterID6 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent6 = ("Omen")
    elif characterID6 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent6 = ("Jett")
    elif characterID6 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent6 = ("Sova")
    elif characterID6 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent6 = ("Fade")

### SORT TEAMS

#BLUE
    if players[5]["teamId"] == ('Blue'): 
        teamBlue.append(name6)
        agentBlue.append(agent6)
        scoreBlue.append(score6)
        killsBlue.append(kills6)
        deathsBlue.append(deaths6)
        assistsBlue.append(assists6)
        roundsBlue.append(rounds6)
#RED
    if players[5]["teamId"] == ('Red'): 
        teamRed.append(name6)
        agentRed.append(agent6)
        scoreRed.append(score6)
        killsRed.append(kills6)
        deathsRed.append(deaths6)
        assistsRed.append(assists6)
        roundsRed.append(rounds6)
        
########## Player 7 info ##########
try:
    player7 = players[6]["stats"]
    score7 = player7["score"]                   
except (TypeError,IndexError):
    pass
                        
else:
    player7 = players[6]["stats"]
    name7 = (players[6]["gameName"]).encode("utf-8")
    characterID7 = players[6]["characterId"]
    score7 = player7["score"]
    kills7 = player7["kills"]
    deaths7 = player7["deaths"]
    assists7 = player7["assists"]
    rounds7 = player7["roundsPlayed"]
    
#### CHARACTER7 CODING ####
    if characterID7 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent7 = ("Breach")
    elif characterID7 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent7 = ("Raze")
    elif characterID7 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent7 = ("Chamber")
    elif characterID7 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent7 = ("Kay/O")
    elif characterID7 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent7 = ("Skye")
    elif characterID7 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent7 = ("Cypher")
    elif characterID7 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent7 = ("Sova")
    elif characterID7 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent7 = ("Killjoy")
    elif characterID7 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent7 = ("Viper")
    elif characterID7 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent7 = ("Phoenix")
    elif characterID7 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent7 = ("Astra")
    elif characterID7 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent7 = ("Brimstone")
    elif characterID7 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent7 = ("Neon")
    elif characterID7 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent7 = ("Yoru")
    elif characterID7 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent7 = ("Sage")
    elif characterID7 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent7 = ("Reyna")
    elif characterID7 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent7 = ("Omen")
    elif characterID7 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent7 = ("Jett")
    elif characterID7 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent7 = ("Sova")
    elif characterID7 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent7 = ("Fade")

### SORT TEAMS

#RED
    if players[6]["teamId"] == ('Red'): 
        teamRed.append(name7)
        agentRed.append(agent7)
        scoreRed.append(score7)
        killsRed.append(kills7)
        deathsRed.append(deaths7)
        assistsRed.append(assists7)
        roundsRed.append(rounds7)
#BLUE
    if players[6]["teamId"] == ('Blue'): 
        teamBlue.append(name7)
        agentBlue.append(agent7)
        scoreBlue.append(score7)
        killsBlue.append(kills7)
        deathsBlue.append(deaths7)
        assistsBlue.append(assists7)
        roundsBlue.append(rounds7)
        
########## Player 8 info ##########
try:
    player8 = players[7]["stats"]
    score8 = player8["score"]                        
except (TypeError,IndexError):
    pass
                            
else:
    player8 = players[7]["stats"]
    name8 = (players[7]["gameName"]).encode("utf-8")
    characterID8 = players[7]["characterId"]
    score8 = player8["score"]
    kills8 = player8["kills"]
    deaths8 = player8["deaths"]
    assists8 = player8["assists"]
    rounds8 = player8["roundsPlayed"]
    
#### CHARACTER8 CODING ####
    if characterID8 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent8 = ("Breach")
    elif characterID8 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent8 = ("Raze")
    elif characterID8 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent8 = ("Chamber")
    elif characterID8 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent8 = ("Kay/O")
    elif characterID8 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent8 = ("Skye")
    elif characterID8 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent8 = ("Cypher")
    elif characterID8 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent8 = ("Sova")
    elif characterID8 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent8 = ("Killjoy")
    elif characterID8 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent8 = ("Viper")
    elif characterID8 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent8 = ("Phoenix")
    elif characterID8 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent8 = ("Astra")
    elif characterID8 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent8 = ("Brimstone")
    elif characterID8 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent8 = ("Neon")
    elif characterID8 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent8 = ("Yoru")
    elif characterID8 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent8 = ("Sage")
    elif characterID8 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent8 = ("Reyna")
    elif characterID8 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent8 = ("Omen")
    elif characterID8 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent8 = ("Jett")
    elif characterID8 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent8 = ("Sova")
    elif characterID8 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent8 = ("Fade")

### SORT TEAMS

#BLUE
    if players[7]["teamId"] == ('Blue'): 
        teamBlue.append(name8)
        agentBlue.append(agent8)
        scoreBlue.append(score8)
        killsBlue.append(kills8)
        deathsBlue.append(deaths8)
        assistsBlue.append(assists8)
        roundsBlue.append(rounds8)
#RED
    if players[7]["teamId"] == ('Red'): 
        teamRed.append(name8)
        agentRed.append(agent8)
        scoreRed.append(score8)
        killsRed.append(kills8)
        deathsRed.append(deaths8)
        assistsRed.append(assists8)
        roundsRed.append(rounds8)

########## Player 9 info ##########
try:
    player9 = players[8]["stats"]
    score9 = player9["score"]                           
except (TypeError,IndexError):
    pass
                                
else:
    player9 = players[8]["stats"]
    name9 = (players[8]["gameName"]).encode("utf-8")
    characterID9 = players[8]["characterId"]
    score9 = player9["score"]
    kills9 = player9["kills"]
    deaths9 = player9["deaths"]
    assists9 = player9["assists"]
    rounds9 = player9["roundsPlayed"]
    
#### CHARACTER9 CODING ####
    if characterID9 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent9 = ("Breach")
    elif characterID9 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent9 = ("Raze")
    elif characterID9 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent9 = ("Chamber")
    elif characterID9 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent9 = ("Kay/O")
    elif characterID9 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent9 = ("Skye")
    elif characterID9 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent9 = ("Cypher")
    elif characterID9 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent9 = ("Sova")
    elif characterID9 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent9 = ("Killjoy")
    elif characterID9 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent9 = ("Viper")
    elif characterID9 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent9 = ("Phoenix")
    elif characterID9 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent9 = ("Astra")
    elif characterID9 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent9 = ("Brimstone")
    elif characterID9 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent9 = ("Neon")
    elif characterID9 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent9 = ("Yoru")
    elif characterID9 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent9 = ("Sage")
    elif characterID9 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent9 = ("Reyna")
    elif characterID9 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent9 = ("Omen")
    elif characterID9 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent9 = ("Jett")
    elif characterID9 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent9 = ("Sova")
    elif characterID9 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent9 = ("Fade")

### SORT TEAMS

#RED
    if players[8]["teamId"] == ('Red'): 
        teamRed.append(name9)
        agentRed.append(agent9)
        scoreRed.append(score9)
        killsRed.append(kills9)
        deathsRed.append(deaths9)
        assistsRed.append(assists9)
        roundsRed.append(rounds9)
#BLUE
    if players[8]["teamId"] == ('Blue'): 
        teamBlue.append(name9)
        agentBlue.append(agent9)
        scoreBlue.append(score9)
        killsBlue.append(kills9)
        deathsBlue.append(deaths9)
        assistsBlue.append(assists9)
        roundsBlue.append(rounds9)

########## Player 10 info ##########
try:
    player10 = players[9]["stats"]
    score10 = player10["score"]                                
except (TypeError,IndexError):
    pass
                                    
else:
    player10 = players[9]["stats"]
    name10 = (players[9]["gameName"]).encode("utf-8")
    characterID10 = players[9]["characterId"]
    score10 = player10["score"]
    kills10 = player10["kills"]
    deaths10 = player10["deaths"]
    assists10 = player10["assists"]
    rounds10 = player10["roundsPlayed"]
    
#### CHARACTER10 CODING ####
    if characterID10 == ("5f8d3a7f-467b-97f3-062c-13acf203c006"):
        agent10 = ("Breach")
    elif characterID10 == ("f94c3b30-42be-e959-889c-5aa313dba261"):
        agent10 = ("Raze")
    elif characterID10 == ("22697a3d-45bf-8dd7-4fec-84a9e28c69d7"):
        agent10 = ("Chamber")
    elif characterID10 == ("601dbbe7-43ce-be57-2a40-4abd24953621"):
        agent10 = ("Kay/O")
    elif characterID10 == ("6f2a04ca-43e0-be17-7f36-b3908627744d"):
        agent10 = ("Skye")
    elif characterID10 == ("117ed9e3-49f3-6512-3ccf-0cada7e3823b"):
        agent10 = ("Cypher")
    elif characterID10 == ("ded3520f-4264-bfed-162d-b080e2abccf9"):
        agent10 = ("Sova")
    elif characterID10 == ("1e58de9c-4950-5125-93e9-a0aee9f98746"):
        agent10 = ("Killjoy")
    elif characterID10 == ("707eab51-4836-f488-046a-cda6bf494859"):
        agent10 = ("Viper")
    elif characterID10 == ("eb93336a-449b-9c1b-0a54-a891f7921d69"):
        agent10 = ("Phoenix")
    elif characterID10 == ("41fb69c1-4189-7b37-f117-bcaf1e96f1bf"):
        agent10 = ("Astra")
    elif characterID10 == ("9f0d8ba9-4140-b941-57d3-a7ad57c6b417"):
        agent10 = ("Brimstone")
    elif characterID10 == ("bb2a4828-46eb-8cd1-e765-15848195d751"):
        agent10 = ("Neon")
    elif characterID10 == ("7f94d92c-4234-0a36-9646-3a87eb8b5c89"):
        agent10 = ("Yoru")
    elif characterID10 == ("569fdd95-4d10-43ab-ca70-79becc718b46"):
        agent10 = ("Sage")
    elif characterID10 == ("a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"):
        agent10 = ("Reyna")
    elif characterID10 == ("8e253930-4c05-31dd-1b6c-968525494517"):
        agent10 = ("Omen")
    elif characterID10 == ("add6443a-41bd-e414-f6ad-e58d267f4e95"):
        agent10 = ("Jett")
    elif characterID10 == ("320b2a48-4d9b-a075-30f1-1f93a9b638fa"):
        agent10 = ("Sova")
    elif characterID10 == ("dade69b4-4f5a-8528-247b-219e5a1facd6"):
        agent10 = ("Fade")
        
### SORT TEAMS

#BLUE
    if players[9]["teamId"] == ('Blue'): 
        teamBlue.append(name10)
        agentBlue.append(agent10)
        scoreBlue.append(score10)
        killsBlue.append(kills10)
        deathsBlue.append(deaths10)
        assistsBlue.append(assists10)
        roundsBlue.append(rounds10)
#RED
    if players[9]["teamId"] == ('Red'): 
        teamRed.append(name10)
        agentRed.append(agent10)
        scoreRed.append(score10)
        killsRed.append(kills10)
        deathsRed.append(deaths10)
        assistsRed.append(assists10)
        roundsRed.append(rounds10)



    
######################################   
########## WRITE .TXT FILES ##########
###################################### 

##### CALCULATING ACS AND KDA #####

#RED TEAM#

for i in range(len(teamRed)):
    kdaRed.append(((killsRed[i])+(assistsRed[i]))/(deathsRed[i]))
    acsRed.append((scoreRed[i])/(roundsRed[i]))

#Writing
    with codecs.open("C:/Users/RaulC/Documents/DM API/APITexts/red/playerName/red"+str(i+1)+".txt", "r+", encoding='utf-8') as f:
        old = f.read() #Read everything in the file
        f.write(str((teamRed[i]).decode("utf-8")))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/agentName/agentRed"+str(i+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("Agent: ")
        f.write(str(agentRed[i]))
        f.close()

    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/acs/acsRed"+str(i+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("ACS: ")
        f.write(str(round(acsRed[i],1)))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/kda/kdaRed"+str(i+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("KDA: ")
        f.write(str(round(kdaRed[i],1)))
        f.close()

#BLUE TEAM#

for x in range(len(teamBlue)):
    kdaBlue.append(((killsBlue[x])+(assistsBlue[x]))/(deathsBlue[x]))
    acsBlue.append((scoreBlue[x])/(roundsBlue[x]))

#Writing
    with codecs.open("C:/Users/RaulC/Documents/DM API/APITexts/blue/playerName/blue"+str(x+1)+".txt", "r+", encoding='utf-8') as f:
        old = f.read() #Read everything in the file
        print(type(teamBlue[x]))
        f.write(str((teamBlue[x]).decode("utf-8")))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/agentName/agentBlue"+str(x+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("Agent: ")
        f.write(str(agentBlue[x]))
        f.close()
    
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/acs/acsBlue"+str(x+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("ACS: ")
        f.write(str(round(acsBlue[x],1)))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/kda/kdaBlue"+str(x+1)+".txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("KDA: ")
        f.write(str(round(kdaBlue[x],1)))
        f.close()


if resultRed == ("True"):
    
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/resultBlue.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write(str(resultRoundsBlue))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/resultRed.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write(str(resultRoundsRed))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/wlRed.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("WIN")
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/wlBlue.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("LOSE")
        f.close()
        
else:
    
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/resultBlue.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write(str(resultRoundsBlue))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/resultRed.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write(str(resultRoundsRed))
        f.close()
        
    with open("C:/Users/RaulC/Documents/DM API/APITexts/red/wlRed.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("LOSE")
        f.close()
    with open("C:/Users/RaulC/Documents/DM API/APITexts/blue/wlBlue.txt", "r+") as f:
        old = f.read() #Read everything in the file
        f.write("WIN")
        f.close()

print (teamBlue)
print ("\n")
print (kdaBlue)
print ("\n")
print (resultRoundsBlue)
print ("--------")
print(teamRed)
print ("\n")
print (kdaRed)
print ("\n")
print (resultRoundsRed)