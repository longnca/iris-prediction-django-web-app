from django.db import models


class PredResults(models.Model):
    """A data model to store the input and results."""
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification