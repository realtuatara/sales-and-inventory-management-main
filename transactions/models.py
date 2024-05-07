from django.db import models
from store.models import Item
from accounts.models import Profile, Vendor
from django_extensions.db.fields import AutoSlugField

# Create your models here.

PAYMENT_CHOICES = [
    ('MP', 'MIR'),
    ('VISA', 'VISA'),
    ('CS', 'CASH'),
    ('VM', 'VIRTUAL MONEY'),
    ('BK', 'BANK')
]

DELIVERY_CHOICES = [
    ('P', 'ОЖИДАЕТСЯ'),
    ('S', 'ДОСТАВЛЕНО')
]

class Sale(models.Model):
    slug = AutoSlugField(unique=True , populate_from='customer_name')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, verbose_name=('Название'))
    customer_name = models.CharField(max_length=20, null=True, blank=True, verbose_name=('Покупатель'))
    transaction_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=('Дата'))
    quantity = models.FloatField(default=0.00, blank=False, null=False, verbose_name=('Количество'))
    payment_method = models.CharField(choices=PAYMENT_CHOICES, max_length=20, blank='True', null=True, verbose_name=('Способ оплаты'))
    price = models.FloatField(default=0.00, blank=False, null=False, verbose_name=('Цена'))
    total_value = models.FloatField(blank=True, null=True, verbose_name=('Итого'))
    amount_received = models.FloatField(default=False, blank=False, null=False, verbose_name=('Получено'))
    balance = models.FloatField(default=False, blank=False, null=False, verbose_name=('Баланс'))
    profile = models.ForeignKey(Profile, verbose_name=('Продавец'), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        amt_received = self.amount_received
        price = self.price
        quantity = self.quantity
        self.total_value = price * quantity
        self.balance = amt_received - self.total_value
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.item.name)

class Purchase(models.Model):
    slug = AutoSlugField(unique=True , populate_from='vendor')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=('Товар'))
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name=('Описание'))
    vendor = models.ForeignKey(Vendor, related_name='vendor', on_delete=models.CASCADE, blank=False, null=False, verbose_name=('Поставщик'))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата заявки'))
    delivery_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=('Дата доставки'))
    quantity = models.FloatField(default=0.00, blank=False, null=False, verbose_name=('Количество'))
    delivery_status = models.CharField(choices=DELIVERY_CHOICES, max_length=3, default='P', blank=False, null=False, verbose_name=('Статус доставки'))
    price = models.FloatField(default=0.00, blank=False, null=False, verbose_name=('Цена за единицу'))
    total_value = models.FloatField()

    def save(self, *args, **kwargs):
        quantity = self.quantity
        price = self.price
        self.total_value = price * quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.item.name

    class Meta:
        ordering = ["order_date"]
