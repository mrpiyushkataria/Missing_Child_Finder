# Missing Child Finder using Face-Recognition

Python - OpenCV2, face_recognition, Tkinter



Working of the project

1. Registration of Missing Children: User clicks on the "Register a Missing Child" button in the user interface. A new window opens where the user enters the details of the missing child, including name, mobile number, address, and uploads an image of the child. The system processes the uploaded image using face detection algorithms to locate and extract the face from the image.
Facial features are extracted from the detected face and encoded into numerical representations known as face encodings. The child's information and face encoding are stored in the database for future reference.

2. Search for Missing Children: User clicks on the "Search for a Missing Child" button in the user interface.
A new window opens where the user uploads an image of a child to be identified. The system processes the uploaded image, detects the face within it using face detection algorithms, and extracts facial features. The extracted facial features are encoded into face encodings. The system compares the face encodings of the uploaded image with the face encodings of registered children in the database. If a match is found, the system displays the details of the matched child, including their name, mobile number, and address.
If match not found its show Matching child not found.

3. User Interface: The user interface is implemented using the Tkinter library in Python. The main window of the application displays two buttons: "Register a Missing Child" and "Search for a Missing Child." Clicking on these buttons opens new windows where users can enter the necessary information or upload images. The user interface provides a user-friendly and intuitive way for users to interact with the system.
