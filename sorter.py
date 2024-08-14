from json import loads
from tkinter import *
from tkinter import ttk

from unsorted import getUnsortedClips
from util import getClips

categorised = dict()

def key(clip):
	return str(clip["publishedAt"] if "publishedAt" in clip else clip["TimeCreated"])

unsorted = getUnsortedClips()
for uuid in unsorted:
	clip = unsorted[uuid]
	categorised[key(clip)] = {
		"sorted": False,
		"data": clip
	}

with getClips() as clipsJson:
	clips = loads(clipsJson.read())
	for uuid in clips:
		clip = clips[uuid]
		if key(clip) in categorised: continue
		categorised[key(clip)] = {
			"sorted": True,
			"data": clip
		}

root = Tk()
container = ttk.Scrollbar(root)
container.pack(expand=True)
ttk.Button(container, command=root.update, text="Refresh")

for date in sorted(categorised):
	clip = categorised[date]["data"]
	print("did a thing")
	# fixme this doesn't want to display
	ttk.Label(container, text=clip["GameTitle"], foreground=("#000000" if categorised[date]["sorted"] else "#FF0000"))

root.update()
container.pack()
root.mainloop()