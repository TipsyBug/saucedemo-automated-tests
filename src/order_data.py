class OrderData:
    user_data = [["", "Ivanov", "1234567", "Error: First Name is required"],
                 ["Denis", "", "1234567", "Error: Last Name is required"],
                 ["Denis", "Ivanov", "", "Error: Postal Code is required"]]

    user_data_with_valid_credential = ["Denis", "Ivanov", "1234567"]

    successful_message = "Thank you for your order!"

