from ..models import SavedJob, AppliedJob
from employee.models import EmployeeProfile


def get_filtered_jobs(queryset, user, table_variant, search_term, framework_choice):
    print(user.is_authenticated)
    print(table_variant)
    if user.is_authenticated:
        queryset = filter_jobs_by_variant(queryset, user, table_variant)
        queryset = filter_jobs_by_search_term(queryset, search_term)
        queryset = filter_jobs_by_framework_choice(queryset, framework_choice)
    else:
        queryset = queryset.filter(is_active=True)
        queryset = filter_jobs_by_search_term(queryset, search_term)
        queryset = filter_jobs_by_framework_choice(queryset, framework_choice)

    return queryset


def get_company_specific_filtered_jobs(queryset, table_variant, sorting_option, search_term):
    queryset = filter_jobs_by_company_variant(queryset, table_variant)
    queryset = filter_by_sorting_option(queryset, sorting_option)
    queryset = filter_jobs_by_search_term(queryset, search_term)

    return queryset


def filter_jobs_by_variant(queryset, user, table_variant):
    if table_variant == 'All Jobs':
        return queryset.filter(is_active=True).exclude(company__user=user)
    elif table_variant == 'Saved Jobs':
        print('saved jobs')
        return filter_saved_jobs(queryset, user)
    elif table_variant == 'Applied Jobs':
        return filter_applied_jobs(queryset, user)
    return queryset


def filter_saved_jobs(queryset, user):
    employee = EmployeeProfile.objects.get(user=user)
    saved_jobs = SavedJob.objects.filter(employee=employee).select_related('job')
    saved_jobs_ids = [saved_job.job.id for saved_job in saved_jobs]
    queryset = queryset.filter(id__in=saved_jobs_ids)
    print(queryset)
    return queryset


def filter_applied_jobs(queryset, user):
    employee = EmployeeProfile.objects.get(user=user)
    applied_jobs = AppliedJob.objects.filter(employee=employee).select_related('job')
    applied_jobs_ids = [applied_job.job.id for applied_job in applied_jobs]
    queryset = queryset.filter(id__in=applied_jobs_ids)
    print(queryset)
    return queryset


def filter_jobs_by_company_variant(queryset, table_variant):
    if table_variant != 'all':
        if table_variant == 'active':
            queryset = queryset.filter(is_active=True)
        elif table_variant == 'inactive':
            queryset = queryset.filter(is_active=False)

    return queryset


def filter_by_sorting_option(queryset, sorting_option):
    if sorting_option != "None":
        if sorting_option == "Latest":
            queryset = queryset.order_by('-date_created')
        elif sorting_option == "Oldest":
            queryset = queryset.order_by('date_created')

    return queryset


def filter_jobs_by_search_term(queryset, search_term):
    if search_term is not None:
        return queryset.filter(title__icontains=search_term)
    return queryset


def filter_jobs_by_framework_choice(queryset, framework_choice):
    if framework_choice is not None:
        return queryset.filter(framework__contains=framework_choice)
    return queryset