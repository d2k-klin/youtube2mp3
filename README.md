# youtube2mp3
## Simple script for download YouTube videos as mp3 files

I have written this simple python script for my daughter to be able to download music from YouTube 
    - application supports providing whole playlist or just a sinle video
    - for playlist it will check of maximum number of parallel tasks and do download in parallel
    - at the end mp3 songs will be save in the mp3 folder

## Prerequisites
Local installation of python and pip

## Setup
    pip install -r requirements.txt

## Run
Playlist download  

    python .\downloader.py -p "https://www.youtube.com/watch?v=ZmDBbnmKpqQ&list=PLdKZ5BB_ofd8Yz2CRuE9HMk5I8UyDNfbz"
    
Single video 

    python .\downloader.py -s "https://www.youtube.com/watch?v=NvQ0ezsRVtY"