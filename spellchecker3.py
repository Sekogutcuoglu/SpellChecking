from spellchecker import SpellChecker
import time
def spell_check(text):
    spell = SpellChecker()
    start_time = time.time()  
    words = text.split()
    misspelled = spell.unknown(words)
    for word in misspelled:
        correct_word = spell.correction(word)
        if correct_word != word:
            text = text.replace(word, correct_word)
    end_time = time.time() 
    elapsed_time = end_time - start_time
    return text, elapsed_time
text = "Thiss is a samplee textt withh somee speling mistakes."
corrected_text, elapsed_time = spell_check(text)
print("Girilen Metin: ", text)
print("Düzeltme: ", corrected_text)
print("Elapsed Time:", elapsed_time, "seconds")
