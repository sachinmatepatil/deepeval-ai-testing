from openai import OpenAI
from difflib import unified_diff
import os

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# Define the prompt
prompt = "Explain what API testing is in one short paragraph."

# Function to get LLM response with specific temperature
def get_response(temp=0.9):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=temp,
        top_p=1.0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Get two responses with same prompt and temperature
response1 = get_response()
response2 = get_response()

# Print the outputs
print("\n🧪 Output 1:\n", response1)
print("\n🧪 Output 2:\n", response2)

# Compare and show differences
print("\n🔍 Differences:\n")
diff = unified_diff(
    response1.splitlines(),
    response2.splitlines(),
    fromfile='Output1',
    tofile='Output2',
    lineterm=''
)

for line in diff:
    print(line)
