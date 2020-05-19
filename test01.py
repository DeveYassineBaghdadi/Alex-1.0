import os
#
#
# PATH = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'Alex_data')
# aud_dir = os.path.join(PATH, 'audios')
# dirs = ['Desktop', 'Documents', 'Downloads', 'Pictures', 'Videos', 'Music']
# ext = ['mp3', 'mpeg']
#
# music_tracks = []
# current_files = [str(f).replace('.mp3', '') for f in os.listdir(aud_dir) if os.path.isfile(os.path.join(aud_dir, f))]
# for dir in dirs:
#     for root, dirs_, f1 in os.walk(os.path.join(os.path.expanduser('~'), dir)):
#         for f_ in f1:
#             ff = str(f_).split('/')[-1].split(f'.{ str(f_.split(".")[-1])}')[0]
#             if  str(f_.split(".")[-1]) in ext and ff not in current_files:
#                 music_tracks.append(os.path.join(root, f_))
#
#
#
# print(current_files)
# print('#'*50)
# print(music_tracks)

validFN = lambda x : x.replace('<', '').replace('>', '').replace(':', '').replace('"', '').replace('/', '').replace('|', '').replace('?', '').replace('*', '')#:"/\|?*


t = ['lksjdhfkhsd98/*+!"£"%', '"£"%d98/jdhf*+']
for i in t:
    print(validFN(i))