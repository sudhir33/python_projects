
#playlist download
#pip install pytube

import os
from pytube import Playlist
url=input("Enter Playlist link")
#this url we have to change to download playlist
playlist = Playlist(url)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
fn=input("Enter new folder name:")
os.mkdir(fn)
k=0
for video in playlist.videos:
    k+=1
    try:
        stream = video.streams.get_by_itag(22)
        stream.download(fn+'/')
        name=video.streams.get_by_itag(22).default_filename
        os.rename(fn+'/'+name, fn+'/'+str(k)+"_"+name+'.mp4')
    except:
        print(k)
        
    
"""

#single flie download
from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=on2hvxBXJH4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=44')
stream = yt.streams.get_by_itag(22)
stream.download("dpp/")
"""




