def search_line_number():
    query = input("Enter what to search for: ").strip().lower()
    found = False

    with open("study.py", "r") as file:
        for line_number, line in enumerate(file, start=1):
            if "###" in line and "Section:" in line:
                section_title = line.split("Section:")[1].strip().lower()
                if query in section_title:
                    print(f"🔍 Match found on line {line_number}: {section_title}")
                    found = True

    if not found:
        print("❌ No match found.")

search_line_number()
