import sys

sys.path.append("../src")

import subtitles
import translator


if __name__ == "__main__":
    filename_in = "subtitles/C_ConneAndProteNetwoAndNetwoSecur_M01_12_IP addresses and network communication.vtt"
    filename_out = "subtitles/C_ConneAndProteNetwoAndNetwoSecur_M01_12_IP addresses and network communication_uk.vtt"

    subtitles_list = subtitles.subtitle_read(filename_in)
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

    print("*" * 40)

    dual_language_subt = subtitles.mix_subtitles(subtitles_list, grouped_list)

    for i in dual_language_subt:
        print(i)

    subtitles.subtitle_save(filename_out, dual_language_subt)
