from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils import timezone

YER_CHOICES = (
    ("Yüksel DUMAN",	"Yüksel DUMAN"),
    ("Hayri ŞİMŞEK",	"Hayri ŞİMŞEK"),
    ("Birgül KALKAN",	"Birgül KALKAN"),
    ("Ercan TOKMAR",	"Ercan TOKMAR"),
    ("Gönül AKIN İLHAN",	"Gönül AKIN İLHAN"),
    ("Durmuş Erdem ARSLANOĞLU",	"Durmuş Erdem ARSLANOĞLU"),
    ("Atilla ŞAHİN",	"Atilla ŞAHİN"),
    ("Gelir ve Kurumlar Vergileri Müdürlüğü",	"Gelir ve Kurumlar Vergileri Müdürlüğü"),
    ("KDV-ÖTV Müdürlüğü",	"KDV-ÖTV Müdürlüğü"),
    ("Usul Müdürlüğü",	"Usul Müdürlüğü"),
    ("Tahsilat Müdürlüğü",	"Tahsilat Müdürlüğü"),
    ("Denetim Koordinasyon Müdürlüğü",	"Denetim Koordinasyon Müdürlüğü"),
    ("İhbar ve Şikayetleri Değerlendirme Müdürlüğü",	"İhbar ve Şikayetleri Değerlendirme Müdürlüğü"),
    ("Personel Müdürlüğü",	"Personel Müdürlüğü"),
    ("Bilgi Edinme Müdürlüğü",	"Bilgi Edinme Müdürlüğü"),
    ("İdari ve Mali İşler Müdürlüğü",	"İdari ve Mali İşler Müdürlüğü"),
    ("Bilgi İşlem ve Elektronik Belge Yönetim Müdürlüğü",	"Bilgi İşlem ve Elektronik Belge Yönetim Müdürlüğü"),
    ("Strateji Müdürlüğü",	"Strateji Müdürlüğü"),
    ("Hukuk Bürosu",	"Hukuk Bürosu"),
    ("Mükellef Hizmetleri Müdürlüğü",	"Mükellef Hizmetleri Müdürlüğü"),
    ("Eğitim Müdürlüğü",	"Eğitim Müdürlüğü"),
    ("Ankara Kurumlar Vergi Dairesi",	"Ankara Kurumlar Vergi Dairesi"),
    ("Yüzüncüyıl  Vergi Dairesi",	"Yüzüncüyıl  Vergi Dairesi"),
    ("Ankara İhtisas Vergi Dairesi",	"Ankara İhtisas Vergi Dairesi"),
    ("İhtisas Vergi Dairesi",	"İhtisas Vergi Dairesi"),
    ("Doğanbey Vergi Dairesi",	"Doğanbey Vergi Dairesi"),
    ("Yenimahalle Vergi Dairesi",	"Yenimahalle Vergi Dairesi"),
    ("1. Nolu Takdir Komisyonu",	"1. Nolu Takdir Komisyonu"),
    ("2. Nolu Takdir Komisyonu",	"2. Nolu Takdir Komisyonu"),
    ("3. Nolu Takdir Komisyonu",	"3. Nolu Takdir Komisyonu"),
    ("Diğer", "Diğer"),
)


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # logged-in user
    tckn = models.CharField("TCKN", max_length=11, validators=[MinLengthValidator(11)])
    ziyaret = models.CharField("Geldiği Yer", choices=YER_CHOICES)
    aciklama = models.TextField("Açıklama", null=True, blank=True)
    giris = models.DateTimeField("Giriş", default=timezone.now)
    cikis = models.DateTimeField("Çıkış", null=True, blank=True)
    kart_no = models.IntegerField("Giriş Kart No:", null=True, blank=True)


    def __str__(self):
        return self.tckn
