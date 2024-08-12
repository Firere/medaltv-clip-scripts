from json import loads
from os import environ

from util import getClips

with getClips() as clips:
	conv = loads(clips.read())
	i = 0
	for _ in conv:
		i += 1
	print(i)
