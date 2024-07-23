Peter Norvig, Google'ın yanlış yazılmış arama sorgularını düzeltebilme yeteneğine şaşıran iki mühendis arkadaşıyla yaptığı sohbetlerden ilham alarak basit bir yazım denetleyici yazmaya karar vermiştir. Google'ın teknolojisinin ardındaki karmaşıklığa rağmen, Norvig, temel ancak işlevsel bir yazım denetleyicinin nispeten kolay bir şekilde geliştirilebileceğini göstermeyi amaçlamıştır.

Bu kod, Python'da Tkinter kütüphanesini kullanarak bir yazım denetleyici uygulaması oluşturur. Programın amacı, kullanıcı tarafından girilen metindeki hatalı kelimeleri tespit etmek ve düzeltilmiş haliyle birlikte öneriler sunmaktır.

1. Veri Toplama: Program, çeşitli hikaye metinlerinin ve kelime sıklığı listelerinin bir derlemesi olan büyük bir metin dosyası (`big.txt`) kullanarak kelimelerin ve frekanslarının bir sözlüğünü oluşturur.
2. Tahmini Üretim: Program, bir kelimenin harflerinde silme, yer değiştirme, değiştirme ve ekleme yaparak yanlış yazılmış bir kelime için olası düzeltmeler üretir.
3. Hata Modeli: Öncelikle kelimenin, kelime tablosunda olup olmadığı kontrol edilir, ardından düzenleme mesafesi 1 ve 2 olan ayrıca kelime tablosunda bulunan adaylar incelenir.
4. Seçim Mekanizması: Program, aday kelimelerin tahmini olasılıklarını karşılaştırarak en muhtemel doğru yazımı seçer

Herhangi bir hazır kütüphane kullanılmadan yapılmıştır. Bu algoritmaya ek, hazır spellchecking kütüphanleride eklenmiştir.

Türkçe spellchecking için Zemberek Kullanılmıştır.


Çalıştırmak için big.txt ile beraber aynı dosya klasörüne almanız gerekir.Diğerleri hazır Kütüphane olduğu için direkt çalıştırabilirsiniz.
