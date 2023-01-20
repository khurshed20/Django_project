from django.shortcuts import render, redirect
from .forms import RecordForm ,PostForm
from .models import *
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView ,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .templatetags import tag
from notifications.signals import notify


# Create your views here.
def RecordView(request):
    if request.method=="POST":
        form=RecordForm(request.POST,request.FILES)
        if form.is_valid():
            if not request.user.is_authenticated: 
              return HttpResponse("Your Registraion /Login is required") 
            object=form.save(commit=False) # commit =False as form still without user data 
            
            object.user=request.user # get logged in user from session data
            
            # AS WE DEFINED ONE To ONE MODEL RELATION FOR ONE USER  ONLY ONE  ENTRY 
            
            if RecordModel.objects.filter(user=request.user).exists() :
                return HttpResponse(" Your already created your Profile")
            object.save()
            subject=form.cleaned_data['subject'] # get subject objects for iteration of multiple subject entry
            for i in subject:
                object.subject.add(i)
                object.save()
            group=form.cleaned_data['group'] # get group objects for iteration of multiple group entry

            for i in group:
                object.group.add(i)
                object.save()    
            messages.success(request,'Record Form has been Successfully Submitted')
            #return HttpResponse("Success")
            return redirect ('/template/')
    else:
        form=RecordForm()
        return render (request, 'education/education.html', {'form':form,'User':request.user})        

def RecordDisplay(request):
    record=RecordModel.objects.all() 
    record=RecordModel.items.all() 
    user=request.user
    if user :
       record_user=RecordModel.objects.filter(user=user.id)
       
    subject=SubjectModel.objects.all()
    
    
    #subject=SubjectModel.objects.filter()
    
    #user=User.objects.filter(id=5)

   # user=User.objects.filter()
    

    group=GroupModel.objects.all()
    math=SubjectModel.objects.get(name='Mathematics')
    record_math=math.subject_set.all()
   # record_math_user=math.subject_set.get(user=request.user.id)

    science=GroupModel.objects.get(name='Science')
    record_science=science.group_set.all()
    business=GroupModel.objects.get(name='Business Studies')
    record_business=business.group_set.all()

    Record_user=record.get(id=request.user.id)
    Record_user.views.add(request.user)
    views= Record_user.views.count()

    liked=False
    recorduser=RecordModel.objects.get(id=user.id)
    if recorduser.likes.filter(id=user.id).exists():
        liked=True

   
    return render (request,'education/record_display.html', {'record':record,'subject':subject,'group':group
         ,'record_math':record_math,'record_science':record_science,'record_business':record_business,'record_user':record_user,
         'user':user,'like':liked,'views':views})       
    

class templateview(TemplateView):
    template_name= 'topic/topics.html'   #'fileupload.html'

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        context['msg1']="Topic Page => this maeesage from TemplateView"
        context['msg2']="No topic has been added yet => this maeesage from TemplateView"

        return context

class RecordView_by_class(FormView):
      template_name='education/education.html'
      form_class=RecordForm
      success_url='/template'

      def form_valid(self, form):
           #login=self.request.user
           if not self.request.user.is_authenticated: 
              return HttpResponse("Log in is required")  

           if RecordModel.objects.filter(user=self.request.user).exists() :
                return HttpResponse(" Your have already created your Profile") 
               
           form.save()
           messages.success(self.request,'Record Form Successfully Submitted')
           return super().form_valid(form)
      def form_invalid(form):


        return super().form_invalid(form)
      def get_success_url(self)-> str :
          return super().get_success_url()  
          #return reverse_lazy ('')  
            
class PostCreateView(CreateView):
    model=PostModel
    form_class=PostForm
    template_name='education/postcreate.html'
    success_url='/'
    
    def form_valid(self, form):
         
         try :     
           form.instance.user=self.request.user 

           form.save()
           return HttpResponse ("Post has been Successfully Created") 
           #return render (self.request, 'education/postcreate.html', {'user': form.instance.user,'msg':'Post has been Successfully Created'} )
                                   
          # return super().form_valid(form)
         except :
            #if self.request.user=='':
              #return HttpResponse ("Login is required") 
            #else:
                 #return render (self.request, 'education/postcreate.html' )
            return redirect ('../post_create' )     # PostCreateView.as_view()
            #return HttpResponse ("Login is required") 
    def form_invalid(form):
            
          return super().form_invalid(form)
    def get_success_url(self)-> str :
          return super().get_success_url()  
         # return reverse_lazy ('topic') 

