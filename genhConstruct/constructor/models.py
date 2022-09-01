from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=255, default=" ", verbose_name="Название")
    slug = models.SlugField(max_length=10, default=" ")
    img = models.ImageField(upload_to='images/element/', verbose_name="Изображение", help_text=".png, то есть без фона")
    color = models.CharField(max_length=8, default="000000", verbose_name='Цвет фона')

    class Meta:
        verbose_name = "Стихия"
        verbose_name_plural = "Стихии"

    def __str__(self):
        return self.name


class TypeWeapon(models.Model):
    name = models.CharField(max_length=255, default=" ", verbose_name="Название")
    img = models.ImageField(upload_to='images/type/weapon', verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")

    class Meta:
        verbose_name = "Тип оружия"
        verbose_name_plural = "Типы оружия"

    def __str__(self):
        return self.name


class Weapon(models.Model):
    type = models.ForeignKey(TypeWeapon, on_delete=models.PROTECT, verbose_name="Тип оружия")
    name = models.CharField(max_length=255, default=" ", verbose_name="Название")
    star = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(5)], verbose_name="Редкость")
    img = models.ImageField(upload_to='images/weapon/', verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")
    passive = models.TextField(blank=True, verbose_name="Пассивная способность")
    # set = models.ForeignKey()

    # mainCharacteristic = models.ForeignKey()
    # secondCharacteristic = models.ForeignKey()
    # mainScale = models.ForeignKey()
    # secondScale = models.ForeignKey()

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"

    def __str__(self):
        return self.name


class WeaponBuild(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.PROTECT, verbose_name="Оружие")
    awakening = models.PositiveIntegerField(default=1, validators=[
                                                                    MinValueValidator(1),
                                                                    MaxValueValidator(5)], verbose_name="Пробуждение")
    level = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(90)], verbose_name="Уровень")

    class Meta:
        verbose_name = "Оружие сборки"
        verbose_name_plural = "Оружие сборки"

    def __str__(self):
        return self.weapon.name


class TypeArtifact(models.Model):
    name = models.CharField(max_length=255, default=" ",  verbose_name="Название")
    img = models.ImageField(upload_to='images/type/artifact', verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")

    class Meta:
        verbose_name = "Тип артефакта"
        verbose_name_plural = "Типы артефактов"

    def __str__(self):
        return self.name


class Artifact(models.Model):
    type = models.ForeignKey(TypeArtifact, on_delete=models.PROTECT, verbose_name="Тип артефакта")
    name = models.CharField(max_length=255, default=" ", verbose_name="Название")
    star = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(5)], verbose_name="Редкость")
    img = models.ImageField(upload_to='images/artifact/', verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")

    # set = models.ForeignKey()
    # mainCharacteristic = models.ForeignKey()
    # secondCharacteristics = models.ForeignKey()
    # mainScale = models.ForeignKey()
    # secondScale = models.ForeignKey()

    class Meta:
        verbose_name = "Артефакт"
        verbose_name_plural = "Артефакты"

    def __str__(self):
        return self.name


class ArtifactBuild(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.PROTECT, verbose_name="Артефакт")
    level = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(20)], verbose_name="Уровень")

    class Meta:
        verbose_name = "Артефакт сборки"
        verbose_name_plural = "Артефакты сборки"

    def __str__(self):
        return self.artifact.name


class Character(models.Model):
    type = models.ForeignKey(TypeWeapon, on_delete=models.PROTECT, verbose_name="Тип оружия")
    star = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(5)], verbose_name="Редкость")
    name = models.CharField(max_length=255, default=" ",  verbose_name="Имя")
    img = models.ImageField(upload_to='images/character/', verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return self.name


class CharacterBuild(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, verbose_name="Персонаж")
    level = models.PositiveIntegerField(default=1, validators=[
                                                                MinValueValidator(1),
                                                                MaxValueValidator(90)], verbose_name="Уровень")

    class Meta:
        verbose_name = "Персонаж сборки"
        verbose_name_plural = "Персонажи сборки"

    def __str__(self):
        return self.character.name


class Build(models.Model):
    nameBuild = models.CharField(max_length=255, default="Сборка № ", verbose_name="Название")
    character = models.ForeignKey(CharacterBuild, on_delete=models.CASCADE, verbose_name="Персонаж")
    weapon = models.ForeignKey(WeaponBuild, on_delete=models.CASCADE, verbose_name="Оружие")
    artifacts = models.ManyToManyField(ArtifactBuild, verbose_name="Артефакты")
    img = models.ImageField(upload_to='images/build/' + str(nameBuild), verbose_name="Изображение",
                            blank=True, help_text=".png, то есть без фона")

    class Meta:
        verbose_name = "Билд"
        verbose_name_plural = "Билды"

    def __str__(self):
        return self.nameBuild
