# Type of jobs that a company can post
JOB_TYPE_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Freelance', 'Freelance'),
    ('Internship', 'Internship'),
    ('Temporary', 'Temporary'),
)

# Language choices for a job
JOB_LANGUAGE_CHOICES = (
    ('English', 'English'),
    ('Arabic', 'Arabic'),
    ('Malay', 'Malay'),
    ('Frensh', 'Frensh'),
    ('Spanish', 'Spanish'),
)

# Experience choices for a job
JOB_EXPERIENCE_CHOICES = (
    ('Fresh Graduate', 'Fresh Graduate'),
    ('1-2 Years', '1-2 Years'),
    ('2-3 Years', '2-3 Years'),
    ('3-5 Years', '3-5 Years'),
    ('5-10 Years', '5-10 Years'),
    ('10+ Years', '10+ Years'),
)

# Location choices for a job
JOB_LOCATION_CHOICES = (
    ('Malaysia', 'Malaysia'),
    ('Singapore', 'Singapore'),
    ('Indonesia', 'Indonesia'),
    ('USA', 'USA'),
    ('UK', 'UK'),
    ('Australia', 'Australia'),
    ('Canada', 'Canada'),
)

# salary choices for a job
JOB_SALARY_CHOICES = (
    ('1000-2000', '1000-2000'),
    ('2000-3000', '2000-3000'),
    ('3000-4000', '3000-4000'),
    ('4000-5000', '4000-5000'),
    ('+5000', '+5000'),
)

# framework choices for a job
FRAMEWORK_CHOICES = [
    # Backend frameworks
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('FastAPI', 'FastAPI'),

    # Frontend frameworks
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Vue.js', 'Vue.js'),
    ('Svelte', 'Svelte'),


    ('Other', 'Other'),
]



