from ..models import SavedJob, AppliedJob
from employee.models import EmployeeProfile


def get_filtered_jobs(qs, user, table_variant, search_term, framework_choice, apply_type_chosen):
    if user.is_authenticated:
        qs = filter_jobs_by_variant(qs, user, table_variant)
        qs = filter_jobs_by_search_term(qs, search_term)
        qs = filter_jobs_by_framework_choice(qs, framework_choice)
        qs = filter_jobs_by_apply_type_choice(qs, apply_type_chosen)
    else:
        qs = qs.filter(is_active=True)
        qs = filter_jobs_by_search_term(qs, search_term)
        qs = filter_jobs_by_framework_choice(qs, framework_choice)
        qs = filter_jobs_by_apply_type_choice(qs, apply_type_chosen)

    return qs


def get_company_specific_filtered_jobs(qs, table_variant, sorting_option, search_term):
    qs = filter_jobs_by_company_variant(qs, table_variant)
    qs = filter_by_sorting_option(qs, sorting_option)
    qs = filter_jobs_by_search_term(qs, search_term)

    return qs


def filter_jobs_by_variant(qs, user, table_variant):
    if table_variant == 'All Jobs':
        return qs.filter(is_active=True).exclude(company__user=user)
    elif table_variant == 'Saved Jobs':
        return filter_saved_jobs(qs, user)
    elif table_variant == 'Applied Jobs':
        return filter_applied_jobs(qs, user)
    return qs


def filter_saved_jobs(qs, user):
    employee = EmployeeProfile.objects.get(user=user)
    saved_jobs = SavedJob.objects.filter(employee=employee).select_related('job')
    saved_jobs_ids = [saved_job.job.id for saved_job in saved_jobs]
    qs = qs.filter(id__in=saved_jobs_ids)
    return qs


def filter_applied_jobs(qs, user):
    employee = EmployeeProfile.objects.get(user=user)
    applied_jobs = AppliedJob.objects.filter(employee=employee).select_related('job')
    applied_jobs_ids = [applied_job.job.id for applied_job in applied_jobs]
    qs = qs.filter(id__in=applied_jobs_ids)
    return qs


def filter_jobs_by_company_variant(qs, table_variant):
    if table_variant != 'all':
        if table_variant == 'active':
            qs = qs.filter(is_active=True)
        elif table_variant == 'inactive':
            qs = qs.filter(is_active=False)

    return qs


def filter_by_sorting_option(qs, sorting_option):
    if sorting_option != "None":
        if sorting_option == "Latest":
            qs = qs.order_by('-date_created')
        elif sorting_option == "Oldest":
            qs = qs.order_by('date_created')

    return qs


def filter_jobs_by_search_term(qs, search_term):
    if search_term is not None:
        return qs.filter(title__icontains=search_term)
    return qs


def filter_jobs_by_framework_choice(qs, framework_choice):
    if framework_choice is not None:
        return qs.filter(framework__contains=framework_choice)
    return qs


def filter_jobs_by_apply_type_choice(qs, apply_type_chosen):
    if apply_type_chosen == "Easy Apply":
        qs = qs.filter(internal=False)
    return qs
