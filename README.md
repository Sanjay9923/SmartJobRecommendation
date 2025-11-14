# Smart Job Recommendation System
## Overview

The Smart Job Recommendation System is a machine-learning powered application that helps match candidates with suitable job opportunities. It compares resume content with job descriptions using NLP methods and provides a list of recommended job roles based on similarity scores.
The system offers a simple web interface where users can upload resumes and instantly view personalized job matches.

## Features

- **Skill-Based Job Matching**: Matches user skills against available jobs using string comparison and scoring logic.
   
- **SQLite Database Integration**: Stores job listings with attributes like job title, company, and required skills.
  
- **Top Recommendations**: Displays the top five best-matched jobs ranked by match percentage.
 
- **Easy to Extend**: Can be upgraded to use NLP, machine learning models, or external APIs (LinkedIn, Indeed, etc.).  


## How It Works

1. The program reads all available jobs from the SQLite database (jobs.db).
   
2. It accepts a list of skills entered by the user (e.g., Python, Flask, SQL).
 
3. Each job’s required skills are compared to the user’s skills.
 
4. A match score (in percentage) is calculated based on overlapping skills.
 
5. The system outputs the *top 5 job recommendations* sorted by match score.
   

## Tech Stack
**Frontend**: HTML, CSS

**Backend**: Python (Flask Framework)

**Database**: SQLite (jobs.db)

**Machine Learning / NLP**: scikit-learn (TF-IDF, Cosine Similarity), Pandas

**Libraries / Tools**: numpy, sqlite3, Flask,Jinja2


## Installation & Setup

1.**Clone the Repository**

git clone https://github.com/Sanjay9923/SmartJobRecommendation.git
cd SmartJobRecommendation

2.**Set Up the Environment**

Make sure Python 3 is installed.

Create and activate a virtual environment (recommended):

python -m venv venv


Windows

venv\Scripts\activate

Install required libraries:

pip install -r requirements.txt

3.**Prepare the Database**

This project uses SQLite for storing job listings.

Run the database setup script:

python create_jobs_db.py


This creates:

jobs.db


with sample job entries, including:

job_title

company

skills_required

If you want to manually create the table instead, use:

CREATE TABLE jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    skills_required TEXT
);


Insert sample jobs:

INSERT INTO jobs (job_title, company, skills_required)
VALUES
('Python Developer', 'Google', 'python, flask, sql'),
('Data Analyst', 'TCS', 'python, excel, sql'),
('Machine Learning Engineer', 'Amazon', 'python, ml, numpy, pandas');

4.**Run the Application (Flask Server)**

Start the job recommendation system:

python app.py

5.**Use the System**

Open your browser and go to:

http://127.0.0.1:5000/


Upload your resume or enter your skills to receive job recommendations.

Example input:

Enter your skills (comma separated): Python, Flask, SQL


Example output:

Top Job Recommendations:
Job: Python Developer — Google — Match: 100%
Job: Data Analyst — TCS — Match: 65%


## Project Structure
SmartJobRecommendation/
│
├── app.py # Main Flask application
├── create_jobs_db.py        # Script to create SQLite job database
│

├── templates/               # HTML templates
│   └── index.html           # Resume upload / skill input page
│

├── static/                  # CSS / JS / Images
│   └── css/style.css
│
└── jobs.db                  # Auto-generated SQLite database


## System Architecture

User Input (Resume / Skills)
          ↓
Flask Backend
          ↓
NLP Text Cleaning & Preprocessing
          ↓
TF-IDF Vectorization
          ↓
Cosine Similarity Scoring
          ↓
Recommendation Engine (Ranking)
          ↓
SQLite Database (jobs.db)
          ↓
Top Job Recommendations Display


## Future Enhancements

Add a Flask or Django web interface for easier user interaction.

Include resume parsing and NLP-based skill extraction.

Integrate APIs for real-time job listings.

Add user authentication and job application tracking.


## Project Contributor

**Sanjay.s** — Developer and Project Lead 
Contributions are welcome. Feel free to submit pull requests or suggest improvements.


## License

This project is open-source and available under the MIT License.


