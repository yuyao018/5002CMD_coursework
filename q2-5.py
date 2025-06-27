from udgraph import UDgraph
from person import Person

def view_all_users(users):
    # function to view all users' names in the system

    while True: # keep the loop running until the user decides to go back to the main menu
        # display a header for the users list
        print("======================================================")
        print("                All Users on POSTGRAM")
        print("======================================================")

        # enumerate through the list of users and print their names with numbering
        for index, user in enumerate(users):
            print(f"{index + 1}. {user.name}")

        # ask user whether they want to go back to the main menu
        back = input("Go back? [y/n]: ").strip().lower() # remove leading/trailing spaces and covert to lowercase

        # call function to help validate 'y/n' input
        if prompt_back(back): # if user confirms to go back
            return # exit the function and return to the main menu

def view_user_profile(users):
    # function to display the profile details of a selected user

    while True: # continue looping until the user decides to stop viewing profiles
        # display the header and list of all user names with corresponding index numbers
        print("======================================================")
        print("            Profile Details of Any User")
        print("======================================================")
        for index, user in enumerate(users):
            print(f"{index + 1}. {user.name}")
        print("======================================================")

        # prompt the user to select a user by entering the corresponding number
        selected_user = int(input(f"Select User (1 - {len(users)}): "))

        # check if the selected number is within the valid range
        if 1 <= selected_user <= len(users):
            user = users[selected_user - 1] # get the corresponding user object; minus 1 to adjust index for 0-based list
            if user.privacy.lower() == "public":
                # if the profile is public, display the user's details
                print("\n======================================================")
                print("                    User Profile")
                print("======================================================")
                print("Name      :", user.name)
                print("Gender    :", user.gender)
                print("Biography :", user.biography)
            else:
                # if the profile is private, inform the viewer that profile details is unavailable
                print(f"\nThe profile details of {user.name} are hidden due to privacy issue.")
        else:
            # notify the user of invalid input if the selected index is out of range
            print("Invalid input! Please select a valid user number.")

        # ask if user wants to view another profile
        back = input("\nView another profile? [y/n]: ").strip().lower()
        if not prompt_back(back): # call function to help validate if user wants to continue
            return # if user don't want to continue, exit the loop and return to main menu

def view_followers(social_graph, users):
    # function to display the list of followers for any selected user in the social graph

    while True: # continue looping until the user decides to exit and return to the main menu
        # display the header and list of all user names with corresponding index numbers
        print("======================================================")
        print("               Followers of Any User")
        print("======================================================")
        for index, user in enumerate(users):
            print(f"{index + 1}. {user.name}")
        print("======================================================")

        # prompt the user to select a user to view their followers
        selected_user = int(input(f"Select User (1 - {len(users)}): "))

        # check if the selected number is within the valid range
        if 1 <= selected_user <= len(users):
                user = users[selected_user - 1] # get the corresponding user object; minus 1 to adjust index for 0-based list

                # find all users who follows the selected user
                # loop through each user in the 'users' list and check if the selected user is in the outgoing adjacent list of each user
                followers = [u for u in users if user in social_graph.list_out_going_adjacent_vertex(u)]

                # display the follower list
                print(f"\nFollowers of {user.name}:")
                if followers: # check if a user has followers. If yes, display the list of followers.
                    for follower in followers:
                        print(f"- {follower.name}")
                else: # If the user has no followers, display no followers are found.
                    print("No followers are found.")
        else:
            # notify the user if the input is out of range
            print("Invalid input! Please select a valid user number.")

        # ask if the user wants to view another user's followers
        back = input("View another user's followers? [y/n]: ").strip().lower()
        if not prompt_back(back): # call function to help validate if the user want to continue or not
            return # exit the loop and return to the main menu

def view_following(social_graph, users):
    # function to display the accounts followed by a selected user

    while True: # continue looping until the user decides to exit and return to the main menu
        # display the header and list of all user names with corresponding index numbers
        print("======================================================")
        print("           Followed Accounts of Any User")
        print("======================================================")
        for index, user in enumerate(users):
            print(f"{index + 1}. {user.name}")
        print("======================================================")

        # prompt the user to select a user by number
        selected_user = int(input(f"Select User (1 - {len(users)}): "))

        # validate if the input is in range
        if 1 <= selected_user <= len(users):
                user = users[selected_user - 1] # get the corresponding user object; minus 1 to adjust index for 0-based list

                # get the list of users that the selected user is following
                following = social_graph.list_out_going_adjacent_vertex(user)

                # display the list of followed accounts
                print(f"\n{user.name} is following:")
                if following: # check if the selected user is following anyone. If yes, display the list of following accounts.
                    for follow in following:
                        print(f"- {follow.name}")
                else: # if the selected user is not following anyone, notify that the user is not following anyone.
                    print("Not following anyone.")
        else:
            # notify the user if the input is out of range
            print("Invalid input! Please select a valid user number.")

        # ask the user whether to view another user's following list
        back = input("View another user's followers? [y/n]: ").strip().lower()
        if not prompt_back(back): # call function to help validate if the user want to continue or not
            return # exit the loop and return to the main menu

