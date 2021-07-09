from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect

class TopView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'data':'',
            'data_user':'',
            'data_comment_num':[],
        }

    #@login_required
    def get(self,request):
        #return render(request,'/home.html',self.params)
        return redirect('/testApp/accounts/login/')