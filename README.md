# Batch Subtitle Translator

Batch subtitle translator for WEBVTT subtitles using Google Translator API

## Test1:

### Code:

```import translator

if __name__ == "__main__":
    q = (
        "Мене звати Тіна, я інженер-програміст у Google. ",
        "Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    result = translator.translate_text("en", q, source="uk")

    print(result)
```

### Result:

```
["My name is Tina and I'm a software engineer at Google.", "As a software engineer, I work on an internal tool  that serves Google's security engineers and network engineers."]
```

## Test2 Chunks:

### Code:

```import translator

if __name__ == "__main__":
    q = (
        "1. Мене звати Тіна, я інженер-програміст у Google.",
        "2. Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "3. який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    result = translator.translate_text("en", q, source="uk", chunk_size=80, verbose=1)

    print(result)
```

### Result:

```
Translate new chunk with 50 chars
Translate new chunk with 63 chars
Translate new chunk with 67 chars
['1. My name is Tina and I am a software engineer at Google.', '2. As a software engineer, I work on an internal tool,', "3. which serves Google's security engineers and network engineers."]
```
