from django.db.models.signals import post_save, post_delete

from .models import User, Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user=instance
        new_profile = Profile.objects.create(
            user=user,
            email=user.email,
            phone= user.phone,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        

def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)


post_delete.connect(delete_user, sender=Profile)


################################### update User with Profile ###################################


def updateProfile(sender, instance, created, **kwargs):
    user = instance
    # if not created:
    #     if User.objects.get(phone=user.phone):
    #         new_profile = User.objects.update(
    #             phone=user.phone,
    #             email=user.email,
    #         )


post_save.connect(updateProfile, sender=Profile)
