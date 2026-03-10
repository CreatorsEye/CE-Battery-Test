# ❓ Frequently Asked Questions – Creators Eye Battery Reporter

## General Questions

### Which tool should I use?
- **Browser Tool**: For most users – simple, visual, no installation.
- **CLI Tool** (coming soon): For developers and automation – runs in terminal.

### Are these tools really free?
Yes! Both tools are completely free and open source under the MIT license.

### Who is Creators Eye?
We're a team of developers building simple, privacy-focused tools that run entirely on your device.  
📧 [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com)

### Do you collect any data?
No. **All data stays on your device.** We don't track you, we don't have servers, and we never see your battery reports.

---

## Browser Tool Questions

### Does it work in Firefox/Safari?
Yes! The browser tool works in all modern browsers:
- **Chrome/Edge**: Full support (folder picking, native Wake Lock).
- **Firefox/Safari**: Folder picking is not supported → reports are saved as ZIP files. Wake Lock is simulated with silent audio (still prevents sleep).

### Will my computer sleep during the test?
No – the tool actively prevents sleep:
- **Chrome/Edge**: Uses native Wake Lock API.
- **Firefox/Safari**: Uses a silent audio loop (works just as well).

### Where are reports saved?
- If you're using **Chrome/Edge** and you've selected a folder: reports go directly into that folder.
- Otherwise: a **ZIP file** is downloaded to your Downloads folder, containing the final report and the full 5‑minute log.

### Why does the test stop at 5%?
Deep discharging a lithium‑ion battery (below 5%) can permanently damage it. Stopping at 5% is a safety feature to prolong your battery's life.

### Can I change the stop percentage?
Currently it's fixed at 5% for safety. Future versions may allow customization.

### What if I accidentally close the tab?
The tool saves your test progress every minute. When you reopen the tool, it will ask if you want to resume the interrupted test.

### Why do I see "Using ZIP fallback" in Chrome/Edge?
This means the folder you previously selected is no longer accessible – it may have been deleted, moved, or its permissions were lost. Simply click the location bar and pick a new folder.

### Can I use this tool on a mobile phone?
No – it's designed for laptops with batteries. Mobile browsers do not support the required Battery API.

---

## CLI Tool Questions (Coming Soon)

### When will the CLI tool be available?
We're working on it! Expected release: **March 2024**. Watch this repository for updates.

### What platforms will it support?
Windows, macOS, and Linux – all via Python 3.

### Will it have the same features as the browser tool?
Yes – 5‑minute logging, auto‑stop at 5%, and CSV export. It will be scriptable and lightweight.

---

## Privacy & Security

### Is my data safe?
Absolutely. All data stays on your computer. The tool never sends anything over the internet.

### Do you use any third‑party services?
The browser tool loads **Chart.js**, **JSZip**, and **FileSaver.js** from CDNs for charts and ZIP creation. These libraries run locally in your browser; no data is sent to them.

### Can I use the tool offline?
Yes – after the first load (which fetches the libraries), you can disconnect from the internet and it will still work.

---

## Still have questions?
📧 Email us: [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com)  
🐛 Open an issue: [GitHub Issues](https://github.com/CreatorsEye/battery-reporter/issues)
