from json import loads

from pyperclip import copy

from util import getClips, getDate

while True:
	uuid = input()
	with getClips() as clips:
		copy(" (" + getDate(loads(clips.read())[uuid]["TimeCreated"]) + ")")
