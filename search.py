from json import loads
from sys import argv

from util import getClips, searchIncludingDate

with getClips() as clipsJson:
	query = argv[1] if len(argv) > 1 else input("Search through clips: ")
	clips = loads(clipsJson.read())
	hits = 0

	for uuid in clips:
		clip = clips[uuid]
		if searchIncludingDate(query, clip):
			hits += 1
			print(clip["GameTitle"])

	if hits == 1:
		print("Found 1 clip")
	else:
		print("Found " + str(hits) + " clips")