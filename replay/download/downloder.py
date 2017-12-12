from lxml import html
import requests
import urllib.request
from tqdm import tqdm
import Validierung

class downloder:

	def __init__(self,Europa=False,Korea=False,Nordamerika=False,Qualitaet=[],Version=""):
		
		#Dient zur ueberpruefung der Version
		self.version=Version
		#Dient zur messung des Fortschritts
		self.absolviert=0
		#Lister ueber URLs der zu Downloadenen Ligen 
		self.liga_url=[]
		#Liste der Downloade Links
		self.links=[]
		#Lister der Links zu den Replayverzeichnissen der Einzelnen Spieler
		self.spieler=[]
		#Dient zur Sicherstellung der Qualitaet
		self.qualitaet=Qualitaet
		#bools zur bestimmung der zu downloadenen Ligen
		self.europa=Europa
		self.nordamerika=Nordamerika
		self.korea=Korea
	
	def sammelnspieler(self,Endseite):
		
		self.liga_ermittlung()
		
		for durchlauf in range(len(self.liga_url)):
			startseite=1
			qualitaet=True
			print(" Das Sammeln der Spieler der Ligawird gestartet.\n Dies kann einige Zeit dauern.\n Es wurden bereits "+str(durchlauf+1)+" heruntergeladen")
			
			while(startseite <= Endseite and qualitaet):
				
				print(startseite)
				#Speichern des Seitenquelltextes
				seite = requests.get(self.liga_url[durchlauf]+str(startseite))
				#Quelltext zu html
				baum = html.fromstring(seite.content)
				#Qualitaet pruefen
				qualitaet=self.qualitaets_sicherung(baum)
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
			
			datum_index=0
			self.fortschritt(len(self.spieler))
			#Das gleiche spiel wie bei der ermittlung
			seite = requests.get(replay_seite)
			baum = html.fromstring(seite.content)
			#Das Datum der replays abgreifen
			datum = baum.xpath('//./td [@title]')
			knoten = baum.xpath('//./a [@href]')
		
			for i in knoten:
			
				if i.get("href")[:10]=="/download/":
				
					validator=Validierung.Validierung(datum[datum_index],self.version)
					
					if validator.datum_validirung():
					
						self.links.append(i.get("href"))
						
					datum_index+=1

			
	def liga_ermittlung(self):
	
		if self.europa:
			self.liga_url.append('http://sc2unmasked.com/Ladder?s=eu&top_league=grandmaster&mode=LOTV_SOLO&page=')
			
		if self.nordamerika:
			self.liga_url.append("http://sc2unmasked.com/Ladder?s=us&top_league=grandmaster&mode=LOTV_SOLO&page=")
			
		if self.korea:
			self.liga_url.append("http://sc2unmasked.com/Ladder?s=kr&top_league=grandmaster&mode=LOTV_SOLO&page=")
	
	def qualitaets_sicherung(self,baum):
		
		knoten = baum.xpath('//./img [@alt]')
		alle_stufen=["gr","ma","di","pl"]
		stufen=[]
		sicher=True
		
		for i in knoten:
			
			if i.get("alt")[:2] in alle_stufen:

				stufen.append(i.get("alt")[:2])
		print(stufen)
		
		for i in stufen:
			
			if not(i in self.qualitaet):
			
				print("falsch")
				sicher=False
		return sicher
				
	
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
				for replay in tqdm(anfrage.iter_content()):
					handle.write(replay)
				
			index+=1
			
	def vorgang(self):
	
		self.sammelnspieler(100)
		self.downloadlink_ermittlung()
		self.download()

if __name__=="__main__":
	Downloade=downloder(True)
	Downloade.sammelnspieler(1)
	Downloade.downloadlink_ermittlung()
	Downloade.download()
	#print(Downloade.links)
	#print(Downloade.spieler)
	#print(len(Downloade.spieler))=21.193