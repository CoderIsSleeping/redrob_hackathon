from agents.jd_agents import JDAgent

jd = """
We are looking for a Backend Engineer.

Requirements:

- 3+ years experience
- Strong Python
- REST APIs
- Docker
- AWS
- Production systems

Nice to Have

- Kafka
- Spark

Must have excellent communication skills.
"""

agent = JDAgent()

rubric = agent.analyse(jd)

# Replace only the old pprint(...) with this

print("=" * 60)
print("ROLE")
print("=" * 60)
print(rubric.role)

print("\nEXPERIENCE")
print(rubric.experience)

print("\nREQUIRED CAPABILITIES")
for c in rubric.required_capabilities:
    print(f"- {c.name}")
    print(f"  Importance : {c.importance}")
    print(f"  Reason     : {c.reason}")

print("\nPREFERRED CAPABILITIES")
for c in rubric.preferred_capabilities:
    print(f"- {c.name}")
    print(f"  Importance : {c.importance}")
    print(f"  Reason     : {c.reason}")

print("\nBEHAVIORAL TRAITS")
for b in rubric.behavioral_traits:
    print(f"- {b.name}")
    print(f"  Importance : {b.importance}")
    print(f"  Reason     : {b.reason}")

print("\nSEARCH QUERY")
print(rubric.search_query)

print("\nSUMMARY")
print(rubric.summary)