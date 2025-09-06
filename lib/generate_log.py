

# generate_log.py
from datetime import datetime
from pathlib import Path
import json


def generate_log(data, out_dir=".", prefix="log_"):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")


    # STEP 2: Filename with today's date e.g., log_20250408.txt
    filename = f"{prefix}{datetime.now().strftime('%Y%m%d')}.txt"
    path = Path(out_dir) / filename

    # STEP 3: Write the log entries to a file
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {path}")
    return str(path)


def fetch_data():
    """Simple API call using requests; returns dict (or {})."""
    try:
        resp = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10,
        )
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}


if __name__ == "__main__":
    # Example usage
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

    # Also persist the fetched data as structured output
    json_name = f"post_{datetime.now().strftime('%Y%m%d')}.json"
    Path(json_name).write_text(json.dumps(post, indent=2), encoding="utf-8")
    print(f"API response saved to {json_name}")
