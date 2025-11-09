# generate_gallery.py
import os, json

images_dir = 'Images'
videos_dir = 'Videos'
out_file = 'gallery.json'

def clean_title(fname):
    name = os.path.splitext(fname)[0]
    return ' '.join(name.replace('_',' ').replace('-',' ').split())

def read_files(d, exts):
    if not os.path.isdir(d): return []
    items = []
    for f in sorted(os.listdir(d)):
        if os.path.isfile(os.path.join(d,f)) and os.path.splitext(f)[1].lower() in exts:
            items.append({'src': f"{d}/{f}".replace('\\','/'), 'title': clean_title(f)})
    return items

posters = read_files(images_dir, {'.png','.jpg','.jpeg','.webp','.gif','.svg'})
videos = read_files(videos_dir, {'.mp4','.webm','.mov'})

with open(out_file, 'w', encoding='utf8') as fh:
    json.dump({'posters': posters, 'videos': videos}, fh, indent=2)

print(f"Wrote {out_file}: {len(posters)} images, {len(videos)} videos")
