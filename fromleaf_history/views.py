from django.shortcuts import render

from fromleaf_common.views import ListCommonView, DetailCommonView

class HistoryView(ListCommonView):
    template_name = 'fromleaf_history/history.html'

class CompanyDetailView(ListCommonView):
    template_name = 'fromleaf_history/company.html'
    
class ProjectDetailView(DetailCommonView):
    template_name = 'fromleaf_history/project_detail.html'