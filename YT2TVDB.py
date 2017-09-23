import re
import cloudconvert


def get_thumbnail_url(youtube_url):
    youtube_url = youtube_url.rstrip()
    # Get YouTube video ID
    if "watch%3Fv%3D" in youtube_url:
        # e.g.: https://www.youtube.com/attribution_link?a=8g8kPrPIi-ecwIsS&u=/watch%3Fv%3DyZv2daTWRZU%26feature%3Dem-uploademail
        search_pattern = re.search("watch%3Fv%3D(.*?)%", youtube_url)
        if search_pattern:
            youtube_id = search_pattern.group(1)
    elif "watch?v%3D" in youtube_url:
        # e.g.: http://www.youtube.com/attribution_link?a=JdfC0C9V6ZI&u=%2Fwatch%3Fv%3DEhxJLojIE_o%26feature%3Dshare
        search_pattern = re.search("v%3D(.*?)&format", youtube_url)
        if search_pattern:
            youtube_id = search_pattern.group(1)
    elif "/e/" in youtube_url:
        # e.g.: http://www.youtube.com/e/dQw4w9WgXcQ
        youtube_url += " "
        search_pattern = re.search("/e/(.*?) ", youtube_url)
        if search_pattern:
            youtube_id = search_pattern.group(1)
    else:
        # All else.
        search_pattern = re.search("(?:[?&]vi?=|\/embed\/|\/\d\d?\/|\/vi?\/|https?:\/\/(?:www\.)?youtu\.be\/)([^&\n?#]+)",
                                   youtube_url)
        if search_pattern:
            youtube_id = search_pattern.group(1)

    youtube_thumbnail_url = f"https://i.ytimg.com/vi/{youtube_id}/maxresdefault.jpg"
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
    thumbnail_url = get_thumbnail_url(youtube_url)
    download_thumbnail(thumbnail_url)

    input("\nPress the return key to exit")  # Prevents CMD from auto-exiting


if __name__ == '__main__':
    main()