def create_new_user(users, social_graph):
    # function to create a new user in the system

    # display the header
    print("======================================================")
    print("           Create a New User Account")
    print("======================================================")

    # prompt the user to input new user details
    while True:
        name = input("Enter name: ")                      # get the name of the user

        # check if there are duplicate names
        if any(user.name.lower() == name.lower() for user in users):
            print("Error: A user with that name already exists. Please enter a different name.")
        elif name == "":
            print("Error: Namce cannot be empty")
        else: break

    while True:
        gender = input("Enter gender (male/female): ")    # get the gender of the user

        # check if the input is correct
        if gender.lower() in ['male', 'female']:
            break
        else:
            print("Error: please enter 'male' or 'female'.")

    biography = input("Enter biography: ")            # get a short biography

    while True:
        privacy = input("Set Privacy (Private/Public): ") # set account privacy

        # check if the input is correct
        if privacy.lower() in ['public', 'private']:
            break
        else:
            print("Error: Please enter 'Private' or 'Public'.")

    # create a new instance of the Person class using the provided data
    new_user = Person(name, gender, biography, privacy)

    # add the new user to the graph as vertex
    social_graph.add_vertex(new_user)

    # add the new user to the list of users
    users.append(new_user)

    # simulate loading effect to enhance user experience
    print("Loading", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)

    # display the confirmation message once the new user is added
    print(f"\n{name} has been added successfully!\n\n\n")

def follow_someone(users, social_graph):
    # function to allow a user to follow another user

    current_user = None # initialize the current user to None

    # prompt until a valid username is entered
    while current_user is None:
        username = input("Enter your username: ")
        for user in users:
            if username == user.name:
                current_user = user # found the current user
                break # break from the loop once the user is found
        if current_user is None:
            print("Invalid user! Enter a valid username.")

    # get the list of users the current user is following
    following = social_graph.list_out_going_adjacent_vertex(current_user)

    # create a list of users that cannot be followed by the selected user
    unfollowable = [user for user in following]
    unfollowable.append(current_user)

    # filter out users that are followable
    followable_users = [user for user in users if user not in unfollowable]

    # display the list of users the current user can follow
    print("======================================================")
    print("               People You Can Follow")
    print("======================================================")
    for user in followable_users:
        print(f"- {user.name}")

    # prompt to select a valid user to follow
    target_user = None
    while target_user is None:
        target_name = input("Enter the name of the user you want to follow: ").strip()
        for user in followable_users:
            if user.name == target_name:
                target_user = user
                break
        if target_user is None:
            print("User not found or you cannot follow yourself. Please try again.")

    # add a directed edge in the graph representing the follow relationship
    social_graph.add_edge(current_user, target_user)

    # display a confirmation message stating the successful following of target user
    print(f"You are now following {target_user.name}.")

def unfollow_someone(users, social_graph):
    # function to allow a user to unfollow another user

    current_user = None # initialize the current user to None

    # prompt until a valid username is input
    while current_user is None:
        username = input("Enter your username: ")
        for user in users:
            if username == user.name:
                current_user = user # found the current user
                break # break from the loop once the user is found
        if current_user is None:
            print("Invalid user! Enter a valid username.")

    # get the list of users the current user is following
    following = social_graph.list_out_going_adjacent_vertex(current_user)

    # if the current user is not following anyone, notify and exit
    if not following:
        print("You are not following anyone.")
        return

    # display the list of users the current user is following
    print("======================================================")
    print("              People You Are Following")
    print("======================================================")
    for user in following:
        print(f"- {user.name}")

    # prompt the user to enter an valid username from the list to unfollow
    target_user = None
    while target_user is None:
        target_name = input("Enter the name of the user you want to unfollow: ").strip()

        # search for the target user in the following list
        for user in following:
            if user.name == target_name:
                target_user = user
                break # exit the loop when a match is found

        # if the entered name is invalid, display user not found
        if target_user is None:
            print("User not found in your followings. Please try again.")

    # remove the edge representing the follow relationship in the graph
    social_graph.remove_edge(current_user, target_user)

    # confirmation message that the target user is unfollowed
    print(f"You have unfollowed {target_user.name}.")

