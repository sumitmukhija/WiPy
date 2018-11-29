#!/usr/bin/env python3
import requests

class Wikipython:

	baseUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="

	def __init__(self, searchQuery):
		processedUrl = self.baseUrl+searchQuery
		response = requests.get(processedUrl)
		json = response.json()
		requiredSubJson = json['query']['pages']
		keyList = list(requiredSubJson.keys())
		pageId = keyList[0]
		try:
			if pageId:
				info = requiredSubJson[pageId]['extract']
				if( info.endswith('may refer to:')):
					print(searchQuery," returned multiple results. Please use a browser for a better search","\n\n")
					return
				listOfStatements = info.split('.')
				firstFiveStatements = listOfStatements[:6]
				print(' '.join(firstFiveStatements).join('\n\n'))
			else:
				print("\nCould not find anything on ", searchQuery,"\n")
		except KeyError:
			print("\nCould not find anything on ", searchQuery, " at this moment.\n")





search = input('Search for: ')
l = ['-' for _ in range(70)]
print(''.join(l))
Wikipython(search)




