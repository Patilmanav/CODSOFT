# Contact Book Application

## Project Description
The Contact Book Application is a desktop application built using Python and Tkinter for managing contacts. It allows users to add, update, search, and delete contact information. This project serves as a practical implementation for managing contact details with a graphical user interface (GUI).

## Features
- **Add Contact**: Add new contacts with details such as Name, Phone, Email, and Address.
- **Update Contact**: Update existing contact details.
- **Delete Contact**: Delete contacts from the contact list.
- **Search Contact**: Search for contacts by name or phone number.
- **Persistent Storage**: Contact details are stored persistently using a database.

## Requirements
- Python 3.10
- Tkinter
- dbHandler module (a custom module to interact with the database)
- uuid library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Patilmanav/CODSOFT.git
    cd CODSOFT/TASK5
    ```

2. **Install dependencies**:
    Ensure you have Python 3 installed. Tkinter comes pre-installed with Python. You might need to install the `uuid` module if it's not already installed.
    ```bash
    pip install uuid
    ```

3. **Set up the database**:
    The `dbHandler` module should handle the database setup. Ensure you have the module in your project directory and configured correctly.

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Using the Application**:
    - **Add a Contact**:
        - Click the "Add" button and fill in the contact details in the popup window.
        - Click "Save" to add the contact.
    - **Update a Contact**:
        - Select a contact from the list.
        - Click the "Update" button and modify the contact details in the popup window.
        - Click "Save" to update the contact.
    - **Delete a Contact**:
        - Select a contact from the list.
        - Click the "Delete" button to remove the contact.
    - **Search for a Contact**:
        - Enter the search term in the search bar.
        - Click the "Search" button to filter the contacts list.

## Screenshots
(Include screenshots of the application here to give users a visual idea of the application)

## Code Overview

### Main Application
The main application is defined in `main.py`. It initializes the Tkinter GUI, sets up the menu, contact list, and buttons, and handles user interactions.

### dbHandler Module
The `dbHandler` module handles interactions with the database, including retrieving, adding, updating, and deleting contacts.

### Key Functions
- `add_contact_popup()`: Opens a popup to add a new contact.
- `update_contact_popup()`: Opens a popup to update selected contact details.
- `contact_popup()`: Creates a generic popup for adding or updating contacts.
- `add_contact()`: Adds a new contact to the list and database.
- `update_contact()`: Updates an existing contact in the list and database.
- `delete_contact()`: Deletes a contact from the list and database.
- `search_contact()`: Filters the contact list based on the search query.
- `update_contact_list()`: Updates the displayed contact list in the GUI.

## Acknowledgments
- Thanks to Cloud Counselage for the opportunity to work on this project.


*Contact Book Application* - Manage your contacts efficiently!
