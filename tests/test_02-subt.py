import sys

sys.path.append("../src")

import subtitles


if __name__ == "__main__":
    subtitles = subtitles.subtitle_read("subtitles/subtitle-02.vtt")
    result = subtitles.grouping_subtitle(subtitles)

    for i in result:
        print(i)
