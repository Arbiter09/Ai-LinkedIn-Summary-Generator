from llm_helper import llm
from few_shot import FewShotResumes

few_shot = FewShotResumes()

def generate_resume(role, industry, skills, achievements, certifications, education, language="English"):
    """
    Generate a professional resume or summary based on the provided details.

    Args:
        role (str): Target role for the resume.
        industry (str): Industry of interest.
        skills (list): List of technical and soft skills.
        achievements (list): List of key achievements.
        certifications (list): List of certifications.
        education (dict): Educational background with degree, institution, and graduation year.
        language (str): Language for the resume. Default is English.

    Returns:
        str: Generated resume or summary.
    """
    prompt = get_prompt(role, industry, skills, achievements, certifications, education, language)
    response = llm.invoke(prompt)
    return response.content

def get_prompt(role, industry, skills, achievements, certifications, education, language):
    """
    Construct the prompt for the LLM to generate a resume or summary.

    Args:
        role (str): Target role.
        industry (str): Industry of interest.
        skills (list): List of skills.
        achievements (list): List of achievements.
        certifications (list): List of certifications.
        education (dict): Educational background.
        language (str): Language for the resume.

    Returns:
        str: Formatted prompt for LLM.
    """
    prompt = f'''
    Generate a professional LinkedIn profile summary or resume snippet based on the following details. No preamble.

    1) Target Role: {role}
    2) Industry: {industry}
    3) Skills: {', '.join(skills)}
    4) Achievements: {', '.join(achievements)}
    5) Certifications: {', '.join(certifications)}
    6) Education: Degree: {education['degree']}, Institution: {education['institution']}, Graduation Year: {education['graduation_year']}
    7) Language: {language}

    If Language is Hinglish, use a mix of Hindi and English, but write the output in English script.
    '''

    examples = few_shot.get_filtered_resumes(role, industry, skills)

    if len(examples) > 0:
        prompt += "\n\n8) Use the writing style as per the following examples:"

    for i, example in enumerate(examples):
        example_text = example.get('text', '')
        prompt += f'\n\nExample {i+1}:\n\n{example_text}'

        if i == 1:  # Use max two examples
            break

    return prompt

if __name__ == "__main__":
    # Example inputs for resume generation
    role = "Data Scientist"
    industry = "Technology"
    skills = ["Python", "Machine Learning", "Data Analysis"]
    achievements = [
        "Developed a machine learning model that increased accuracy by 20%",
        "Led a team to deploy a big data pipeline, reducing processing time by 30%",
        "Published a research paper in a top-tier journal"
    ]
    certifications = ["AWS Certified Machine Learning Specialist", "Certified Data Scientist (CDS)"]
    education = {
        "degree": "Master's in Computer Science",
        "institution": "University of XYZ",
        "graduation_year": 2018
    }

    print(generate_resume(role, industry, skills, achievements, certifications, education))
