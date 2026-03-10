# Quick Start Guide

Get started with CEBT in 1 minute.

---

## Choose Your Version

### 🌐 HTML GUI (Simplest)
1. Go to the [GUI/HTML](../GUI/HTML/) folder
2. Download `battery-reporter.html`
3. Double-click to open in your browser
4. Click **"I Agree"** (first time only)
5. Charge your laptop to 100%
6. Unplug the charger
7. Click **START TEST**
8. Keep the tab open (you can minimize it)
9. Test stops automatically at 5%
10. Report saves to your chosen folder

---

### 💻 Desktop GUI (Windows/Mac)
1. Go to the [GUI/DESKTOP](../GUI/DESKTOP/) folder
2. Download the app for your OS:
   - **Windows:** `CEBT-GUI.exe`
   - **macOS:** `CEBT-GUI.app`
3. Double-click to run
4. Follow the same steps as HTML version

---

### ⌨️ CLI (All OS)
1. Make sure **Python 3.6+** is installed
2. Go to the [CLI/BIN](../CLI/BIN/) folder
3. Run the installer for your OS:
   - **Windows:** Double-click `install-windows.bat`
   - **macOS:** Run `bash install-macos.sh`
   - **Linux:** Run `bash install-linux.sh`
4. Open a new terminal and type:
   ```bash
   cebt /S
   ```

---

## First Time Using CLI?

When you run `cebt /L` to open a report, you'll be prompted to get the HTML viewer:

```text
❌ battery-reporter.html not found!

Options:
[1] Manual download - Open GitHub page + instructions
[2] Auto-download - Save directly to this folder
[3] Cancel - Exit
```

Choose **Option 2** for automatic download, or **Option 1** to download manually.

---

## Understanding Results

After a test completes, you'll get:

| File | Description |
|:---|:---|
| `*_log.txt` | 5-minute readings (timestamp + percentage) |
| `*_report.html` | HTML report with charts and summary |

The HTML report shows:
* Start and end time
* Total duration
* Battery health estimate
* Complete 5-minute log
* Discharge chart

---

## Battery Health Ratings

| Rating | Estimated Full Charge |
|:---|:---|
| **Excellent** | 8+ hours |
| **Good** | 6-8 hours |
| **Fair** | 4-6 hours |
| **Poor** | Less than 4 hours |

---

## Default Output Folders

| OS | Default Folder |
|:---|:---|
| **Windows** | `Documents\CEBT-Reports\` |
| **macOS** | `Documents/CEBT-Reports/` |
| **Linux** | `~/CEBT-Reports/` |

**To change in CLI:** `cebt /O "C:\your-folder"`

---

## Next Steps

* Read the [FAQ](FAQ.md) for common questions
* Check [Troubleshooting](troubleshooting.md) if you run into issues
* View all [CLI Commands](commands.md)
* Review our [Privacy Policy](legal/privacy.md)

---

## Need Help?

* **GitHub Issues:** [https://github.com/CreatorsEye/battery-reporter/issues](https://github.com/CreatorsEye/battery-reporter/issues)
* **Email:** Creatorseye@gmail.com
