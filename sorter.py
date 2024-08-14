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
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky="nsew")
container = ttk.Frame(canvas)
canvas.create_window((0, 0), window=container, anchor="nw")
ttk.Button(container, command=root.update, text="Refresh").grid(column=0, row=0)

i = 1
for date in sorted(categorised):
	clip = categorised[date]["data"]
	ttk.Label(container, text=clip["GameTitle"], foreground=("#000000" if categorised[date]["sorted"] else "#FF0000")).grid(column=0, row=i)
	i += 1

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(column=1, row=0, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.update()
root.mainloop()