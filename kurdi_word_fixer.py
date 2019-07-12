import re
from kurdish import ku


class Fixer:
    def vev(self, x):
        self.x = x
        return re.sub(
            re.compile(
                r"([هڵتیکمبدروپگنزڕ]|^[هڵتیکمبدروپگنزڕ]|\b[هڵتیکمبدروپگنزڕ])(ە)([ئنرژدمکبتوگڕحیسه]|^[ئنرژدمکبتوگڕحیسه]|\b[ئنرژدمکبتوگڕحیسه])"
            ),
            r"\1ە\3",
            x,
        )

    def vev2(self, x):
        self.x = x
        return re.sub(
            re.compile(
                r"([ئنرژدمکبتوگڕحیسه]|^[ئنرژدمکبتوگڕحیسه]|\b[ئنرژدمکبتوگڕحیسه])(ه)([هڵتیکمبدروپگنزڕ]|^[هڵتیکمبدروپگنزڕ]|\b[هڵتیکمبدروپگنزڕ])"
            ),
            r"\1ە\3",
            x,
        )

    def vev3(self, x):
        self.x = x
        return re.sub(
            re.compile(
                r"([هئمجچخبدڵنکیگپبزڕعغفقوشت]|^[هئمجچخبدڵنکیگپبزڕعغفقوشت]|\b[هئمجچخبدڵنکیگپبزڕعغفقوشت])(ه)([یترڕزژسشدکقمنڵعوخچح]|^[یترڕزژسشدکقمنڵعوخچح]|\b[یترڕزژسشدکقمنڵعوخچح])"
            ),
            r"\1ە\3",
            x,
        )

    def vev4(self, x):
        self.x = x
        return re.sub(re.compile(r"اا"), r"الا", x)

    def hhh(self, x):
        self.x = x
        return re.sub(re.compile(r"ههه"), r"ەهە", x)

    def e_start(self, x):
        self.x = x
        return re.sub(re.compile(r"^ە|\bە"), r"", x)

    def ee(self, x):
        self.x = x
        return re.sub(re.compile(r"ەە"), r"لە", x)

    def hee(self, x):
        self.x = x
        return re.sub(re.compile(r"^هئ|\bهئ"), r"ئ", x)

    def hee1(self, x):
        self.x = x
        return re.sub(re.compile(r"^(هئ|\bهئ)|هئ"), r"لەئ", x)

    def hee2(self, x):
        self.x = x
        return re.sub(
            re.compile(r"([ئبپتجچحخدرڕزژسشعغفڤقکگلڵمنه])(ه)(ئ)"), r"\1ە \3", x
        )

    def eww(self, x):
        self.x = x
        return re.sub(re.compile(r"(ە)(و$|و\b)"), r"\1", x)

    def a_startt(self, x):
        self.x = x
        return re.sub(re.compile(r"^ا|\bا"), r"لا", x)

    def o_startt(self, x):
        self.x = x
        return re.sub(re.compile(r"(^ۆ|\bۆ|^ێ|\bێ)"), r"ل\1", x)

    def h_startt(self, x):
        self.x = x
        return re.sub(re.compile(r"(^ڵ|\bڵ)"), r"هە\1", x)

    def e_end(self, x):
        self.x = x
        return re.sub(re.compile(r"(ه$|ه\b|ه‌$|ه‌\b)"), r"ە", x)

    def result(self, content):
        self.content = content
        all_funcs = (
            Fixer().hhh,
            Fixer().vev3,
            Fixer().vev,
            Fixer().vev2,
            Fixer().vev4,
            Fixer().e_start,
            Fixer().ee,
            Fixer().hee,
            Fixer().hee1,
            Fixer().hee2,
            Fixer().eww,
            Fixer().a_startt,
            Fixer().o_startt,
            Fixer().h_startt,
            Fixer().e_end,
        )

        for func in all_funcs:
            content = func(content)

        return content


with open("kurdi_words.txt", "r", encoding="utf-8") as f:
    for word in f:
        with open("new_list.txt", "a", encoding="utf-8") as f:
            if word:
                word = Fixer().result(ku.Hemwar().Ar_Char_to_Ku(word))
                f.write(word)
            else:
                pass
