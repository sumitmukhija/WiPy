import urllib2

class Wikipython:

	baseUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="

	def __init__(self, searchQuery):
		processedUrl = baseUrl+searchQuery
		content = urllib2.urlopen(processedUrl).read()
		print(content)



Wikipython('Software')



