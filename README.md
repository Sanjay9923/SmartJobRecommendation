# Smart Job Recommendation System

## Overview

The Smart Job Recommendation System is a machine-learning powered application that helps match candidates with suitable job opportunities. It compares resume content with job descriptions using NLP methods and provides a list of recommended job roles based on similarity scores.
The system offers a simple web interface where users can upload resumes and instantly view personalized job matches.


## Preview (Screenshot)

### Job-Matching-Interface.png

![Screenshot (1)](https://github.com/user-attachments/assets/7e76bfcc-a07a-4f30-b217-d9ae7e047e81)


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


## Project Structure
```bash
Smart Job Recommendation/
│
├── smart_job_recommend.py     # Main Python script for recommendations
├── database.py                # Database helper functions
├── JobRecommendationGUI.java  # Java GUI version
└── jobs.db                    # SQLite database with job records
```   


## Getting Started

This project runs as a Java-based desktop application. You don’t need a web server or Python setup. Just compile and run the Java GUI file.

1.**Clone or Download the Project**
```bash
git clone https://github.com/Sanjay9923/SmartJobRecommendation.git
cd SmartJobRecommendation
```
2.**Compile the Java File**

Open CMD inside the project folder and run:
```bash
javac JobRecommendationGUI.java
```
This will generate the .class file.

3.**Run the Application**
```bash
java JobRecommendationGUI
```
The Smart Job Recommendation System window will open automatically.

4.**Enter Your Skills**

Type your skills in the input box (comma separated), for example:
```bash
Python, Java, HTML, CSS, JavaScript
```
Click Get Recommendations, and the system will show matching job roles with percentage scores.


## Technologies Used

**Frontend**: Java Swing (GUI)

**Backend**: Python (Core logic for job matching)

**Database**: SQLite (jobs.db)

**Libraries / Tools**: JDBC (database connection), sqlite-jdbc driver, sqlite3 (Python DB API), Java AWT/Swing components


## Future Improvements

- Add a Flask or Django web interface for easier user interaction.

- Include resume parsing and NLP-based skill extraction.

- Integrate APIs for real-time job listings.

- Add user authentication and job application tracking.


##  Author

Sanjay.s — Developer and Project Lead 

Contributions are welcome. Feel free to submit pull requests or suggest improvements.


## License

This project is **free to use** and does not contains any license.

