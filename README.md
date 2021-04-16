# youtube2mp3
## Simple script for download YouTube videos as mp3 files

I have written this simple python script for my daughter to be able to download music from YouTube;
    application supports providing whole playlist or just a single video url;
    for playlist it will check for maximum number of availble threads and start the download in parallel;
    at the end song(s) will be saved in the mp3 folder;

## Prerequisites
Local installation of python and pip

## Setup
    pip install -r requirements.txt

## Run
playlist download  

    python .\downloader.py -p "https://www.youtube.com/watch?v=ZmDBbnmKpqQ&list=PLdKZ5BB_ofd8Yz2CRuE9HMk5I8UyDNfbz"
    
single video download

    python .\downloader.py -s "https://www.youtube.com/watch?v=NvQ0ezsRVtY"