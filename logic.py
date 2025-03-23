# Tugas #3
from translate import Translator
import requests
from collections import defaultdict

# Tugas #5

class TextAnalysis():   
    
    # Tugas #1
    memory = defaultdict(list)
    def __init__(self, text, owner):
        # Tugas #2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "en", "id")

        # Tugas #6
        self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("No sé cómo ayudar", "es", "en")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Task #4
            penerjemah = Translator(from_lang=from_lang, to_lang=to_lang)
            terjemahan = penerjemah.translate(text)
            return terjemahan
        except:
            return "Gagal menerjemahkan"