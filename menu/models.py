from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name="Меню")
    slug = models.SlugField(max_length=32, blank=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
    
    def __str__(self):
        return self.title


class Items(models.Model):
    title = models.CharField(max_length=128, blank=True, verbose_name="Подменю")
    slug = models.SlugField(max_length=32, blank=True, unique=True)
    menu = models.ForeignKey(Menu, blank=True, related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey("Items", blank=True, null=True, related_name="child", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подменю"
        verbose_name_plural = "Подменю"
    
    def __str__(self):
        return self.title