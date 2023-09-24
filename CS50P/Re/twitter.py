import re

url = input("URl: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):

    print(f"Username: {matches.group(1)}")
else:
    print("Invalid")
