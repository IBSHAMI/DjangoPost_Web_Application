#!/bin/sh 

celery -A DjangoPost worker --beat -l info 