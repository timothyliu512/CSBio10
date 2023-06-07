from sys import argv


codonSequences = {}	#Dictionary for codon table

importedFastA = open(argv[1],"r").read()	#Read in fastA as string
codon = open(argv[2],"r").read().split()	#Read in codon table as list for each row

def makeDictionary(codonList, codonDictionary):   #Puts codon table into dictionary. Parameters are a list of codons, the dictionary you want to put it in
	for i in range(0, len(codonList), 3 ):
		codonDictionary[codonList[i]] = codonList[i+1]

def formatFastA(rawFastAFile): #Takes in raw fastA data and converts it into a string with all the nucleotides
	if rawFastAFile[0] == ">":	#If fastA has a header
		formattedFastAFile = rawFastAFile.split('\n')[1:]
		return ''.join(formattedFastAFile).strip().upper()
	else:				#No header in fastA, just sequences
		return rawFastAFile.strip().upper()

def findSubstringIndices(string, substring):	#Find all possible start indexes for a substring in a string
	return [i for i in range(len(string)) if string.startswith(substring, i)]

def readSequence(sequence, codonDictionary ):
	start_indices = findSubstringIndices(sequence, "ATG") #Find all the possible start codons
	for startIndex in start_indices: #Start at all possible start codons
		codonList = [] #Store each individual codon separately in a list
		for i in range(startIndex, len(sequence), 3):	#Read 3 nucleotides at a time from sequence
			if (i+3) > len(sequence):	#If can't read 3 nucleotides at a time, stop
				break
			elif sequence[i:i+3] == 'TGA':	#Stop when stop codon is encountered
				codonList.append(sequence[i:i+3])
				break
			elif sequence[i:i+3] == 'TAA':
				codonList.append(sequence[i:i+3])
				break
			elif sequence[i:i+3] == 'TAG':
				codonList.append(sequence[i:i+3])
				break
			else:
				codonList.append(sequence[i:i+3]) #Store individual codon in the list
	#	for codon in codonList:
		#	print (codon, end = ' ')
		#print('\n')
		for codon in codonList:	#Match each codon in the list with its amino acid
			print( codonDictionary[codon], end = '' )
		print('\n')

def readSequenceBackwards(sequence, codonDictionary):
	reverseStrand = ""
	for nucleotide in sequence:	#Go through each nucleotide and get the complementary nucleotide
		if nucleotide == 'A':	#Then add it to the reverse sequence
			reverseStrand = reverseStrand + 'T'
		if nucleotide == 'T':
			reverseStrand = reverseStrand + 'A'
		if nucleotide == 'G':
			reverseStrand = reverseStrand + 'C'
		if nucleotide == 'C':
			reverseStrand = reverseStrand + 'G'	
	sequence = reverseStrand[::-1]	#Reverse the sequence to get the complementary strand to original
	start_indices = findSubstringIndices(sequence, "ATG") #Find all possible start codon positions
	for startIndex in start_indices:	#Start at each start codon found
		codonList = [] #Hold each individual codon in a list
		for i in range(startIndex, len(sequence), 3):   #Read 3 nucleotides at a time from sequence
			if (i+3) > len(sequence):       #If can't read 3 nucleotides at a time, stop
				break
			elif sequence[i:i+3] == 'TGA':  #Stop when stop codon is encountered
				codonList.append(sequence[i:i+3])
				break
			elif sequence[i:i+3] == 'TAA':
				codonList.append(sequence[i:i+3])
				break
			elif sequence[i:i+3] == 'TAG':
				codonList.append(sequence[i:i+3])
				break
			else:
				codonList.append(sequence[i:i+3]) #Store individual codon in the list
		for codon in codonList: #Match each codon in the list with its amino acid
			print( codonDictionary[codon], end = '' )
		print('\n')



makeDictionary(codon,codonSequences) #Set up dictionary
formattedFastA = formatFastA(importedFastA)  #Format fastA to get just single string of all sequences
readSequence( formattedFastA, codonSequences )
readSequenceBackwards( formattedFastA, codonSequences )


