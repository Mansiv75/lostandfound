### **📌 LOST & FOUND API**
A Django-based REST API to report, track, and match lost & found items.  
---

## **🔗 Live Deployment**
🚀 API is live at: **[Deployment Link](https://lostandfound-8td0.onrender.com)**  
📘 API Documentation (Swagger): **[Swagger Docs](https://lostandfound-8td0.onrender.com/swagger/)**  
📕 API Documentation (ReDoc): **[ReDoc Docs](https://lostandfound-8td0.onrender.com/redoc/)**  

---

## **🛠 Features**
- 📝 **Report Lost & Found Items**: Users can report lost or found items.  
- 🔍 **Search & Match**: Matches lost items with reported found items.  
- 📍 **Location-Based Search**: Retrieve nearby lost or found items.  
- 📧 **Email Notifications**: Get notified when a lost item is found!  
- 🔑 **User Authentication**: Secure user authentication with JWT.  
- 📜 **Item History**: Users can view their previously reported lost and found items.  
- 📸 **Media Uploads**: Upload images for better identification.  
- 📖 **Interactive API Docs**: Swagger & ReDoc documentation for testing.  

---

## **🚀 Quick Start**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/lostandfound-api.git
cd lostandfound-api
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **4️⃣ Create a Superuser**
```sh
python manage.py createsuperuser
```

### **5️⃣ Configure Email Notifications**
Update your `.env` file with SMTP credentials:
```
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```
Your API will be live at **http://127.0.0.1:8000/**  

---

## **📡 API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/users/register/` | Register a new user |
| `POST` | `/users/login/` | Login & get JWT token |
| `POST` | `/lost-items/` | Report a lost item |
| `POST` | `/found-items/` | Report a found item |
| `GET` | `/lost-items/` | Retrieve all lost items |
| `GET` | `/found-items/` | Retrieve all found items |
| `GET` | `/match-items/` | Match lost items with found ones (triggers email notification) |
| `DELETE` | `/lost-items/{id}/` | Delete a lost item (once found) |
| `DELETE` | `/found-items/{id}/` | Delete a found item (once returned) |
| `GET` | `/lost-items/history/` | View user's lost item history |
| `GET` | `/found-items/history/` | View user's found item history |
| `GET` | `/nearby-lost-items/` | Retrieve nearby lost items |
| `GET` | `/nearby-found-items/` | Retrieve nearby found items |
| `GET` | `/swagger/` | API Documentation (Swagger UI) |
| `GET` | `/redoc/` | API Documentation (ReDoc) |

---
![image](https://github.com/user-attachments/assets/d387ad25-6f27-4c4a-bf1b-cc2051f7a7c9)
![image](https://github.com/user-attachments/assets/70cfbaba-6f40-4b76-85a0-ddfd63f653ce)
![WhatsApp Image 2025-02-10 at 21 39 03_772700e6](https://github.com/user-attachments/assets/707ea1d1-c46a-4dde-8bb1-59a04b63991a)
![WhatsApp Image 2025-02-10 at 21 41 51_2e5fc86b](https://github.com/user-attachments/assets/03125478-112f-4a32-a0b5-392c7ee8d922)
![WhatsApp Image 2025-02-10 at 21 42 48_5cb7352a](https://github.com/user-attachments/assets/8df7d1df-6038-44d9-91c4-7878a080e5b9)
![WhatsApp Image 2025-02-10 at 21 50 18_165709cc](https://github.com/user-attachments/assets/0ad9d01d-b8dc-4f19-b4d5-7ed73d24dba6)
![WhatsApp Image 2025-02-10 at 21 54 43_740c1909](https://github.com/user-attachments/assets/5314390d-4fbe-46c4-aaea-f060b42e6146)
![WhatsApp Image 2025-02-10 at 21 55 48_e9201239](https://github.com/user-attachments/assets/ebfcd5b9-6551-4a5e-8e32-27872b14990a)
![WhatsApp Image 2025-02-10 at 23 21 58_6faa693f](https://github.com/user-attachments/assets/001f2e6d-6e4d-490c-8655-d04e479f9b47)
![WhatsApp Image 2025-02-10 at 21 59 23_4eac4aa3](https://github.com/user-attachments/assets/99db0e6b-ac41-4039-a3c8-d10e4a33aa66)
![WhatsApp Image 2025-02-10 at 22 06 00_aeea0dd6](https://github.com/user-attachments/assets/42b29526-8485-4ec3-8b3d-855f98b9869f)
![WhatsApp Image 2025-02-10 at 21 38 58_c20df3de](https://github.com/user-attachments/assets/3f2513ec-7a44-416a-997b-2df8fd580bdd)

---


## **🛠 Tech Stack**
- **Backend**: Django, Django REST Framework  
- **Database**: SQLite  
- **Auth**: JWT (JSON Web Tokens)  
- **Email Service**: SMTP (Configured for Gmail, but customizable)  
- **Hosting**: Render  
- **Docs**: drf-yasg (Swagger, ReDoc)  

---

## **🚀 Deployment on Render**
This API is deployed on **Render**. To deploy your own version:
1. Push your code to **GitHub/GitLab**.
2. Create a **new Render Web Service**.
3. Set up **environment variables** (e.g., `SECRET_KEY`, `DEBUG=False`, `EMAIL_HOST`, etc.).
4. Deploy & start the service.

---

## **📜 License**
This project is licensed under the **BSD License**.  

---

## **📬 Contact**
For any queries or issues, reach out to:  
📧 **Email**: mv072004@gmail.com  
🐙 **GitHub**: [My GitHub Profile](https://github.com/Mansiv75/)  

