# Cloud-Based Article CMS Using Flask and Azure

## 1. Project Overview

This project is a **Cloud-Based Content Management System (CMS)** developed using **Python Flask** and deployed with cloud services provided by **Microsoft Azure**. The application allows authenticated users to create, manage, and view articles with images. All article data is stored in **Azure SQL Database**, while uploaded images are stored in **Azure Blob Storage**.

The system provides basic CMS functionality including:

- User registration and login
- Secure authentication
- Article creation with title, author, body, and image
- Image upload to cloud storage
- Article storage and retrieval from cloud database

The project demonstrates how modern web applications integrate **backend frameworks, cloud databases, and object storage systems**.

---

# 2. Technologies Used

## Backend

- Python  
- Flask Framework  
- SQLAlchemy ORM  
- Werkzeug Security  

## Cloud Services

- Azure SQL Database  
- Azure Blob Storage  

## Frontend

- HTML  
- CSS  

## Database

- Microsoft SQL Server (Azure SQL)

---

# 3. System Architecture

The system consists of the following components:

## 1. Frontend Layer

- HTML and CSS interface  
- Allows users to submit article data and images.

## 2. Backend Layer

- Flask application handles routing, authentication, and data processing.  
- SQLAlchemy ORM interacts with the Azure SQL database.

## 3. Cloud Storage Layer

- Azure Blob Storage stores uploaded images.  
- Each image receives a unique URL after upload.

## 4. Database Layer

- Azure SQL Database stores structured article and user data.

The architecture ensures scalability and secure storage using cloud infrastructure.

---

# 4. Application Workflow

The application works through the following steps:

## User Registration

A new user registers with username, email, and password. Passwords are securely hashed before storing them in the database.

## User Login

Registered users log in using their credentials. Flask sessions maintain authentication.

## Article Creation

Users can create a new article by entering:

- Title  
- Author  
- Body content  
- Image file  

## Image Upload

The image file is uploaded to Azure Blob Storage. A unique filename is generated using UUID to avoid conflicts.

## Database Storage

Article details along with the image URL are stored in the Azure SQL Database.

## Display Articles

All stored articles are retrieved from the database and displayed on the homepage.

---

# 5. Database Design

## User Table

| Column | Description |
|------|-------------|
| id | Primary key |
| username | Unique username |
| email | Unique email |
| password | Hashed password |

## Post Table

| Column | Description |
|------|-------------|
| id | Primary key |
| title | Article title |
| author | Article author |
| content | Article body text |
| image_url | URL of uploaded image |

---

# 6. Key Features

- Secure user authentication  
- Password hashing for security  
- Cloud-based image storage  
- Scalable database infrastructure  
- Simple CMS interface  
- Article publishing capability  

---

# 7. Security Implementation

The application implements several security practices:

- Password hashing using Werkzeug security utilities  
- Secure user session management  
- Unique constraints on username and email  
- Cloud-based storage for secure file handling  

These practices help protect user credentials and ensure secure data management.

---

# 8. Advantages of Using Cloud Services

Using Microsoft Azure provides several benefits:

- High scalability for growing applications  
- Reliable cloud infrastructure  
- Secure storage services  
- Easy integration with web applications  
- Reduced dependency on local servers  

Cloud platforms also improve availability and simplify deployment.

---

# 9. Future Enhancements

The project can be extended with additional CMS features such as:

- Edit and delete articles  
- Comment system  
- Rich text editor for article formatting  
- User profile management  
- Image preview before upload  
- Full deployment using Azure App Service  

These enhancements would improve usability and expand CMS functionality.

---

# 10. Deployment Resource Analysis

To deploy this application on Azure, two major compute services were evaluated:

- **Azure Virtual Machine (VM)**
- **Azure App Service**

Both services support hosting Python web applications but differ in cost, scalability, availability, and workflow management.

---

## Cost Analysis

| Service | Cost Characteristics |
|------|----------------|
| Azure Virtual Machine | VM pricing depends on CPU, RAM, and storage configuration. For example, a small B1s VM costs approximately \$13–\$15 per month, but additional costs may apply for storage, networking, and system maintenance. |
| Azure App Service | App Service provides tier-based pricing. The Basic tier starts around \$13 per month and includes infrastructure management handled by Azure. |

Although both options have similar starting costs, App Service reduces operational overhead.

---

## Scalability Analysis

| Service | Scalability |
|------|-------------|
| Azure Virtual Machine | Scaling requires manual resizing of the VM or creating additional VMs with load balancing. |
| Azure App Service | App Service supports automatic scaling based on traffic and application demand. |

App Service provides more convenient and efficient scaling for web applications.

---

## Availability Analysis

| Service | Availability |
|------|--------------|
| Azure Virtual Machine | Requires configuring availability sets or zones to ensure high availability and fault tolerance. |
| Azure App Service | Provides built-in high availability managed by the Azure platform. |

App Service offers better default reliability without additional configuration.

---

## Workflow Analysis

| Service | Workflow |
|------|----------|
| Azure Virtual Machine | Developers must manage the operating system, install dependencies, apply security patches, and configure the web server environment. |
| Azure App Service | Developers only deploy the application code while Azure manages the underlying infrastructure and runtime environment. |

App Service simplifies development and deployment workflows.

---

# 11. Deployment Decision

For this CMS application, **Azure App Service is the preferred deployment option**. It provides a fully managed environment that simplifies deployment and reduces infrastructure management tasks. Since the application is a Python Flask web application, App Service offers built-in support for hosting web applications while allowing easy scaling and monitoring.

Using App Service allows developers to focus on application development rather than managing servers and infrastructure.

---

# 12. When the Decision Might Change

The decision to use Azure App Service could change if the application required **greater control over the operating system or custom server configurations**. In such cases, an **Azure Virtual Machine** would be more appropriate because it allows full access to the server environment and installation of custom software.

If the application required specialized runtime environments, custom networking configurations, or advanced system-level control, deploying it on a Virtual Machine would provide the necessary flexibility.

---

# 13. Conclusion

This project demonstrates how a modern web application can be built using **Flask and Azure cloud services**. By integrating a relational database with object storage, the system efficiently manages both structured article data and media files.

The CMS provides a practical example of **cloud-based web development**, combining backend frameworks, secure authentication, and scalable cloud infrastructure. This project forms a strong foundation for building more advanced cloud-native applications.