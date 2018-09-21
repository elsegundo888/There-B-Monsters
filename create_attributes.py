#create species or character class
import json
def create_log(type):
    try:
        fname=type+".json"
        with open(fname) as f:
            log=json.load(f)
    except:
         log={}
    query="Enter "+type+" : "
    c= input(query)
	#tests if type already exists
    if c.upper() not in log.keys():
        log[c.upper()] = {}
        atts=log[c.upper()]
        if type.upper()=="SPECIES":
            att_list={"Description":"string",
			"Max Age":"int", "Max Health":"int",
			"Max Damage":"int","Max Dexterity":"int",
			"Hit %":"int","Block %":"int","Natural Fighter":"yn"}
        elif type.upper()=="CLASSES":
            att_list={"Description":"string",
	    	"Health Bonus (+/-)":"int",
			"Damage Bonus (+/-)":"int","Dexterity Bonus (+/-)":"int",
            "Warrior":"yn","Magic User":"yn","Monster":"yn"}
#calls the adds attribute values func	
        for key in att_list:
            print(att_list,att_list[key])
            atts=addval(key,atts,att_list[key])
    else:
        print(type+" already exists")
    savelog(fname,log)
    return log

#collects and adds attribute and its
#value to a class or species dictionary
def addval(x,log,fmt):
    status=0
    while status==0:
        val=input("Enter {}: ".format(x))
        status=testtype(val,fmt)
    if x not in log.keys():
        log[x]=val
    else:
        print("Error already exists")
    return log

#test if the user input is of valid type
def testtype(v,f):
    if f =="int":
        try:
            v=int(v)
            return 1
        except:
            print("\nNumber Must Be an Integer\n")
            return 0
    if f=="yn":
        if v.upper()==("Y"or"N"or"YES"or"NO"):
            return 1
        else:
            print("\nEnter Y or N ONLY\n")
            return 0
    if f=="string":
        return 1
#saves new class or species to a json file 
def savelog(file,data):
	with open(file, "w") as save_file:
		json.dump(data,save_file)	
log=create_log("Species")
print(log)

	