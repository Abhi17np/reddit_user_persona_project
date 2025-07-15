## Setup & Execution Instructions

### 1. Clone the repository

git clone https://github.com/Abhi17np/reddit_user_persona_project.git

cd reddit_user_persona_project

### 2. Install dependencies

pip install -r requirements.txt

### 3. Create a `.env` file in the project root

This file stores your secret API keys required to run the project securely.  
It is **not committed to GitHub** for safety.

#### Required keys inside `.env`:
Refer to the .env.example

### 4. Run the script
python main.py

### 5. Enter a Reddit username or profile URL when prompted
Enter Reddit profile URL or username: https://www.reddit.com/user/kojied/

### 6. Output
The generated user persona will be saved in the output/ folder as:

output/user_persona_<username>.txt
