from django.http import HttpResponse
from django.shortcuts import render
from . api_response import API_Response

from django.views import View 
from plotly.graph_objs import Bar
from plotly import offline

def API_RESPONSE(request):
     response_dict= API_Response()
     repo_dict=response_dict['items']
     repo_zero=repo_dict[0]
     repo_zero_keys=len(repo_zero)
     repo_zero_keynames=repo_zero.keys()
     repo_names, stars=[], []
     
     for i in repo_dict :

         repo_names.append(i['name'])
         stars.append(i['stargazers_count'])
     data=[ {
          'type':'bar',
          'x':repo_names,
          'y':stars,
          'marker':{ 'color':'rgb(60,60,60)',
                     'line':{'width':1.5,'color':'blue'}

          }, 'opacity':.8,
     }]
     my_layout={
          'title':'Most-Starred Python Project on Github',
          'titlefont':{'size':20},
          'xaxis':{'title':'Repository','titlefont':{'size':20},
          'tickfont':{'size':14}},
          'yaxis':{'title':'Stars','titlefont':{'size':20},
          'tickfont':{'size':14},},}

     
     fig= {'data': data, 'layout':my_layout}
     offline.plot(fig, filename='API_Response/api_git.html')


     return render (request, 'API_Response/api_git.html', {'response_dict':response_dict,'repo_dict':repo_dict,
     
     'repo_zero':repo_zero,'repo_zero_keys':repo_zero_keys,'repo_zero_keynames':repo_zero_keynames,'fig':fig})
