from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

#^ ile başlıyor - "başlangıç'.
#post/ sadece URL'nin başlangıçtan sonra post ve /. ifadelerinin geçmesi gerektiği anlamına geliyor. Şimdilik iyi gidiyor.
#(?P<pk>[0-9]+) - bu kısım biraz daha karışık. Buranın anlamı şu: Django bu alana yerleştirdiğimiz her şeyi alacak ve onu pk adında bir değişken olarak view'e aktaracak. [0-9] bize eşleşenlerin sadece rakam (yani harf olamaz) olabileceğini söylüyor (0 ile 9 arasındaki her şey). + en az bir veya daha fazla rakam olması gerektiğini ifade ediyor. Yani http://127.0.0.1:8000/post// eşleşmez ama http://127.0.0.1:8000/post/1234567890/ eşleşir!
#/ - gene bir /'e ihtiyacımız var
#$ - "son"!
