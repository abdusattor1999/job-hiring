from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company')
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='Kompaniya nomi')
    email = models.EmailField(verbose_name='Email manzil')
    topic = models.CharField(verbose_name='Faoliyat sohasi', max_length=50)
    about = models.TextField(verbose_name='Kompaniya haqida')
    address = models.CharField(max_length=150, verbose_name='Yuridik manzil (ixtiyoriy)', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Companies'
    
    @property
    def get_image(self):
        image = 'Image none'
        if self.image:
            return self.image.url
        else:
            return image

    def __str__(self) -> str:
        return self.name
    
    


DEGREE_CHOICES = (
    ("O'rta", "O'rta"),
    ("O'rta Maxsus", "O'rta Maxsus"),
    ("Tugallanmagan oliy", "Tugallanmagan oliy"),
    ("Oliy", "Oliy"),
    ("Magistr", "Magistr"),
)

class Qualification(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Shaxs')
    sphere = models.CharField(max_length=60, verbose_name="Tajriba turi")
    period = models.CharField(max_length=20, verbose_name='Tajriba muddati')

    def __str__(self) -> str:
        return f"{self.sphere.capitalize()} - {self.period}"

class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=50, verbose_name='Familiya')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='Yosh')
    about = models.TextField(verbose_name='Shaxs haqida', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default="O'rta Maxsus")
    kasbi = models.CharField(verbose_name='Kasbi', blank=True, null=True, max_length=50)
    is_busy = models.BooleanField(verbose_name='Ishlaydi', default=False)
    address = models.CharField(max_length=100, verbose_name="Manzil")
    
    def __str__(self) -> str:
        return self.first_name
