MENU_PROMPT = 'Enter "c" to create a blog, "l" to list a blog, "r" to read one, or "q" to quit'
blogs = dict()  # blog_name: Blog Object


def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with the choice
    # Eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog))