def prompt_back(back):
    # function to prompt user to confirm whether they want to go back to main menu or continue
    while True:
        if back == "y":
            return True
        elif back == "n":
            return False
        else:
            # If input is invalid, ask again
            print("Invalid input. Please enter 'y' or 'n'.")


# def view_user_profile(users):
#     while True:
#         print("======================================================")
#         print("            Profile Details of Any User")
#         print("======================================================")
#         for index, user in enumerate(users):
#             print(f"{index + 1}. {user.name}")
#         print("======================================================")
#         selected_user = int(input(f"Select User (1 - {len(users)}): "))

#         if 1 <= selected_user <= len(users):
#             user = users[selected_user - 1]
#             print("\n======================================================")
#             print("                    User Profile")
#             print("======================================================")
#             print("Name      :", user.name)
#             print("Gender    :", user.gender)
#             print("Biography :", user.biography)
#         else:
#             print("Invalid input! Please select a valid user number.")
#         back = input("\nView another profile? [y/n]: ").strip().lower()
#         if not prompt_back(back):
#             return

def main():
    # create user profiles
    sarah = Person("Sarah", "female", "Loves music", "private")
    wendy = Person("wendy", "female", "Loves fashion", "public")
    jaden = Person("Jaden", "male", "All Time Gamer", "public")
    alice = Person("Alice", "female", "Photographer and traveler", "public")
    bob = Person("Bob", "male", "Coffee lover and tech enthusiast", "private")
    clara = Person("Clara", "female", "Bookworm and writer", "public")
    david = Person("David", "male", "Fitness coach and nutritionist", "public")
    eva = Person("Eva", "female", "Music teacher and pianist", "private")

    # create a unweighted directed graph to represent the social network
    social_graph = UDgraph[Person]()

    # add all users as vertices in the graph
    social_graph.add_vertex(sarah)
    social_graph.add_vertex(wendy)
    social_graph.add_vertex(jaden)
    social_graph.add_vertex(alice)
    social_graph.add_vertex(bob)
    social_graph.add_vertex(clara)
    social_graph.add_vertex(david)
    social_graph.add_vertex(eva)

    # define follow relationships as directed edges in the graph
    social_graph.add_edge(sarah, wendy)
    social_graph.add_edge(wendy, sarah)
    social_graph.add_edge(jaden, sarah)
    social_graph.add_edge(david, wendy)
    social_graph.add_edge(sarah, alice)
    social_graph.add_edge(wendy, david)
    social_graph.add_edge(jaden, david)
    social_graph.add_edge(clara, alice)
    social_graph.add_edge(bob, david)
    social_graph.add_edge(eva, wendy)

    # store all users in a list
    all_users = [sarah, wendy, jaden, alice, bob, clara, david, eva]

    # start the main menu loop
    while True:
        # display main menu
        print("======================================================")
        print("            SOCIAL MEDIA APP - POSTGRAM")
        print("======================================================")
        print("1. View all users")
        print("2. View a user's profile")
        print("3. View followers of a user")
        print("4. View who a user is following")
        print("5. Create new user")
        print("6. Follow someone")
        print("7. Unfollow someone")
        print("8. Exit\n")

        # prompt user to select input
        choice = int(input("Enter your choice => "))

        # call the appropriate function based on user chouice
        if choice == 1:
            view_all_users(all_users)                 # list all users
        elif choice == 2:
            view_user_profile(all_users)              # view a specific user's profile
        elif choice == 3:
            view_followers(social_graph, all_users)   # show followers of a user
        elif choice == 4:
            view_following(social_graph, all_users)   # show followings of a user
        elif choice == 5:
            create_new_user(all_users, social_graph)  # add a new user to the graph
        elif choice == 6:
            follow_someone(all_users, social_graph)   # allow a user to follow another user
        elif choice == 7:
            unfollow_someone(all_users, social_graph) # allow a user to unfollow another user
        elif choice == 8:
            break                                     # exit the loop and end the program
        else:
            print("Invalid selection! Please enter a valid number (1 - 8).\n") # user choice out of range, ask user to input a valid number

if __name__ == "__main__":
    main()