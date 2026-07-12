print("=" * 45)
print("           CONTACT BOOK")
print("=" * 45)

contacts = {}

while True:

    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # -----------------------------
    # Add Contact
    # -----------------------------
    if choice == "1":

        name = input("\nEnter Name: ").strip().title()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("\n✅ Contact added successfully!")

    # -----------------------------
    # View Contacts
    # -----------------------------
    elif choice == "2":

        if len(contacts) == 0:
            print("\nNo contacts found.")

        else:

            print("\nCONTACT LIST")
            print("-" * 45)

            for name, details in contacts.items():

                print(f"Name  : {name}")
                print(f"Phone : {details['phone']}")
                print(f"Email : {details['email']}")
                print("-" * 45)

    # -----------------------------
    # Search Contact
    # -----------------------------
    elif choice == "3":

        search_name = input("\nEnter contact name to search: ").strip().title()

        if search_name in contacts:

            print("\nCONTACT FOUND")
            print("-" * 45)

            print(f"Name  : {search_name}")
            print(f"Phone : {contacts[search_name]['phone']}")
            print(f"Email : {contacts[search_name]['email']}")
            print("-" * 45)

        else:

            print("\n❌ Contact not found.")

    # -----------------------------
    # Update Contact
    # -----------------------------
    elif choice == "4":

        update_name = input("\nEnter contact name to update: ").strip().title()

        if update_name in contacts:

            new_phone = input("Enter New Phone Number: ").strip()
            new_email = input("Enter New Email Address: ").strip()

            contacts[update_name]["phone"] = new_phone
            contacts[update_name]["email"] = new_email

            print("\n✅ Contact updated successfully!")

        else:

            print("\n❌ Contact not found.")

    # -----------------------------
    # Delete Contact
    # -----------------------------
    elif choice == "5":

        delete_name = input("\nEnter contact name to delete: ").strip().title()

        if delete_name in contacts:

            del contacts[delete_name]

            print("\n✅ Contact deleted successfully!")

        else:

            print("\n❌ Contact not found.")

    # -----------------------------
    # Exit
    # -----------------------------
    elif choice == "6":

        print("\nThank you for using Contact Book!")
        break

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:

        print("\n❌ Invalid choice! Please try again.")