from employeeapi.viewsets import EmpoloyeeViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee',EmpoloyeeViewset)