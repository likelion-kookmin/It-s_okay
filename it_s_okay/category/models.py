from django.db import models


class Large_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Medium_category(models.Model):
    name = models.CharField(max_length=20)
    large_category = models.ForeignKey(Large_category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Small_category(models.Model):
    name = models.CharField(max_length=20)
    medium_category = models.ForeignKey(Medium_category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
