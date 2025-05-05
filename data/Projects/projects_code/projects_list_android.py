# Andriod Mobile Development

from fuzzywuzzy import process

AndroidProjects = [
    {
        "ID": 1,
        "title": "Student Career And Personality Prediction Android Application",
        "description": "This application helps students assess their capabilities and identify their interests to predict suitable career areas, thereby improving performance and motivation. Recruiters can also use it to determine appropriate job roles for candidates.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Machine Learning", "Data Analysis"],
        "proposed_algorithms": ["Decision Trees", "Neural Networks", "K-Means Clustering"]
    },
    {
        "ID": 2,
        "title": "Online Shopping Android Application",
        "description": "An e-commerce application allowing companies to promote and sell products online, providing consumers with a wider market of products accessible via mobile devices with internet connectivity.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "SQL", "Payment Gateway Integration"],
        "proposed_algorithms": ["Recommendation Systems", "Collaborative Filtering", "Content-Based Filtering"]
    },
    {
        "ID": 3,
        "title": "Android Based Complaint Management System",
        "description": "An application that allows the public to post petitions or complaints, track their status, and get them resolved efficiently without bribery.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "RESTful APIs", "SQL"],
        "proposed_algorithms": ["Classification", "Clustering", "Natural Language Processing"]
    },
    {
        "ID": 4,
        "title": "Disease Prediction Android Application using Machine Learning",
        "description": "An application using patient treatment history and health data to predict diseases through data mining and machine learning techniques, utilizing big data technology for improved accuracy.",
        "category": "Android Mobile Development, Machine Learning",
        "required_skills": ["Java", "Android Studio", "Machine Learning", "Big Data"],
        "proposed_algorithms": ["Deep Learning", "Random Forest", "Support Vector Machines"]
    },
    {
        "ID": 5,
        "title": "Android Password Based Remote Door Opener System Project",
        "description": "A secure door opening system controlled by entering a password through an Android application, useful for security personnel who need to operate doors without manual intervention.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Password Authentication", "Bluetooth Communication"]
    },
    {
        "ID": 6,
        "title": "Home Appliance Control Using Android Application",
        "description": "An application to control electrical loads via Bluetooth input signals received from an Android device, beneficial for elderly and handicapped individuals.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Load Control"]
    },
    {
        "ID": 7,
        "title": "Robot Controlled By Android Application",
        "description": "A robotic vehicle controlled remotely via an Android device, with Bluetooth communication for command transmission and 8051 microcontroller for operation.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Motor Control"]
    },
    {
        "ID": 8,
        "title": "Android Controlled Remote AC Power Control",
        "description": "An application to control AC power applied to a load by adjusting the firing angle of a thyristor via an Android device, ensuring efficient power supply control.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Power Control"]
    },
    {
        "ID": 9,
        "title": "Android Controlled Remote Password Security",
        "description": "A security system that allows authorized personnel to change and enter passwords remotely through an Android application, enhancing organizational security.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Password Authentication", "Bluetooth Communication"]
    },
    {
        "ID": 10,
        "title": "Density Based Traffic Controlling System With Android Override",
        "description": "A traffic signal system that overrides normal signal timings during emergencies, using an Android application to give priority signals in high-density or emergency situations.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Density Measurement"]
    },
    {
        "ID": 11,
        "title": "Android Controlled Notice Board Project",
        "description": "An electronic notice board controlled by an Android device via Bluetooth, displaying messages on an LCD screen for use in colleges, offices, and public places.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Display Control"]
    },
    {
        "ID": 12,
        "title": "Android Based Home Automation System",
        "description": "An application to control electrical loads via Bluetooth signals received from an Android device, making it easier for aged or handicapped individuals to operate home appliances.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Load Control"]
    },
    {
        "ID": 13,
        "title": "DC Motor Speed Control By Android",
        "description": "A system to control the speed and direction of a DC motor using commands sent from an Android device via Bluetooth, with 8051 microcontroller for operation.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Motor Control"]
    },
    {
        "ID": 14,
        "title": "Programmable Sequential Load Operation Controlled By Android Application Project",
        "description": "A system to switch industrial loads sequentially using an Android application, providing a cost-effective alternative to programmable logic controllers.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Sequential Control", "Load Switching"]
    },
    {
        "ID": 15,
        "title": "Android Controlled Automobile",
        "description": "A battery-powered automobile controlled wirelessly through an Android application, using Bluetooth for command transmission and 8051 microcontroller for operation.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Motor Control"]
    },
    {
        "ID": 16,
        "title": "Android Controlled Fire Fighter Robot",
        "description": "A fire-fighting robotic vehicle controlled via an Android application, equipped with a water tank and pump, and operated using Bluetooth commands and 8051 microcontroller.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Water Pump Control"]
    },
    {
        "ID": 17,
        "title": "Android Controlled Spy Robot With Night Vision Camera",
        "description": "A robotic vehicle equipped with a night vision camera for remote monitoring, controlled via an Android application, with Bluetooth communication and 8051 microcontroller.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Camera Control"]
    },
    {
        "ID": 18,
        "title": "Android Military Spying & Bomb Disposal Robot",
        "description": "A robotic vehicle and arm for high-risk operations, equipped with a night vision camera, controlled via an Android application, using Bluetooth and 8051 microcontroller.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Robotic Arm Control"]
    },
    {
        "ID": 19,
        "title": "Android Controlled Pick And Place Robotic Arm Vehicle Project",
        "description": "A pick-and-place robotic arm mounted on a vehicle, controlled wirelessly via an Android application using Bluetooth and 8051 microcontroller for operation.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Robotic Arm Control"]
    },
    {
        "ID": 20,
        "title": "Voice Controlled Robotic Vehicle",
        "description": "A robotic vehicle controlled through voice commands received via an Android application, with Bluetooth communication and 8051 microcontroller for operation.",
        "category": "Android Mobile Development",
        "required_skills": ["Java", "Android Studio", "Bluetooth", "Speech Recognition", "8051 Microcontroller"],
        "proposed_algorithms": ["Signal Processing", "Speech Recognition"]
    },
    {
        "title": "Tab Based Library Book Availability & Location Finder On Wifi",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A tab-based system for large libraries to assist users at the librarian counter by showing book availability and location. If unavailable, it provides return dates. The system allows users to search for books by category and includes an admin server/PC for management.",
        "skills_required": ["Android Studio", "Java", "SQL"],
        "proposed_algorithms": ["Database Management", "Information Retrieval"]
    },
    {
        "title": "Railway Tracking and Arrival Time Prediction",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A system for tracking trains and predicting arrival times. It tracks train timings and updates the schedule at subsequent stations. The system handles delays and adjusts the timing information accordingly.",
        "skills_required": ["Java", "Android Studio", "Database Management"],
        "proposed_algorithms": ["Time Series Analysis", "Prediction Models"]
    },
    {
        "title": "Android Smart City Traveler",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An application to help travelers create schedules for exploring a city based on their preferences and available time. Developed in Java for Android and ASP.NET for the web portal.",
        "skills_required": ["Java", "ASP.NET", "Database Management"],
        "proposed_algorithms": ["Recommendation Systems", "Scheduling Algorithms"]
    },
    {
        "title": "Android Campus Portal With Graphical Reporting",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A student portal for managing and accessing student information. The web interface is used by admins for management, and the Android application is used by students for accessing information and helpdesk services.",
        "skills_required": ["ASP.NET", "C#", "Java"],
        "proposed_algorithms": ["Data Management", "Reporting Tools"]
    },
    {
        "title": "Card Payment Security Using RSA",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development"],
        "description": "An encryption system for secure card payments using the RSA algorithm. It ensures that transaction data is securely stored and transmitted, protecting against unauthorized access.",
        "skills_required": ["Java", "RSA Algorithm"],
        "proposed_algorithms": ["Asymmetric Encryption", "Data Security"]
    },
    {
        "title": "E Authentication System Using QR Code & OTP",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A secure authentication system using QR codes and OTPs. It provides resistance to shoulder surfing and accidental logins. Users register and log in using QR codes and OTPs.",
        "skills_required": ["Java", "Web Development", "OTP Systems"],
        "proposed_algorithms": ["QR Code Generation", "OTP Authentication"]
    },
    {
        "title": "Android Joystick Application",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development"],
        "description": "An application that turns an Android phone into a joystick to control PC keyboard functions. It supports button mapping for gaming or other PC functions.",
        "skills_required": ["Java", "Android Studio"],
        "proposed_algorithms": ["Input Mapping", "User Interface Design"]
    },
    {
        "title": "Android Based Parking Booking System",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A system for reserving parking spaces online. Users can view available spaces and book them for specific time slots. It includes features for viewing and canceling bookings.",
        "skills_required": ["Java", "Web Development", "Database Management"],
        "proposed_algorithms": ["Reservation Management", "User Interface Design"]
    },
    {
        "title": "Android Places Finder Project",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development"],
        "description": "An application for finding places based on server-stored data. Users can search for places and add new ones with details such as location and description.",
        "skills_required": ["Java", "Android Studio"],
        "proposed_algorithms": ["Search Algorithms", "Data Management"]
    },
    {
        "title": "Grocery Shopping Android",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An online grocery shopping application that allows users to browse, add items to their cart, and make secure payments. The system manages product and order data on the server side.",
        "skills_required": ["Java", "Web Development", "Payment Integration"],
        "proposed_algorithms": ["E-commerce Systems", "Transaction Management"]
    },
    {
        "title": "Android AI Diet Consultant",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Artificial Intelligence & ML", "Web", "Desktop Application"],
        "description": "An AI-based diet consultant that provides personalized diet plans based on user data such as body type, weight, and height. It acts similarly to a human dietitian.",
        "skills_required": ["Java", "AI/ML", "Android Studio"],
        "proposed_algorithms": ["Personalized Recommendations", "Diet Planning Algorithms"]
    },
    {
        "title": "Android Voting System",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An application for casting votes using mobile devices. It allows users to vote on various issues and provides admins with vote counts and reports.",
        "skills_required": ["Java", "Web Development", "Database Management"],
        "proposed_algorithms": ["Voting Systems", "Data Aggregation"]
    },
    {
        "title": "Android Graphical Information System",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An application for searching and adding places on a map. Users can input new places and their details, including images, to the system.",
        "skills_required": ["Java", "Android Studio", "GIS"],
        "proposed_algorithms": ["Geographic Information Systems", "Data Entry"]
    },
    {
        "title": "Android Bluetooth Chat",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Sensor"],
        "description": "A Bluetooth-based chat application allowing users to create profiles, chat with a server, and transfer text files. The system maintains chat history.",
        "skills_required": ["Java", "Bluetooth Communication"],
        "proposed_algorithms": ["Bluetooth Communication", "Profile Management"]
    },
    {
        "title": "Android Sentence Framer Application",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An application designed to help users frame English sentences using images. It displays categories and uses selected images to generate sentences.",
        "skills_required": ["Java", "Android Studio", "Image Processing"],
        "proposed_algorithms": ["Sentence Generation", "Image Selection"]
    },
    {
        "title": "Android Pc Controller Using Wifi",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Sensor"],
        "description": "An application that turns an Android phone into a PC mouse and keyboard. It allows users to control PC functions through their mobile device.",
        "skills_required": ["Java", "Wi-Fi Communication"],
        "proposed_algorithms": ["Remote Control", "Input Mapping"]
    },
    {
        "title": "Student Faculty Document Sharing Android Project",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "An online portal for document sharing between students and faculty. Faculty upload documents to a web server, and students access them through an Android app.",
        "skills_required": ["Java", "Web Development", "Document Management"],
        "proposed_algorithms": ["Document Sharing", "Access Control"]
    },
    {
        "title": "Android Local Train Ticketing Project",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "BSC IT & BCA", "BSC IT & BSC CS", "MCA", "MSC IT", "Web", "Desktop Application"],
        "description": "A ticketing system for local trains that allows users to book and print tickets online. It includes login for users and admins and supports ticket booking with source and destination selection.",
        "skills_required": ["Java", "Web Development", "Ticket Management"],
        "proposed_algorithms": ["Ticketing Systems", "Location Management"]
    },
    {
        "title": "Smart Android Graphical Password Strategy",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A graphical password system using patterns on a grid of fruit images. Users register a pattern as their password, which changes the positions of fruits for added security.",
        "skills_required": ["Java", "Android Studio"],
        "proposed_algorithms": ["Pattern Recognition", "Security Protocols"]
    },
    {
        "title": "Vehicle Tracking Using Driver Mobile Gps Tracking",
        "category": "Android Mobile Development",
        "technologies_used": ["Android Mobile development", "Web", "Desktop Application"],
        "description": "A GPS-based vehicle tracking system that tracks and reports the location of vehicles to admins. It can be used in call taxis to monitor driver locations.",
        "skills_required": ["Java", "GPS Tracking", "Web Development"],
        "proposed_algorithms": ["GPS Tracking", "Location Reporting"]
    },
    {
    "ID": "1",
    "title": "Android Employee Tracker",
    "description": "A system that combines a web and android application where field employees use the android app and admins/HR use the web app. The employee's image and GPS location are captured and sent to the admin every 5 minutes, providing real-time tracking.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking", "Web Development"],
    "proposed_algorithms": ["Image Capture", "Location Tracking"]
    },
    {
    "ID": "2",
    "title": "Geo Trends Classification Over Maps Android",
    "description": "An android app that allows users to comment on trends with their GPS location tagged. Admins can view these locations through a web application, and users can use hashtags to categorize trends.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking", "Web Development"],
    "proposed_algorithms": ["Geotagging", "Trend Analysis"]
  },
  {
    "ID": "3",
    "title": "Your Personal Nutritionist Using FatSecret API",
    "description": "An app that uses the FatSecret API to provide nutritional information, recipe suggestions, and diet planning to users. It helps users make informed decisions about their diet.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "API Integration"],
    "proposed_algorithms": ["Nutritional Analysis", "Recipe Recommendation"]
  },
  {
    "ID": "4",
    "title": "Voice Assistant For Visually Impaired",
    "description": "An innovative voice assistant app designed to help visually impaired individuals interact with their phones using voice commands. It includes features like message reading, call logging, and battery level checking.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Speech Recognition"],
    "proposed_algorithms": ["Speech-to-Text", "Voice Commands"]
  },
  {
    "ID": "5",
    "title": "Android File Manager Application Project",
    "description": "A file manager app with features for moving, sharing, compressing, and streaming files. It also integrates with cloud storage and includes tools for file management.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "File Management", "Cloud Integration"],
    "proposed_algorithms": ["File Compression", "Cloud Sync"]
  },
  {
    "ID": "6",
    "title": "Android Smart City Traveler",
    "description": "An app that creates travel schedules for users based on their preferences and time available. It uses Java for Android and ASP.NET for the web portal.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Java", "ASP.NET"],
    "proposed_algorithms": ["Travel Scheduling", "Preference Analysis"]
  },
  {
    "ID": "7",
    "title": "Android Graphical Image Password Project",
    "description": "A security system that allows users to set a picture-based password. The picture is divided into parts that must be selected in the correct order for authentication.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Image Processing"],
    "proposed_algorithms": ["Image Segmentation", "Pattern Recognition"]
  },
  {
    "ID": "8",
    "title": "Android Based School Bus Tracking System",
    "description": "An application where drivers use the android app and admins/parents use the web app to track school buses in real-time. GPS coordinates are tracked and stored every 5 minutes.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking", "Web Development"],
    "proposed_algorithms": ["Real-time Tracking", "Location Storage"]
  },
  {
    "ID": "9",
    "title": "Android Attendance System",
    "description": "An app designed for school/college faculty to take attendance using their phones, reducing paper use and saving time. It includes features for creating attendance sheets and marking attendance.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Database Management"],
    "proposed_algorithms": ["Attendance Tracking", "Data Management"]
  },
  {
    "ID": "10",
    "title": "Android Text Encryption Using Various Algorithms",
    "description": "An app that provides text encryption and decryption using algorithms such as AES, DES, and MD5. Users can encrypt their messages before sending them through communication apps.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Encryption", "Security"],
    "proposed_algorithms": ["AES", "DES", "MD5"]
  },
  {
    "ID": "11",
    "title": "Cooperative Housing Society Manager Project",
    "description": "A web portal for managing housing societies, including bill calculation, member queries, and automated functionality for billing and receipts.",
    "category": "Android Mobile development",
    "required_skills": ["Web Development", "Database Management", "Networking"],
    "proposed_algorithms": ["Automated Billing", "Query Management"]
  },
  {
    "ID": "12",
    "title": "Advanced Intelligent Tourist Guide",
    "description": "An application that provides place recommendations based on user preferences, including details about places, images, and tags. It uses Asp.NET for the web part and a database for storing place information.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Web Development", "Database Management"],
    "proposed_algorithms": ["Recommendation System", "Preference Matching"]
  },
  {
    "ID": "13",
    "title": "Intelligent Tourist Guide",
    "description": "A system that helps users find paths to tourist attractions based on their criteria such as museums, historical objects, and restaurants. It is designed for use on mobile devices with GPS.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Navigation"],
    "proposed_algorithms": ["Pathfinding", "Criteria Matching"]
  },
  {
    "ID": "14",
    "title": "Online Pizza Ordering System",
    "description": "An online ordering system for pizza that allows users to select pizzas, make payments, and reduces miscommunication and ordering time.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "E-commerce", "Payment Integration"],
    "proposed_algorithms": ["Order Management", "Payment Processing"]
  },
  {
    "ID": "15",
    "title": "Automated Payroll With GPS Tracking And Image Capture",
    "description": "A system that tracks employees' GPS location and captures their image during login and logout for payroll purposes. The data is managed via a web application.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking", "Image Capture"],
    "proposed_algorithms": ["GPS Tracking", "Image Processing"]
  },
  {
    "ID": "16",
    "title": "Android Smart Ticketing Using RFID",
    "description": "An advanced ticketing system using RFID for passenger management in buses. It includes an android app for passengers and drivers, and a web app for admins.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "RFID", "Web Development"],
    "proposed_algorithms": ["RFID Ticketing", "Real-time Tracking"]
  },
  {
    "ID": "17",
    "title": "Restaurant Table Booking Android Application",
    "description": "An app for restaurant reservations and table management, allowing diners to book tables online and helping restaurants manage their bookings more efficiently.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Reservation Management"],
    "proposed_algorithms": ["Table Management", "Reservation System"]
  },
  {
    "ID": "18",
    "title": "Child Monitoring System App",
    "description": "An app for tracking children's location and monitoring their call logs, messages, and contacts using GPS and telephony services.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking", "Telephony Services"],
    "proposed_algorithms": ["Location Tracking", "Data Monitoring"]
  },
  {
    "ID": "19",
    "title": "Android Geo Fencing App Project",
    "description": "An app that allows parents to set a geo-fence around their child's location and track them using GPS. It includes features for creating and updating geo-fences.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "GPS Tracking"],
    "proposed_algorithms": ["Geo-fencing", "Location Tracking"]
  },
  {
    "ID": "20",
    "title": "Railway Ticket Booking System Using Qr Code",
    "description": "A smart ticket booking system that uses QR codes for tickets. The system validates tickets using GPS and stores user information in a secure SQL database.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "QR Code Integration", "Database Management"],
    "proposed_algorithms": ["QR Code Generation", "GPS Validation"]
  },
  {
    "ID": "21",
    "title": "Mobile Based Attendance System",
    "description": "An app that allows teachers to mark attendance via their mobile devices. It includes features for viewing and managing student attendance records.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "Database Management"],
    "proposed_algorithms": ["Attendance Tracking", "Data Management"]
  },
  {
    "ID": "1",
    "title": "A Location- and Diversity-aware News Feed System for Mobile Users",
    "description": "A location-aware news feed system that allows users to share geo-tagged messages and receive nearby messages relevant to them. It includes location prediction, relevance measure, and a news feed scheduler.",
    "category": "Android Mobile development",
    "required_skills": ["Location Prediction", "Relevance Measure", "News Feed Scheduling"],
    "proposed_algorithms": ["Location Prediction Algorithm", "Vector Space Model", "News Feed Scheduling"]
  },
  {
    "ID": "2",
    "title": "Design of a Secured E-voting System",
    "description": "An e-voting system that ensures security through homomorphic encryption and blind signature schemes, implemented on an embedded system with RFID for voter eligibility verification.",
    "category": "Android Mobile development",
    "required_skills": ["E-voting Security", "Homomorphic Encryption", "Blind Signature", "RFID"],
    "proposed_algorithms": ["Homomorphic Encryption", "Blind Signature Scheme"]
  },
  {
    "ID": "3",
    "title": "Shopping Application System With Near Field Communication (NFC) Based on Android",
    "description": "A mobile shopping application that integrates NFC technology for seamless transactions, allowing users to make payments without carrying cash.",
    "category": "Android Mobile development",
    "required_skills": ["NFC Integration", "Mobile Commerce", "Payment Systems"],
    "proposed_algorithms": ["NFC Technology", "Payment Processing"]
  },
  {
    "ID": "4",
    "title": "Developing an Android Based Learning Application for Mobile Devices",
    "description": "A learning application that connects Android devices with Moodle, offering features like alerts, file downloads, chats, forums, and grade management through REST and JSON.",
    "category": "Android Mobile development",
    "required_skills": ["Android Development", "REST API", "JSON", "Moodle Integration"],
    "proposed_algorithms": ["REST API Integration", "Client-Server Architecture"]
  },
  {
    "ID": "5",
    "title": "Location Based Reminder Using GPS For Mobile",
    "description": "A location-based reminder system that uses GPS to trigger reminders based on user location. The system addresses context management and service triggers.",
    "category": "Android Mobile development",
    "required_skills": ["GPS Tracking", "Context Management", "Service Trigger Mechanism"],
    "proposed_algorithms": ["Context Management", "Service Trigger Mechanism"]
  },
  {
    "ID": "6",
    "title": "Location Based Services using Android Mobile Operating System",
    "description": "A location-based information system that provides personalized and real-time data using Android devices. Applications include security, traffic surveys, and surveillance.",
    "category": "Android Mobile development",
    "required_skills": ["Location-Based Services", "Android Development", "Real-Time Data"],
    "proposed_algorithms": ["Real-Time Location Tracking", "Personalized Information"]
  },
  {
    "ID": "7",
    "title": "OCRAndroid: A Framework to Digitize Text Using Mobile Phones",
    "description": "A framework for developing OCR-based applications on Android phones, combining image preprocessing and an OCR engine. Demonstrates with PocketPal and PocketReader applications.",
    "category": "Android Mobile development",
    "required_skills": ["OCR", "Image Processing", "Android Development"],
    "proposed_algorithms": ["Image Preprocessing", "Optical Character Recognition"]
  },
  {
    "ID": "8",
    "title": "Mobile Phone Based Drunk Driving Detection",
    "description": "A system for detecting drunk driving using a mobile phone's accelerometer and orientation sensor. The phone detects dangerous maneuvers and alerts the driver or calls for help.",
    "category": "Android Mobile development",
    "required_skills": ["Accelerometer", "Orientation Sensor", "Driving Pattern Analysis"],
    "proposed_algorithms": ["Accelerometer Data Analysis", "Driving Pattern Recognition"]
  },
  {
    "ID": "9",
    "title": "Android Based Elimination of Potholes",
    "description": "A web-based project where users can report potholes by uploading images. The system allows for user credentials, complaint tracking, and administrative management.",
    "category": "Android Mobile development",
    "required_skills": ["Image Upload", "Web Management", "User Authentication"],
    "proposed_algorithms": ["Image Submission", "Complaint Management"]
  },
  {
    "ID": "10",
    "title": "A Personalized Mobile Search Engine",
    "description": "A personalized search engine that uses user preferences and GPS location to adapt search results. It balances content and location concepts with an ontology-based profile.",
    "category": "Android Mobile development",
    "required_skills": ["Search Engine Design", "Ontology-Based Profiling", "Location-Based Services"],
    "proposed_algorithms": ["Personalized Ranking", "Concept Classification"]
  },
  {
    "ID": "11",
    "title": "Designing the Next Generation of Mobile Tourism Application based on Situation Awareness",
    "description": "A mobile tourism application designed to improve travelers' situation awareness. It uses context awareness to enhance pre-visit and visit phases for better travel experiences.",
    "category": "Android Mobile development",
    "required_skills": ["Context Awareness", "Tourism Application Design", "User Experience"],
    "proposed_algorithms": ["Context Awareness", "Situation Awareness Enhancement"]
  },
    {
        "ID": "16",
        "title": "Voice Based Notice Board Using Android",
        "description": "This project presents an innovative Android-based notice display system where users can display notices without typing them manually. The announcer speaks the message through an Android phone, which is then wirelessly transferred and displayed on an LCD screen interfaced with an 8051 microcontroller.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "8051 Microcontroller", "Bluetooth Communication"],
        "proposed_algorithms": ["Speech Recognition", "Wireless Data Transmission"]
    },
    {
        "ID": "17",
        "title": "Android Antenna Positioning System",
        "description": "An Android-based system for positioning antennas using an application. The system uses an 8051 microcontroller, LCD screen, and stepper motor to position the antenna accurately based on user commands received through a Bluetooth receiver.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "8051 Microcontroller", "Stepper Motors", "Bluetooth Communication"],
        "proposed_algorithms": ["Angle Calculation", "Motor Control"]
    },
    {
        "ID": "18",
        "title": "Android Circuit Breaker",
        "description": "A password-based circuit breaker system controlled through an Android application. It enhances safety by allowing line men to control circuit breakers remotely, ensuring they can safely perform maintenance tasks.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "8051 Microcontroller", "Password Security"],
        "proposed_algorithms": ["Password Verification", "Circuit Control"]
    },
    {
        "ID": "19",
        "title": "Android Controlled Wildlife Observation Robot",
        "description": "A robot controlled via an Android phone for safe wildlife observation. It features a wireless camera and is equipped with an 8051 microcontroller to process user commands sent through Bluetooth.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "8051 Microcontroller", "Wireless Camera", "Bluetooth Communication"],
        "proposed_algorithms": ["Camera Streaming", "Wireless Control"]
    },
    {
        "ID": "20",
        "title": "Mobile Banking Project",
        "description": "A mobile banking application that allows users to perform various banking functions such as checking balance, transferring funds, and requesting checkbooks, all from their mobile phones.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "J2ME", "Mobile Banking"],
        "proposed_algorithms": ["Transaction Management", "Balance Enquiry"]
    },
    {
        "ID": "21",
        "title": "Driver Card With QR Code Identification",
        "description": "A system that tracks driver activities using QR code identification. Each driver scans a unique QR code upon arrival and departure to record working hours and calculate monthly pay.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "QR Code Scanning", "Database Management"],
        "proposed_algorithms": ["QR Code Recognition", "Time Tracking"]
    },
    {
        "ID": "22",
        "title": "Mobile(location based) Advertisement System",
        "description": "A system that provides location-based advertisements using Bluetooth technology. It broadcasts data to mobile devices within a specific area without requiring client-side software installation.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "Bluetooth Communication", "Location-Based Services"],
        "proposed_algorithms": ["Data Broadcasting", "Location Detection"]
    },
    {
        "ID": "23",
        "title": "Hotel Reservation Android",
        "description": "An Android application for booking hotel rooms. Users can view room availability, make online payments, and receive booking confirmations, including additional facilities like Jacuzzi and swimming pool.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "Online Payment Integration", "Database Management"],
        "proposed_algorithms": ["Room Availability Checking", "Payment Processing"]
    },
    {
        "ID": "24",
        "title": "Student Attendance System By QR Scan",
        "description": "A system that uses QR codes for student attendance tracking. Students scan their QR codes, which record the time and date of scanning in a database, automating attendance management.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "QR Code Scanning", "Database Management"],
        "proposed_algorithms": ["QR Code Recognition", "Attendance Recording"]
    },
    {
        "ID": "25",
        "title": "WiFi Shopping Guide Project",
        "description": "An online shopping system that provides users with various packages and offers. It includes features for user registration, login, and product browsing, all through an effective graphical interface.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "WiFi Connectivity", "E-commerce"],
        "proposed_algorithms": ["Product Browsing", "Offer Management"]
    },
    {
        "ID": "26",
        "title": "Mobile Quiz Through WiFi Project",
        "description": "An Android application that facilitates playing quizzes over WiFi. It features an admin interface for managing questions and answers, and users receive quiz questions on their devices.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "WiFi Connectivity", "Quiz Management"],
        "proposed_algorithms": ["Quiz Question Distribution", "Answer Evaluation"]
    },
    {
        "ID": "27",
        "title": "Android Merchant Application Using QR",
        "description": "A QR code-based application for cashless transactions between merchants and consumers. It includes two apps: one for merchants to scan QR codes and one for consumers to generate them.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "QR Code Scanning", "Payment Integration"],
        "proposed_algorithms": ["QR Code Scanning", "Transaction Processing"]
    },
    {
        "ID": "28",
        "title": "Bus Pass Android Project",
        "description": "An Android application for managing bus pass information. Users can apply for pass renewal, cancellation, and make payments online while viewing routes and schemes.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "Online Payment Integration", "Route Management"],
        "proposed_algorithms": ["Pass Management", "Payment Processing"]
    },
    {
        "ID": "29",
        "title": "Mobile Attendance System Project",
        "description": "An automated attendance system for schools and colleges using an Android app. It allows faculty to create and manage attendance sheets, mark attendance, and reduce paper usage.",
        "category": "Android Mobile Development",
        "required_skills": ["Android Development", "Attendance Management", "Database Management"],
        "proposed_algorithms": ["Attendance Tracking", "Data Management"]
    }
]

