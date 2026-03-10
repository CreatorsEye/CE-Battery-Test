# CEBT Desktop for macOS

Standalone macOS application for battery testing. No browser needed.

---

## 📥 Download

[⬇️ CEBT-GUI.app](./CEBT-GUI.app)

**Requirements:** macOS 11 or later (Intel and Apple Silicon)

---

## 🚀 Quick Start

1. Download `CEBT-GUI.app`
2. **First time only**: Right-click the app and select "Open"
3. Click "Open" in the security dialog
4. Click "I Agree" in the app
5. Charge your laptop to 100%
6. Unplug the charger
7. Click START TEST
8. Keep the app open (you can minimize it)
9. Test stops automatically at 5%
10. Report saves to your chosen folder

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Standalone** | No browser needed – runs as native macOS app |
| **Wake Lock** | Prevents computer from sleeping during test |
| **5-minute logging** | Automatically records battery level every 5 minutes |
| **Auto-stop at 5%** | Protects battery from deep discharge |
| **Discharge chart** | Visual graph of battery drain after each test |
| **Test comparison** | Compare durations of your last 5 tests |
| **Dark mode** | Automatically matches your system theme |
| **Folder selection** | Pick where reports are saved |
| **Recovery** | If app closes accidentally, you can resume the test |
| **Privacy first** | All data stays on your device |

---

## 📸 Screenshots

*(Screenshots would be added here)*

---

## 📂 Default Output Folder

Reports are saved to: `Documents/CEBT-Reports/`

Example: `/Users/YourName/Documents/CEBT-Reports/`

You can change this in the app settings.

---

## ❓ Frequently Asked Questions

### Why does macOS show a security warning?
The app is not signed with an Apple developer certificate. This is common for open-source tools.

**To open:**
1. Right-click the app
2. Select "Open" from the context menu
3. Click "Open" in the dialog
4. The app will now open normally (you only need to do this once)

### Is it safe?
Yes. The app runs entirely on your device. No data is sent anywhere. The source code is available on GitHub for inspection.

### Can I use it on Intel Macs?
Yes. The app is Universal Binary and works on both Intel and Apple Silicon.

### Can I use it on macOS 10.15 or older?
macOS 11 or later is required. For older versions, use the HTML GUI version instead.

### Where are reports saved?
Default: `Documents/CEBT-Reports/`. You can choose any folder when starting a test.

### Can I close the app during test?
No – the test stops if you close the app. However, it saves progress every minute and will ask to resume when you reopen.

---

## ⚠️ Troubleshooting

### "App is damaged" warning
If you see "CEBT-GUI.app is damaged and can't be opened":

1. Open Terminal
2. Run this command:
   ```bash
   xattr -d com.apple.quarantine /path/to/CEBT-GUI.app
