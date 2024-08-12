from json import loads

from util import getClips

with getClips() as clipsJson:
	print(len(loads(clipsJson.read())))
