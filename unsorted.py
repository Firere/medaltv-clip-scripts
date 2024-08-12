from json import loads
from sys import argv

from util import getClips, getDate, searchIncludingDate

with getClips() as clipsJson:
	query = argv[1] or input("Search through clips not in an album: ")
	clips = loads(clipsJson.read())
	hits = 0
	for uuid in clips:
		clip = clips[uuid]
		if searchIncludingDate(query, clip) and ("contentCollections" not in clip["Content"] or clip["Content"]["contentCollections"] == []):
			hits += 1
			print("\t" + clip["GameTitle"])
			print("\t\t" + "Recorded: " + getDate(clip["TimeCreated"]))
			if "publishedAt" in clip:
				print("\t\t" + "Published: " + getDate(clip["publishedAt"] / 1000))
	
	if hits == 1:
		print("Found 1 unsorted clip")
	else:
		print("Found " + str(hits) + " unsorted clips")