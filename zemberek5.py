from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
)
from zemberek.morphology import TurkishMorphology
from zemberek.tokenization import TurkishTokenizer

morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

examples = [
    "Yrn okua gidecem",
    "Tmm, yarin havuza giricem ve aksama kadar yaticam :)",
    "ah aynen ya annemde fark ettı siz evinizden cıkmayın diyo",
    "gercek mı bu? Yuh! Artık unutulması bile beklenmiyo",
    "Hayır hayat telaşm olmasa alacam buraları gökdelen dikicem.",
    "yok hocam kesınlıkle oyle birşey yok",
    "herseyi soyle hayatında olmaması gerek bence boyle ınsanların falan baskı yapıyosa",
    "email adresim zemberek_python@loodos.com",
    "Kıredi başvrusu yapmk istiyrum.",
    "Bankanizin hesp blgilerini ogrenmek istyorm.",
    "yetkli birne ulasmak istiyom.",
    "akaryakit calısanı olark geldım.",
]

for example in examples:
    print(example)
    print(normalizer.normalize(example), "\n")

# SPELLING SUGGESTION
sc = TurkishSpellChecker(morphology)
li = [
    "okuyablirim",
    "tartısıyor",
    "Ankarada",
    "knlıca",
    "yapablrim",
    "kıredi",
    "geldm",
    "geliyom",
    "aldm",
    "asln",
]
for word in li:
    print(word + " --> " + " ".join(sc.suggest_for_word(word)))

# SENTENCE BOUNDARY DETECTION
extractor = TurkishSentenceExtractor()
print("Extractor instance created in: ")

text = "İnsanoğlu aslında ne para ne sevgi ne kariyer ne şöhret ne de çevre ile sonsuza dek mutlu olabilecek bir " \
       "yapıya sahiptir. Dış kaynaklardan gelebilecek bu mutluluklar sadece belirli bir zaman için insanı mutlu " \
       "kılıyor. Kişi bu kaynakları elde ettiği zaman belirli bir dönem için kendini iyi hissediyor, ancak alışma " \
       "dönemine girdiği andan itibaren bu iyilik hali hızla tükeniyor. Mutlu olma sanatının özü bu değildir. Gerçek " \
       "mutluluk, kişinin her türlü olaya ve duruma karşı kendini pozitif tutarak mutlu hissedebilmesi halidir. Bu " \
       "davranış şeklini edinen insan, zor günlerde güçlü, mutlu günlerde zevk alan biri olur ve mutluluğu kalıcı " \
       "kılar. "

sentences = extractor.from_paragraph(text)
print(f"Sentences separated")

for sentence in sentences:
    print(sentence)
print("\n")

# TOKENIZATION
tokenizer = TurkishTokenizer.DEFAULT

tokens = tokenizer.tokenize("Saat 12:00.")
for token in tokens:
    print("Content = ", token.content)
    print("Type = ", token.type_.name)
    print("Start = ", token.start)
    print("Stop = ", token.end, "\n")

# SINGLE WORD MORPHOLOGICAL ANALYSIS
results = morphology.analyze("kalemin")
for result in results:
    print(result)
print("\n")

# SENTENCE ANALYSIS AND DISAMBIGUATION

sentence = "Yarın kar yağacak."
analysis = morphology.analyze_sentence(sentence)
after = morphology.disambiguate(sentence, analysis)

print("\nBefore disambiguation")
for e in analysis:
    print(f"Word = {e.inp}")
    for s in e:
        print(s.format_string())
