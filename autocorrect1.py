from autocorrect import Speller
import time

class SpellChecker:
    def __init__(self):
        self.spell = Speller(lang='en')

    def correct_text(self, text):
        corrected_text = self.spell(text)
        return corrected_text

def main():
    start_time = time.time()  # Başlangıç zamanını kaydet
    spell_checker = SpellChecker()
    original_text = "Thiss is a samplee textt, withh somee speling mistakes."
    corrected_text = spell_checker.correct_text(original_text)
    end_time = time.time()  # Bitiş zamanını kaydet
    print("Corrected Text:", corrected_text)
    elapsed_time = end_time - start_time  # Geçen süreyi hesapla
    print("Elapsed Time:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
