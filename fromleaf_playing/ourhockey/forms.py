from django import forms

from fromleaf_playing.ourhockey.models.GameDay import GameDay
from fromleaf_playing.ourhockey.models.Post import Post

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

class CheckAttendForm(forms.Form):
    attend = forms.BooleanField(required=True)

class AddGameDayForm(forms.ModelForm):   
    class Meta:
        model = GameDay
        fields = ['game_day', 'game_type']
          
        widgets = {
            'game_day': forms.DateInput(
                attrs={'id': 'post_gameday', },
            ),
            'game_type': forms.TextInput(
                attrs={'id': 'post_gametype', },
            ),
        }
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }
             
