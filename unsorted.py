from json import loads
from sys import argv

from util import getClips, getDate

with getClips() as clipsJson:
	query = argv[1] or input("Search through clips not in an album: ")
	clips = loads(clipsJson.read())
	hits = dict()
	for uuid in clips:
		clip = clips[uuid]
		if (query in clip["GameTitle"] or query in getDate(clip["TimeCreated"])) and ("contentCollections" not in clip["Content"] or clip["Content"]["contentCollections"] == []):
			hits[uuid] = clip
	
	if len(hits) > 0:
		for uuid in hits:
			clip = hits[uuid]
			print("\t" + clip["GameTitle"])
			print("\t\t" + "Recorded: " + getDate(clip["TimeCreated"]))
			if "publishedAt" in clip:
				print("\t\t" + "Published: " + getDate(clip["publishedAt"] / 1000))
		print("Found " + str(len(hits)) + " unsorted clips")