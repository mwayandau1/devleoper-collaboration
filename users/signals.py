from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    print("profile signals triggerred")
    if created:
        user = instance
        profile =Profile.objects.create(user=user, username=user.username, 
                                        email=user.email, name=user.first_name)
        subject = 'Welcome to DevColab'
        body = 'We are happy you have joined us!'
        send_mail(subject,
                  body,
                  settings.EMAIL_HOST_USER,
                  [profile.email],
                  fail_silently=False
                  )
        
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# post_save.connect(createProfile, sender=User)
# post_delete.connect(profileDeleted, sender=Profile)
