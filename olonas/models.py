from django.db import models

# Create your models here.

class Faritany(models.Model):
    anarana = models.CharField(max_length=50)

    def __str__(self):
        return self.anarana   

class Faritra(models.Model):
    anarana = models.CharField(max_length=50)
    faritany = models.ForeignKey(Faritany, on_delete=models.CASCADE)

    def __str__(self):
        return self.anarana
    
class Fivondronana(models.Model):
    anarana = models.CharField(max_length=50)
    faritra = models.ForeignKey(Faritra, on_delete=models.CASCADE)

    def __str__(self):
        return self.anarana

class Firaisana(models.Model):
    anarana = models.CharField(max_length=50)
    fivondronana = models.ForeignKey(Fivondronana, on_delete=models.CASCADE)

    def __str__(self):
        return self.anarana

class Olona(models.Model):
	id = models.BigAutoField(primary_key=True)
	anarana = models.CharField(max_length=50)
	fanampiny = models.CharField(max_length=50)
	daty_nahaterahana = models.DateField()
	lahy_vavy =  models.CharField(max_length=4)
	toerana_nahaterahana = models.CharField(max_length=50)
	firenena_onenana = models.CharField(max_length=50 )
	faritra = models.ForeignKey(Faritra, on_delete=models.CASCADE, default = 0, blank=True, null=True)
	fivondronana = models.ForeignKey(Fivondronana, on_delete=models.CASCADE, default = 0, blank=True, null=True)
	firaisana = models.ForeignKey(Firaisana, on_delete=models.CASCADE, default = 0, blank=True, null=True)
	adiresy = models.CharField(max_length=50)
	diplaoma = models.CharField(max_length=50)
	asa = models.CharField(max_length=50)
	ray = models.BigIntegerField()	
	reny = models.BigIntegerField()
	fizokiana = models.IntegerField()
	fiantsoana = models.CharField(max_length=20, default='tsisy')
	

class Vady(models.Model):
	id_lahy = models.BigIntegerField()
	id_vavy = models.BigIntegerField()