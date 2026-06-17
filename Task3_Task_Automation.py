import re

print("Task Automation with Python Scripts")
print("Email Address Extractor")

source_file = input("Enter the input text file name: ").strip()
output_file = input("Enter the output file name or press Enter for emails_found.txt: ").strip()

if output_file == "":
    output_file = "emails_found.txt"

try:
    with open(source_file, "r", encoding="utf-8") as file:
        text = file.read()

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    found_emails = re.findall(email_pattern, text)
    unique_emails = list(dict.fromkeys(found_emails))

    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    if unique_emails:
        print("\nEmail addresses found:", len(unique_emails))

        for email in unique_emails:
            print(email)

        print("\nThe email addresses were saved in", output_file)
    else:
        print("No email addresses were found.")
        print("An empty output file was created.")

except FileNotFoundError:
    print("The input file was not found.")
except PermissionError:
    print("Permission was denied while opening or saving the file.")
except OSError:
    print("A file error occurred.")
