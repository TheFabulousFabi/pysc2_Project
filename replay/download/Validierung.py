

class Validierung:
	#noch zu tun die Liste vervollständigen
	
	def __init__(self,Datum="",Version=""):
	
		self.zeitraum=[]
		self.datum=Datum.text
		self.datum_geparst=[]
		self.version=Version
		
	def datum_validirung(self):
	
		self.ermittle_zeitraum()
		self.parse_datum()
		return self.zwischen()
		
			
	
	def ermittle_zeitraum(self):
		
		patch40=["4.0",[2017,11,14],[2017,12,31]]
		patch319=["3.19",[2017,10,10],[2017,11,13]]
		patch318=["3.18",[2017,9,19],[2017,10,9]]
		patch317=["3.17",[2017,7,18],[2017,9,18]]
		patches=[patch40,patch319,patch318,patch317]
		
		for patch in patches:
			
			if patch[0]==self.version:
				
				self.zeitraum.append(patch[1])
				self.zeitraum.append(patch[2])
	
	def parse_datum(self):
		
		temp_tag=0
		temp_monat=0
		temp_jahr=0
		datum_info=[["Jan",1],["Feb",2],["Mar",3],["Arp",4],["Mai",5],["Jun",6],["Jul",7],["Aug",8],["Sep",9],["Oct",10],["Nov",11],["Dec",12]]
		
		temp_tag=int(self.datum[:2])
		temp_jahr=int(self.datum[8:12])
		
		
		for i in datum_info:
		
			if i[0]==self.datum[3:6]:
			
				temp_monat=i[1]
		
		self.datum_geparst.append(temp_jahr)
		self.datum_geparst.append(temp_monat)
		self.datum_geparst.append(temp_tag)
		
	def zwischen(self): 
	
		for i in range(3):
			
			if self.datum_geparst[i] > self.zeitraum[0][i] and self.datum_geparst[i] < self.zeitraum[1][i] or (self.datum_geparst[i] >= self.zeitraum[0][i] and self.datum_geparst[i] < self.zeitraum[1][i] and i==0):
			
				return True
				
			if i ==1:	
			
				if self.datum_geparst[i]==self.zeitraum[1][i] and self.datum_geparst[i+1]<=self.zeitraum[1][i+1]:
				
					return True
				
			if self.datum_geparst[i] == self.zeitraum[0][i] or self.datum_geparst[i] == self.zeitraum[1][i]:
				
				if i == 2:
					
					return True
				
			else:
				
				return False