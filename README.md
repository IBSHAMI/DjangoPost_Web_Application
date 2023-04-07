# DjangoPost

DjangoPost is a comprehensive job board application that allows users to sign in or sign up and engage in various job-related activities. As an employee, you can complete your profile, upload your resume, and apply for jobs. As a company, you can create a company profile, post jobs, manage job postings, and review applicants. The application features an easy apply option for jobs posted by company users and displays scraped job postings as well.

## Features

- User authentication (Sign in/Sign up)
- Employee profile creation and resume uploads
- Company profile creation and job postings management
- Job search and filtering
- Save jobs for later viewing
- Apply for jobs and check application status
- Company management of job applicants (download resumes or reject applications)
- Display scraped job postings from external sources
- Easy apply feature for company-posted jobs

## Tech Stack

### Frontend

1. Vue.js
2. Bootstrap

### Backend

1. Python
2. Django
3. Django REST framework
4. Celery
5. AWS S3 Buckets
6. Selenium

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Node.js
- Python
- Django

### Installation

1. Clone the repository

git clone https://github.com/IBSHAMI/DjangoPost_Web_Application.git

2. Navigate to the project directory

```

cd DjangoPost_Web_Application

```

3. Install frontend dependencies

```
cd frontend
npm install
```

4. Install backend dependencies

```

cd backend
pip install -r requirements.txt

```

### Running the Application

1. Start the frontend development server
```
cd frontend
npm run dev
```
2. Start the backend development server

```
cd backend
python manage.py runserver
```

3. Access the application at `http://127.0.0.1:5173/`

## Contributing

Contributions are welcome! Feel free to submit issues or create pull requests for new features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Vue.js](https://vuejs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/)
- [AWS S3 Buckets](https://aws.amazon.com/s3/)
- [Selenium](https://www.selenium.dev/)
