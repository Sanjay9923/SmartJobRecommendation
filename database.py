# create_jobs_db.py
import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create jobs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    skills_required TEXT
);
""")

# Insert sample jobs
jobs = [
    ("Python Developer", "Google", "python, flask, sql"),
    ("Java Developer", "Infosys", "java, spring, sql"),
    ("Data Analyst", "TCS", "python, excel, sql"),
    ("Web Developer", "Wipro", "html, css, javascript"),
    ("Machine Learning Engineer", "Amazon", "python, ml, numpy, pandas")
]

cursor.executemany("INSERT INTO jobs (job_title, company, skills_required) VALUES (?, ?, ?)", jobs)
conn.commit()
conn.close()

print("Database created with sample jobs ✅")
