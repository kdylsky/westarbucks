from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'menus'


class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drink'


class(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    drink_id = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size_id = models.ForeignKey('Size', on_delete=models.CASCADE)


class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'size'


class Image(models.Model):
    img_url = models.CharField(max_length=2000)
    drink_id = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'




class Allergy_drink(models.Model):
    drink_id = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'




class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

