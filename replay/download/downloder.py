from lxml import html
import requests
import urllib.request
from tqdm import tqdm


class downloder:

	def __init__(self,Europa=False,Korea=False,Nordamerika=False):
		
		#Dient zur messung des Fortschritts
		self.absolviert=0
		#Lister ueber URLs der zu Downloadenen Ligen 
		self.liga_url=[]
		#Liste der Downloade Links
		self.links=[]
		#Lister der Links zu den Replayverzeichnissen der Einzelnen Spieler
		self.spieler=[]
		#bools zur bestimmung der zu downloadenen Ligen
		self.europa=Europa
		self.nordamerika=Nordamerika
		self.korea=Korea
	
	def sammelnspieler(self,Endseite):
		
		self.liga_ermittlung()
		
		for durchlauf in range(len(self.liga_url)):
			startseite=1
		
			while(startseite <= Endseite):
				
				#zeigt den Fortschritt an
				self.fortschritt(len(self.liga_url)*Endseite)
				#Speichern des Seitenquelltextes
				seite = requests.get(self.liga_url[durchlauf]+str(startseite))
				#Quelltext zu html
				baum = html.fromstring(seite.content)
				#Mittels xpath alle relavanten Knoten, die einen Link beinhalten speichern 
				knoten = baum.xpath('//tr/td/a [@href]')
				
				for i in knoten:
					#Die Links nach den Relevanten filtern und speichern 
					if i.get("href")[:33]=="http://sc2replaystats.com/player/":
						self.spieler.append(i.get("href"))
						
				#naechste Seite
				startseite+=1
				
	def downloadlink_ermittlung(self):
	
		for replay_seite in self.spieler:
		
			self.fortschritt(len(self.spieler))
			#Das gleiche spiel wie bei der ermittlung
			seite = requests.get(replay_seite)
			baum = html.fromstring(seite.content)
			knoten = baum.xpath('//./a [@href]')
			
			for i in knoten:
				if i.get("href")[:10]=="/download/":
					self.links.append(i.get("href"))
			
	def liga_ermittlung(self):
	
		if self.europa:
			self.liga_url.append('http://sc2unmasked.com/Ladder?s=eu&top_league=grandmaster&mode=LOTV_SOLO&page=')
			
		if self.nordamerika:
			self.liga_url.append("http://sc2unmasked.com/Ladder?s=us&top_league=grandmaster&mode=LOTV_SOLO&page=")
			
		if self.korea:
			self.liga_url.append("http://sc2unmasked.com/Ladder?s=kr&top_league=grandmaster&mode=LOTV_SOLO&page=")
	
	def fortschritt(self,Ziel):
		
		print(str(self.absolviert)+" von "+str(Ziel))
		self.absolviert+=1
		
		if self.absolviert==Ziel:
		
			print("Vorgang abgeschlossen")
			self.absolviert=0
			
	def download(self):
		
		index=1
		for link in self.links:
		
			self.fortschritt(len(self.links))
			dateiname="Starcraftreplay_"
			anfrage = urllib.request.urlretrieve("http://sc2replaystats.com"+link)
			url = "http://sc2replaystats.com"+link
			anfrage = requests.get(url, stream=True)

			with open(dateiname+str(index)+".SC2Replay", "wb") as handle:
				for data in tqdm(anfrage.iter_content()):
					handle.write(data)
				
			index+=1

if __name__=="__main__":
	Downloade=downloder(True)
	Downloade.sammelnspieler(1)
	Downloade.downloadlink_ermittlung()
	Downloade.download()
	#print(Downloade.links)
	#print(Downloade.spieler)
	#print(len(Downloade.spieler))=21.193