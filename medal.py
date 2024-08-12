from datetime import datetime
from json import loads
from os import environ

from pyperclip import copy

while True:
	uuid = input()
	with open(environ["APPDATA"] + "\\Medal\\store\\clips.json", "r", encoding="utf-8") as clips:
		copy(" (" + str(datetime.fromtimestamp(loads(clips.read())[uuid]["TimeCreated"])) + ")")
