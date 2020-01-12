from django.db import models

from datetime import  datetime



class TimingModedel(models.Model):

	start_date = models.DateTimeField()

	end_date = models.DateTimeField()

	def is_current_year(self):
        if datetime.date.today() >= self.start_date and datetime.date.today() <= self.end_date:
            return True
        else:
            return False 

    def __unicode__(self):
        return "%s-%s" % (self.first_day_of_school.year, self.last_day_of_school.year)

    # def save(self, force_insert=False, force_update=False):
    #     if self.is_current_year:
    #         self.current=True
    #     super(SchoolYear, self).save(force_insert, force_update) # Call the "real" save() method.

    # class Meta:
    #     verbose_name = "MODELNAME"
    #     verbose_name_plural = "MODELNAMEs"

    def __str__(self):
        pass



    