from genericpath import exists
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import sys
import re
import threading
import multiprocessing
import queue
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p", "--playlist", dest="playlist_input",
                    help="Youtube URL to a playlist", nargs='?', default=None)

parser.add_argument("-s", "--song", dest="song_input",
                    help="Youtube URL to a single song", nargs='?', default=None)

args = parser.parse_args()

def convert2mp3(folder, file):
  full_path = os.path.join(folder, file)
  output_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
  clip = mp.AudioFileClip(full_path).subclip(10,) # disable if do not want any clipping
  clip.write_audiofile(output_path)
  os.remove(full_path)

def download_song(folder, url):
  if not (os.path.exists(folder + "/" + YouTube(url).title + ".mp3")):
    filepath = YouTube(url).streams.filter(only_audio=True).first().download(folder, skip_existing=True)
    print(YouTube(url).title) 
    convert2mp3(folder,filepath)

def worker(folder):
    while True:
        item = q.get()
        download_song(folder, item)
        q.task_done()

tgt_folder=os.curdir+"/mp3"
if not os.path.exists(tgt_folder):
    os.makedirs(tgt_folder)

if (args.song_input):
  download_song(tgt_folder,args.song_input)

if (args.playlist_input):  
  playlist = Playlist(args.playlist_input)

  q = queue.Queue()
  for url in playlist:
    q.put(url)

  cpus = multiprocessing.cpu_count()
  for i in range(cpus):
    t = threading.Thread(target=worker,args=(tgt_folder,))
    t.daemon = True
    t.start()

  q.join() # Block until all tasks are done



