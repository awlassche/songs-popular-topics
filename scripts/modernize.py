import codecs
import histolexic

f = codecs.open("dbnl_src/plain/plain.all","r","utf-8")
fmod = codecs.open("dbnl_src/plain/plain.modern.all","w","utf-8")

mapping = dict()
linenr=0
found = 0
notfound = 0
#histolexic.find_lemma("goet",True)
#raw_input()

for line in f:
	linenr+=1
	if linenr % 100 == 0:
		print linenr
	#print line
	line = line.replace(",","")
	line = line.replace(".","")
	line = line.replace("-","")
	line = line.replace(" - ","")
	tokens = line.lower().split()
	tokens_modern = []
	for token in tokens:
		#print "token",token
		if token not in mapping:
			res = histolexic.find_lemma(token,False)
			#print "res=",res,type(res)
			#print "lex ok"
			if res == None or res == "":
				res = ""
				print token, "not found"
				notfound += 1
			else:
				print token, res
				found += 1
			res_fields = res.split(" - ")
			#print res_fields[0]
			#raw_input()
			mapping[token] = res_fields[0]
			print "map size:",len(mapping),"found:",found,"notfound:",notfound
		if mapping[token] != "":
			tokens_modern.append(mapping[token])
		else:
			tokens_modern.append(token)
	fmod.write(" ".join(tokens_modern)+"\n")
	#print(" ".join(tokens_modern))
	#raw_input()
	#if linenr>5:
	#	fmod.close()
	#	break
