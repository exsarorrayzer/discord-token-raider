🔥 Discord SKULL Token Rxider Tool

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge" />
</p>

A powerful and modular Discord messaging tool built with Python and Rich library for educational purposes.

⚠️ IMPORTANT DISCLAIMER

Warning: This tool is created for educational purposes only. Using it may violate Discord's Terms of Service and could result in account termination. The developers are not responsible for any misuse of this software. Use at your own risk.

---

🚀 Features

✨ Core Functionality

· 📨 DM Messaging - Send messages to direct message channels 
· 🏰 Guild Messaging - Post messages in server channels
· 👥 Group Messaging - Message in group channels
· 🔄 Multi-Token Support - Rotate between multiple accounts
· ⚡ Random Token Selection - Automatically switch tokens for each message

🔧 Management Tools

· 🔐 Token Management - Add, view, and manage Discord tokens
· ⚙️ Config System - Easy configuration via JSON files
· 🎨 Beautiful UI - Rich terminal interface with colors and panels
· 📊 Real-time Status - Live feedback for each operation

🛡️ Safety Features

· ✅ Input Validation - Proper token and configuration checks
· 🔒 Secure Handling - Safe token storage and management
· ⚠️ Error Handling - Comprehensive error reporting and recovery

---

📦 Installation

Prerequisites

· Python 3.8 or higher
· pip package manager

Step-by-Step Setup

1. Clone the Repository

```bash
git clone https://github.com/exsarorrayzer/skull-tokenraider.git
cd discord-tool
```

1. Install Dependencies

```bash
pip install -r requirements.txt
```

1. Set Up Configuration

```bash
# The tool will auto-generate config.json if missing
# Edit config.json with your settings:
{
    "dm": {
        "channel_id": "123456789",
        "message": "Your DM message here"
    },
    "guild": {
        "channel_id": "987654321", 
        "message": "Your guild message here",
        "amount": 5
    },
    "group": {
        "channel_id": "555555555",
        "message": "Your group message here", 
        "amount": 3
    }
}
```

1. Add Your Tokens

```bash
# Edit tokens.txt and add your Discord tokens:
# Remove placeholder text and add one token per line
```

---

🎯 Usage

Starting the Tool

```bash
python main.py
```

Main Menu Options

Option Command Description
📨 DM Spam 1 Send messages to direct messages
🏰 Guild Spam 2 Post messages in server channels
👥 Group Spam 3 Message in group channels
🔧 Token Management 4 Manage your Discord tokens
⚙️ Config Info 5 View current configuration
👤 Developer Info 6 Show developer information
🚪 Exit 0 Exit the application

Token Management Submenu

Option Command Description
📋 Token List 1 View all loaded tokens
➕ Add Token 2 Add new token to tokens.txt
🧹 Clear Placeholders 3 Remove example text from tokens file
🔙 Back 0 Return to main menu

---

🏗️ Project Structure

```
discord-tool/
├── main.py                 # Main application entry point
├── config.json            # Configuration settings
├── tokens.txt             # Discord tokens storage
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── modules/              # Core functionality modules
    ├── banner.py         # ASCII art and branding
    ├── creds.py          # Developer information
    ├── token_manager.py  # Token handling utilities
    ├── dm_spammer.py     # Direct message functionality
    ├── guild_spammer.py  # Server message functionality  
    ├── group_spammer.py  # Group message functionality
    └── utils.py          # Common utilities and helpers
```

---

⚙️ Configuration

config.json Explained

```json
{
    "dm": {
        "channel_id": "123456789",        # Target DM channel ID
        "message": "Hello from DM!"       # Message to send
    },
    "guild": {
        "channel_id": "987654321",        # Target server channel ID  
        "message": "Hello from guild!",   # Message to send
        "amount": 5                       # Number of messages to send
    },
    "group": {
        "channel_id": "555555555",        # Target group channel ID
        "message": "Hello from group!",   # Message to send
        "amount": 3                       # Number of messages to send
    }
}
```

tokens.txt Format

```
# One token per line
# Remove all placeholder text before adding your tokens
token here
```

---

🔧 Troubleshooting

Common Issues

Problem Solution
ModuleNotFoundError Run pip install -r requirements.txt
Invalid Token Error Check token format in tokens.txt
Channel ID Error Verify channel IDs in config.json
Permission Denied Ensure bot has proper channel permissions

Error Messages

· ❌ No tokens found! - Add tokens to tokens.txt file
· ❌ Invalid channel ID! - Check channel ID in configuration
· ❌ Request failed! - Verify token validity and permissions

---

🛡️ Security Notes

· 🔒 Never share your tokens.txt file
· 🔒 Use environment variables for production
· 🔒 Regularly rotate your tokens
· 🔒 Keep the tool updated

---

📊 Performance Tips

· ✅ Use multiple tokens for better performance
· ✅ Adjust message amounts based on your needs
· ✅ Monitor Discord rate limits
· ✅ Use proper error handling in configuration

---

🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

---

👨‍💻 Developer

exsarorrayzer

· GitHub: exsarorrayzer
· Instagram: exsarorrayzer
· Discord: noinfonocontext
· YouTube: exsarorrayzer

---

📄 License

This project is for educational purposes only. Use responsibly and in accordance with Discord's Terms of Service.

---

⭐ Support

If you find this project helpful, please give it a star on GitHub!

---

Remember: Always use such tools responsibly and ethically. Education is the primary purpose of this software.

---

<p align="center">
  <strong>Made with ❤️ for educational purposes</strong>
</p>