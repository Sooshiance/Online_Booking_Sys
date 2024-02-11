from django.db.models.signals import post_save, post_delete

from .models import ArrotModel, GolsaModel, Wallet


def update_wallet(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        wallet = Wallet.objects.get_or_create(user=user)[0]
        wallet.reach_limit += 1
        wallet.save()


post_save.connect(update_wallet, sender=ArrotModel)

post_save.connect(update_wallet, sender=GolsaModel)
