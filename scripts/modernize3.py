import codecs
import histolexic3
import nltk
import os
from utils import is_punct

TOKENIZER = nltk.tokenize.word_tokenize

mapping = dict()
found = 0
notfound = 0
#histolexic.find_lemma("goet",True)
#raw_input()

filenr = 0

for file in os.listdir("/Users/alielassche/Documents/GitHub/songs-popular-topics/txt-timeset"):
	f = codecs.open("/Users/alielassche/Documents/GitHub/songs-popular-topics/txt-timeset/" + file, "r", "utf-8")
	fmod = codecs.open("/Users/alielassche/Documents/GitHub/songs-popular-topics/txt-timeset_modern/" + "modern." + file, "w", "utf-8")
	
	print(filenr, file)
	filenr = filenr + 1
	# if filenr >= 10:
	# 	break

	for line in f:
		line = line.replace(",", "")
		line = line.replace(".", "")
		line = line.replace("-", "")
		line = line.replace(" - ", "")
		line = line.replace("\bhy\b ", "hij")
		line = line.replace("\bgy\b ", "gij")
		line = line.replace("\bghy\b", "gij")
		line = line.replace("\bwy\b", "wij")
		# tokens = line.lower().split()
		tokens = TOKENIZER(line, language='dutch')
		tokens_modern = []
		for token in tokens:
			#print("token",token)
			if token not in mapping:
				res = histolexic3.find_lemma(token, False) # find_lemma(token, False)
				#print("res=",res,type(res))
				#print("lex ok")
				if res == None or res == "":
					res = ""
					#print(token, "not found")
					notfound += 1
				else:
					#print(token, res)
					found += 1
				res_fields = res.split(" - ")
				#print(res_fields[0])
				#raw_input()
				mapping[token] = res_fields[0]
				#print("map size:", len(mapping), "found:", found, "notfound:", notfound)
			if mapping[token] != "":
				tokens_modern.append(mapping[token])
			else:
				tokens_modern.append(token)
		fmod.write(" ".join(tokens_modern)+"\n")
	f.close()
	fmod.close()
		#print(" ".join(tokens_modern))
		#raw_input()
		#if linenr>5:
		#	fmod.close()
		#	break
