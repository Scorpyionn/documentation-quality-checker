📝 Documentation Quality Checker

An Automated Documentation Analysis & Quality Assurance Tool

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Project-Under%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

📌 Overview

Documentation Quality Checker is a Python-based application designed to help technical writers and developers improve the quality, consistency, and readability of technical documentation.

The project focuses on automating repetitive documentation review tasks, reducing manual effort, and identifying common writing and formatting issues.

Users can upload Markdown or text documents and receive an automated quality analysis report highlighting potential issues along with suggestions for improvement.

The goal is to make documentation reviews faster, more consistent, and more reliable while keeping human review an essential part of the publishing process.

🎯 Problem Statement

Technical documentation plays an important role in helping users understand software products and technical workflows.

However, reviewing documentation manually can be time-consuming. Common issues include:

- Repeated words and spelling mistakes.
- Grammar and sentence construction errors.
- Inconsistent technical terminology.
- Broken hyperlinks.
- Poor sentence readability.
- Missing or incorrectly structured headings.

This project aims to automate these repetitive checks through a simple and accessible interface.

🚀 Key Features

1. Document Upload
- Upload Markdown (`.md`) and text (`.txt`) files.
- Preview document content before analysis.

2. Repeated Word Detection
- Identifies accidentally repeated words.
- Provides suggestions for improving the text.

3. Grammar and Spelling Analysis
- Uses LanguageTool for grammar and spelling checks.
- Identifies potential writing mistakes.
- Provides suggested corrections.

4. Terminology Validation
- Checks technical terminology against a predefined dictionary.
- Identifies inconsistent naming conventions.
- Suggests standard terminology.

5. Broken Link Detection
- Extracts hyperlinks from Markdown documents.
- Checks link accessibility.
- Identifies potentially broken links.

6. Sentence Readability
- Identifies excessively long sentences.
- Suggests breaking complex sentences into shorter ones.

7. Documentation Structure Validation
- Checks for missing Markdown headings.

🛠️ Technology Stack

| Technology            | Purpose                           |
|                       |                                   |
| Python                | Core application logic            |
| Streamlit             | Interactive web interface         |
| Regular Expressions   | Text pattern detection            |
| LanguageTool          | Grammar and spelling analysis     |
| Requests              | HTTP link validation              |
| Markdown              | Structured documentation          |
| Git & GitHub          | Version control and collaboration |

📂 Project Structure

```text
Documentation-Quality-Checker/
│
├── checks/
│   ├── __init__.py
│   ├── quality_checker.py
│   ├── grammar_check.py
│   └── link_checker.py
│
├── samples/
│   └── sample_document.md
│
├── reports/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

Additional validation modules will be added as development progresses.

⚙️ Installation and Setup

Prerequisites

- Python 3.10 or later.
- Java runtime for the local LanguageTool engine.
- Git.
- Visual Studio Code (recommended).

Step 1: Clone the Repository

```bash
git clone https://github.com/Scorpyionn/documentation-quality-checker.git
```

Step 2: Navigate to the Project

```bash
cd documentation-quality-checker
```

Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Step 4: Activate the Environment

For Windows:

```bash
.venv\Scripts\activate
```

Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Step 6: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Default local address:

```text
http://localhost:8501
```

🔍 How It Works

The application follows a simple workflow:

1. User uploads a Markdown or text document.
2. The application extracts the document content.
3. The analysis engine processes the text.
4. Different validation modules identify potential issues.
5. Results are categorised into errors and warnings.
6. Users receive suggestions to improve documentation quality.

📊 Sample Analysis

The application has been tested using sample Markdown documents containing intentional documentation issues.

Example results:

| Validation              |Detected Issue           |
|                         |                         |
| Repeated Words          | application application |
| Terminology             | Github → GitHub         |
| Terminology             | Gen AI → GenAI          |
| Grammar                 | Incorrect verb usage    |
| Broken Links            | Inaccessible URL        |

🔮 Future Improvements

The project is actively being developed. Planned improvements include:

- Advanced Markdown validation.
- Custom terminology dictionaries.
- Documentation style-guide enforcement.
- Downloadable quality analysis reports.
- Documentation quality scoring.
- AI-assisted documentation suggestions.
- Semantic search and document retrieval.
- Git-based documentation quality checks.

🔐 Accuracy and Human Review

Automated checking tools can occasionally produce false positives or miss context-specific errors.

Therefore, the application is intended to assist technical writers rather than replace human reviewers.

All suggested changes should be reviewed before being incorporated into published documentation.

👨‍💻 Author

Raj Chaudhari

B.Tech – Computer Science and Engineering  
Specialization:- Artificial Intelligence and Analytics

Interests:
- Generative AI
- Technical Writing
- Python Automation
- Machine Learning
- Documentation Engineering

Built as a practical exploration of Python automation, technical writing, and documentation quality assurance.
