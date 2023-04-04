from ..models import Job
from employee.models import EmployeeProfile


def create_data_dictionary(user, job_id):
    job = Job.objects.get(pk=job_id)
    employee = EmployeeProfile.objects.get(user=user)
    data = {'employee': employee.pk, 'job': job.pk}
    return data, job


def check_if_user_can_apply(job):
    if not job.is_active or job.internal:
        return False
    return True


def check_if_job_not_created_by_user(job, user):
    """
    User cant apply to a job they created
    """
    if not job.internal:
        if job.company.user == user:
            return False
    return True
