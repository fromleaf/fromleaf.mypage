from django.test import TestCase

from fromleaf_playing.ourhockey.models.Player import Person, Player, Member

class OurhockeyTestCase(TestCase):
    
    def insert_player(self, **kwargs):
        player = Player.objects.create(**kwargs)
        player.using('ourhockey').save()
        
    def insert_player_data(self):
        self.insert_player(
                           back_number=10,
                           position='LF',
                        )
        self.insert_player(
                           back_number=11,
                           position='LD',
                        )
        self.insert_player(
                           back_number=12,
                           position='C',
                        )