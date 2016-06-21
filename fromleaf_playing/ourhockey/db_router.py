from django.conf import settings


class OurhockeyRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read ourhockey models go to settings.DARLY_DATBASE.
        """
        if model._meta.app_label == 'ourhockey':
            return settings.OURHOCKEY_DATBASE
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ourhockey models go to settings.DARLY_DATBASE.
        """
        if model._meta.app_label == 'ourhockey':
            return settings.OURHOCKEY_DATBASE
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ourhockey app is involved.
        """
        if obj1._meta.app_label == 'ourhockey' or obj2._meta.app_label == 'ourhockey':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ourhockey app only appears in the 'settings.DARLY_DATBASE'
        database.
        """
        if app_label == 'ourhockey':
            return db == settings.OURHOCKEY_DATBASE
        return None