from django.apps import AppConfig


class ArrotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arrot'
    
    def ready(self) -> None:
        import arrot.signals
