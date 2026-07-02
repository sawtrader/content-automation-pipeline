import pandas as pd
from tqdm import tqdm
import requests
import time
import os
from datetime import datetime
from generator import generate_content

def check_ollama():
    try:
        requests.get("http://localhost:11434", timeout=5)
        return True
    except:
        return False

def process_csv(input_file="sample_input.csv"):
    df = pd.read_csv(input_file)

    twitter_rows = []
    linkedin_rows = []
    email_rows = []
    blog_rows = []

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Generating content"):
        topic = str(row.get("topic", "")).strip()
        tone = str(row.get("tone", "professional")).strip()
        target_audience = str(row.get("target_audience", "general audience")).strip()
        brand_name = str(row.get("brand_name", "Brand")).strip()

        if not topic:
            continue

        content = generate_content(topic, tone, target_audience, brand_name)

        # Twitter
        twitter = content.get("twitter", {})
        twitter_rows.append({
            "Topic": topic,
            "Brand": brand_name,
            "Variant 1": twitter.get("variant_1", ""),
            "Variant 2": twitter.get("variant_2", ""),
            "Variant 3": twitter.get("variant_3", "")
        })

        # LinkedIn
        linkedin_rows.append({
            "Topic": topic,
            "Brand": brand_name,
            "Post Content": content.get("linkedin", "")
        })

        # Email
        email = content.get("email", {})
        email_rows.append({
            "Topic": topic,
            "Brand": brand_name,
            "Subject Line": email.get("subject", ""),
            "Preview Text": email.get("preview", "")
        })

        # Blog titles
        titles = content.get("blog_titles", [])
        while len(titles) < 5:
            titles.append("")
        blog_rows.append({
            "Topic": topic,
            "Brand": brand_name,
            "Title 1": titles[0],
            "Title 2": titles[1],
            "Title 3": titles[2],
            "Title 4": titles[3],
            "Title 5": titles[4]
        })

        time.sleep(0.3)

    return twitter_rows, linkedin_rows, email_rows, blog_rows

def save_excel(twitter_rows, linkedin_rows, email_rows, blog_rows):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"content_output_{timestamp}.xlsx"

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        pd.DataFrame(twitter_rows).to_excel(
            writer, index=False, sheet_name="Twitter"
        )
        pd.DataFrame(linkedin_rows).to_excel(
            writer, index=False, sheet_name="LinkedIn"
        )
        pd.DataFrame(email_rows).to_excel(
            writer, index=False, sheet_name="Email"
        )
        pd.DataFrame(blog_rows).to_excel(
            writer, index=False, sheet_name="Blog Titles"
        )
        pd.DataFrame([{
            "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Total Topics": len(twitter_rows),
            "Twitter Posts": len(twitter_rows) * 3,
            "LinkedIn Posts": len(linkedin_rows),
            "Email Copies": len(email_rows),
            "Blog Titles": len(blog_rows) * 5,
            "Model": "llama3.1:8b (local GPU)"
        }]).to_excel(writer, index=False, sheet_name="Summary")

    return output_file


if __name__ == "__main__":
    print("=" * 45)
    print("   AI Content Automation Pipeline")
    print("   Powered by Ollama (Local GPU)")
    print("=" * 45 + "\n")

    if not check_ollama():
        print("❌ Ollama tidak terdeteksi!")
        print("   Jalankan 'ollama serve' di terminal lain dulu.")
        exit(1)
    print("✅ Ollama terdeteksi\n")

    if not os.path.exists("sample_input.csv"):
        print("❌ sample_input.csv tidak ditemukan!")
        exit(1)

    df_preview = pd.read_csv("sample_input.csv")
    print(f"📂 Input: sample_input.csv ({len(df_preview)} topik)\n")

    twitter_rows, linkedin_rows, email_rows, blog_rows = process_csv()

    print("\n💾 Menyimpan ke Excel...")
    output_file = save_excel(twitter_rows, linkedin_rows, email_rows, blog_rows)

    print(f"\n✅ SELESAI!")
    print(f"📊 Output: {output_file}")
    print(f"   Twitter  : {len(twitter_rows) * 3} posts")
    print(f"   LinkedIn : {len(linkedin_rows)} posts")
    print(f"   Email    : {len(email_rows)} copies")
    print(f"   Blog     : {len(blog_rows) * 5} titles")
    print(f"\nBuka file Excel untuk lihat hasilnya!")