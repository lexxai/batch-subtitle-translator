import sys

sys.path.append("../src")

import translator

if __name__ == "__main__":
    q = (
        "1. Мене звати Тіна, я інженер-програміст у Google.",
        "2. Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "3. який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    result = translator.translate_text("en", q, source="uk")

    # print(result)

    # result = translator.translate_text("en", q, source="uk", chunk_size=80, verbose=1)

    # print(result)

    print("\n".join(result))
