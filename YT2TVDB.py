import re

youtube_url = input("Type or paste the YouTube link: ") + " "

# Get YouTube video unique code
if "watch?v=" in youtube_url:
    if "&feature" in youtube_url:
        # e.g.: https://www.youtube.com/watch?v=yZv2daTWRZU&feature=em-uploademail
        search_pattern = re.search("watch\?v=(.*?)&feature", youtube_url)
        if search_pattern:
            youtube_code = search_pattern.group(1)
    else:
        # e.g.: https://www.youtube.com/watch?v=yZv2daTWRZU
        search_pattern = re.search("watch\?v=(.*?) ", youtube_url)
        if search_pattern:
            youtube_code = search_pattern.group(1)
elif "watch%3Fv%3D" in youtube_url:
    # e.g.: https://www.youtube.com/attribution_link?a=8g8kPrPIi-ecwIsS&u=/watch%3Fv%3DyZv2daTWRZU%26feature%3Dem-uploademail
    search_pattern = re.search("watch%3Fv%3D(.*?)%", youtube_url)
    if search_pattern:
        youtube_code = search_pattern.group(1)
elif "youtu.be" in youtube_url:
    # e.g.: https://youtu.be/yZv2daTWRZU
    search_pattern = re.search("youtu\.be/(.*?) ", youtube_url)
    if search_pattern:
        youtube_code = search_pattern.group(1)

# print(f"YouTube video unique code: {youtube_code}")

input("\nPress any key to exit") # Prevents CMD from auto-exiting