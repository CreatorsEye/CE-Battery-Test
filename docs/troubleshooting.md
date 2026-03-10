# 🔧 Troubleshooting Guide – Creators Eye Battery Reporter

## Browser Tool

### Battery percentage not showing
- **Cause**: Your browser may not support the Battery API, or the API is disabled.
- **Solution**: Use the latest version of Chrome, Edge, or Firefox. If the problem persists, try enabling the API in your browser flags (usually not needed).

### Wake Lock not working
- **Chrome/Edge**: Wake Lock requires a secure context (localhost or HTTPS). If you're opening the file directly from disk (`file://`), it should still work in Chrome. If not, try using a local server (e.g., `python -m http.server`).
- **Firefox/Safari**: Wake Lock is not natively supported, but the tool uses a silent audio fallback – it should still prevent sleep. If your computer still sleeps, ensure audio is not muted in the browser.

### Folder picker doesn't open
- **Cause**: Your browser does not support the File System Access API (Firefox, Safari, older browsers).
- **Solution**: The tool automatically falls back to ZIP downloads – this is normal and works perfectly. You'll still get all your data.

### "Using ZIP fallback" warning in Chrome/Edge
- **Cause**: The folder you previously selected is no longer accessible. It may have been deleted, moved, or its permissions revoked (e.g., after clearing browser data).
- **Solution**: Click the location bar ("Report saved to: ...") and select a new folder. The warning will disappear.

### Test stopped unexpectedly
- **Cause**: The browser tab was closed, or the computer went to sleep (if Wake Lock failed).
- **Solution**: Reopen the tool. It will detect an incomplete test and ask if you want to resume. Click "Yes" to continue from the last saved point.

### Chart not showing
- **Cause**: No tests have been completed yet.
- **Solution**: Run a test first. The chart appears after a test completes.

### Previous reports not showing
- **Cause**: Browser storage may have been cleared, or no tests have been run.
- **Solution**: Reports are stored in your browser's `localStorage`. If you clear browsing data, they are lost. Always save important reports as files.

### Test won't start
- **Cause**: Battery is charging, or battery level is below 95%.
- **Solution**: Unplug the charger and ensure battery is at least 95% charged.

### The info icon popup doesn't appear
- **Cause**: Hover may not work on touch devices.
- **Solution**: Tap the icon on mobile/tablet (though the tool is not designed for mobile). On desktop, ensure you hover directly over the ⓘ.

---

## General Issues

### I found a bug
Please [open an issue](https://github.com/CreatorsEye/battery-reporter/issues) with:
- Browser name and version
- Steps to reproduce
- Any error messages (check browser console: F12)

### I have a feature request
We'd love to hear it! [Start a discussion](https://github.com/CreatorsEye/battery-reporter/discussions) or email us.

### Need help?
📧 [Creatorseye@gmail.com](mailto:Creatorseye@gmail.com) – we'll respond as soon as possible.
