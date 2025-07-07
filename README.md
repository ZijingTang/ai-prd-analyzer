
# AI PRD Analyzer

This is a lightweight Streamlit app that analyzes PRD/TD documents using OpenAI's GPT-4.
It helps product managers extract key changes, risks, innovation highlights, and test case suggestions.

## Files

- `ai_prd_analyzer_app_with_openai.py`: Main Streamlit app
- `prompt_templates.json`: Prompt library for different analysis tasks
- `requirements.txt`: Required packages for deployment

## Deployment

To deploy on [Streamlit Cloud](https://streamlit.io/cloud):

1. Upload this repo to GitHub
2. Go to Streamlit Cloud > "New App" > Select your repo
3. Set the entrypoint file to: `ai_prd_analyzer_app_with_openai.py`
4. Deploy and enjoy!

## How to Use

- Upload a PRD or technical document (.pdf/.docx/.txt)
- Choose an analysis type
- Provide your OpenAI API key
- Generate structured analysis results

