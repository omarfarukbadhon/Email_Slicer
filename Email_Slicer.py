provided_email=input("Enter your mail ID: ").strip() #strip function remove unwanted spaces

username=provided_email[:provided_email.index('@')] # ":" is slicing operator and index file seraches for given element or character and return its index number

domain=provided_email[provided_email.index('@') + 1:]

print(f"Your username {username} and domain of your mail is {domain}") # f-string 



