# AI LinkedIn Summary Generator

## Overview

The **AI LinkedIn Summary Generator** is a Streamlit-based web application designed to simplify the process of creating professional resumes and LinkedIn summaries. Leveraging advanced AI capabilities, the tool generates tailored, polished, and industry-relevant career profiles based on user inputs such as skills, achievements, certifications, and education.

## Features

- **Interactive User Interface**: A user-friendly Streamlit interface for inputting career details.
- **LinkedIn Profile Summary**: Generates concise, professional summaries tailored for LinkedIn.
- **Full Career Overview**: Provides a detailed career summary (not a traditional resume format) highlighting key strengths, achievements, and skills.
- **Customization**: Allows users to input specific roles, industries, skills, achievements, certifications, and education.
- **Fallback Mechanism**: Ensures the tool works even when certain fields (e.g., achievements) are left blank.

## How It Works

1. **Input Details**:
   - Enter your target role, industry, skills, achievements, certifications, and education details into the form.
2. **Generate Summary**:
   - Click the "Generate Resume" button to receive:
     - A LinkedIn-compatible summary.
     - A detailed career overview.
3. **View Output**:
   - Copy the outputs directly or modify them further as needed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-resume-generator.git
   cd ai-resume-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

4. Open your browser at the URL provided by Streamlit (e.g., `http://localhost:8501`).

## Technologies Used

- **Streamlit**: For building the interactive user interface.
- **Python**: Core programming language.
- **LLM Integration**: Generates personalized summaries using advanced language models.

## Project Structure

```
.
├── main.py               # Main Streamlit app script
├── few_shot.py           # Logic for handling filtered examples
├── resume_generator.py   # Core logic for generating summaries and resumes
├── requirements.txt      # List of required Python packages
├── data/                 # Folder for storing processed data
├── README.md             # Project documentation
```

## Example Outputs

### LinkedIn Profile Summary

```
Data Scientist | Technology Innovator

Seasoned Data Scientist with expertise in Python, Machine Learning, and Data Analysis. Proven track record of driving impactful solutions and innovation.

Key Highlights:
- Won a Hackathon at Smart Hacks 2024
- Built an AI Resume Builder

Education:
- Master's in Computer Science, Stony Brook University (2024)

Excited to leverage my skills to drive growth and innovation in a forward-thinking organization.
```

###  Career Highlightss

```
Results-Driven Data Scientist with a strong background in Machine Learning and Data Analysis, leveraging Python to drive business growth and innovation in the technology industry.

Proven track record of delivering high-impact projects, including winning the prestigious Smart Hacks 2024 Hackathon and developing an AI-powered Resume Builder.

Certified in AWS Machine Learning and Data Science, with a Master's degree in Computer Science from Stony Brook University (2024).

Key strengths include:
- Machine Learning (ML) modeling and deployment
- Data Analysis and Visualization
- Python programming
- Cloud-based infrastructure (AWS)
- AI and automation

I am excited to join a dynamic team where I can apply my skills and experience to drive business success and stay at the forefront of technological advancements.
```


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or feedback, feel free to reach out!
