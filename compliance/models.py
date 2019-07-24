from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

# class Company_Masters(models.Model):
# 	comp_id = models.CharField(max_length=2,primary_key=True)
# 	comp_name = models.CharField(max_length=100)
	

# class Location_Masters(models.Model):
# 	loc_id = models.PositiveIntegerField(validators=[MaxValueValidator(99)], primary_key=True)
# 	loc_name = models.CharField(max_length=100)
# 	comp_id = models.ForeignKey(Company_Masters, on_delete=models.CASCADE , null=True )
	

# class dept(models.Model):
# 	dept_id = models.CharField(max_length=4, primary_key=True)
# 	dept_name = models.CharField(max_length=100)
# 	loc_id = models.ForeignKey(Location_Masters, on_delete=models.CASCADE , null=True)
	

# class emplo(models.Model):
# 	emp_id = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], primary_key=True)
# 	emp_name = models.CharField(max_length=100)
# 	dept_id = models.ForeignKey(dept, on_delete=models.CASCADE , null=True)
# 	email = models.CharField(max_length=200, null=True, blank=True)

# class Comp_Info(models.Model):
# 	loc_id = models.ForeignKey(Location_Masters, on_delete=models.CASCADE , null=True)
# 	category = models.CharField(max_length=100)
# 	reg_no = models.CharField(max_length=100)
# 	license_type = models.CharField(max_length=200)
# 	law_authority = models.CharField(max_length=250,null=True,blank=True)
# 	date_purchase = models.DateField(("Date"),null=True,blank=True)
# 	date_expiry = models.DateField(("Date"),null=True,blank=True)
# 	renewal = models.CharField(max_length=200, null=True,blank=True)
# 	present_fees = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999999999999)],null=True,blank=True)
# 	primary_emp = models.ForeignKey(emplo, related_name = 'Prim_emp' , on_delete=models.CASCADE , null=True)
# 	sec_emp = models.ForeignKey(emplo, related_name = 'secd_emp', on_delete=models.CASCADE , null=True)
# 	custody = models.CharField(max_length=20)


class compli(models.Model):
	comp_id = models.CharField(max_length=8)
	loc_name = models.CharField(max_length=100)
	comp_name = models.CharField(max_length=100)
	month = models.CharField(max_length=50)
	renewal = models.DateField(("Renewal Date (YYYY-MM-DD)"),null=True,blank=True)
	category = models.CharField(max_length=100)
	license_no = models.CharField(max_length=200)
	license_type = models.CharField(max_length=200)
	law_authority = models.CharField(max_length=250,null=True,blank=True)
	date_purchase = models.DateField(("Purchase Date"),null=True,blank=True)
	date_expiry = models.DateField(("Expiry Date"),null=True,blank=True)
	present_fees = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999999999999)],null=True,blank=True)
	primary_emp = models.CharField(max_length=100)
	sec_emp = models.CharField(max_length=100)
	custody = models.CharField(max_length=20)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.comp_id

	def get_absolute_url(self):
		return reverse('compli-detail', kwargs = {'pk' : self.pk})






	  