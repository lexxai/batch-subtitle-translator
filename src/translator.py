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
        i = 0
        while i < len(text_list):
            line = text_list[i].strip()
            if text_size + len(line) < chunk_size:
                chunk.append(line)
                text_size += len(line)
            elif chunk:
                result_list.append(chunk)
                chunk = []
                text_size = 0
            i += 1
        result_list.append(chunk)

        result_big_list = []

        for part in result_list:
            if part:
                if verbose:
                    print(f"Translate new chunk with {text_size} chars")
                result = func(args[0], part, **kwargs)
                result_big_list.extend(result)

        # print(result_big_list)

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
        if json_result and json_result[0]:
            result = (str(i[0]).replace(separator, "").strip() for i in json_result[0])
            result = filter(lambda x: x, result)
    return result


if __name__ == "__main__":
    q1 = r"My name is Tina and I'm a software engineer at Google. u~~~u  As a software engineer, I work on an internal tool that serves the security engineers and network engineers at Google. u~~~u  Network security is important because we want to make sure that our network systems are safe and resilient to be able to defend against malicious hackers, and that we have the ability to protect our user data. u~~~u  Working with network security allows to see the overview of the whole company's network systems, which is super cool. u~~~u  My favorite part of my job is the impact I get to have on the community that I serve at Google. u~~~u  I would say most of my day is a lot of coding, design, talking to security teams and network teams on their priorities and their blockers and being able to come up with a solution. u~~~u  There are often going to be requests that come from network teams and security teams that have specific requirements on certain platforms or on a feature that they need in one of the network policies, and usually we would escalate that and try to work on a fix for that. u~~~u  One piece of advice I would give for someone who wants to take on the cybersecurity journey is to be able to always keep learning and be curious about how things work. u~~~u  Because security is an ever changing field, cybersecurity is definitely a team sport. u~~~u  Everybody has something to contribute, and especially on cybersecurity problems, there can be a lot of possibilities and a lot of different solutions to one problem. u~~~u  It's always great to be able to have people to brainstorm with and to track down issues together because things can get very complex sometimes, but it's also a fun process to be able to work on things together. u~~~u"

    # q = "Hello world.u~~~u And other parts of wold."

    q = (
        "Мене звати Тіна, я інженер-програміст у Google. ",
        "Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    separator = "u~~~u"
    q_list = (q1 * 1).split(separator)

    result = translate_text("uk", q_list)
    # result = translate_text("en", q, source="uk")

    # print(result)

    print("Result:\n", "\n".join(result))
