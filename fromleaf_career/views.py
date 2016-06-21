from django.shortcuts import render
from django.conf import settings

from fromleaf_common.utils import database as db
from fromleaf_common.utils.database import UserData, CompanyData
from fromleaf_common.views import CommonListView, CommonDetailView
from fromleaf_career.models import Company, Project


class CareerView(CommonListView):
    
    template_name = 'fromleaf_career/career.html'
    context_object_name = 'company_list'
    
    def get_queryset(self):
        user_data = UserData(settings.USER_EMAIL)
        return Company.objects.filter(member_info=user_data.get_member_info())
    
    def get_context_data(self, **kwargs):
        context = super(CareerView, self).get_context_data(**kwargs)
        
        return context
        

class CompanyDetailView(CommonDetailView):
    template_name = 'fromleaf_career/company.html'
    model = Company
    context_object_name = 'company'
 
    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        company_data = CompanyData(settings.USER_EMAIL)
        company = self.get_object()
        context['project_list'] = company_data.get_project_list_of_company(company)
        return context
