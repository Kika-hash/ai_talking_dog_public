from openai import OpenAI
from config import config_key, config_organization


def back_end(question):
    api_key = config_key()
    api_organization = config_organization()
    client = OpenAI(api_key=api_key, organization=api_organization)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a talking dog named Baldi: green eyes, gold fur, labrador, 5 years old, from Poland, funny, stubborn, sometimes malicious, but children loves you"},
                  {"role": "user", "content": question}],
        stream=False,
    )

    return response.choices[0].message.content