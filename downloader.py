import urllib2,re,os

def speak(string):
	print "[*] "+string

def link_fetcher():
	speak("Fetching Episode URLs")
	results=[]
	response=urllib2.urlopen("http://animewaffles.tv/Details-Fullmetal-Alchemist-90")
	for i in re.findall("td-lang-subbed(.*)td",response.read()):
		results.append(i.split('"')[2])
	speak("Done")
	speak(str(len(results))+" episodes")	
	return results

def url_fetch():#results):
	speak("Fetching mp4 links")
	mp4Links=[]
	counter=1
	#for i in results: #change link here to download episode. i am in single mode
	data=urllib2.urlopen("http://animewaffles.tv/JKLM-One-Piece-Episode-19-English-Subbed-48013")
	data=data.read()
	m=re.search("IFRAME (.*)FRAMEBORDER",data)
	mp4Links.append(m.group(1).strip("=SRC'")[:-2])
	print "\r[*] "+str(counter),
		#counter+=1
	print ""
	speak("Done")
	return mp4Links

def downLoader(links):
	speak("Download starting")
	episode=18
	for link in links:
		file_name="OP/episode"+str(episode)+".mp4"
		episode+=1
		data=urllib2.urlopen(link)
		for line in data.readlines():
			if "file" in line:
				break
		u = urllib2.urlopen(line.strip().strip(",")[9:-1])
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = float(meta.getheaders("Content-Length")[0])/1024
		print "Downloading: %s KB: %s" % (file_name, int(file_size))

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			status = r"%10d " % (file_size_dl/1024)		
			percentage="{0:.2f}".format(float(file_size_dl*100/file_size/1024))
			status+=str(percentage)+"%"
			status = status + chr(8)*(len(status)+1)
			print status,
		#os.system("clear")
	f.close()

def main():
	os.system("cls")
	#downLoader(url_fetch(link_fetcher()))
	downLoader(url_fetch())
	#single mode
	return 0

if __name__ == '__main__':
	main()

