import json

with open("legacy.json", "r", encoding="utf-8") as clips_old:
    with open("clipsmerged.json", "r", encoding="utf-8") as clips_new:
        with open("clipsmergedlegacy.json", "w", encoding="utf-8") as merged:
            clips_old = json.loads(clips_old.read())
            clips_new = json.loads(clips_new.read())
            for clip in clips_new:
                clips_old[clip] = clips_new[clip]

            merged.write(json.dumps(clips_old))
