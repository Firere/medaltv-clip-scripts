from json import loads
from sys import argv

from util import getClips, getDate, searchIncludingDate


def getUnsortedClips(verbose=False):
	with getClips() as clipsJson:
		query = argv[1] if len(argv) > 1 else input("Search through clips not in an album: ")
		clips = loads(clipsJson.read())
		hits = dict()
		for uuid in clips:
			clip = clips[uuid]

			if not (searchIncludingDate(query, clip) and ("contentCollections" not in clip["Content"] or clip["Content"]["contentCollections"] == [])): continue

			hits[uuid] = clip
			if not verbose: continue

			print(clip["GameTitle"])
			print("\t" + "Recorded: " + getDate(clip["TimeCreated"]))
			if "publishedAt" in clip:
				print("\t" + "Published: " + getDate(clip["publishedAt"] / 1000))
	
		if len(hits) == 1:
			print("Found 1 unsorted clip")
		else:
			print("Found " + str(len(hits)) + " unsorted clips")

		return hits

if __name__ == "__main__":
	getUnsortedClips(True)