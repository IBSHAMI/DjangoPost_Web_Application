from celery import shared_task

from .models import Job
from .scraper import get_jobs_data


@shared_task(name='test')
def test():
    print('test')


@shared_task(name='scrape_jobs_data')
def scrape_jobs_data(job_title, location, num_pages):
    # get jobs data from indeed
    jobs_data = get_jobs_data(job_title, location, num_pages)
    # create jobs from the data that we got
    Job.objects.create_jobs(jobs_data, location)
