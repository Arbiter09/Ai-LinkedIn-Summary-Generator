import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def process_resumes(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8') as file:
        resumes = json.load(file)
        enriched_resumes = []

        for resume in resumes:
            try:
                metadata = extract_metadata(resume)
                resume_with_metadata = resume | metadata
                enriched_resumes.append(resume_with_metadata)
            except OutputParserException as e:
                print(f"Error processing resume: {resume.get('name', 'Unknown')}. Details: {str(e)}")

    unified_skills = get_unified_skills(enriched_resumes)
    for resume in enriched_resumes:
        current_skills = resume.get('skills', [])
        new_skills = {unified_skills.get(skill, skill) for skill in current_skills}
        resume['skills'] = list(new_skills)

    if processed_file_path:
        with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
            json.dump(enriched_resumes, outfile, indent=4)

def preprocess_resume(resume):
    return {
        "name": resume.get("name", ""),
        "industry": resume.get("industry", ""),
        "key_achievements": resume.get("key_achievements", [])[:5]  # Limit to 5 achievements
    }

def extract_metadata(resume):
    processed_resume = preprocess_resume(resume)
    template = '''
    You are given a resume object. Extract the following metadata:
    - achievement_count: Number of key achievements (integer).
    - career_domain: The primary career domain (string).
    - soft_skills: List of inferred soft skills (array of strings).

    Return only a valid JSON object with exactly these keys. No additional text, code, or explanations.

    Resume:
    {resume}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"resume": json.dumps(processed_resume)})

    try:
        raw_response = response.content.strip()
        json_parser = JsonOutputParser()
        res = json_parser.parse(raw_response)
        return res
    except OutputParserException:
        print(f"Invalid JSON output received: {response.content}")
        return {
            "achievement_count": len(processed_resume.get("key_achievements", [])),
            "career_domain": processed_resume.get("industry", "Unknown"),
            "soft_skills": []
        }

def get_unified_skills(resumes_with_metadata):
    unique_skills = set()

    for resume in resumes_with_metadata:
        unique_skills.update(resume.get('skills', []))

    unique_skills_list = ','.join(unique_skills)

    template = '''I will give you a list of skills. Unify similar skills into categories:
    1. Merge similar skills (e.g., "Python Programming" -> "Python").
    2. Return only a JSON object where the original skill is the key and the unified skill is the value. No additional text, code, or explanations.

    Skills:
    {skills}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"skills": unique_skills_list})

    try:
        raw_response = response.content.strip()
        json_parser = JsonOutputParser()
        res = json_parser.parse(raw_response)
        return res
    except OutputParserException:
        print(f"Invalid JSON output received: {response.content}")
        return {}

if __name__ == "__main__":
    process_resumes("data/raw_resumes.json", "data/processed_resumes.json")
