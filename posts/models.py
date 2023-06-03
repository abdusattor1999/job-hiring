from django.db import models
from accounts.models import Company
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nomi')
    slug = AutoSlugField(populate_from='name')
    vacancies = models.PositiveIntegerField(default=0, verbose_name='Vakansiyalar')
    category = models.ForeignKey('self', blank=True, null=True, verbose_name='Kategoriyasi', on_delete=models.CASCADE, related_name='self_category')
    status = models.BooleanField(default=True, verbose_name='Aktivligi')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Nomi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    description = models.TextField(verbose_name="qo'shimcha malumot")
    address = models.CharField(max_length=50, verbose_name='Manzil')
    job_type = models.CharField(max_length=50, verbose_name="Bandlik turi")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Oylik maosh")
    status = models.BooleanField(default=True, verbose_name='Aktivligi')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
	    return reverse('posts:post_detail', args=[self.id])


@receiver(post_save, sender=Post)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        try:
            categ = Category.objects.filter(post=instance).last()
            soni = categ.vacancies
            soni += 1
            categ.vacancies = soni
            categ.save()
        except:
            print("Saveda Xatolik !!!")    


@receiver(pre_delete, sender=Post)
def handle_page_delete(sender, **kwargs):
    try:
        obj = kwargs['instance']
        categ = Category.objects.filter(post=obj).last()
        soni = categ.vacancies
        soni -= 1
        categ.vacancies = soni
        categ.save()
    except:
        print("Deleteda xatolik !")

