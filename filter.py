import json
  
# Opening JSON file
f = open('media.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

for serie in data["hits"]["hits"]:
    serie["_source"]["title"]["keyword"]
    #print(serie["_source"]["title"]["keyword"])
    if "seasons" in serie["_source"]:
        for season in serie["_source"]["seasons"]:
            #print(season)
            if len(season["episodeIds"]) > 1 and len(season["episodeIds"]) < 15:
                print(serie["_source"]["title"]["keyword"])
                print(serie["_source"]["id"])
                print(season["episodeIds"])
                print("###############################################################")
    
# Closing file
f.close()