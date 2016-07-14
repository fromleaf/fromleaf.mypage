from fromleaf_common.views import CommonTemplateView, CommonListView, CommonFormView, CommonDetailView

PLAYING_MENU_LIST = ['darly', 'ourhockey', 'playground']


DARLY_MENU_LIST = [
    'main',
    'photo_album'
]

OURHOCKEY_MENU_LIST = [
    'main',
    'member_list',
    'game_schedule',
    'select_today_attend',
    'today_attended_list',
]

PLAYGROUND_MENU_LIST = [
    'main',
    'crawler',
]


class PlayingCommonTemplateView(CommonTemplateView):

    def get_context_data(self, **kwargs):
        context = super(
            PlayingCommonTemplateView, self).get_context_data(**kwargs)
        context['playing_menu_list'] = PLAYING_MENU_LIST
        context['darly_menu_list'] = DARLY_MENU_LIST
        context['ourhockey_menu_list'] = OURHOCKEY_MENU_LIST
        context['playground_menu_list'] = PLAYGROUND_MENU_LIST

        return context


class PlayingCommonListView(CommonListView):

    def get_context_data(self, **kwargs):
        context = super(PlayingCommonListView, self).get_context_data(**kwargs)
        context['playing_menu_list'] = PLAYING_MENU_LIST
        context['darly_menu_list'] = DARLY_MENU_LIST
        context['ourhockey_menu_list'] = OURHOCKEY_MENU_LIST
        context['playground_menu_list'] = PLAYGROUND_MENU_LIST

        return context


class PlayingCommonFormView(CommonFormView):

    def get_context_data(self, **kwargs):
        context = super(PlayingCommonFormView, self).get_context_data(**kwargs)
        context['playing_menu_list'] = PLAYING_MENU_LIST
        context['darly_menu_list'] = DARLY_MENU_LIST
        context['ourhockey_menu_list'] = OURHOCKEY_MENU_LIST
        context['playground_menu_list'] = PLAYGROUND_MENU_LIST

        return context


class PlayingCommonDetailView(CommonDetailView):

    def get_context_data(self, **kwargs):
        context = super(
            PlayingCommonDetailView, self).get_context_data(**kwargs)
        context['playing_menu_list'] = PLAYING_MENU_LIST
        context['darly_menu_list'] = DARLY_MENU_LIST
        context['ourhockey_menu_list'] = OURHOCKEY_MENU_LIST
        context['playground_menu_list'] = PLAYGROUND_MENU_LIST

        return context
