import requests

"""
https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=uk&dt=t&q=TEXT

"""


def chunk(func):
    def wrapper(*args, chunk_size=10000, verbose: int = 0, **kwargs):
        text_list: list[str] = args[1]
        text_size = 0
        result_list = []
        chunk = []
        for line in text_list:
            line = line.strip()
            if text_size + len(line) < chunk_size:
                chunk.append(line)
                text_size += len(line)
            elif chunk and len(line) < chunk_size:
                result_list.append(chunk)
                chunk = []
                chunk.append(line)
                text_size = len(line)
        result_list.append(chunk)
        result_big_list = []
        for part in result_list:
            if part:
                if verbose:
                    chars = sum(len(i) for i in part)
                    print(f"Translate new chunk with {chars} chars")
                result = func(args[0], part, **kwargs)
                result_big_list.extend(result)
        return result_big_list

    return wrapper


@chunk
def translate_text(
    target: str, text_list: list[str], source: str = "en", separator: str = "u~~~u"
) -> list[str]:
    url = "https://translate.googleapis.com/translate_a/single"
    result = ()
    sl = source
    text = f" {separator} ".join(text_list)
    params = {"client": "gtx", "sl": sl, "tl": target, "dt": "t", "q": text}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0"
        "Safari/537.36 Edg/114.0.1823.79"
    }
    r = requests.get(url, params=params, headers=headers)
    try:
        json_result = r.json()
    except Exception:
        ...
    else:
        result = []
        if json_result and json_result[0]:
            return_string = " ".join(i[0].strip() for i in json_result[0])
            splitted = return_string.split(separator)
            splitted = map(lambda x: x.strip(), splitted)
            result.extend(splitted)
            result = list(filter(lambda x: x, result))
    return result
