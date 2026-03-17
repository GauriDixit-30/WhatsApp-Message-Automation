# 📲 WhatsApp Message Automation

A simple Python-based automation tool that allows users to schedule and send WhatsApp messages automatically at a specified date and time using the Twilio API.

This project demonstrates the use of Python automation, APIs, and scheduling logic to send messages without manual interaction.

---

## 🚀 Features

* Send WhatsApp messages automatically.
* Schedule messages for a specific **date and time**.
* Uses **Twilio API** for secure message delivery.
* User-friendly **command-line input**.
* Handles errors if the scheduled time is in the past.

---

## 🛠️ Technologies Used

* **Python**
* **Twilio API**
* **Datetime module**
* **Time module**

---

## 📂 Project Structure

```
WhatsApp-Message-Automation
│
├── main.py          # Main Python script
└── README.md        # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/GauriDixit-30/WhatsApp-Message-Automation.git
cd WhatsApp-Message-Automation
```

---

### 2️⃣ Install Required Library

```
pip install twilio
```

---

### 3️⃣ Setup Twilio Credentials

Replace the following values in the code with your Twilio credentials:

```
account_sid = "Your Twilio Account SID"
auth_token = "Your Twilio Auth Token"
```

Also replace the sender number:

```
from_='whatsapp:Your Twilio WhatsApp Number'
```

---

## ▶️ How to Run the Project

Run the Python script:

```
python main.py
```

The program will ask for:

* Recipient name
* WhatsApp number (with country code)
* Message content
* Date to send the message
* Time to send the message

Example input:

```
Enter the recipient's name: John
Enter the recipient's WhatsApp number with country code: +919876543210
Enter the message you want to send: Hello John!
Enter the date to send the message: 2026-03-20
Enter the time to send the message: 14:30
```

The message will automatically be sent at the scheduled time.

---

## 📌 Example Output

```
Message scheduled to be sent to John at 2026-03-20 14:30:00
Message sent successfully! Message SID: SMxxxxxxxxxxxxxxxx
```

---

## ⚠️ Important Notes

* The recipient must **join the Twilio WhatsApp Sandbox** before receiving messages.
* Make sure the **phone number includes the country code**.
* Never expose your **Twilio Auth Token publicly**.

---

## 💡 Future Improvements

* GUI interface for easier use
* Multiple message scheduling
* Message templates
* Contact list support

---

## 👩‍💻 Author

**Gauri Dixit**

B.Tech Computer Science
Full Stack Development & AI/ML Enthusiast

GitHub:
https://github.com/GauriDixit-30

---


