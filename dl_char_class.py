#character classes 
class warrior(character):	
	@property
	def amfighter(self):
		return True
	@property
	def max_ap(self):
		return 50
	@property
	def max_hp(self):
		return 100