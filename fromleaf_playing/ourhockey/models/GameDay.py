from django.db import models

class GameDay(models.Model):
    
    def __init__(self, *args, **kwargs):
        super(GameDay, self).__init__(*args, **kwargs)
    
    def __unicode__(self):  # __str__ on Python3
        return self.gameday
    
    game_day = models.DateField()
    game_type = models.CharField(max_length=45)