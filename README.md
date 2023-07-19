# Batch Subtitle Translator

Batch subtitle translator for WEBVTT subtitles using Google Translator API.

The tool is a follow-up to my Chrome plugin: CST - Coursera Subtitle Translate
https://github.com/lexxai/coursera-subtitle-translate-extension
for offline batch subtitle translation in bilingual mode.

## Test1:

### Code:

```
import translator

if __name__ == "__main__":
    q = (
        "1. Мене звати Тіна, я інженер-програміст у Google. А також щось тут з двох речень.",
        "2. Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "3. який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    result = translator.translate_text("en", q, source="uk")

    print("\n".join(result))
```

### Result:

```
1. My name is Tina and I am a software engineer at Google. And also something here from two sentences.
2. As a software engineer, I work on an internal tool,
3. that serves Google's security engineers and network engineers.
```

## Test2 Chunks:

### Code:

```
import translator

if __name__ == "__main__":
    q = (
        "1. Мене звати Тіна, я інженер-програміст у Google. А також щось тут з двох речень.",
        "2. Як інженер-програміст, я працюю над внутрішнім інструментом, ",
        "3. який обслуговує інженерів безпеки та мережевих інженерів Google.",
    )

    result = translator.translate_text("en", q, source="uk", chunk_size=120, verbose=1)

    print("\n".join(result))
```

### Result:

```
Translate new chunk with 82 chars
Translate new chunk with 63 chars
Translate new chunk with 67 chars
1. My name is Tina and I am a software engineer at Google. And also something here from two sentences.
2. As a software engineer, I work on an internal tool,
3. which serves Google's security engineers and network engineers.
```

# Next later ...

## PARSE FILE

import webvtt

```
WEBVTT

1
00:00:00.020 --> 00:00:02.160
Let's learn about how. Let's learn about how.

2
00:00:02.160 --> 00:00:05.310
IP addresses are used to
communicate over a network!

3
00:00:05.310 --> 00:00:07.905
IP stands for internet protocol?

4
00:00:07.905 --> 00:00:11.460
An internet protocol
address, or IP address, is

5
00:00:11.460 --> 00:00:13.680
a unique string of
characters that identifies

6
00:00:13.680 --> 00:00:16.275
a location of a
device on the internet.

7
00:00:16.275 --> 00:00:19.515
Each device on the internet
has a unique IP address,

8
00:00:19.515 --> 00:00:21.180
just like every
house on a street

9
00:00:21.180 --> 00:00:23.440
has its own mailing address.

10
00:00:24.440 --> 00:00:26.345
There are two types
of IP addresses:

11
00:00:26.345 --> 00:00:29.420
IP version 4, or IPv4,

12
00:00:29.420 --> 00:00:32.855
and IP version 6, or IPv6.

13
00:00:32.855 --> 00:00:36.085
Let's look at examples
of an IPv4 address.

```

## Grouping subtitles and translate it

```
00:00:00.020 00:00:02.160 Let's learn about how. Let's learn about how.
00:00:02.160 00:00:05.310 IP addresses are used to communicate over a network!
00:00:05.310 00:00:07.905 IP stands for internet protocol?
00:00:07.905 00:00:16.275 An internet protocol address, or IP address, isa unique string of characters that identifies a location of a device on the internet.
00:00:16.275 00:00:23.440 Each device on the internet has a unique IP address,just like every house on a street has its own mailing address.
00:00:24.440 00:00:32.855 There are two types of IP addresses:IP version 4, or IPv4, and IP version 6, or IPv6.
00:00:32.855 00:00:36.085 Let's look at examples of an IPv4 address.
********************
00:00:00.020 00:00:02.160 Давайте дізнаємося, як. Давайте дізнаємося, як.
00:00:02.160 00:00:05.310 IP-адреси використовуються для спілкування через мережу!
00:00:05.310 00:00:07.905 IP означає Інтернет-протокол?
00:00:07.905 00:00:16.275 Адреса Інтернет-протоколу або IP-адреса — це унікальний рядок символів, який визначає місцезнаходження пристрою в Інтернеті.
00:00:16.275 00:00:23.440 Кожен пристрій в Інтернеті має унікальну IP-адресу, так само як кожен будинок на вулиці має власну поштову адресу.
00:00:24.440 00:00:32.855 Існує два типи IP-адрес: IP версії 4 або IPv4 та IP версії 6 або IPv6.
00:00:32.855 00:00:36.085 Давайте розглянемо приклади адреси IPv4.
```
