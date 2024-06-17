'''
Contact Book
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
'''

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import uuid
import dbHandler

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Initialize contacts list with some default values
        self.contacts = []
        for i in dbHandler.get_contacts():
            self.contacts.append(i)
        
        # Search Bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.pack(pady=5)

        # Style for Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", anchor="center")
        style.configure("Treeview", rowheight=25)
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Treeview", font=("Arial", 10), foreground="black")
        style.configure("Treeview.Cell", anchor="center")

        # Contact List
        self.contact_list = ttk.Treeview(root, columns=("ID", "Name", "Phone", "Email", "Address"), show='headings', style="Treeview")
        self.contact_list.heading("ID", text="ID")
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.heading("Email", text="Email")
        self.contact_list.heading("Address", text="Address")
        self.contact_list.column("ID", width=0, stretch=tk.NO)
        self.contact_list.column("Name", anchor="center")
        self.contact_list.column("Phone", anchor="center")
        self.contact_list.column("Email", anchor="center")
        self.contact_list.column("Address", anchor="center")
        self.contact_list.pack(pady=20, fill=tk.BOTH, expand=True)

        # Action Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_contact_popup)
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_contact_popup)
        self.update_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Populate initial contacts
        self.update_contact_list()

    def add_contact_popup(self):
        self.contact_popup("Add Contact")

    def update_contact_popup(self):
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Update Contact", "Please select a contact to update.")
            return
        contact_id = self.contact_list.item(selected_item)["values"][0]
        contact = next(contact for contact in self.contacts if contact[0] == contact_id)
        self.contact_popup("Update Contact", contact)

    def contact_popup(self, title, contact=None):
        popup = tk.Toplevel()
        popup.title(title)

        tk.Label(popup, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        name_var = tk.StringVar(value=contact[1] if contact else "")
        name_entry = tk.Entry(popup, textvariable=name_var)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(popup, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        phone_var = tk.StringVar(value=contact[2] if contact else "")
        phone_entry = tk.Entry(popup, textvariable=phone_var)
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(popup, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        email_var = tk.StringVar(value=contact[3] if contact else "")
        email_entry = tk.Entry(popup, textvariable=email_var)
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(popup, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        address_var = tk.StringVar(value=contact[4] if contact else "")
        address_entry = tk.Entry(popup, textvariable=address_var)
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        if title == "Add Contact":
            save_button = tk.Button(popup, text="Save", command=lambda: self.add_contact(name_var, phone_var, email_var, address_var, popup))
        else:
            save_button = tk.Button(popup, text="Save", command=lambda: self.update_contact(contact[0], name_var, phone_var, email_var, address_var, popup))
        
        save_button.grid(row=4, column=0, columnspan=2, pady=10)
        cancel_button = tk.Button(popup, text="Cancel", command=popup.destroy)
        cancel_button.grid(row=5, column=0, columnspan=2, pady=5)

    def add_contact(self, name_var, phone_var, email_var, address_var, popup):
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()
        try:
            if not name or not phone:
                messagebox.showwarning("Add Contact", "Name and Phone are required fields.")
                return
            
            contact_id = str(uuid.uuid4())
            self.contacts.append((contact_id, name, phone, email, address))
            dbHandler.add_contact(name, phone, email, address)
            self.update_contact_list()
            popup.destroy()
            
        except Exception as e:
            print(e)
            messagebox.showwarning("Add Contact", e)


    def update_contact(self, contact_id, name_var, phone_var, email_var, address_var, popup):
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()

        if not name or not phone:
            messagebox.showwarning("Update Contact", "Name and Phone are required fields.")
            return

        index = next(i for i, contact in enumerate(self.contacts) if contact[0] == contact_id)
        print(self.contacts[index])
        dbHandler.update_contact(name=name,contact=phone,email=email,address=address,old_contact=self.contacts[index])
        self.contacts[index] = (contact_id, name, phone, email, address)
        self.update_contact_list()
        popup.destroy()

    def delete_contact(self):
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Delete Contact", "Please select a contact to delete.")
            return
        contact_id = self.contact_list.item(selected_item)["values"][0]
        dbHandler.delete_contect(self.contact_list.item(selected_item)["values"])
        self.contacts = [contact for contact in self.contacts if contact[0] != contact_id]
        
        self.update_contact_list()

    def search_contact(self):
        query = self.search_var.get()
        filtered_contacts = [contact for contact in self.contacts if query.lower() in contact[1].lower() or query.lower() in contact[2]]
        self.update_contact_list(filtered_contacts)

    def update_contact_list(self, contacts=None):
        for i in self.contact_list.get_children():
            self.contact_list.delete(i)
        
        if contacts is None:
            contacts = self.contacts

        for contact in contacts:
            self.contact_list.insert("", tk.END, values=(contact[0], contact[1], contact[2], contact[3], contact[4]))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.geometry("800x500")
    root.minsize(800,500)
    root.mainloop()
