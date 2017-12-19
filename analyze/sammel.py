import json

def sammeln(obs):

    arrayVal=[0,0,0,0,0,0,0,0]
    arrayWords=["minerals:","vespene:","food_cap:","food_used:","food_army:","food_workers:","army_count:","game_loop:"]

    out = str(obs).split(' ')
    out2 = str(obs).split('\n')
    
    
    for i in range(0,len(arrayWords)):

               
        try:
            arrayVal[i] = out[out.index(arrayWords[i]) + 1]

        except ValueError:
            arrayVal[i] = -1


    apm = 69
    

    #print("STRIP")

    for i in range(0, len(arrayVal)):     #STRIP \n after number (why is it there?!?!) 
        arrayVal[i] = arrayVal[i].strip()

    #print("SUCHEN...")
    try:
        overlord = [i for i, x in enumerate(out2) if x == "      unit_type: 106"] # trim X 
    
    except:
        overlord = []

    #print(len(numba))


    #print("JSON GENERATE")

    jason = {
        "gamestep": arrayVal[7],
        "apm": apm,
        "common": [
            {
                "minerals": arrayVal[0],
                "vespene": arrayVal[1],
                "foodcap": arrayVal[2],
                "foodused": arrayVal[3],
                "foodarmy": arrayVal[4],
                "foodworkers": arrayVal[5],
                "armycount": arrayVal[6]
            }
        ],
        "unitIDs": [
            {
                "overlord": len(overlord)
            }
        ]
    }
    
#    print("SAVE TO FILE")

    with open("jason.json",mode = "a") as fh:
        json.dump(jason,fh)

    try:

        file = open("jason.json","a")
        file.write("\n")
        file.close()


    except:
        pass



    
"""
    print("WRITE TO FILE")
    try:

        file = open("jason.json","a")
        file.write(str(len(numba)) + "\n")

        

        file.close()
    except:
        pass
        """