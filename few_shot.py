import pandas as pd
import json

class FewShotResumes:
    def __init__(self, file_path="data/processed_resumes.json"):
        self.df = None
        self.unique_roles = None
        self.load_resumes(file_path)

    def load_resumes(self, file_path):
        """
        Load and preprocess resumes from a JSON file.
        """
        with open(file_path, encoding="utf-8") as f:
            resumes = json.load(f)
            self.df = pd.json_normalize(resumes)

            # Collect unique roles and industries
            self.df['role'] = self.df['current_role']
            self.unique_roles = self.df['role'].unique().tolist()

    def get_filtered_resumes(self, role, industry, skills):
        """
        Filter resumes based on role, industry, and skills.

        Args:
            role (str): Target role.
            industry (str): Target industry.
            skills (list): List of skills to filter by.

        Returns:
            list: Filtered resumes as a list of dictionaries.
        """
        df_filtered = self.df[
            (self.df['role'] == role) &
            (self.df['industry'] == industry) &
            (self.df['skills'].apply(lambda x: any(skill in x for skill in skills)))
        ]
        return df_filtered.to_dict(orient='records')

    def get_unique_roles(self):
        """
        Get unique roles from the dataset.

        Returns:
            list: List of unique roles.
        """
        return self.unique_roles

if __name__ == "__main__":
    fs = FewShotResumes()

    # Example: Filtering resumes for the role "Data Scientist" in the "Technology" industry
    resumes = fs.get_filtered_resumes(
        role="Data Scientist",
        industry="Technology",
        skills=["Python", "Machine Learning", "Data Analysis"]
    )
    print(resumes)
