from django.shortcuts import render
import pyshorteners
from django.views import View


class shortner(View):
   def post(self,request):
      long=request.POST['url']
      shortner=pyshorteners.Shortener()
      short=shortner.tinyurl.short(long)

      return render(request,'index.html',{'short':short})
   def get(self,request):
      return render(request, 'index.html')





