from datetime import datetime
from os import environ


def getClips():
	return open(environ["APPDATA"] + "\\Medal\\store\\clips.json", "r", encoding="utf-8")

def getDate(timestamp):
	return str(datetime.fromtimestamp(timestamp))

def searchIncludingDate(query, clip):
	return query in clip["GameTitle"] or query in getDate(clip["TimeCreated"])