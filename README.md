# BlackJack-Card-Counter

**Blackjack Hi-Lo card counting trainer.**

Train your Blackjack card counting skills using the Hi-Lo method. Available for Android.

<p align="center">
  <br>
  <img width="500" height="500" alt="logo" src="https://github.com/user-attachments/assets/7340a8e7-b242-4b7c-89d9-15c156945d38" /><br>
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/platform-Android-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python">
</p>

### Hi-Lo Counting System
- **Cards 2-6:** +1
- **Cards 7-9:** 0  
- **Cards 10, J, Q, K, A:** -1

Keep the running count in your head as cards are revealed.

## Features

- **Normal Mode**: Press the "next" button to continue counting cards manually
- **Timed Mode**: Select the speed, and count cards
- **Simple GUI**: Intuitive interface for users
- **Portable**: Works on Android

## Quick Start

### Prerequisites

- Python 3.11 or higher
- BeeWare Briefcase

### Installation

1. Clone the repository
```bash
git clone https://github.com/Lif28/BlackJack-Card-Counter.git
cd BlackJack-Card-Counter/blackjack
```

2. Create virtual environment and install Briefcase
```bash
python3 -m venv beeware-venv
```

On Windows:
```bash
beeware-venv\Scripts\activate
pip3 install briefcase
```

On Linux:
```bash
source beeware-venv/bin/activate
pip3 install briefcase
```

3. Run the application

In development mode:
```bash
briefcase dev
```

Build for android:
```bash
briefcase create android
briefcase build android
briefcase run android
```

## Usage

### Normal Mode

Practice card counting at your own pace. Tap through cards manually and test your running count periodically.
<p align="center">
  <br>
  <img width="200" alt="NormalMode" src="https://github.com/user-attachments/assets/cebb8719-be0d-47b4-97ce-abd32a88fbcc" /><br>
</p>

### Timed Mode

Challenge yourself with automatic card progression. Adjust the speed from 0.5 to 2 seconds per card using the slider. Pause anytime with the Stop/Resume button.
<p align="center">
  <br>
  <img width="200" alt="TimedMode" src="https://github.com/user-attachments/assets/6d0f6cef-7a9b-415f-9fe7-4b169c3e85b3" /><br>
</p>

### Navigation

Use the menu (three dots) in the top-right corner to return to the home screen at any time.

<p align="center">
  <br>
  <img width="200" alt="TimedMode" src="https://github.com/user-attachments/assets/643b85d2-1232-4d8c-aefd-a4e00bc2dfcd" /><br>
</p>

## Project Structure

```
blackjack/
├── src/
│   └── blackjack/
│       ├── resources/
│       │   ├── cards/              # 52 playing card images
│       │   ├── logo.png
│       │   ├── icon.png
│       │   └── icon-*.png          # Android icons (various sizes)
│       ├── __init__.py
│       ├── __main__.py
│       └── app.py                  # Main application code
├── tests/
│   ├── __init__.py
│   ├── blackjack.py
│   └── test_app.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml                  # Project configuration & dependencies
└── CHANGELOG.md                    # Version history
```

## Dependencies

- **Python 3.11+** - Programming language
- **BeeWare Toga ~0.5.0** - Cross-platform GUI framework
- **BeeWare Briefcase** - Packaging tool for mobile/desktop apps


All dependencies are managed through `pyproject.toml`. No separate `requirements.txt` needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

