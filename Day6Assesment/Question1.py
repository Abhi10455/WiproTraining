import re
employee_id = "EMP123"
match_emp = re.match(r"(EMP)(\d{3})", employee_id)

if match_emp:
    print("Valid Employee ID")
    print("Full Match :", match_emp.group(0))
    print("Group 1    :", match_emp.group(1))
    print("Group 2    :", match_emp.group(2))
else:
    print("Invalid Employee ID")

text = "Please contact us at support123@example.com for assistance."

email_pattern = r"([\w\.]+)@([\w]+)\.(\w+)"
search_email = re.search(email_pattern, text)

if search_email:
    print("\nEmail Found")
    print("Full Email :", search_email.group(0))
    print("Username  :", search_email.group(1))
    print("Domain    :", search_email.group(2))
    print("Extension :", search_email.group(3))
else:
    print("No email found")

sample_text = "ID A1   Code_99"

pattern = r"(\w+)\s+(\w+\d*)"
result = re.search(pattern, sample_text)

if result:
    print("\nMeta-characters and Special Sequences Demo")
    print("Full Match :", result.group(0))
    print("Group 1    :", result.group(1))
    print("Group 2    :", result.group(2))
