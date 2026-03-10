# CEBT GUI Versions

Graphical user interface versions of the Creators Eye Battery Tester.

---

## Available Versions

| Version | Platform | Description |
|---------|----------|-------------|
| [**HTML GUI**](./HTML/) | Windows, macOS, Linux | One HTML file, open in any browser |
| [**Desktop GUI**](./DESKTOP/) | Windows, macOS | Standalone apps, no browser needed |

---

## Quick Comparison

| Feature | HTML GUI | Desktop GUI |
|---------|----------|-------------|
| Platform support | Windows, macOS, Linux | Windows, macOS |
| Installation | None – just download | None – just download |
| File size | ~600KB | ~50-80MB |
| Browser needed | Yes (Chrome, Edge, Firefox, Safari) | No |
| Works offline | Yes (after first load) | Yes |
| Wake Lock | ✅ Yes | ✅ Yes |
| 5-minute logging | ✅ Yes | ✅ Yes |
| Auto-stop at 5% | ✅ Yes | ✅ Yes |
| Charts & graphs | ✅ Yes | ✅ Yes |
| Test comparison | ✅ Yes | ✅ Yes |
| Dark mode | ✅ Yes | ✅ Yes |
| Folder selection | ✅ Yes | ✅ Yes |
| Test recovery | ✅ Yes | ✅ Yes |

---

## Which One Should You Choose?

### Choose **HTML GUI** if:
- You want the simplest option
- You use Linux
- You prefer opening files in your browser
- You want the smallest download

👉 [Go to HTML GUI](./HTML/)

---

### Choose **Desktop GUI** if:
- You want a standalone app (no browser)
- You use Windows or macOS
- You prefer native applications
- You don't mind a larger download

👉 [Go to Desktop GUI](./DESKTOP/)

---

## Common Features (Both Versions)

### Starting a Test
1. Open the app/HTML file
2. Click "I Agree" (first time only)
3. Charge your laptop to 100%
4. Unplug the charger
5. Click **START TEST**
6. Keep the window open (you can minimize it)
7. Test stops automatically at 5%

### During the Test
- Live battery percentage display
- 5-minute automatic logging
- Elapsed timer
- Next log countdown

### After the Test
- Discharge chart
- Test summary
- Health estimate
- Complete 5-minute log

### Viewing History
- List of all previous tests
- Click any test to view full report
- Compare durations

---

## Reports

Both versions save the same files:

| File | Description |
|------|-------------|
| `*_log.txt` | 5-minute readings (timestamp + percentage) |
| `*_report.html` | Full report with charts and summary |

Default save locations:

| OS | HTML GUI | Desktop GUI |
|----|----------|-------------|
| Windows | Your chosen folder or Downloads | `Documents\CEBT-Reports\` |
| macOS | Your chosen folder or Downloads | `Documents/CEBT-Reports/` |
| Linux | Your chosen folder or Downloads | N/A |

---

## Screenshots

*(Screenshots would be added here)*

---

## Privacy

**Both versions are 100% offline. No data leaves your device.**

- No tracking
- No analytics
- No cloud uploads
- No data collection

For details, see the [Privacy Policy](../DOCS/legal/privacy.md).

---

## System Requirements

### HTML GUI
- Any operating system
- Modern browser (Chrome, Edge, Firefox, Safari)
- Battery-powered laptop

### Desktop GUI
- **Windows**: Windows 10 or later (64-bit)
- **macOS**: macOS 11 or later (Intel/Apple Silicon)

---

## Need Help?

- [HTML GUI README](./HTML/README.md)
- [Desktop GUI README](./DESKTOP/README.md)
- [FAQ](../DOCS/FAQ.md)
- [Troubleshooting](../DOCS/troubleshooting.md)
- GitHub Issues: https://github.com/CreatorsEye/battery-reporter/issues
- Email: Creatorseye@gmail.com

---

## License

MIT – Free for everyone. Use, modify, and share.
