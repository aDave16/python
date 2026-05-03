import datetime

users = {}# Dictionary to store user credentials
posts = []# List to store all posts


# Utility Functions
def get_current_date():
    #Return current date
    return datetime.datetime.now().strftime("%d-%m-%Y")

#user input is not empty
def input_not_empty(strg):
    while True:
        value = input(strg).strip()
        if value == "":
            print("Field cannot be empty")
        else:
            return value


# User Registration
def register():
    print("\n--- User Registration ---")

    while True:
        username = input_not_empty("Enter username: ")#chek if username is not empty

        if username in users:#check if username already exists in users dictionary
            print("Username already exists. Try another.")
        else:
            break

    password = input_not_empty("Enter password: ")
    users[username] = password

    print("Registration successful!")

# User Login
def login():
    print("\n--- Login ---")

    for attempt in range(3):#allow user to attempt login 3 times
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:#check if username exists and password matches
            print("Login successful!")
            return username
        else:
            print("Invalid credentials.")

    print("Too many failed attempts.")
    return None

# Create Post
def create_post(current_user):
    print("\n--- Create New Post ---")

    title = input_not_empty("Title: ")
    description = input_not_empty("Description: ")

    choice = input("Use current date? (y/n): ").lower()

    match choice:
        case "n":
            date = input_not_empty("Enter date (DD-MM-YYYY): ")
        case _:
            date = get_current_date()

    post = {
        "author": current_user,
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)
    print("Post created successfully!")

# View All Posts
def view_posts():
    print("\n--- All Posts ---")

    if not posts:
        print("No posts available.")
        return

    for i, post in enumerate(posts, start=1):#each post is displayed with index and details
    #enumerate function is used to loop through the posts list and get both the index (i) and the post itself
        print(f"\nPost #{i}")
        print(f"Author      : {post['author']}")
        print(f"Title       : {post['title']}")
        print(f"Date        : {post['date']}")
        print(f"Description : {post['description']}")

# Search Posts
def search_posts():
    print("\n--- Search Posts by Username ---")

    username = input("Enter username: ")
    found = False#if post not found for given username

    for post in posts:
        if post["author"] == username:
            if not found:
                print(f"\nPosts by {username}:")
            found = True

            print(f"\nTitle       : {post['title']}")
            print(f"Date        : {post['date']}")
            print(f"Description : {post['description']}")

    if not found:
        print("No posts found for this user.")

# Dashboard Menu
def dashboard(username):
    while True:
        print(f"\n--- Welcome {username} ---")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")

        choice = input("Enter choice: ")

        match choice:
            case 1:
                create_post(username)
            case 2:
                view_posts()
            case 3:
                search_posts()
            case 4:
                print("Logging out...")
                break
            case _:
                print("Invalid choice")

# Program Starts Here
while True:
    print("\n*** PostBoard ***")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    match choice:
        case 1:
            register()
        case 2:
            user = login()
            if user:
                dashboard(user)#if login is successful, user is taken to dashboard where they can create posts, view all posts, or search posts by username
        case 3:
            break
        case _:
            print("Invalid option.")