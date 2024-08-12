from json import loads
from sys import argv

from util import getClips, searchIncludingDate

with getClips() as clipsJson:
	clips = loads(clipsJson.read())

	if argv[1] == None:
		print(len(clips))
	else:
		i = 0
		for uuid in clips:
			clip = clips[uuid]
			if searchIncludingDate(argv[1], clip):
				i += 1
		print(i)