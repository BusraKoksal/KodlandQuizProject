Kodland Task
Bu proje, Kodland eğitmenlik başvurusu kapsamında geliştirdiğim Python ve Flask tabanlı bir uygulamadır. Uygulama, kullanıcıların soruları yanıtlayarak bir puanlama sistemi üzerinden sonuç almasını sağlar. Sorular bir SQLite veritabanında saklanır ve kullanıcılar sisteme kaydolduktan sonra cevapladıkları sorulara göre puan alırlar.

Özellikler
Kullanıcılar, bir kullanıcı adı ve e-posta ile sisteme kaydolurlar.
Sorular bir veritabanında saklanır ve kullanıcılar bu soruları cevaplar.
Kullanıcı doğru cevapladığı sorular üzerinden değerlendirilir.
Kullanıcının anlık skoru ve en yüksek skoru sistemde saklanır.
Kullanıcılar, önceden alınmış en yüksek skoru görebilirler.
Gereksinimler
Python 3.8 ve üstü
Flask
SQLAlchemy
SQLite
Kurulum
Projeyi bilgisayarınıza klonlayın:

git clone https://github.com/BusraKoksal/KodlandQuizProject.git 
Gerekli paketleri yükleyin:

pip install -r requirements.txt
Veritabanını oluşturun ve başlangıç verilerini yükleyin:

python main.py
Flask uygulamanızı başlatın:

python main.py
Uygulama, varsayılan olarak http://127.0.0.1:5000/ adresinde çalışacaktır.

Kullanım
Web uygulamasına gittiğinizde, kullanıcı adı ve e-posta adresinizi girerek sisteme kaydolabilirsiniz.
Soruları yanıtladıktan sonra, doğru cevapladığınız sorular üzerinden skorunuzu görüntüleyebilirsiniz.
Puanlarınız, uygulama tarafından kaydedilir ve sisteme giriş yaptıktan sonra görüntülenebilir.
