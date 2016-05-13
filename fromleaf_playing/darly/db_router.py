from django.conf import settings


class DarlyRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read darly models go to settings.DARLY_DATBASE.
        """
        if model._meta.app_label == 'darly':
            return settings.DARLY_DATBASE
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write darly models go to settings.DARLY_DATBASE.
        """
        if model._meta.app_label == 'darly':
            return settings.DARLY_DATBASE
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the darly app is involved.
        """
        if obj1._meta.app_label == 'darly' or obj2._meta.app_label == 'darly':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the darly app only appears in the 'settings.DARLY_DATBASE'
        database.
        """
        if app_label == 'darly':
            return db == settings.DARLY_DATBASE
        return None