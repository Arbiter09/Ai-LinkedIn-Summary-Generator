import streamlit as st
from few_shot import FewShotResumes
from resume_generator import generate_resume

# Main app layout
def main():
    st.subheader("AI Resume Generator")

    # Create columns for input fields
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    fs = FewShotResumes()
    roles = fs.get_unique_roles()

    with col1:
        # Input for Target Role
        selected_role = st.selectbox("Target Role", options=roles)

    with col2:
        # Input for Industry
        selected_industry = st.text_input("Industry", value="Technology")

    with col3:
        # Input for Skills
        selected_skills = st.text_area(
            "Skills (comma-separated)",
            value="Python, Machine Learning, Data Analysis"
        ).split(",")

    with col4:
        # Input for Achievements
        selected_achievements = st.text_area(
            "Key Achievements (comma-separated)",
            value=""
        ).split(",")

    # Input for Certifications
    certifications = st.text_area(
        "Certifications (comma-separated)",
        value="AWS Certified Machine Learning Specialist, Certified Data Scientist (CDS)"
    ).split(",")

    # Input for Education
    degree = st.text_input("Degree", value="Master's in Computer Science")
    institution = st.text_input("Institution", value="Stony Brook University")
    graduation_year = st.text_input("Graduation Year", value="2024")

    education = {
        "degree": degree,
        "institution": institution,
        "graduation_year": graduation_year
    }

    # Generate Button
    if st.button("Generate Resume"):
        resume = generate_resume(
            role=selected_role,
            industry=selected_industry,
            skills=[skill.strip() for skill in selected_skills if skill.strip()],
            achievements=[achievement.strip() for achievement in selected_achievements if achievement.strip()],
            certifications=[cert.strip() for cert in certifications if cert.strip()],
            education=education,
        )

        # Optimize output for LinkedIn summary
        summary = generate_linkedin_summary(
            role=selected_role,
            industry=selected_industry,
            skills=selected_skills,
            achievements=selected_achievements,
            education=education
        )

        st.subheader("LinkedIn Profile Summary")
        st.write(summary)

        st.subheader("Career Highlights")
        st.write(resume)

def generate_linkedin_summary(role, industry, skills, achievements, education):
    """
    Generate a concise LinkedIn summary from the provided details.

    Args:
        role (str): Target role.
        industry (str): Industry of interest.
        skills (list): List of skills.
        achievements (list): List of achievements.
        education (dict): Educational background.

    Returns:
        str: LinkedIn summary.
    """
    achievement_1 = achievements[0] if len(achievements) > 0 else "No notable achievements provided yet."
    achievement_2 = achievements[1] if len(achievements) > 1 else ""

    summary = f"""
    **{role} | {industry} Innovator**

    Seasoned {role} with expertise in {', '.join(skills)}. Proven track record of driving impactful solutions and innovation.

    **Key Highlights**:
    - {achievement_1}
    """

    if achievement_2:
        summary += f"\n    - {achievement_2}"

    summary += f"""

    **Education**:
    - {education['degree']}, {education['institution']} ({education['graduation_year']})

    Excited to leverage my skills to drive growth and innovation in a forward-thinking organization.
    """

    return summary

# Run the app
if __name__ == "__main__":
    main()
