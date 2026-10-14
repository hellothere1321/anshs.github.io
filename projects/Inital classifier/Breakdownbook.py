import re

with open("Book.txt", "r", encoding="utf-8") as file:
    content = file.read()                               # open the text file in read only and save it

pattern = r'“(.*?)”'  # set a specific pattern using raw text that regex will later try to recognize, r essentially means everything inside the quotes including backslashes is string

characters = { "Crowley": ["Crowley", "Crawly", "the serpent"], "Aziraphale": ["Aziraphale", "the angel"] } # set up characters that will be checked through
speech_words = ["said", "asked", "replied", "answered", "muttered", "whispered", "shouted"]

def find_speaker(before, after):
    before = before.lower()
    after = after.lower()
    for character, aliases in characters.items():
        for alias in aliases:
            alias = alias.lower()
            for speech_word in speech_words:
                if speech_word + " " + alias in after:
                    return character

                if alias + " " + speech_word in before:
                    return character
    return "unknown"


matches = list(re.finditer(pattern, content, re.DOTALL))

for i, match in enumerate(matches):

    if i == 0:
        before = content[:match.start()]
    else:
        before = content[matches[i - 1].end():match.start()]

    if i == len(matches) - 1:
        after = content[match.end():]
    else:
        after = content[match.end():matches[i + 1].start()]

    before_con = before.split()[-10:]
    after_con = after.split()[:10]

    before_con = " ".join(before_con)
    after_con = " ".join(after_con)

    speaker = find_speaker(before_con, after_con)

    print(speaker + ": " + before_con + " " + match.group() + " " + after_con)
    print()
    