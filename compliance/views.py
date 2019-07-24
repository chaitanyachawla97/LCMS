from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import compli
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
  	#mylist = (Company_Masters.objects.all(), Location_Masters.objects.all() , dept.objects.all(), emplo.objects.all())
  	context = {
  		'mylist': compliance.objects.all()
  	}
  	return render(request,'compliance/home.html',context)

	
class PostListView(ListView):
    model = compli
    template_name = 'compliance/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'mylist'
    ordering = ['renewal']

class PostDetailView(DetailView):
    model = compli

class PostCreateView(LoginRequiredMixin, CreateView):
    model = compli
    fields = ['comp_id', 'loc_name', 'comp_name', 'month', 'renewal' , 'category','license_no', 'license_type', 'primary_emp', 'sec_emp', 'custody']    

    def form_valid(self, form):
    	form.instance.user = self.request.user	
    	return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = compli
    fields = ['comp_id', 'loc_name', 'comp_name', 'month', 'renewal' , 'category','license_no', 'license_type', 'primary_emp', 'sec_emp', 'custody']    

    def form_valid(self, form):
    	form.instance.user = self.request.user	
    	return super().form_valid(form)         	

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = compli
    success_url = '/'


def about(request):
	return render(request,'compliance/about.html')	