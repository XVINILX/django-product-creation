from django.db import models

class Base(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class User(Base):
    email = models.EmailField()
    password = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
    

class Product(Base):
    name = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f'O produto {self.name} tem preço de R${self.price}'