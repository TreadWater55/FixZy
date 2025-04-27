import os
import json
import openai
import difflib

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_issues(category_filter=None):
    with open("data/diy_issues.json", "r") as f:
        data = json.load(f)
    return data

def find_relevant_issues(user_input, category_filter=None):
    issues = load_issues(category_filter)
    scored_issues = []

    for issue in issues:
        problem = issue["problem"]
        match_score = difflib.SequenceMatcher(None, user_input.lower(), problem.lower()).ratio()
        if match_score > 0.4:
            scored_issues.append((match_score, issue))

    scored_issues.sort(reverse=True, key=lambda x: x[0])

    return [issue for _, issue in scored_issues[:3]]

def synthesize_response(user_input, category_filter=None):
    relevant_issues = find_relevant_issues(user_input, category_filter)

    if relevant_issues:
        return relevant_issues[0]

    prompt = f"""
You're a professional home repair expert working inside an app called Fixzy.

A user describes this issue:

"{user_input}"

Please suggest:
- **Likely Cause** (1-2 sentences)
- **Recommended Fix** (1-3 sentences)
- **Tools Needed** (comma-separated list)
- **Materials Needed** (comma-separated list)
- **Estimated Time** (short, like '30 minutes')
- **Difficulty** (Easy, Medium, Hard)

Respond structured like:

Likely Cause: [your answer]
Recommended Fix: [your answer]
Tools Needed: [your answer]
Materials Needed: [your answer]
Estimated Time: [your answer]
Difficulty: [your answer]

Keep it professional and short.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return "Fixzy Suggestions\n" + response.choices[0].message["content"]