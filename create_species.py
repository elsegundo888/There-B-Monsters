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
			att_list=["Maximum Age","Maximum Health","Maximum Damage","Maximum Dexterity","Maximum Magic Power","Description of Species"]
			for item in att_list:
				atts=addval(item,atts)
		elif type.upper()=="CLASSES":
			att_list=["Health Bonus","Damage Bonus"]
			for item in att_list:
				atts=addval(item,atts)
	else:
		print(type+" already exists")
	savelog(fname,log)
	return log
	#adds attribute and its value to species key
def addval(x,log):
	val=input("Enter {}: ".format(x))
	if x not in log.keys():
		log[x]=val
	else:
		print("Error already exists")
	return log
def savelog(file,data):
	with open(file, "w") as save_file:
		json.dump(data,save_file)	
log=create_log("Species")
print(log)

	
