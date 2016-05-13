from django.conf import settings

class DefaultRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read fromleaf models go to settings.DEFAULT_DATABASE.
        """
        if model._meta.app_label == 'fromleaf':
            return 'default'
        elif model._meta.app_label == 'fromleaf_playing.darly':
            return 'darly'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write fromleaf models go to settings.DEFAULT_DATABASE.
        """
        if model._meta.app_label == 'fromleaf':
            return 'default'
        elif model._meta.app_label == 'darly':
            return 'darly'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the fromleaf app is involved.
        """
        if obj1._meta.app_label == 'fromleaf' or obj2._meta.app_label == 'fromleaf':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the fromleaf app only appears in the 'settings.DEFAULT_DATABASE'
        database.
        """
        if app_label == 'fromleaf':
            return db == 'default'
        elif app_label == 'darly':
            return 'darly'
        return None