from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employee.models import EmployeeProfile
from company.models import CompanyProfile



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_if_profile_complete(request):
    user = request.user
    data = {}
    
    employee_profile = EmployeeProfile.objects.get(user=user)
    if any(field == '' or field is None for field in employee_profile.__dict__.values() if field != employee_profile.profile_picture):
        data['employee_profile_complete'] =  False
    else: 
        data['employee_profile_complete'] =  True
    
    company = CompanyProfile.objects.get(user=user)
    if any(field == '' or field is None for field in company.__dict__.values() if field != company.company_logo):
        data['company_profile_complete'] =  False
    else: 
        data['company_profile_complete'] =  True
    
    return Response(data)
    
    
    




