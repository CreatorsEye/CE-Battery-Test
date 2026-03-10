# CEBT Desktop GUI Versions

Standalone desktop applications for Windows and macOS. No browser needed.

---

## Available Versions

| Platform | Download | Requirements |
|:---|:---|:---|
| **Windows** | [`CEBT-GUI.exe`](./windows/CEBT-GUI.exe) | Windows 10 or later (64-bit) |
| **macOS** | [`CEBT-GUI.app`](./macos/CEBT-GUI.app) | macOS 11 or later (Intel/Apple Silicon) |

---

## Quick Comparison

| Feature | Windows | macOS |
|:---|:---:|:---:|
| Standalone app | ✅ Yes | ✅ Yes |
| No browser needed | ✅ Yes | ✅ Yes |
| Wake Lock | ✅ Yes | ✅ Yes |
| 5-minute logging | ✅ Yes | ✅ Yes |
| Auto-stop at 5% | ✅ Yes | ✅ Yes |
| Charts & graphs | ✅ Yes | ✅ Yes |
| Test comparison | ✅ Yes | ✅ Yes |
| Dark mode | ✅ Yes | ✅ Yes |
| Folder selection | ✅ Yes | ✅ Yes |
| Test recovery | ✅ Yes | ✅ Yes |

---

## Which One Should You Download?

| If you have... | Download... |
|:---|:---|
| Windows 10 or 11 | [Windows version](./windows/CEBT-GUI.exe) |
| macOS 11 or later (Intel) | [macOS version](./macos/CEBT-GUI.app) |
| macOS 11 or later (Apple Silicon M1/M2/M3) | [macOS version](./macos/CEBT-GUI.app) – Universal Binary |
| Linux | Use [HTML GUI](../HTML/) or [CLI](../../CLI/) instead |

---

## First-Time Setup

### Windows
1. **Download** `CEBT-GUI.exe`
2. **Double-click** to run
3. If Windows Defender shows a warning, click **"More info"** then **"Run anyway"**
4. The app will open

### macOS
1. **Download** `CEBT-GUI.app`
2. **Do not double-click yet**
3. **Right-click** the app and select **"Open"**
4. Click **"Open"** in the security dialog
5. The app will open (you only need to do this once)

---

## Common Features (Both Versions)

### Starting a Test
1. Click **"I Agree"** (first time only)
2. Charge your laptop to 100%
3. **Unplug** the charger
4. Click **START TEST**
5. Keep the app open (you can minimize it)
6. Test stops automatically at 5%

### Viewing Results
* **Current test**: Live percentage and log
* **After test**: Chart and summary
* **History**: Compare all past tests

### Reports
Reports are saved as:
* `*_log.txt` – 5-minute readings
* `*_report.html` – Full report with charts

**Default folder:** `Documents/CEBT-Reports/`

---

## Screenshots

*(Screenshots would be added here)*

---

## Frequently Asked Questions

### Do I need to install anything?
No. Just download and run. Both versions are self-contained.

### Are these apps safe?
Yes. They run entirely on your device. No data is sent anywhere. The source code is open for inspection.

### Why does antivirus/macOS warn about the app?
The apps are not digitally signed. This is common for open-source tools. The warnings are false positives.

### Can I use these on older OS versions?
* **Windows**: Windows 10 or later recommended
* **macOS**: 11 or later required
* For older versions, use the HTML GUI instead

### Do I need internet?
No. Both apps work completely offline.

---

## Troubleshooting

### Windows
| Issue | Solution |
|:---|:---|
| App won't start | Download again – file may be corrupted |
| Antivirus warning | Click "More info" → "Run anyway" |
| Wake Lock not working | Run on battery power, try as administrator |

### macOS
| Issue | Solution |
|:---|:---|
| "App is damaged" | Right-click → Open |
| Can't open at all | System Settings → Privacy & Security → Open Anyway |
| Permission denied | Check if app is quarantined: `xattr -d com.apple.quarantine CEBT-GUI.app` |

For more details, see:
* [Windows README](./windows/README.md)
* [macOS README](./macos/README.md)

---

## Uninstall

Simply delete the app file. No registry entries, no leftovers.

---

## Building from Source

The desktop apps are built using Electron. To build them yourself:

```bash
git clone https://github.com/CreatorsEye/battery-reporter.git
cd battery-reporter/GUI/DESKTOP
npm install
npm run build
```

See the source code for more details.

---

## License

**MIT** – Free for everyone. Use, modify, and share.

---

## Contact

* 📧 **Email:** Creatorseye@gmail.com
* 🐛 **GitHub Issues:** [Open an issue](https://github.com/CreatorsEye/battery-reporter/issues)
