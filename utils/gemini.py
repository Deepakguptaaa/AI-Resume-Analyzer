from google import genai
from dotenv import load_dotenv
import os

# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# -----------------------------
# Resume Analysis
# -----------------------------

def analyze_resume(resume_text):

    prompt = f"""
You are a Senior Technical Recruiter and ATS Resume Expert.

Analyze the following resume professionally.

Return ONLY in this format.

# ATS Score
85

# Strengths
- Point 1
- Point 2

# Weaknesses
- Point 1
- Point 2

# Technical Skills Found
- Skill
- Skill

# Missing Skills
- Skill
- Skill

# Certifications Recommended
- Certification
- Certification

# Suggested Projects
- Project
- Project

# Resume Improvement Suggestions
- Suggestion
- Suggestion

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Job Description Match
# -----------------------------

def analyze_job_match(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Expert.

Compare this resume with the job description.

Return ONLY in this format.

# Match Score
85

# Matching Skills
- Skill
- Skill

# Missing Skills
- Skill
- Skill

# Resume Improvements
- Improvement
- Improvement

# ATS Optimization Tips
- Tip
- Tip

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# -----------------------------
# Resume Optimizer
# -----------------------------

def optimize_resume(resume_text):

    prompt = f"""
You are an expert Resume Writer and ATS Specialist.

Rewrite the following resume professionally.

Rules:
- Keep all information truthful.
- Improve grammar and wording.
- Use strong action verbs.
- Make bullet points ATS-friendly.
- Highlight measurable achievements where possible.
- Maintain a professional tone.

Return ONLY the optimized resume.

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# -----------------------------
# Cover Letter Generator
# -----------------------------

def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are an experienced HR Recruiter.

Using the resume and job description below, write a professional cover letter.

Requirements:
- Professional tone
- Around 300–400 words
- Mention the candidate's strengths
- Match the job requirements
- End with a polite closing

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text