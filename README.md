# Smart Job Recommendation System
## Overview
The *Smart Job Recommendation System* helps users find suitable job opportunities based on their skill set. It matches a candidate’s provided skills with the skill requirements listed in a job database and recommends the most relevant job roles.

This system is simple, efficient, and can be integrated into larger web or desktop applications (for example, as part of a career guidance or recruitment platform).

---

## Features
- *Skill-Based Job Matching:* Matches user skills against available jobs using string comparison and scoring logic.  
- *SQLite Database Integration:* Stores job listings with attributes like job title, company, and required skills.  
- *Top Recommendations:* Displays the top five best-matched jobs ranked by match percentage.  
- *Easy to Extend:* Can be upgraded to use NLP, machine learning models, or external APIs (LinkedIn, Indeed, etc.).  

---

## How It Works
1. The program reads all available jobs from the SQLite database (jobs.db).
2. It accepts a list of skills entered by the user (e.g., Python, Flask, SQL).
3. Each job’s required skills are compared to the user’s skills.
4. A match score (in percentage) is calculated based on overlapping skills.
5. The system outputs the *top 5 job recommendations* sorted by match score.
   
## Tech Stack
*Frontend:* HTML, CSS, JavaScript  
*Backend:* Python (Flask Framework)  
*Database:* MySQL  
*Libraries/Tools:* scikit-learn, Pandas, NLTK, ## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sanjay9923/SmartJobRecommendation.git
cd SmartJobRecommendation
2. Set Up the Environment
Make sure you have Python 3 installed.

Install dependencies (if any are listed in requirements.txt):

bash
Copy code
pip install -r requirements.txt
3. Prepare the Database
Ensure your SQLite database file is named jobs.db and contains a table named jobs with the following structure:

sql
Copy code
CREATE TABLE jobs (
    job_id INTEGER PRIMARY KEY,
    job_title TEXT,
    company TEXT,
    skills_required TEXT
);
You can insert sample data like this:

sql
Copy code
INSERT INTO jobs (job_title, company, skills_required)
VALUES
('Software Engineer', 'TechCorp', 'Python, SQL, Flask'),
('Data Analyst', 'InsightAI', 'Python, Excel, Machine Learning'),
('Web Developer', 'WebWorks', 'HTML, CSS, JavaScript');
4. Run the Program
bash
Copy code
python smart_job_recommend.py
Enter your skills when prompted, separated by commas:

java
Copy code
Enter your skills (comma separated): Python, Flask, SQL
5. View Recommendations
Example output:

yaml
Copy code
Top Job Recommendations:
Job: Software Engineer, Company: TechCorp, Match: 100.00%
Job: Data Analyst, Company: InsightAI, Match: 50.00%
📊 System Flow
pgsql
Copy code
User Input → Skill Parser → Job Matching Algorithm → Top 5 Recommendations
             ↕
           jobs.db (SQLite)
💡 Future Enhancements
Add a Flask or Django web interface for easier user interaction.

Include resume parsing and NLP-based skill extraction.

Integrate APIs for real-time job listings.

Add user authentication and job application tracking.

👨‍💻 Contributors
Sanjay S. – Developer & Project Lead

📜 License
This project is released under the MIT License.dotenv, smtplib


