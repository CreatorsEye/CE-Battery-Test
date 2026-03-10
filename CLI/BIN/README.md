# CEBT – CLI for End Users

## Installers

| OS | File | What to Do |
|----|------|------------|
| Windows | install-windows.bat | Double-click to install |
| macOS | install-macos.sh | Run: `bash install-macos.sh` |
| Linux | install-linux.sh | Run: `bash install-linux.sh` |

---

## After Installation

Open any terminal and type:

```bash
cebt /S     # Start test
cebt /R     # Show results
cebt /C     # Compare tests
cebt /L     # Open last report in browser
cebt /O     # Set output folder
cebt /H     # Show help
```

---

## HTML File for Reports

The first time you run `cebt /L`, you will see:

```text
❌ battery-reporter.html not found!

Options:
[1] Manual download - Open GitHub page + instructions
[2] Auto-download - Save directly to this folder
[3] Cancel - Exit
```

**Choose:**

* **Option 1:** Browser opens to GitHub. Download the file and place it in the current folder.
* **Option 2:** Downloads automatically to the current folder.
* **Option 3:** Exits without doing anything.

After the HTML file is in place, `cebt /L` will open your reports in the browser.

---

## Default Output Folder

Reports are saved to: `Documents/CEBT-Reports/`

To change: `cebt /O "C:\your-folder"`

---

## Commands Details

### `/S` – Start Test
```bash
cebt /S
```
Begins a new battery drain test. Logs every 5 minutes and stops at 5%.

### `/R` – Show Results
```bash
cebt /R
```
Displays the most recent test results in a table format.

### `/C` – Compare Tests
```bash
cebt /C
```
Shows a comparison of all your past tests.

### `/L` – Open Last Report
```bash
cebt /L
```
Opens the most recent HTML report in your browser. Will prompt for HTML file if missing.

### `/O` – Set Output Folder
```bash
cebt /O "C:\path\to\folder"
```
Changes where test logs and reports are saved.

### `/H` – Show Help
```bash
cebt /H
```
Displays this help information.

---

## Examples

```bash
# Start a new test
cebt /S

# Set custom output folder
cebt /O "D:\battery-tests"

# View last results
cebt /R

# Open report in browser
cebt /L

# Compare all tests
cebt /C
```

---

## Troubleshooting

**Q: I get "command not found" after installation.** **A:** Restart your terminal or open a new one.

**Q: Python is not installed.** **A:** Download from [python.org](https://www.python.org/) and run the installer again.

**Q: Download fails with "SSL error".** **A:** Use manual download option instead.

**Q: Reports folder not found.** **A:** Run a test first with `cebt /S` to create it.

---

## Need Help?

* **GitHub Issues:** [https://github.com/CreatorsEye/battery-reporter/issues](https://github.com/CreatorsEye/battery-reporter/issues)
* **Email:** Creatorseye@gmail.com
