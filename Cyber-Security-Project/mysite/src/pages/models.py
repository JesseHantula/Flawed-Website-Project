from django.db import models
from django.core.exceptions import ValidationError

class List(models.Model):
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	#for flaw 2, we add a field to check if the list has been verified
	verified = models.BooleanField(default=False)

	#to fix flaw 1, add this function to check that the password is strong enough
	"""
	def save(self, *args, **kwargs):
		if len(self.password) < 8:
			raise ValidationError("The password must be at least 8 characters long.")
		if not any(c.isupper() for c in self.password):
			raise ValidationError("The password must contain at least one uppercase letter.")
		if not any(c.islower() for c in self.password):
			raise ValidationError("The password must contain at least one lowercase letter.")
		if not any(c.isdigit() for c in self.password):
			raise ValidationError("The password must contain at least one digit.")
		super().save(*args, **kwargs)
	"""
	
class Item(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)