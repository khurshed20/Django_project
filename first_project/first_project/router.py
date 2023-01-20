from users.viewsets import userviewsets
from rest_framework import routers
from Rest_Api.views import CompanyViewSets
router= routers.DefaultRouter()
router.register('user', userviewsets) # 'user' => path , userviewsets => users/viewset.py/ userviewsets 
router.register('comp',CompanyViewSets) # 'company' => path , Companyviewsets => Rest_Api/views.py/ Companyviewwsets 



