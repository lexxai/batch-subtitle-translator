import webvtt


def subtitle_read(filename: str) -> list[webvtt.Caption]:
    captions = webvtt.read(filename)
    return captions


"""
00:00:00.020
00:00:02.160
Let's learn about how
00:00:02.160
00:00:05.310
IP addresses are used to
communicate over a network.
00:00:05.310
00:00:07.905
IP stands for internet protocol.
00:00:07.905
00:00:11.460
An internet protocol
address, or IP address, is
"""


def grouping_subtitle(captions: list[webvtt.Caption]) -> list[webvtt.Caption]:
    stop_list = (".", "!", "?")
    result = []
    first = True
    for caption in captions:
        caption.text = str(caption.text).replace("\n", " ")
        if first:
            first = False
            row = webvtt.Caption(caption.start, caption.end, caption.text)
            if str(caption.text).strip().endswith(stop_list):
                result.append(row)
                first = True
        else:
            if str(caption.text).strip().endswith(stop_list):
                row.text += "" + caption.text
                row.end = caption.end
                result.append(row)
                first = True
            else:
                row.text += caption.text + " "
                row.end = caption.end
    if not first:
        result.append(row)
    return result


if __name__ == "__main__":
    subtitles = subtitle_read("../tests/subtitles/subtitle-02.vtt")

    result = grouping_subtitle(subtitles)

    for i in result:
        print(i)

"""
00:00:00.020 00:00:05.310 Let's learn about howIP addresses are used to communicate over a network!
00:00:05.310 00:00:07.905 IP stands for internet protocol?
00:00:07.905 00:00:16.275 An internet protocol address, or IP address, isa unique string of characters that identifies a location of a device on the internet.  
00:00:16.275 00:00:23.440 Each device on the internet has a unique IP address,just like every house on a street has its own mailing address.
00:00:24.440 00:00:32.855 There are two types of IP addresses:IP version 4, or IPv4, and IP version 6, or IPv6.
00:00:32.855 00:00:36.085 Let's look at examples of an IPv4 address.
"""
