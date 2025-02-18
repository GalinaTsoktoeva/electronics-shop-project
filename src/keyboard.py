from src.item import Item


class MixinLang:
    Lanquage = "EN"

    def __init__(self):
        self.__language = self.Lanquage

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_lang):
        if new_lang in ["RU", "EN"]:
            self.__language = new_lang
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):

        if self.language == self.Lanquage:
            self.language = "RU"
        elif self.language == "RU":
            self.language = self.Lanquage

        return self



class KeyBoard(Item, MixinLang):
    def __init__(self, *args):
        super().__init__(*args)
