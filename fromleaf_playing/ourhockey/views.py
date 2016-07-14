import json

from datetime import datetime

from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, UnreadablePostError
from django.views.generic.edit import FormMixin

from fromleaf_common.utils import database as db
from fromleaf_common.utils.database import UserData

from fromleaf_playing.common.views import PlayingCommonTemplateView, PlayingCommonListView
from fromleaf_playing.ourhockey.forms import CheckAttendForm, AddGameDayForm
from fromleaf_playing.ourhockey.models.Member import Person, Player, Member, Attendance
from fromleaf_playing.ourhockey.models.GameDay import GameDay  

class OurHockeyMainView(PlayingCommonTemplateView):
    
    template_name = 'ourhockey/ourhockey_main.html'

    def get_context_data(self, **kwargs):
        context = super(OurHockeyMainView, self).get_context_data(**kwargs)
        
        return context
    
    
class MemberListView(PlayingCommonListView):

    template_name = 'ourhockey/member_list.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return Member.objects.using('ourhockey').all()

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)

        return context
    

class GameScheduleListView(FormMixin, PlayingCommonListView):

    template_name = 'ourhockey/game_schedule.html'
    context_object_name = 'gameday_list'
    form_class = AddGameDayForm

    def get_queryset(self):
        return GameDay.objects.using('ourhockey').all()

    def get_context_data(self, **kwargs):
        context = super(GameScheduleListView, self).get_context_data(**kwargs)
        return context

    def post(self, request):
        try:
            post_gameday = request.POST.get('post_gameday')
            post_gametype = request.POST.get('post_gametype')
            response_data = {}

            gameday = GameDay(game_day=post_gameday, game_type=post_gametype)
            gameday.save()

            response_data['result'] = 'Create post successful!'
            response_data['game_day'] = gameday.game_day
            response_data['game_type'] = gameday.game_type

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        except UnreadablePostError:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )

    
class SelectTodayAttendListView(PlayingCommonListView):

    template_name = 'ourhockey/select_today_attend.html'
    context_object_name = 'select_member_list'

    def get_queryset(self):
        select_member_list = []
        dict_member = {}
        member_list = Member.objects.using('ourhockey').all()

        for member_ in member_list:
            try:
                attended_ = Attendance.objects.using('ourhockey').get(
                    attended=True,
                    attended_date=datetime.today(),
                    member=member_
                )
                dict_member = {'member': member_, 'attended': attended_}
                select_member_list.append(dict_member)
            except ObjectDoesNotExist:
                dict_member = {'member': member_}
                select_member_list.append(dict_member)

        return select_member_list

    def get_context_data(self, **kwargs):
        context = super(
            SelectTodayAttendListView, self).get_context_data(**kwargs)
        return context

def update_today_attend_member(request):
    """
    description: Update today's attendance of members
    get: request
    return: 
        - json(result of attendance of members)
        - content_type: application/json
    """
    if request.method == 'POST':
        post_attend = request.POST.get('attend')

        if post_attend.checked is 'checked':
            attend_member = Member(id=post_attend.value)
            attendance = Attendance(member=attend_member)
            attendance.attended = True
            attendance.save()

        for member_id in request.POST.getlist('attend'):
            attend_member = Member(id=member_id)
            attendance = Attendance(member=attend_member)
            attendance.attended = True
            attendance.save()

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

######################### BEGIN AJAX 연습 ############################
from django.http import HttpResponseRedirect
from fromleaf_playing.ourhockey.models.Post import Post
from fromleaf_playing.ourhockey.forms import PostForm   

 
def home(req):

    tmpl_vars = {
        'all_posts': Post.objects.reverse(),
        'form': PostForm()
    }
    return render(req, 'ourhockey/post_index.html', tmpl_vars)


def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user.username)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postid'] = post.id
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

########################## END AJAX 연습중 ########################
    

class SelectedTodayAttendListView(PlayingCommonListView):

    template_name = 'ourhockey/selected_today_attend.html'
    context_object_name = 'selected_member_list'

    def get_queryset(self):
        select_member_list = []
        dict_member = {}
        member_list = Member.objects.using('ourhockey').all()

        for _member in member_list:
            try:
                _attended = Attendance.objects.using('ourhockey').get(
                    attended=True,
                    attended_date=datetime.today(),
                    member=_member
                )
                dict_member = {'member': _member, 'attended': _attended}
                select_member_list.append(dict_member)
            except ObjectDoesNotExist:
                dict_member = {'member': _member}
                select_member_list.append(dict_member)

        return select_member_list

    def get_context_data(self, **kwargs):
        context = super(
            SelectedTodayAttendListView, self).get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        selected_member_list = self.get_queryset()

        return render(request, self.template_name, {
            'selected_member_list': selected_member_list,
        })
    
    
    
class TodayAttendedMemberListView(PlayingCommonListView):
    template_name = 'ourhockey/today_attended_list.html'
    context_object_name = 'attended_list'
    
    def get_queryset(self):
        attended_list = Attendance.objects.using('ourhockey').filter(
            attended=True,
            attended_date=datetime.today()
        )
        return attended_list

    def get_context_data(self, **kwargs):
        context = super(
            TodayAttendedMemberListView, self).get_context_data(**kwargs)

        return context
