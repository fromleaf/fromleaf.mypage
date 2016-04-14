from django.shortcuts import render

from fromleaf_common.utils import database as db
from fromleaf_common.views import ListCommonView
from fromleaf_myskill.models import SkillSet

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

class MySkillView(ListCommonView):

    template_name = 'fromleaf_myskill/myskill.html'
    context_object_name = 'skill_list'
    
    def get_queryset(self):
        current_member_info = db.get_current_member_info(USER_EMAIL)
        current_user_info = db.get_current_user_info(current_member_info)
        current_page_info = db.get_current_page_info(self, current_member_info)
        return SkillSet.objects.filter(my_skill_page=current_page_info)
    
    def get_context_data(self, **kwargs):
        context = super(MySkillView, self).get_context_data(**kwargs)
        
        development_skill_list = []
        cooperation_skill_list = []
        os_skill_list = []
        personality_skill_list = []
        etc_skill_list = []
        
        skillset_list = self.get_queryset()
        
        for skill in skillset_list:
            if skill.kind == 'DEVELOPMENT':
                development_skill_list.append(skill)
            elif skill.kind == 'COOPERATION':
                cooperation_skill_list.append(skill)
            elif skill.kind == 'OS':
                os_skill_list.append(skill)
            elif skill.kind == 'PERSONALITY':
                personality_skill_list.append(skill)
            elif skill.kind == 'ETC':
                etc_skill_list.append(skill)
            else:
                etc_skill_list.append(skill)
        
        context['development_skill_list'] = development_skill_list
        context['cooperation_skill_list'] = cooperation_skill_list
        context['os_skill_list'] = os_skill_list
        context['personality_skill_list'] = personality_skill_list
        context['etc_skill_list'] = etc_skill_list
        
        return context