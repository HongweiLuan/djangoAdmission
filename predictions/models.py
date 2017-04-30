from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




class Prediction(models.Model):
    RANK_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    Admission_CHOICES = (
        (1, 'Admit'),
        (-1, 'Deny'),
        (3, 'Unknown'),
    )
    user = models.ForeignKey(User)
    GPA = models.FloatField(null=True, blank=True, default=None)
    TOFEL = models.FloatField(null=True, blank=True, default=None)
    SATI = models.FloatField(null=True, blank=True, default=None)
    SchoolRankGroup = models.IntegerField(choices=RANK_CHOICES)
    Admission = models.IntegerField(choices=Admission_CHOICES)
    Predict = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.get_username()+ '_' + str(self.GPA) + '_' + str(self.TOFEL) + '_' + str(self.SATI) + '_' + str(self.SchoolRankGroup) + '_' + str(self.Admission) +  '_' + str(self.Predict)


