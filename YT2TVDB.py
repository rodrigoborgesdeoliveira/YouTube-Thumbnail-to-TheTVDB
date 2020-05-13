#! python3
import re
import cloudconvert

def get_thumbnail_url(youtube_url, thumbnail_res):
    youtube_url = youtube_url.rstrip()

    # Get YouTube video ID
    search_pattern = re.search("(?:\/|%3D|v=|vi=)([0-9A-z-_]{11})(?:[%#?&]|$)", youtube_url)
    if search_pattern:
        youtube_id = search_pattern.group(1)

    youtube_thumbnail_url = f"https://i.ytimg.com/vi/{youtube_id}/{thumbnail_res}default.jpg"
    print(f"\nVideo's max resolution thumbnail: {youtube_thumbnail_url}")

    return youtube_thumbnail_url


def download_thumbnail(youtube_thumbnail_url):
    # Get the API key from the API_KEY file
    with open("API_KEY", "r") as file:
        API_KEY = file.read()

    # All of cloudconvert's processes and conversions
    print("Creating process...")
    api = cloudconvert.Api(API_KEY)
    process = api.createProcess({
        "inputformat": "jpg",
        "outputformat": "jpg"
    })

    print("Converting image...")

    process.start({
        "input": "download",
        "file": youtube_thumbnail_url,
        "outputformat": "jpg",
        "preset": "AduhH6JcFl",
        "wait": True
    })

    process.refresh()

    process.wait()
    print(process["message"])

    print("Downloading image to the same directory as the YT2TVDB.py file...")
    process.download()
    print("Download finished!")


def main():
    youtube_url = input("Type or paste the YouTube link: ")
    try:
        thumbnail_url = get_thumbnail_url(youtube_url, "maxres")
        download_thumbnail(thumbnail_url)
    except:
        print("Max resolution failed, retrying with a lower resolution")
        thumbnail_url = get_thumbnail_url(youtube_url, "mq")
        download_thumbnail(thumbnail_url)

    input("\nPress the return key to exit")  # Prevents CMD from auto-exiting


if __name__ == '__main__':
    main()
