import re

def parse_bugs(raw_text: str) -> list:
    """
    Parses Gemini raw response into a list of bug dictionaries.
    """

    # Handle case where no bugs found
    if "NO_BUGS_FOUND" in raw_text:
        return []

    bugs = []

    # Find all BUG_START...BUG_END blocks
    pattern = r"BUG_START(.*?)BUG_END"
    matches = re.findall(pattern, raw_text, re.DOTALL)

    for match in matches:
        bug = {}
        lines = match.strip().split("\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("title:"):
                bug["title"] = line.replace("title:", "").strip()

            elif line.startswith("location:"):
                bug["location"] = line.replace("location:", "").strip()

            elif line.startswith("severity:"):
                severity = line.replace("severity:", "").strip()
                bug["severity"] = severity
                # Add color code for frontend
                if severity == "High":
                    bug["severity_color"] = "red"
                elif severity == "Medium":
                    bug["severity_color"] = "yellow"
                else:
                    bug["severity_color"] = "green"

            elif line.startswith("description:"):
                bug["description"] = line.replace("description:", "").strip()

            elif line.startswith("fix:"):
                bug["fix"] = line.replace("fix:", "").strip()

        # Only add if we got all fields
        if all(k in bug for k in ["title", "location", "severity", "description", "fix"]):
            bugs.append(bug)

    return bugs