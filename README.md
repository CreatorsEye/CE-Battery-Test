# CEBT – Creators Eye Battery Tester

Test your laptop battery health with one tool, three ways.
100% free, open source, and privacy-focused.

---

## Features (All Versions)

- **5-minute logging** – Automatically records battery level every 5 minutes
- **Auto-stop at 5%** – Protects battery from deep discharge
- **Discharge chart** – Visual graph of battery drain
- **Test comparison** – Compare results from different days
- **Wake Lock** – Prevents computer from sleeping during test
- **Dark mode** – Matches your system theme
- **100% offline** – No data leaves your device
- **Free & open source** – MIT license

---

## Quick Start

### HTML GUI (Simplest)
1. Go to [GUI/HTML folder](./GUI/HTML/)
2. Download `battery-reporter.html`
3. Double-click to open in browser
4. Click "I Agree", charge to 100%, unplug
5. Click START TEST
6. Wait for test to complete at 5%

### Desktop GUI (Windows/Mac)
1. Go to [GUI/DESKTOP folder](./GUI/DESKTOP/)
2. Download the app for your OS
3. Double-click to run
4. Follow same steps as HTML version

### CLI (All OS)
1. Install Python 3.6 or higher
2. Go to [CLI/BIN folder](./CLI/BIN/)
3. Run installer for your OS
4. Type `cebt /S` in terminal

---

## Repository Structure

**Root Files**
- `README.md` – This file
- `LICENSE` – MIT license

**Folders**

| Folder | Description |
|--------|-------------|
| [GUI/HTML](./GUI/HTML/) | Browser version – one HTML file, works everywhere |
| [GUI/DESKTOP](./GUI/DESKTOP/) | Desktop apps for Windows and macOS |
| [CLI/BIN](./CLI/BIN/) | CLI installers for end users |
| [CLI/PYTHON-ONLY](./CLI/PYTHON-ONLY/) | Python source for developers |
| [DOCS](./DOCS/) | Documentation and guides |

---

## Documentation

| Document | Description |
|----------|-------------|
| [Quick Start Guide](./DOCS/quick-start.md) | Get running in 1 minute |
| [FAQ](./DOCS/FAQ.md) | Frequently asked questions |
| [CLI Commands](./DOCS/commands.md) | All terminal commands explained |
| [Troubleshooting](./DOCS/troubleshooting.md) | Fix common issues |
| [Privacy Policy](./DOCS/legal/privacy.md) | Your data stays yours |

---

## Battery Health Ratings

| Rating | Estimated Full Charge |
|--------|----------------------|
| Excellent | 8+ hours |
| Good | 6-8 hours |
| Fair | 4-6 hours |
| Poor | Less than 4 hours |

Health is estimated based on your actual discharge rate during tests.

---

## Privacy

**All versions are 100% offline. No data leaves your device.**

- No tracking
- No analytics
- No cloud uploads
- No data collection
- Open source – verify it yourself

Read the full [Privacy Policy](./DOCS/legal/privacy.md).

---

## About Creators Eye

We build simple, privacy-focused tools that run entirely on your device.
No data collection. No tracking. Just tools that work.

Email: Creatorseye@gmail.com
GitHub Issues: https://github.com/CreatorsEye/battery-reporter/issues

---

## License

MIT – Free for everyone. Use, modify, and share.

Copyright (c) 2026 Creators Eye Team
