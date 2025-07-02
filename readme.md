# 🛠️ ParametricPrint
**Natural language to OpenSCAD** – AI-powered parametric CAD for makers, engineers, and 3D printing enthusiasts.

---

## 🔍 Overview

**ParametricPrint** is a lightweight, AI-powered Streamlit app that lets you describe a part in plain English and instantly get a parametric `.scad` file using OpenSCAD syntax.

Whether you're prototyping electronics enclosures or creating snap-fit joints, this tool gives you editable, scriptable 3D models — no CAD experience required.

---

## ✨ Features

- 🧠 Powered by GPT-4 via OpenAI
- 💬 Natural language to parametric OpenSCAD
- 📥 One-click `.scad` download
- 🔧 Easily customizable output
- 🧪 Ready to extend for Fusion 360 scripting (coming soon)

---

## 🚀 Getting Started

### 🖥️ Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/YOUR_USERNAME/ParametricPrint.git
cd ParametricPrint
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
🔐 Add Your OpenAI API Key
Create a .env file in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=sk-YourActualKeyHere
▶️ Run the App
bash
Copy
Edit
streamlit run app/main.py
Visit http://localhost:8501 in your browser.

💡 Example Prompt
text
Copy
Edit
A rectangular electronics enclosure with four corner screw holes and a removable slotted lid.
🧱 Output Example
scad
Copy
Edit
width = 80;
height = 40;
depth = 30;

difference() {
  cube([width, height, depth]);
  // Lid and screw hole logic here...
}


🔐 Add Your OpenAI API Key
Create a .env file in the root directory:
OPENAI_API_KEY=sk-YourActualKeyHere

▶️ Run the App
streamlit run app/main.py
Visit http://localhost:8501 in your browser.

💡 Example Prompt
A rectangular electronics enclosure with four corner screw holes and a removable slotted lid.

🧱 Output Example
width = 80;
height = 40;
depth = 30;

difference() {
  cube([width, height, depth]);
  // Lid and screw hole logic here...
}