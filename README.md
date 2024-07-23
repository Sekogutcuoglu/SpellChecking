Peter Norvig, Google'ın yanlış yazılmış arama sorgularını düzeltebilme yeteneğine şaşıran iki mühendis arkadaşıyla yaptığı sohbetlerden ilham alarak basit bir yazım denetleyici yazmaya karar vermiştir. Google'ın teknolojisinin ardındaki karmaşıklığa rağmen, Norvig, temel ancak işlevsel bir yazım denetleyicinin nispeten kolay bir şekilde geliştirilebileceğini göstermeyi amaçlamıştır.

Bu kod, Python'da Tkinter kütüphanesini kullanarak bir yazım denetleyici uygulaması oluşturur. Programın amacı, kullanıcı tarafından girilen metindeki hatalı kelimeleri tespit etmek ve düzeltilmiş haliyle birlikte öneriler sunmaktır.

1. Veri Toplama: Program, çeşitli hikaye metinlerinin ve kelime sıklığı listelerinin bir derlemesi olan büyük bir metin dosyası (`big.txt`) kullanarak kelimelerin ve frekanslarının bir sözlüğünü oluşturur.
2. Tahmini Üretim: Program, bir kelimenin harflerinde silme, yer değiştirme, değiştirme ve ekleme yaparak yanlış yazılmış bir kelime için olası düzeltmeler üretir.
3. Hata Modeli: Öncelikle kelimenin, kelime tablosunda olup olmadığı kontrol edilir, ardından düzenleme mesafesi 1 ve 2 olan ayrıca kelime tablosunda bulunan adaylar incelenir.
4. Seçim Mekanizması: Program, aday kelimelerin tahmini olasılıklarını karşılaştırarak en muhtemel doğru yazımı seçer

Herhangi bir hazır kütüphane kullanılmadan yapılmıştır. Bu algoritmaya ek, hazır spellchecking kütüphanleride eklenmiştir.

Türkçe spellchecking için Zemberek Kullanılmıştır.


Çalıştırmak için big.txt ile beraber aynı dosya klasörüne almanız gerekir.Diğerleri hazır Kütüphane olduğu için direkt çalıştırabilirsiniz.


**********************************************************ENGLISH************************************************************


Peter Norvig, inspired by conversations with two engineer friends who were amazed by Google's ability to correct misspelled search queries, decided to write a simple spell checker. Despite the complexity behind Google's technology, Norvig aimed to demonstrate that a basic yet functional spell checker could be developed relatively easily.

This code creates a spell checker application using the Tkinter library in Python. The purpose of the program is to identify misspelled words in user-entered text and provide corrected versions along with suggestions.

1.Data Collection: The program uses a large text file (big.txt), a compilation of various story texts and word frequency lists, to create a dictionary of words and their frequencies.
2.Candidate Generation: The program generates possible corrections for a misspelled word by deleting, transposing, replacing, and inserting letters.
3.Error Model: It first checks if the word exists in the word table, then examines candidates within an edit distance of 1 and 2 that are also in the word table.
4.Selection Mechanism: The program selects the most probable correct spelling by comparing the estimated probabilities of the candidate words.
This implementation is done without using any ready-made libraries. Additionally, it includes pre-existing spell-checking libraries.

For Turkish spell-checking, Zemberek is used.

To run the program, place it in the same directory as big.txt. The other libraries are pre-installed, so the program can be run directly.
