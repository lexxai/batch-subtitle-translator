import sys

sys.path.append("../src")

import subtitles
import translator


if __name__ == "__main__":
    subtitles_list = subtitles.subtitle_read("subtitles/subtitle-02.vtt")
    grouped_list = subtitles.grouping_subtitle(subtitles_list)

    for i in grouped_list:
        print(i)

    q = (c.text for c in grouped_list)
    translated_result = translator.translate_text("uk", q)
    for group_capt, translated_row in zip(grouped_list, translated_result):
        group_capt.text = translated_row

    print("*" * 20)

    for i in grouped_list:
        print(i)
