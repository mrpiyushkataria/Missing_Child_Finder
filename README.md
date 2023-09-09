# Missing Child Finder using Face-Recognition

Python - OpenCV2, face_recognition, Tkinter



Working of the project

1. Registration of Missing Children: User clicks on the "Register a Missing Child" button in the user interface.
<img width="282" alt="image" src="https://github.com/mrpiyushkataria/Missing_Child_Finder/assets/57060900/f53e84c2-9d53-406c-a369-7370c4680455">

2. A new window opens where the user enters the details of the missing child, including name, mobile number, address, and uploads an image of the child. The system processes the uploaded image using face detection algorithms to locate and extract the face from the image.
<img width="281" alt="image" src="https://github.com/mrpiyushkataria/Missing_Child_Finder/assets/57060900/64030737-1bb4-4de4-a3e8-455dfe83e2ed">
Facial features are extracted from the detected face and encoded into numerical representations known as face encodings. The child's information and face encoding are stored in the database for future reference.
<img width="370" alt="image" src="https://github.com/mrpiyushkataria/Missing_Child_Finder/assets/57060900/00f7f41c-0fe6-4da7-8fb2-d16e70ac38a8">


3. Search for Missing Children: User clicks on the "Search for a Missing Child" button in the user interface.
   A new window opens where the user uploads an image of a child to be identified.
<img width="412" alt="image" src="https://github.com/mrpiyushkataria/Missing_Child_Finder/assets/57060900/8038c79d-49cc-427c-a257-918e042e6c3a">
The system processes the uploaded image, detects the face within it using face detection algorithms, and extracts facial features. The extracted facial features are encoded into face encodings. The system compares the face encodings of the uploaded image with the face encodings of registered children in the database. If a match is found, the system displays the details of the matched child, including their name, mobile number, and address.
If match not found its show Matching child not found.
<img width="413" alt="image" src="https://github.com/mrpiyushkataria/Missing_Child_Finder/assets/57060900/a6bd0105-affe-4f06-86db-1314f289b20d">


4. User Interface: The user interface is implemented using the Tkinter library in Python. The main window of the application displays two buttons: "Register a Missing Child" and "Search for a Missing Child." Clicking on these buttons opens new windows where users can enter the necessary information or upload images. The user interface provides a user-friendly and intuitive way for users to interact with the system.
