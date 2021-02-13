import requests
import re
import urllib.request
import os
import argparse

# this ANSI code lets us erase the current line
ERASE_LINE = "\x1b[2K"


def download(path, mediaUrl, iterate=False, noLayerPath=None):
    print("\r" + ERASE_LINE, end="")
    print("\033[92m✔ Downloading media...\033[0m",end="", flush=True)
    urllib.request.urlretrieve(mediaUrl, path)
    print("\r" + ERASE_LINE, end="")
    print(f"\033[92m✔ Download complete: \033[0m{path}")

    # Download the video without overlay
    if iterate == True:
        print("\033[92m✔ Downloading media with no overlay...\033[0m",end="", flush=True)
        urllib.request.urlretrieve(mediaUrl.replace("embedded", "media"), noLayerPath)
        print("\r" + ERASE_LINE, end="")
        print(f"\033[92m✔ Download complete: \033[0m{noLayerPath}")


def start(mapUrl):
    # If this variable is True, that means that the given SnapMap story
    # contains a layer and that means we need to download the video two times.
    # First time is with the layer and the second is without the layer.
    iterate = False

    # Extract the id from the given url
    id = re.findall(r"snap\/(.*?)\/", mapUrl)[0]
    
    API = f"https://storysharing.snapchat.com/v1/fetch/m:{id}"
    
    print("\r" + ERASE_LINE, end="")
    print("\033[92m✔ Fetching JSON data... \033[0m",end="", flush=True)
    r = requests.get(API)
    data = r.json()

    mediaType = data.get("story").get("snaps")[0].get("media").get("type")
    title = data.get("story").get("metadata").get("title")
    mediaUrl = data.get("story").get("snaps")[0].get("media").get("mediaUrl")

    # Make a directory where the media will be saved
    os.makedirs(title, exist_ok=True)

    # If the video has a overlay, make a sub directory where the so called raw
    # video will be saved
    if "embedded" in mediaUrl:
        os.makedirs(f"{title}/no_layer", exist_ok=True)
        # Download the video 2 times.
        #  1. With the layer
        #  2. Without the layer
        iterate = True

    # Get the file extension of media.
    # There are other methods to see what file extension to use,
    # but this is shorter than the others
    extension = mediaUrl.split("/")[-1].split(".")[-1].split("?")[0]
    
    fname = f"{id}.{extension}"
    path = f"{title}/{fname}"
    noLayerPath = f"{title}/no_layer/{fname}"

    download(iterate=iterate, path=path, noLayerPath=noLayerPath, mediaUrl=mediaUrl)


def main():
    parser = argparse.ArgumentParser(description = "A SnapMap story downloader")
    parser.add_argument('url', action="store",
    help="The url to the story on SnapMap")
    
    args = parser.parse_args()
    
    start(args.url)

if __name__=="__main__":
    main()
