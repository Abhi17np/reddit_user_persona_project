import os
from reddit_scraper import scrape_user_content
from persona_builder import build_prompt, generate_persona

def clean_username(url_or_name):
    if url_or_name.startswith("http"):
        return url_or_name.strip("/").split("/")[-1]
    return url_or_name.strip()

if __name__ == "__main__":
    print("📘 Reddit User Persona Generator")
    input_url = input("Enter Reddit profile URL or username: ")
    username = clean_username(input_url)

    print(f"🔍 Extracted username: u/{username}")
    print("📥 Fetching Reddit content...")

    texts = scrape_user_content(username)

    if not texts:
        print("❌ No data found. Exiting.")
        exit()

    print("🧠 Building prompt and generating persona...")
    prompt = build_prompt(username, texts)
    persona = generate_persona(prompt)

    output_path = f"output/user_persona_{username}.txt"
    os.makedirs("output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona for u/{username} saved to: {output_path}")
