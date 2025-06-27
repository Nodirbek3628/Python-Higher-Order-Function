# Email domenlarini ajratish

# Quyidagi email ro’yxatidan faqat `gmail.com` domeniga tegishlilarni ajrating.

# ```python
# emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]


def email_domin(email):
    if email[-10:] == "@gmail.com":
        return email
    

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

result =  filter(email_domin,emails)
print(list(result))