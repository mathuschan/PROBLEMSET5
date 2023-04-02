from django.db import models

class Element(models.Model):
    value = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default='Mathuschan')
    id = models.AutoField(primary_key=True)


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    element = models.CharField(max_length=255, default="default_value", blank=True)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} - {self.person}"


