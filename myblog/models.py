from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    yazar = models.ForeignKey(User)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olusturulma_tarihi = models.DateTimeField(default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

#models.CharField - kısıtlı uzunlukta metin tanımlamak için kullanılır.
#models.TextField - bu da uzun metinleri tanımlar. Blog gönderileri için biçilmiş kaftan, değil mi?
#models.DateTimeField -bu da gün ve saati tanımlamada kullanılır.
#models.ForeignKey - başka bir model ile bağlantı içerir.
