import tkinter as tk
from tkinter import filedialog
import cv2
import face_recognition

# Sample database list to store child data
database = []

# Function to add a child to the database
def add_child(name, mobile, address, image):
    # Load the child's image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    face_locations = face_recognition.face_locations(rgb_image)
    if len(face_locations) != 1:
        print("No face or multiple faces found in the image.")
        return

    # Compute face encodings for the detected face(s)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    # Store the child's data and face encoding in the database
    child_data = {
        "name": name,
        "mobile": mobile,
        "address": address,
        "face_encoding": face_encodings[0]
    }
    database.append(child_data)  # Add the child data to the database list

    print("Child added to the database.")

# Function to search for a matching face in the database
def search_child(image):
    # Load the search image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the search image
    face_locations = face_recognition.face_locations(rgb_image)
    if len(face_locations) != 1:
        print("No face or multiple faces found in the search image.")
        return None

    # Compute face encodings for the search image
    search_face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    # Loop through the child data in the database and compare face encodings
    for child_data in database:
        stored_face_encoding = child_data["face_encoding"]

        # Compare the face encodings
        matches = face_recognition.compare_faces([stored_face_encoding], search_face_encodings[0])

        if matches[0]:
            return child_data

    # No match found
    return None

# Function to register a missing child
def register_child():
    register_window = tk.Toplevel(root)
    register_window.title("Register Missing Child")

    def browse_image():
        file_path = filedialog.askopenfilename()
        image_path.set(file_path)

    def register():
        name = name_entry.get()
        mobile = mobile_entry.get()
        address = address_entry.get()
        image = cv2.imread(image_path.get())

        add_child(name, mobile, address, image)
        register_window.destroy()

    image_path = tk.StringVar()

    name_label = tk.Label(register_window, text="Child's Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5)

    name_entry = tk.Entry(register_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    mobile_label = tk.Label(register_window, text="Mobile Number:")
    mobile_label.grid(row=1, column=0, padx=10, pady=5)

    mobile_entry = tk.Entry(register_window)
    mobile_entry.grid(row=1, column=1, padx=10, pady=5)

    address_label = tk.Label(register_window, text="Address:")
    address_label.grid(row=2, column=0, padx=10, pady=5)

    address_entry = tk.Entry(register_window)
    address_entry.grid(row=2, column=1, padx=10, pady=5)


    image_label = tk.Label(register_window, text="Child's Image:")
    image_label.grid(row=3, column=0, padx=10, pady=5)

    image_entry = tk.Entry(register_window, textvariable=image_path, state="readonly")
    image_entry.grid(row=3, column=1, padx=10, pady=5)

    browse_button = tk.Button(register_window, text="Browse", command=browse_image)
    browse_button.grid(row=3, column=2, padx=10, pady=5)

    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.grid(row=4, column=1, padx=10, pady=5)

# Function to search for a missing child
def search_child_menu():
    search_window = tk.Toplevel(root)
    search_window.title("Search Missing Child")

    def browse_image():
        file_path = filedialog.askopenfilename()
        image_path.set(file_path)

    def search():
        image = cv2.imread(image_path.get())

        result = search_child(image)
        if result:
            result_text.set("Matching child found!\n\n"
                            "Child's Name: {}\n"
                            "Mobile Number: {}\n"
                            "Address: {}".format(result["name"], result["mobile"], result["address"]))
        else:
            result_text.set("No matching child found.")

    image_path = tk.StringVar()
    result_text = tk.StringVar()

    image_label = tk.Label(search_window, text="Search Image:")
    image_label.grid(row=0, column=0, padx=10, pady=5)

    image_entry = tk.Entry(search_window, textvariable=image_path, state="readonly")
    image_entry.grid(row=0, column=1, padx=10, pady=5)

    browse_button = tk.Button(search_window, text="Browse", command=browse_image)
    browse_button.grid(row=0, column=2, padx=10, pady=5)

    search_button = tk.Button(search_window, text="Search", command=search)
    search_button.grid(row=1, column=1, padx=10, pady=5)

    result_label = tk.Label(search_window, textvariable=result_text)
    result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Create the main window
root = tk.Tk()
root.title("Child Missing System")

# Create buttons for registration and search
register_button = tk.Button(root, text="Register a Missing Child", command=register_child)
register_button.pack(pady=10)

search_button = tk.Button(root, text="Search for a Missing Child", command=search_child_menu)
search_button.pack(pady=10)

# Run the application
root.mainloop()
