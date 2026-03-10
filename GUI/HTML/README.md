# CEBT – HTML GUI Version

The simplest way to test your laptop battery. One HTML file, no installation, works in any browser.

---

## Download

[⬇️ Click here to download battery-reporter.html](./battery-reporter.html)

Right-click and select "Save link as..." to download the file.

---

## Quick Start

1. **Open the file** in Chrome, Edge, Firefox, or Safari
2. **First time only**: Click "I Agree" to accept the terms
3. **Charge your laptop** to 100%
4. **Unplug the charger**
5. Click **START TEST**
6. **Use your laptop normally** (keep this tab open – you can minimize it)
7. The test **stops automatically** when battery reaches **5%**
8. A report is saved to your chosen folder (or Downloads as a ZIP file)

---

## Features

| Feature | Description |
|---------|-------------|
| Universal | Works in Chrome, Edge, Firefox, Safari |
| Wake Lock | Prevents your computer from sleeping during the test |
| 5-minute logging | Automatically records battery level every 5 minutes |
| Auto-stop at 5% | Protects battery from deep discharge |
| Discharge chart | Visual graph of battery drain after each test |
| Test comparison | Compare durations of your last 5 tests |
| Dark mode | Automatically matches your system theme |
| Folder selection | Pick a folder for reports (Chrome/Edge) – falls back to ZIP for all browsers |
| Recovery | If the tab closes accidentally, you can resume the test |
| Privacy first | All data stays on your device – nothing is uploaded |

---

## Screenshots

### Main Interface
![Main Interface](./screenshot-main.png)

### Test Running
![Test Running](./screenshot-test.png)

### Final Report with Chart
![Report](./screenshot-report.png)

---

## Frequently Asked Questions

**Q: Does it work in Firefox?**  
A: Yes! Firefox is fully supported. Folder selection is not available, so reports are saved as ZIP files – which contain the same information.

**Q: Will my computer sleep during the test?**  
A: No – the tool uses Wake Lock (native in Chrome/Edge, audio fallback in Firefox) to keep your system awake.

**Q: Where are reports saved?**  
A: If you're using Chrome/Edge and you pick a folder, reports go there. Otherwise, a ZIP file is downloaded to your Downloads folder.

**Q: Can I close the browser tab during the test?**  
A: No – the test stops if the tab is closed. However, the tool saves progress every minute, so when you reopen it you'll be asked if you want to resume.

**Q: Why does it stop at 5%?**  
A: Deep discharging lithium-ion batteries (below 5%) can permanently damage them. Stopping at 5% is a safety feature.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Battery percentage not showing | Use Chrome, Edge, or Firefox latest version |
| Wake Lock inactive | Firefox uses audio fallback – it still works |
| Folder picker doesn't open | Your browser saves as ZIP – perfectly fine |
| "Using ZIP fallback" in Chrome/Edge | Click location bar and pick a new folder |
| Test interrupted | Reopen tool – it will ask to resume |

---

## About Creators Eye

This tool is part of the Creators Eye collection – simple, privacy-focused tools that run entirely on your device.

Email: Creatorseye@gmail.com

---

## License

MIT – Free for everyone. Use, modify, and share.
