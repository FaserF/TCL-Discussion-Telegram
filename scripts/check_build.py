import os
import re
import sys

# Ensure stdout uses UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def check_rendering_artifacts(html_content, filename):
    # Regex to find unrendered items, ignoring ones inside <code> or <pre>
    stripped_content = re.sub(r'<(code|pre).*?>.*?</\1>', '', html_content, flags=re.DOTALL)

    issues = []

    # Check for unrendered icons
    icons = re.findall(r':material-[a-z0-9-]+:', stripped_content)
    if icons:
        issues.extend([f"Icon: {i}" for i in icons])

    # Check for unrendered admonitions
    admonitions = re.findall(r'(?:^|\s)(?:!!!|\?\?\?)\s+[a0-z]+', stripped_content)
    if admonitions:
        issues.extend([f"Admonition: {a}" for a in admonitions])

    # Check for failed GitHub-style alerts
    alerts = re.findall(r'\[\![A-Z]+\]', stripped_content)
    if alerts:
        issues.extend([f"Alert: {a}" for a in alerts])

    if issues:
        print(f"[ERROR] In {filename}: Found unrendered items: {issues}")
        return False
    return True

def validate_build(site_dir="site"):
    if not os.path.exists(site_dir):
        print(f"[ERROR] site directory '{site_dir}' does not exist.")
        return False

    all_pass = True
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if not check_rendering_artifacts(content, path):
                        all_pass = False

    if all_pass:
        print("[SUCCESS] Rendering check passed.")
    else:
        print("[FAILURE] Rendering check failed.")
    return all_pass

if __name__ == "__main__":
    if not validate_build():
        sys.exit(1)
