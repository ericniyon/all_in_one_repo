from django.db import models


DISTRICTS = 'district'
SECTORS = 'sector'
STATUS = (
    (DISTRICTS, 'district'),
    (SECTORS, 'sector')
)
HOT_SEASON='hot'
COLD_SEASON='cold'
CLIMATE=(
	(HOT_SEASON, 'hot'),
	(COLD_SEASON, 'cold')
	)

class CartData(models.Model):
    name = models.CharField(max_length=100, blank=True)
    groupe = models.CharField(max_length=10, choices=STATUS)
    survived = models.BooleanField()
    climate=models.CharField(max_length=100, choices=CLIMATE, default='Undefined')
    year = models.DateField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
    	return self.name

       
    
	
		