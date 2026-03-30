# AI Bug and code reviewer

A web app that uses NVIDIA Nemotron 3 Super AI to analyze your code and give detailed feedback on bugs, security issues, code quality, and improvements.

## Features

- Detects bugs and errors
- Identifies security vulnerabilities like SQL injection and hardcoded passwords
- Reviews code quality and style
- Gives actionable suggestions
- Supports Python, JavaScript, Java, C++, C#, TypeScript
- Overall score out of 10

## Tech Stack

- Python
- Streamlit
- NVIDIA Nemotron 3 Super via OpenRouter API
- python-dotenv
- requests

## How to Run

1. Clone the repository
```
   git clone https://github.com/m3nddd/ai-code-reviewer.git
   cd ai-code-reviewer
```

2. Install dependencies
```
   pip install -r requirements.txt
```

3. Create a `.env` file in the root folder
```
   OPENROUTER_API_KEY=your_api_key_here
```

4. Run the app
```
   python -m streamlit run frontend/ui.py
```

## Project Structure
```
ai-code-reviewer/
├── app/
│   └── analyzer.py
├── frontend/
│   └── ui.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```


## Note
Don't forget to replace API_KEY = "OPENROUTER_API_KEY" in analyzer.py file with your real API KEY