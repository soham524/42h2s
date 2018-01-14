import urllib2
data = urllib2.urlopen("https://projects.intra.42.fr/uploads/document/document/422/names.txt")
d = {}
for line in data:
	(first, last) = line.split()
	print first
	d[first]=[last]
print d