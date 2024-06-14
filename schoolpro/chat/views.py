from django.shortcuts import render
from django.views import View

# Create your views here.
class lobby(View):
  def get(self,request):
    return render(request,'chat/lobby.html')