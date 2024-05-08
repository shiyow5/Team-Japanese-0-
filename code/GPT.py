import sqlite3
import os

# Connect to SQLite database
conn = sqlite3.connect('file_manager.db')
c = conn.cursor()

# Create table to store file metadata
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY, original_name TEXT, updated_name TEXT, content TEXT)''')
conn.commit()

def upload_file(file_path, new_name=None):
    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    original_name = os.path.basename(file_path)
    if new_name:
        updated_name = new_name
    else:
        updated_name = original_name

    c.execute("INSERT INTO files (original_name, updated_name, content) VALUES (?, ?, ?)",
              (original_name, updated_name, content))
    conn.commit()

def search_file(file_name):
    c.execute("SELECT * FROM files WHERE (original_name = ?) or (updated_name = ?)", (file_name, file_name))
    file_data = c.fetchone()
    if file_data:
        return file_data
    else:
        return None

def update_file(original_name, new_name):
    c.execute("UPDATE files SET updated_name = ? WHERE (original_name = ?) or (updated_name = ?)", (new_name, original_name, original_name))
    conn.commit()

def delete_file(file_name):
    c.execute("DELETE FROM files WHERE (original_name = ?) or (updated_name = ?)", (file_name, file_name))
    conn.commit()

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Upload file")
        print("2. Search for file")
        print("3. Update file name")
        print("4. Delete file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter file path: ")
            new_name = input("Enter new name (press Enter to keep original name): ").strip()
            upload_file(file_path, new_name)

        elif choice == '2':
            file_name = input("Enter file name: ")
            file_data = search_file(file_name)
            if file_data:
                print("File found!")
                print("Original name:", file_data[1])
                print("Updated name:", file_data[2])
                print("Content:\n", file_data[3])
            else:
                print("File not found.")

        elif choice == '3':
            original_name = input("Enter file name: ")
            new_name = input("Enter new name: ")
            update_file(original_name, new_name)
            print("File name updated successfully.")

        elif choice == '4':
            file_name = input("Enter file name to delete: ")
            delete_file(file_name)
            print("File deleted successfully.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
