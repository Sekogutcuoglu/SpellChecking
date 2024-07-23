import enchant
import time

class SpellChecker:
    def __init__(self):
        self.dict = enchant.Dict("en_US")

    def correct_text(self, text):
        start_time = time.time() 
        corrected_words = []
        incorrect_count = 0
        total_words = 0
        words = text.split()
        for word in words:
            total_words += 1
            if not self.dict.check(word):
                incorrect_count += 1
               
                suggestions = self.dict.suggest(word)
                if suggestions:
                   
                    corrected_words.append(suggestions[0])
                else:
                    
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        corrected_text = ' '.join(corrected_words)
      
        end_time = time.time()  
        elapsed_time = end_time - start_time  
        return corrected_text,elapsed_time

def main():
    spell_checker = SpellChecker()
    text = "he run"
    corrected_text, elapsed_time = spell_checker.correct_text(text)
    print("Corrected Text:", corrected_text)
    print("Elapsed Time:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
