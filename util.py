from os import environ
from datetime import datetime

def getClips():
	return open(environ["APPDATA"] + "\\Medal\\store\\clips.json", "r", encoding="utf-8")

def getDate(timestamp):
	return str(datetime.fromtimestamp(timestamp))