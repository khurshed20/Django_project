import requests
from django.shortcuts import render,redirect
from rest_framework.response  import Response
from rest_framework.decorators import api_view          # for function view
from rest_framework.views import APIView     # for class view
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated ,AllowAny  # for class view
from rest_framework.decorators import permission_classes     # for function view
from rest_framework.authentication import TokenAuthentication  # for class view
from Rest_Api.models import Company, Topic_Entry_comment
from Rest_Api.models import Topic ,Topic_Entry
from .forms import TopicForm , CompanyModelForm
from .forms import EntryForm,EntryCommentForm
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.decorators import login_required 
import json
from .serializers import CompanySerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here

  ##    REST  API  START 

class company(APIView) :
    # def get(self,request,*args,**kwargs):
    authentication_classes=[TokenAuthentication,]
    #authentication_classes=[TokenObtainPairView,]
    permission_classes= [IsAuthenticated,] # [AllowAny,]  #

    def get(self,request,id=None):   
       #id1=None
       user=request.user
       print(user)
       try:
          id1=self.request.data['id']
       # company_object=Company.objects.all()
       #if id :
          company_object=Company.objects.get(id=id1)
          serializers=CompanySerializer(company_object)
         # return Response({'status':'Success','Company':serializers.data},status=200)
          return Response({'data':serializers.data,'status':200}, status=200)
       #elif id1 :
       except :
        # if id :
         try:
           company_object=Company.objects.get(id=id)

           serializers=CompanySerializer(company_object)
           return Response({'status':'Success','data':serializers.data},status=200)
         
        # else :
         except:
           company_object=Company.objects.all()
           serializers=CompanySerializer(company_object,many=True)
           return Response ({'status':'success','data':serializers.data},status=status.HTTP_200_OK)
          #return Response({'status':'Error','data':"please Enter Company Id"},status=200)

    def post(self,request):
       # print("Received")
       # mail=request.data['mail']
        serializers=CompanySerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response ({'status':'Success','data':serializers.data},status=status.HTTP_200_OK)
        else :
             return Response ({'status':'Error','data':serializers.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch (self,request,id=None):
         id=request.data['id']
         company_object=Company.objects.get(id=id)
        
        # data={"id":request.data['id'],"name":request.data['name']}
         serializers=CompanySerializer(company_object,data=request.data, partial=True)
         if serializers.is_valid():
            serializers.save()
            return Response ({'status':'Success','data':serializers.data})

         else :
             return Response ({'status':'Error','data':serializers.errors})

    def delete(self,request,id=None):
        try :

        #id=request.data['id']
           company_object=get_object_or_404(Company,id=id)
           company_object.delete()
           return Response ({'status':'Success','ID':id,'data':"Record Deleted"})
        except :
             id=request.data['id']
             company_object=get_object_or_404(Company,id=id)
             company_object.delete()
             return Response ({'status':'Success','ID':id,'data':"Record Deleted"})

           
def CompanyInfo_RestApi_post(request) :
    if request.method=="POST":
        form=CompanyModelForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        auth_data={'username':username , 'password':password}
        #auth_data={'username':'admin' , 'password':'admin123'}
        url_auth='http://127.0.0.1:8000/token/'
        api_auth=requests.post(url=url_auth, json=auth_data)
        try:
            api_auth_res=json.loads(api_auth.text)
        except:
           api_auth_res=None
        token=api_auth_res['token']
        #return HttpResponse('Token :' +token)
        print(token)    
        #token='b0557e7595f43fa60067bb895ddf8a4e6a1ece19'
        data=form.data
        url_company="http://127.0.0.1:8000/api/company/"
        api_company=requests.post(url=url_company, data=data, headers={'Authorization':f'Token {token}'})
        try:
            api_company_res=json.loads(api_company.text)
            return render (request, 'Rest_Api/companyInfo_RestApi.html',{ 'token':token, 'response':api_company_res}) 
           # return HttpResponse(api_company )
        except:
           api_company_res=None
        print(api_company) 

    else:
        form=CompanyModelForm()    
        return render (request, 'Rest_Api/companyInfo_RestApi.html',{'form':form}) 
        
        
def CompanyInfo_RestApi_get (request) :
        if request.method=="POST":
           
            username1=request.POST['username1']
            password1=request.POST['password1']
            id=request.POST['id']
            #id=id.strip()
            auth_data1={'username':username1 , 'password':password1}
            url_auth1='http://127.0.0.1:8000/token/'
            api_auth1=requests.post(url=url_auth1, json=auth_data1)
            try:
                api_auth_res=json.loads(api_auth1.text)
            except:
               api_auth_res=None
            token1=api_auth_res['token']
            #return HttpResponse('Token :' +token)
           # print(token)    
            #token='b0557e7595f43fa60067bb895ddf8a4e6a1ece19'
            
            url_company="http://127.0.0.1:8000/api/company/"
            api_company1=requests.get(url=url_company, data={'id':id}, headers={'Authorization':f'Token {token1}'})
            try:
                api_company_res1=json.loads(api_company1.text)
                #return HttpResponse(api_company1)
                return render (request, 'Rest_Api/companyInfo_RestApiGet.html',{ 'token':token1, 'response':api_company_res1}) 
            # return HttpResponse(api_company )
            except:
              api_company_res1=None



              
             
        else: 
             
            return render (request, 'Rest_Api/companyInfo_RestApiGet.html')        



      ##  REST API END

  
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def firstApi(request):
    comment=Topic_Entry_comment.objects.filter() # from 'entry' function 
    topic=[]
    entry_id=[]
    topic_entry=[]
    commentator=[]
    comment_text=[]
    comment_id=[]

    for i in comment: # from 'entry' function
         topic.append(i.topic_entry.topic) 
         entry_id.append(i.topic_entry.id)
         topic_entry.append(i.topic_entry.text)
         commentator.append(i.commenter)
         comment_text.append(i.text) 
         comment_id.append(i.id) 
    #topic=json.dumps( topic)
    #=json.dumps( entry_id)
    #topic_entry=json.dumps( topic_entry)
   # commentator=json.dumps(commentator)
    #comment_text=json.dumps( comment_text)
    context={
            
           # "topic": topic,
            "entry_id":entry_id,
            "topic_entry":topic_entry,
           # "commentator": commentator,
            "comment":comment_text
          }

    if request.method=="POST":
        name=request.data['name']
        email=request.data['email']
        password=request.data['password']
        email1='mail@khurshed.xyz'
        password1='admin_123'
        
        if email==email1 and password==password :
            context1={
            "Name": name,
            "Email":email,
            
            #"topic": topic,
            'entry_id':entry_id,
            'topic_entry':topic_entry,
            "comment Id": comment_id,
            #' commentator': commentator,
            'comment':comment_text
                 
        }
            return Response(context1)
        else :
            return Response("You entered invalid data")

    context2={
            "Name": "Khurshed Hasan",
            "URL":"https://khurshed.xyz",
             #"topic":topic,
             "entry_id":entry_id,
            "topic_entry":topic_entry,
            #"commentator":commentator,
            "comment Id": comment_id,
            "comment":comment_text
        }
    return Response(context2)
 

def rest_call(requests):
    url='http://127.0.0.1:8000/api/company/'
    headers={'Authorization' : 'Token  23c2a954248787d2c14699a0d1a74374e2a88bfb/'}
    r=requests.get(url,headers=headers)
    #r= HttpRequest.get(url)
    print("Status code : ",r.status_code)
    response_api=r.json()
    return Response (response_api)

class CompanyViewSets (viewsets.ModelViewSet):
       queryset=Company.objects.all()
       serializer_class=CompanySerializer


def topic (request):
    topics=Topic.objects.order_by('date_added')
    #topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topic':topics}
    return render(request,'topic/topics.html',context)

@login_required
def entry (request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    #if topic.owner !=request.user:
       # raise Http404
    id_entry=[]
    entries=topic.topic_entry_set.order_by('date_added')
    zipped=''
    xyz=''
    for i in entries:
       
       id_entry= [i]
    comment_text=[]
    entry_text=[]


    entry_id=[]
    comment_id =[]
    commenter=[]
    comment=[]

    #comment=Topic_Entry_comment.objects.get(id=id_entry) # to get 01 object
    comment=Topic_Entry_comment.objects.filter() # to get multiple objects
    #comments=entries.topic_entry_comment_set.order_by('date_added')
    
    for i in comment :
       
        entry_id.append(i.topic_entry.id)
        entry_text.append(i.topic_entry.text)
        commenter.append(i.commenter)
        comment_id.append(i.id)
        comment_text.append(i.text) 
        length=len(entry_id)
        zipped=zip(entry_id,entry_text,comment_id,commenter, comment_text)
        zipped=list(zipped)
        Entry_Id=[]
        Entry_text=[]
        Comment_Id=[]
        xyz=[]
        COMMENT=[]
        COMMENT1=[]
        COMMENT2=[]
    length=len(entry_id)    
    for i in range(length):
        for j in range(i+1,length):
          if entry_id[i] ==entry_id[j] and entry_id[i] !=False:
            COMMENT1=[entry_text[i],comment_text]
            
            entry_id[j]=False
            COMMENT2.append(COMMENT1) 
         
        if entry_id[i] !=False:
            COMMENT1=[] 
            COMMENT1=[entry_text[i],(comment_text)]
           
            COMMENT2.append(COMMENT1)
            COMMENT=[entry_id[i],COMMENT2] 
           #entry_id[i] =False
            xyz.append(COMMENT)
            COMMENT1=[] 
            COMMENT2=[]

       # xyz.append(COMMENT2)
     
    #length=len(zipped)
      #comments=[comment] objects.filter()
      
    #comment=entries.topic_entry_comment_set #.order_by()
    
    context={'topic':topic,'entry_id':entry_id,'entry_text':entry_text, 'comment_id':comment_id,
    'commenter':commenter,'comment_text':comment_text,
    'entry':entries,'id_entry':id_entry,'length':length,'zipped':zipped,'xyz':xyz,'comment':comment}
    return render(request,'topic/entry.html',context)

@login_required
def new_topic(request):
    if request.method !='POST':
        form=TopicForm()

    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return redirect ('topics')   #('../topic/')

    context={'form':form}
    return render (request,'topic/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if topic.owner !=request.user:
        raise Http404
    #TopicEntry=topic.topic_entry_set.order_by('date_added')
    if request.method !='POST':
        form=EntryForm()
        

    else:
        form=EntryForm(data=request.POST)
        #topic_id=request.POST["id"]
        if form.is_valid():
            
            new_entry=form.save(commit=False)
            
            new_entry.topic=topic
            new_entry.save()
            print(new_entry)
            return redirect ('entries', topic_id) #('../../topic/11',topic_id)

    context={'form':form,'topic':topic}
    context1={'topic':topic,'form':form}
    return render (request,'topic/new_entry.html',context)
    #return render (request,'topic/test.html',context1)

# Comment
@login_required
def comment_entry(request,entry_id,topic_id):
    topic_entry=Topic_Entry.objects.get(id=entry_id)
    #TopicEntry=topic.topic_entry_set.order_by('date_added')
    
    if request.method !='POST':
        form=EntryCommentForm()
        

    else:
        form=EntryCommentForm(data=request.POST)
        #topic_id=request.POST["id"]
        if form.is_valid():
            
            new_comment=form.save(commit=False)
            
            new_comment.topic=topic_entry
            new_comment.save()
            
            return redirect ('entries',topic_id) #('../../topic/11',topic_id)

    context={'form':form,'topic':topic_entry,'topic_id':topic_id}
    context1={'topic':topic_entry,'form':form}
    return render (request,'topic/test.html',context)
    #return render (request,'topic/test.html',context1)

@login_required
def edit_entry(request,entry_id):
    entry=Topic_Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner !=request.user:
        raise Http404

    if request.method != 'POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST) 
        if form.is_valid :
            form.save()
            return redirect('entries', topic_id=topic.id) 
    context={'topic':topic,'entry':entry,'form':form}  
    return render (request,'topic/edit_entry.html', context)        

    


