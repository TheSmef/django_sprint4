from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Класс, отвечающий за настройку core."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Служебное'
    verbose_name_plural = 'Служебное'
