from django.shortcuts import render
from django.conf import settings

from fromleaf_common.utils import database as db
from fromleaf_common.views import ListCommonView, DetailCommonView
from fromleaf_career.models import Company, Project


class CareerView(ListCommonView):
    
    template_name = 'fromleaf_career/career.html'
    context_object_name = 'company_list'
    
    def get_queryset(self):
        current_member_info = db.get_current_member_info(settings.USER_EMAIL)
        current_page_info = db.get_current_page_info(self, current_member_info)
        return Company.objects.filter(career_page=current_page_info)
    
    def get_context_data(self, **kwargs):
        context = super(CareerView, self).get_context_data(**kwargs)
        
        return context
        

class CompanyDetailView(DetailCommonView):
    template_name = 'fromleaf_career/company.html'
    model = Company
    context_object_name = 'company'
 
    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        current_company = self.get_object()
        context['project_list'] = db.get_current_project_list(current_company)
        return context
    
    
class ProjectDetailView(DetailCommonView):
    template_name = 'fromleaf_career/project_detail.html'
