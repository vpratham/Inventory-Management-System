import re
from tkinter import messagebox
def sanitize_input(desc):
    # Remove HTML tags
    sanitized_desc = re.sub(r'<.*?>', '', desc) 
    # Remove any <script> tags
    sanitized_desc = re.sub(r'(?i)<script.*?>.*?</script>', '', sanitized_desc) 
    return sanitized_desc.strip()

def sanitize(n, e, d):
    name = n
    email = e
    desc = d

    # Check name and email patterns, and ensure description is valid
    if (bool(re.match(r'^[a-zA-Z\s]+$', name)) and 
        bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)) and 
        bool(desc) and 
        len(desc) <= 500):
        
        print(1)
        clean_desc = sanitize_input(desc)

        # Remove single and double quotes from the sanitized description
        clean_desc = re.sub(r'[\'"]', '', clean_desc)

        clean_desc = clean_desc.replace(';', '_').replace('=', ' equals ')

        try:
            print(2)

            # Use clean_desc in the SQL query
            sql_query = f"INSERT INTO abc (name, email, description) VALUES (%s, %s, %s)"
        
            # Print the SQL query with parameters for debugging
            print(sql_query % (name, email, clean_desc))  # Use clean_desc here
            
        except Exception as e:  # Catch specific exceptions if needed
            print(f"An error occurred: {e}")
            return False
        else:
            #query_add(name,email,clean_desc)
            return True

    else:
        messagebox.showerror("Invalid Entry", "Please submit valid name & email id")  # Alert user
        return False



# Example usage
#sanitize('a', 'a@b.com', "jon' or 'a'='a';--")
