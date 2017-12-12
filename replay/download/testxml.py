from lxml import html
import requests
import urllib.request
from tqdm import tqdm

def test1():
	#die Liegen sind Grandmaster=gr Master=ma Diamand=di Platin=pl Gold=go Silber=si Broze=br
	liga=[]
	seite = requests.get('http://sc2unmasked.com/Ladder?s=eu&top_league=grandmaster&mode=LOTV_SOLO&page=200')
	baum = html.fromstring(seite.content)
	knoten = baum.xpath('//./img [@alt]')

	for i in knoten:

		if i.get("alt")[:2]=="pl":
			liga.append(i.get("alt"))

		if i.get("alt")[:2]=="ma":
			print("ihhh, ein Master \n STOOOOOOOOOOP")
	
	print(liga)
	print(len(liga))
	
def test2():

	a=[0,1,2,3,4]
	
	for i in range(6):
		if i in a:
			print("What fuer ein wunderschoenes Leben diddaldidldaldum")
		else:
			print("oh, Nein")

def test_datum_abgriff():
	
	seite = requests.get('http://sc2replaystats.com/player/249268?tab=replays')
	baum = html.fromstring(seite.content)
	knoten = baum.xpath('//./td [@title]')
	
	for i in knoten:
		
		print(i.text)
	
	return knoten
		
def test_datum_rechen():
	#http://wiki.teamliquid.net/starcraft2/Patches
	#Erzeugen eier Statischen Liste
	datum_info=[["Jan",1,31],["Feb",2,29],["Mar",3,31],["Arp",4,30],["Mai",5,31],["Jun",6,31],["Jul",7,31],["Aug",8,31],["Sep",9,30],["Oct",10,31],["Nov",11,30],["Dec",12,31]]
	#das Datum kommt in diesem Format
	input="12 Sep, 2018"
	vergleich_2="15 Sep, 2018"
	vergleich_1="13 Aug, 2017"

	def ermittlung(datum):
		
		temp_tag=0
		temp_monat=0
		temp_jahr=0
		
		temp_tag=int(datum[:2])
		temp_jahr=int(datum[8:12])
		
		for i in datum_info:
		
			if i[0]==datum[3:6]:
			
				temp_monat=i[1]
		
		return [temp_jahr,temp_monat,temp_tag]
		
	def zwischen(datum,vrg_datum_1,verg_datum_2): 
	
		for i in range(3):
		
			if datum[i] > vrg_datum_1[i] and datum[i] < verg_datum_2[i] or (datum[i] >= vrg_datum_1[i] and datum[i] < verg_datum_2[i] and i<=1):
			
				print(JO)
				return True
			
			if i==1:
			
				if datum[i]==verg_datum_2[i] and datum[i+1]<=verg_datum_2[i+1]:
				
					return True
			
			if datum[i] == vrg_datum_1[i] or datum[i] == verg_datum_2[i]:
				
				if i == 2:
					
					print(jo)
					return True
				
			else:
				print("oh Nein")
				return False
			
	input_datum=ermittlung(input)
	vergleichs_datum_1=ermittlung(vergleich_1)
	vergleichs_datum_2=ermittlung(vergleich_2)
	
	ist_dazwischen=zwischen(input_datum,vergleichs_datum_1,vergleichs_datum_2)
	print(ist_dazwischen)
	print(vergleichs_datum_1)
	print(vergleichs_datum_2)
	#Der monat ist groesser
		

test_datum_rechen()