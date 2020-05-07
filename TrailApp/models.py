from django.db import models


class members(models.Model):
    Id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    starttime = models.DateTimeField(auto_now=True)
    endtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Id, self.real_name, self.tz, self.phone_number, self.starttime,self.endtime