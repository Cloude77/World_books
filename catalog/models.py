from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр книги")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите язык книги",
                            verbose_name="Язык книги")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя автора",
                                  verbose_name="Имя автора")
    last_name = models.CharField(max_length=100,
                                 help_text="Введите фамилию автора",
                                 verbose_name="Фамилия автора")
    date_of_birth = models.DateField(
                                 help_text="Введите дату рождения",
                                 verbose_name="Дата рождения",
                                 null=True, blank=True)
    date_of_death = models.DateField(
                                 help_text="Введите дату смерти",
                                 verbose_name="Дата смерти",
                                 null=True, blank=True)

    def __str__(self):
        return self.last_name



#
# class MyModelName(models.Model):
#     my_field_name = models.CharField(max_length=20,
#                                      help_text="Не более 20 символов")
#
#     class Meta:
#         ordering = ["-my_field_name"]
#
#     def get_absolute_url(self):
#         return reverse('model-detail-view', args=[str(self.id)])
#
#     def __str__(self):
#         return self.field_name

# a_record = MyModelName(my_field_name="Книга о вкусной еде")
# a_record.save()
