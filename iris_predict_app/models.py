from django.db import models


class PredResults(models.Model):
    """A data model to store the input and results."""
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)

    class Meta:
        """Tells Django how to use plural names of Pred Results."""
        verbose_name_plural = 'Pred results'

    def __str__(self):
        return self.classification