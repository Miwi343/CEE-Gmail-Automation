# Omnifo: Automated News Extraction and Summarization for CEE

## Description:
The Omnifo project is designed to help the Center for Emerging Economies (CEE) efficiently manage the influx of information from various newsletters. By automating the extraction and summarization of relevant news from Gmail newsletters, Omnifo enables CEE employees to quickly digest important news structured by country and topic.

## Setup:
1. Clone the Repository Locally
```
git clone https://github.com/your-username/omnifo.git
cd omnifo
```
2. Set Up the Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
```
3. Install Requirements
```
pip install -r requirements.txt
```
4. Set Up the .env File
Copy the contents of .env-example to a new file named .env.
Obtain your OpenAI API key from OpenAI.
Add your OPENAI_API_KEY to the .env file.
Example .env File
```
OPENAI_API_KEY=your_openai_api_key
```
6. Run main.py
```
python main.py
```

## How to Contribute:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.

## Acknowledgements:
Alex de Roos for initially developing the Gmail webscraper.
Mihir Kulshreshtha for creating this repository.
Ken Stibler for advising this project.
