import os
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def analyze_index_html():
    if not os.path.exists(INDEX_PATH):
        return None

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    total_lines = len(lines)
    total_bytes = os.path.getsize(INDEX_PATH)

    sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', content)
    bento_cards = len(re.findall(r'class=["\'][^"\']*glass-card', content))
    tech_items = len(re.findall(r'class=["\'][^"\']*tech-item', content))

    return {
        "total_lines": total_lines,
        "total_size_kb": round(total_bytes / 1024, 2),
        "sections": sections,
        "bento_cards": bento_cards,
        "tech_items": tech_items,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def update_readme():
    stats = analyze_index_html()
    if not stats:
        print("index.html not found!")
        return

    auto_block = f"""<!-- START_AUTO_UPDATE -->
| Metric | Value |
| :--- | :--- |
| **Site Architecture** | Single-File Standalone HTML (`index.html`) |
| **Package Overhead** | **0 NPM packages / 0 Build steps** |
| **Total Code Size** | {stats['total_size_kb']} KB ({stats['total_lines']} lines) |
| **Bento Cards & Glass Panels** | {stats['bento_cards']} interactive cards |
| **Technologies & Capabilities** | {stats['tech_items']} core focus items |
| **Tracked Page Sections** | `{", ".join(stats['sections'])}` |
| **Last Auto-Synced** | `{stats['last_updated']}` |
<!-- END_AUTO_UPDATE -->"""

    if not os.path.exists(README_PATH):
        readme_content = f"# Velaryn Website\n\n{auto_block}\n"
    else:
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()

        if "<!-- START_AUTO_UPDATE -->" in readme_content and "<!-- END_AUTO_UPDATE -->" in readme_content:
            readme_content = re.sub(
                r"<!-- START_AUTO_UPDATE -->.*?<!-- END_AUTO_UPDATE -->",
                auto_block,
                readme_content,
                flags=re.DOTALL
            )
        else:
            readme_content += f"\n\n## Auto-Generated Status\n\n{auto_block}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md successfully updated with latest index.html metrics!")

if __name__ == "__main__":
    update_readme()
