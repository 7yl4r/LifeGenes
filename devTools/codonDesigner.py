from random import randrange

BASES = ['A', 'B', 'C', 'D']  # DNA Base Pairs (BP)

# prints a list of unique, random codon strings
def codonList(length, number):
	maxCodons = len(BASES) ** length
	if number > maxCodons:
		print 'ERR: cannot create ' + str(number) + ' unique strings of length ' + str(length) + '; only ' + str(
			maxCodons) + ' permutations exist.'
	else:
		codons = list()
		for i in range(number):
			while True:
				c = randomCodon(length)
				if not (c in codons):
					codons.append(c)
					break
				# print len(codons)
		print 'codons=' + str(codons)
		return codons


# returns a radndomly calculated codon
def randomCodon(length):
	codon = list()
	for ii in range(length):
		codon.append(BASES[randrange(0, len(BASES))])
	return ''.join(codon)  # ''.join converts char array to string
