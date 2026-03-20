🌐 GUI-Based DNS Enumeration Tool

A Python-based graphical application that allows users to perform DNS enumeration easily without using command-line tools. The tool retrieves essential DNS records such as A, MX, NS, and TXT through a clean and intuitive interface.

🚀 Features:-
🖥️ User-friendly GUI (Tkinter-based)
🔍 Retrieve DNS records (A, MX, NS, TXT)
✅ Domain name validation
⚡ Optimized DNS query performance (reduced timeout)
📊 Structured tabular result display
💾 Save results to a .txt file
⌨️ Keyboard shortcuts (Enter to scan, Ctrl+L to clear)

🛠️ Technologies Used:-
Python
Tkinter (GUI Development)
dnspython (DNS Resolution)

📂 Project Structure:-
dns_enumerator_gui/
│── gui_app.py          # Main GUI application
│── dns_lookup.py       # DNS query functions
│── requirements.txt    # Required dependencies
│── README.md           # Project documentation

⚙️ Installation & Setup:-
1. Clone the repository
git clone https://github.com/your-username/dns-enumerator-gui.git
cd dns-enumerator-gui
2. Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install dnspython
4. Run the application
python gui_app.py

📸 Usage:-
Enter a domain name (e.g., google.com)
Click Scan DNS or press Enter
View results in the table
Optionally save results to a .txt file

🎯 Use Cases:-
Learning DNS and networking concepts
Basic cybersecurity reconnaissance
Educational demonstrations of GUI-based tools

👨‍💻 Author:-
Sumit Chatterjee
