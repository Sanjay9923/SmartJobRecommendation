# smart_job_recommend.py
import sqlite3

def get_jobs():
    """Fetch all jobs from the database"""
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT job_id, job_title, company, skills_required FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs

def recommend_jobs(candidate_skills):
    """Match candidate skills with job skills and recommend top jobs"""
    # Convert candidate skills into a set (lowercase, clean)
    candidate_skills = set(skill.strip().lower() for skill in candidate_skills.split(','))
    jobs = get_jobs()
    recommendations = []

    for job in jobs:
        job_id, job_title, company, skills_required = job
        job_skills = set(skill.strip().lower() for skill in skills_required.split(','))
        matched_skills = candidate_skills & job_skills  # intersection
        if job_skills:  # avoid division by zero
            score = len(matched_skills) / len(job_skills) * 100
        else:
            score = 0
        if score > 0:
            recommendations.append((job_title, company, score))

    # Sort by best match (descending order)
    recommendations.sort(key=lambda x: x[2], reverse=True)
    return recommendations[:5]  # Top 5 jobs

# Run directly (for testing or when called from Java GUI)
if __name__ == "__main__":
    candidate_skills = input("Enter your skills (comma separated): ")
    top_jobs = recommend_jobs(candidate_skills)
    print("Top Job Recommendations:")
    for job in top_jobs:
        print(f"Job: {job[0]}, Company: {job[1]}, Match: {job[2]:.2f}%")
