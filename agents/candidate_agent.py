"""
Candidate Intelligence Agent

Evaluates a candidate using
Gemini reasoning.
"""

import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from models.schemas import CandidateReport

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


SYSTEM_PROMPT = """
You are an experienced Senior Technical Recruiter.

Your task is NOT to summarize a resume.

Your task is to evaluate the candidate.

Return ONLY valid JSON.

Schema

{
    "candidate_profile":{

        "current_role":"",

        "career_stage":"",

        "primary_domain":"",

        "secondary_domains":[],

        "career_direction":""
    },

    "capabilities":[

        {

            "name":"",

            "level":"Professional | Academic | Personal Projects | Learning",

            "reason":"",

            "evidence":[]
        }

    ],

    "strengths":[],

    "risks":[],

    "growth_potential":{

        "level":"High | Medium | Low",

        "reason":""
    },

    "consistency_analysis":{

        "status":"High | Medium | Low",

        "reason":""
    },

    "summary":""
}

Rules

Allowed capability names

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

Determine

- Professional capabilities
- Learning capabilities
- Career direction
- Evidence supporting every capability

Do NOT rank the candidate.

Do NOT compare against any job description.

Return ONLY JSON.
"""


class CandidateAgent:

    def __init__(self):

        self.model = model

    def analyse(self, candidate_card, rule_evidence):

        prompt = f"""
{SYSTEM_PROMPT}

Candidate Card

{json.dumps(candidate_card, indent=2)}

Rule Engine Output

{json.dumps(rule_evidence, indent=2, default=lambda o: o.__dict__)}

"""

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        data = json.loads(text)

        return CandidateReport.model_validate(data)