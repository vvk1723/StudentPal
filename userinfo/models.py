## @file models.py
#  @author SYNTAX
#  @date 28 Oct 2017
#  
#  @brief This is a file conatining some classes using python.
#
#  It contains of classe named Profile

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from StudentPal import settings
from django.core.validators import MaxValueValidator, MinValueValidator

## class Profile 
#
# maintains data related to profile of user
# dob,univ,gender are some of its parts
#
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	univ = models.CharField(blank=True, max_length=100, default='')
	current_sem = models.PositiveSmallIntegerField(
		default=0,
		validators=[MaxValueValidator(10)]
		)
	gender = models.CharField(
        max_length=1,
		choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'I prefer not to say')),
        blank=True,
		default='')
	aboutme = models.TextField(blank=True, default='')
	
	def __str__(self):
		return "%s's profile" %self.user


@receiver(post_save, sender=User)
## Used to create user profile
# 
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
## Used to save user profile
# 
def save_user_profile(sender, instance, **kwargs):
   	instance.profile.save()
