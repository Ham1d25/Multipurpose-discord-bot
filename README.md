# 🤖 Multipurpose Discord Bot

A **multipurpose Discord bot** built with **Python** and **discord.py**, using modern **slash commands (app_commands)**. The bot provides essential moderation, utility, and information features to help manage Discord servers easily and efficiently.

---

## ✨ Features

### 🛠️ Moderation

* `/kick` – Kick members from the server
* `/ban` – Ban members
* `/unban` – Unban members
* `/timeout` – Timeout members for a specific duration
* `/untimeout` – Remove timeout from members
* `/clear-channel` – Clear all messages in a channel
* `/channel-delete` – Delete text or voice channels
* `/lock` – Lock text or voice channels
* `/unlock` – Unlock text or voice channels

### 📊 Information

* `/server-info` – Display detailed server information
* `/user-info` – Display information about a user or yourself

### 🧰 Utility

* `/ping` – Check bot latency
* `/hello` – Simple greeting command
* `/say` – Make the bot send a custom message

---

## 🔐 Permissions

Commands use Discord’s **built-in permission system** to ensure proper access control, including:

* `Kick Members`
* `Ban Members`
* `Manage Messages`
* `Manage Channels`
* `Moderate Members`

Only users with the required permissions can execute moderation commands.

---

## 🧑‍💻 Built With

* **Python**
* **discord.py**
* **Discord Slash Commands (app_commands)**

---

## 🚀 Getting Started

### 1️⃣ Requirements

* Python **3.10+**
* A Discord bot token
* `discord.py` installed

```bash
pip install -U discord.py
```

---

### 2️⃣ Setup

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

2. Open the project folder and edit the bot token:

```python
Token = "YOUR_BOT_TOKEN_HERE"
```

⚠️ **Never share your bot token publicly.**

---

### 3️⃣ Run the Bot

```bash
python main.py
```

Once the bot is online, slash commands will automatically sync with your server.

---

## 📌 Notes

* This bot is designed as a **learning-friendly base project**.
* You can easily extend it with music, logging, leveling, or database support.
* Uses modern Discord features and follows a clean structure.

---

## 🧠 Future Ideas

* 🎵 Music commands
* 📈 Leveling system
* 🗂️ Logging & moderation history
* 🌍 Multi-language support
* 🗄️ Database integration

---

## 📄 License

This project is open-source and free to use. You are welcome to modify and expand it for your own servers.

---

⭐ If you like this project, consider giving it a star on GitHub!

