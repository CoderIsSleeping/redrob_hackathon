"""
JD Intelligence Agent

Reads a Job Description and converts it into
a structured hiring rubric using Gemini.
"""

import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from models.schemas import HiringRubric


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


SYSTEM_PROMPT = """
You are an expert technical recruiter.

Your task is to convert a software engineering job description into a structured hiring rubric.

Return ONLY valid JSON.

Schema:

{
    "role":"",

    "experience":{
        "minimum":0,
        "preferred":0,
        "reason":""
    },

    "required_capabilities":[
        {
            "name":"",
            "importance":0,
            "reason":""
        }
    ],

    "preferred_capabilities":[
        {
            "name":"",
            "importance":0,
            "reason":""
        }
    ],

    "behavioral_traits":[
        {
            "name":"",
            "importance":0,
            "reason":""
        }
    ],

    "negative_signals":[],

    "search_query":"",

    "summary":""
}

Use ONLY these capability names:

backend
frontend
ai_ml
data_engineering
cloud
devops
leadership
product
database
mobile
security

Behavioral traits must ONLY be one of:

communication
leadership
ownership
teamwork
adaptability
problem_solving
learning
mentoring

Importance Scale

10 = absolutely mandatory

8 = very important

6 = important

4 = useful

2 = optional

Rules

- Infer capability from technologies.
- Explain every capability with a short reason.
- Keep reasons under 20 words.
- Generate a concise semantic search query using only important technical keywords.
- Return ONLY JSON.

You are an experienced technical recruiter.

Your job is to analyse a software engineering job description.

Return ONLY valid JSON.

Schema:

{
    "role": "",

    "experience": {
        "minimum": 0,
        "preferred": 0
    },

    "required_capabilities":[
    {
    "name":"",
    "importance":0
    }
    ]

    "preferred_capabilities":[
    {
    "name":"",
    "importance":0
    }
    ]

    "behavioral_traits": [],

    "negative_signals": [],

    "summary": ""
}

Rules:

Use ONLY these capability names:

backend
frontend
ai_ml
data_engineering
cloud
devops
leadership
product
database
mobile
security



Do not invent new capability names.

Additional Rules

- Infer capabilities from technologies rather than copying technology names.
- Do not repeat the same capability twice.
- Do not include technologies inside capability names.
- Keep every reason under 20 words.
- Generate a search query using only important technical keywords.
- Ignore company names.
- Ignore salary information.
- Ignore location.
- Ignore visa or sponsorship requirements.
- Ignore generic HR statements.
- Return ONLY valid JSON.

Return ONLY JSON.
"""


class JDAgent:

    def __init__(self):

        self.model = model

    def analyse(self, job_description):

        prompt = f"""
{SYSTEM_PROMPT}

Job Description:

{job_description}
"""

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        data = json.loads(text)

        return HiringRubric.model_validate(data)