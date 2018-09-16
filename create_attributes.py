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
			"Maximum Age":"int", "Maximum Health":"int",
			"Maximum Damage":"int","Maximum Dexterity":"int",
			"Hit Percentage":"int","Block Percentage":"int"}
		elif type.upper()=="CLASSES":
			att_list={"Description of Class":"string",
			"Health Bonus (+/-)":"int",
			"Damage Bonus (+/-)":"int","Dexterity Bonus (+/-)":"int"}
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
	val=input("Enter {}: ".format(x))	
	if x not in log.keys():
		log[x]=val
	else:
		print("Error already exists")
	return log

#saves new class or species to a json file 
#of the same name
def savelog(file,data):
	with open(file, "w") as save_file:
		json.dump(data,save_file)	
log=create_log("Species")
print(log)

	