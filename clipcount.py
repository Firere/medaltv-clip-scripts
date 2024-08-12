from json import loads
from os import environ

with open(environ["APPDATA"] + "\\Medal\\store\\clips.json", "r", encoding="utf-8") as clips:
	conv = loads(clips.read())
	i = 0
	for _ in conv:
		i += 1
	print(i)