# adding indices
for i,app in enumerate(AndroidProjects):
    app['ID'] = i+1



## Adding the links to the right AndroidProjects

# links extracted from website using beatifulsoup
links = [
"https://projectideas.co.in/student-career-and-personality-prediction-android-application/",
"https://projectideas.co.in/online-shopping-android-application/",
"https://projectideas.co.in/android-based-complaint-management-system/",
"https://projectideas.co.in/disease-prediction-android-application-using-machine-learning/",
"https://projectideas.co.in/android-password-based-remote-door-opener-system-project/",
"https://projectideas.co.in/home-appliance-control-using-android-application/",
"https://projectideas.co.in/robot-controlled-by-android-application/",
"https://projectideas.co.in/android-controlled-remote-ac-power-control/",
"https://projectideas.co.in/android-controlled-remote-password-security/",
"https://projectideas.co.in/density-based-traffic-controlling-system-with-android-override/",
"https://projectideas.co.in/android-controlled-notice-board-project/",
"https://projectideas.co.in/android-based-home-automation-system/",
"https://projectideas.co.in/dc-motor-speed-control-by-android/",
"https://projectideas.co.in/programmable-sequential-load-operation-controlled-by-android-application-project/",
"https://projectideas.co.in/android-controlled-automobile/",
"https://projectideas.co.in/android-controlled-fire-fighter-robot/",
"https://projectideas.co.in/android-controlled-spy-robot-with-night-vision-camera/",
"https://projectideas.co.in/android-military-spying-bomb-disposal-robot/",
"https://projectideas.co.in/android-controlled-pick-and-place-robotic-arm-vehicle-project/",
"https://projectideas.co.in/voice-controlled-robotic-vehicle/",
"https://projectideas.co.in/voice-based-notice-board-using-android/",
"https://projectideas.co.in/android-antenna-positioning-system/",
"https://projectideas.co.in/android-circuit-breaker/",
"https://projectideas.co.in/android-controlled-wildlife-observation-robot/",
"https://projectideas.co.in/mobile-banking-project-dotnet/",
"https://projectideas.co.in/driver-card-with-qr-code-identification-dotnet/",
"https://projectideas.co.in/mobile-location-based-advertisement-system-dotnet/",
"https://projectideas.co.in/hotel-reservation-android-dotnet/",
"https://projectideas.co.in/student-attendance-system-by-qr-scan-dotnet/",
"https://projectideas.co.in/wifi-shopping-guide-project-dotnet-dotnet/",
"https://projectideas.co.in/mobile-quiz-through-wifi-project-dotnet/",
"https://projectideas.co.in/android-merchant-application-using-qr-dotnet/",
"https://projectideas.co.in/bus-pass-android-project-dotnet/",
"https://projectideas.co.in/mobile-attendance-system-project-dotnet/",
"https://projectideas.co.in/tab-based-library-book-availability-location-finder-on-wifi-dotnet/",
"https://projectideas.co.in/railway-tracking-and-arrival-time-prediction-dotnet/",
"https://projectideas.co.in/android-smart-city-traveler-dotnet/",
"https://projectideas.co.in/android-campus-portal-with-graphical-reporting-dotnet/",
"https://projectideas.co.in/card-payment-security-using-rsa-dotnet/",
"https://projectideas.co.in/e-authentication-system-using-qr-code-otp-dotnet/",
"https://projectideas.co.in/android-joystick-application-android/",
"https://projectideas.co.in/android-based-parking-booking-system-android/",
"https://projectideas.co.in/android-places-finder-project-android/",
"https://projectideas.co.in/grocery-shopping-android-android/",
"https://projectideas.co.in/android-ai-diet-consultant-android/",
"https://projectideas.co.in/android-voting-system-android/",
"https://projectideas.co.in/android-graphical-information-system-android/",
"https://projectideas.co.in/android-bluetooth-chat-android/",
"https://projectideas.co.in/android-sentence-framer-application-android/",
"https://projectideas.co.in/android-pc-controller-using-wifi-android/",
"https://projectideas.co.in/student-faculty-document-sharing-android-project-android/",
"https://projectideas.co.in/android-local-train-ticketing-project-android/",
"https://projectideas.co.in/smart-android-graphical-password-strategy-android/",
"https://projectideas.co.in/vehicle-tracking-using-driver-mobile-gps-tracking-android/",
"https://projectideas.co.in/android-employee-tracker-android/",
"https://projectideas.co.in/geo-trends-classification-over-maps-android-android/",
"https://projectideas.co.in/your-personal-nutritionist-using-fatsecret-api-android/",
"https://projectideas.co.in/voice-assistant-for-visually-impaired-android/",
"https://projectideas.co.in/android-file-manager-application-project-android/",
"https://projectideas.co.in/android-smart-city-traveler-android/",
"https://projectideas.co.in/android-graphical-image-password-project-android/",
"https://projectideas.co.in/android-based-school-bus-tracking-system-android/",
"https://projectideas.co.in/android-attendance-system-android/",
"https://projectideas.co.in/android-text-encryption-using-various-algorithms-android/",
"https://projectideas.co.in/cooperative-housing-society-manager-project-ideas/",
"https://projectideas.co.in/advanced-intelligent-tourist-guide-project-ideas/",
"https://projectideas.co.in/intelligent-tourist-guide-project-ideas/",
"https://projectideas.co.in/online-pizza-ordering-system-project-ideas/",
"https://projectideas.co.in/automated-payroll-gps-tracking-image-capture/",
"https://projectideas.co.in/android-smart-ticketing-using-rfid/",
"https://projectideas.co.in/restaurant-table-booking-android-application/",
"https://projectideas.co.in/child-monitoring-system-app/",
"https://projectideas.co.in/android-geo-fencing-app-project/",
"https://projectideas.co.in/railway-ticket-booking-system-using-qr-code/",
"https://projectideas.co.in/mobile-based-attendance-system/",
"https://projectideas.co.in/location-diversity-aware-news-feed-system-mobile-users/",
"https://projectideas.co.in/design-secured-e-voting-system/",
"https://projectideas.co.in/shopping-application-system-near-field-communication-nfc-based-android/",
"https://projectideas.co.in/developing-android-based-learning-application-mobile-devices/",
"https://projectideas.co.in/location-based-reminder-using-gps-mobile/",
"https://projectideas.co.in/location-based-services-using-android-mobile-operating-system/",
"https://projectideas.co.in/ocrandroid-framework-digitize-text-using-mobile-phones/",
"https://projectideas.co.in/mobile-phone-based-drunk-driving-detection/",
"https://projectideas.co.in/android-based-elimination-potholes/",
"https://projectideas.co.in/personalized-mobile-search-engine/",
"https://projectideas.co.in/designing-next-generation-mobile-tourism-application-based-situation-awareness/"
]


# Dictionary to hold the title and its corresponding URL
title_url_mapping = {}
urls = [link[27:] for link in links]
titles = [d['title'] for d in AndroidProjects]

# Iterate over titles
for title in titles:
    # Find the best match for the title from URLs
    best_match, score = process.extractOne(title, urls)
    # Add to the dictionary if score is high enough
    if score > 80:  # You can adjust the threshold as needed
        title_url_mapping[title] = best_match
        # Remove the best match URL from the list to avoid duplicate matches
        urls.remove(best_match)

# Print the result
for title, url in title_url_mapping.items():
    # print(f"Title: {title}")
    # print(f"URL: {url}\n")
    for proj in AndroidProjects:
        if proj['title']==title:
            proj['URL']= links[0][:27]+url

# print(AndroidProjects[5])
print(len(links)) #86
print(len(AndroidProjects)) #86

from utils import write_selected_dict_values_to_file

write_selected_dict_values_to_file(AndroidProjects, 'AndroidProjects.txt')