class PostListView(ListView):  
    template_name='education/listview.html'
    #queryset=PostModel.objects.filter()
    queryset=RecordModel.objects.filter()

    context_object_name='post'
        
    def get_context_data(self, **kwargs):
        
         context= super().get_context_data(**kwargs)  
         #context['post'] =context.get('object_list') 
         context['msg'] ='This  Total  Post  List'
         context['subjects']=SubjectModel.objects.all()
         context['group']=GroupModel.objects.all()
         return context
          
class PostDetailView(DetailView):
   template_name='education/postdetails.html'
   model=RecordModel 
  # model=PostModel

   def get_context_data(self, **kwargs):
         self.object.views.add(self.request.user)
         liked=False
         if self.object.likes.filter(id=self.request.user.id).exists():
          liked=True
         context= super().get_context_data(**kwargs) 
         post=context.get('object')
         #comment=Comment.objects.all()
      
         comments=Comment.objects.filter(post=self.object.id ,parent_comment= None)
         replies=Comment.objects.filter(post=self.object.id ).exclude(parent_comment=None) 
         DictofReply={}
         for reply in replies :
            if reply.parent_comment.id not in DictofReply.keys():
                DictofReply[reply.parent_comment.id]=[reply]
            else :
                DictofReply[reply.parent_comment.id].append(reply)    
         context['post'] =context.get('object')  # =>  this line is optional 
         context['msg'] ='This is Individual Post Details'

         context['like'] =liked
         context['comments'] =comments
         #context['replies'] =replies
         context['DictofReply'] = DictofReply
         
         #
         # context['comment'] =comment
         return context
        
class PostEditView(UpdateView):
    model=RecordModel
    #model=PostModel
    #form_class=PostForm
    form_class=RecordForm
    template_name='education/postcreate.html'
    #success_url='/'

    def get_success_url(self) :
          id=self.object.id
          #return super().get_success_url()  
          return reverse_lazy ('PostDetailView',kwargs={'pk':id}) 

class PostDeleteView(DeleteView):
     model=RecordModel
     template_name='education/postdelete.html'
     success_url=reverse_lazy ('PostListView') 


def search (request):
    query=request.POST.get('search',' ')
    if query :
        queryset=(Q(name__icontains=query))|(Q(address__icontains=query))|(Q(medium__icontains=query))|(Q(category__icontains=query))|(Q(subject__name__icontains=query))|(Q(group__name__icontains=query))
        results=RecordModel.objects.filter(queryset).distinct()
    else:
        results=[]
    context={'result':results}
    return render(request, 'education/search.html',context)

def filter (request):
   
    if request.method=="POST" :
        subject=request.POST['subject']
        group=request.POST['group'] 
        amount_from=request.POST['amount_from'] 
        amount_to=request.POST['amount_to'] 
        available=request.POST['available'] 

        if subject or group:
           queryset=(Q(subject__name__icontains=subject)) & (Q(group__name__icontains=group)) # & for both instead of | (or)
           results=RecordModel.objects.filter(queryset).distinct()
           if available :
              results=results.filter(available=True)
           if amount_from :
             results=results.filter(amount__gte=amount_from)
           if amount_to:
             results=results.filter(amount__lte=amount_to)
        else:
           results=[]  
        context={'result':results}       
        return render(request, 'education/search.html',context)
    #return render(request, 'education/listview.html')    
def likepost(request, id):
    if request.method=="POST":
       
        record_user=RecordModel.objects.get(id=id)
        postId=record_user.id
        if record_user.likes.filter(id=request.user.id).exists():
           record_user.likes.remove(request.user) 
        else :
           record_user.likes.add(request.user)  
           if request.user != record_user.user :
            notify.send(request.user, recipient=record_user.user , verb="has liked your post" + f''' <a href="/education/post_details/{postId}/ " > Go </a>''')  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect(f'../post_details/{postId}/')
def add_comment (request):
    if request.method=="POST":
        comment=request.POST['text'] # New Comment or reply of a comment
        parent_id=request.POST['parent_id'] # id of main comment (if) 
        post_id=request.POST['post_id']
        
        #if (request.POST['parent_id']).strip():
           # ID=True
        #else :
           # ID=False    
        post=RecordModel.objects.get(id=post_id)
        if len(comment)==0 :
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #  back to comment page/original page
        if parent_id.strip():
            parent_comment=Comment.objects.get(id=parent_id)
            newcomment=Comment(text=comment, user=request.user, post=post, parent_comment=parent_comment) # comment reply
            newcomment.save() 
        else :
           newcomment=Comment(text=comment, user=request.user, post=post ) # new comment 
           newcomment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #  back to comment page/original page  

def notification (request):
    return render (request, 'education/notification.html')        