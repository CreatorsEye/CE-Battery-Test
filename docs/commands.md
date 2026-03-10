# CLI Commands Reference

All commands work the same on Windows, macOS, and Linux.

---

## Command Summary

| Command | Description | Example |
|:---|:---|:---|
| `/S` | Start a new battery test | `cebt /S` |
| `/R` | Show last test results | `cebt /R` |
| `/C` | Compare all tests | `cebt /C` |
| `/L` | Open last report in browser | `cebt /L` |
| `/O` | Set output folder | `cebt /O "C:\tests"` |
| `/H` | Show help | `cebt /H` |

---

## Detailed Usage

### `/S` – Start Test

```bash
cebt /S
```

Starts a new battery drain test.

**What happens:**
* Checks battery level (recommends 100% but allows any)
* Creates log file in output folder
* Logs battery percentage every 5 minutes
* Automatically stops at 5%
* Generates HTML report with charts

**Output files:**
```text
[output folder]/
├── test-2024-03-10-143022_log.txt     # 5-minute readings
└── test-2024-03-10-143022_report.html  # Final report
```

---

### `/R` – Show Results

```bash
cebt /R
```

Displays the most recent test results in a formatted table.

**Example output:**
```text
============================================================
CEBT - Test Results (test-2024-03-10-143022)
============================================================
Started  : 2024-03-10 14:30:22 (100%)
Ended    : 2024-03-10 16:50:15 (5%)
Duration : 2h 19m 53s
Health   : Good (est. full charge: 6h 45m)

5-Minute Log:
Time      Percent
14:30:22  100%
14:35:24  98%
14:40:19  95%
... (truncated) ...
16:45:18  8%
16:50:15  5%
```

---

### `/C` – Compare Tests

```bash
cebt /C
```

Shows a comparison of all your past tests.

**Example output:**
```text
============================================================
CEBT - Test Comparison
============================================================
Found 5 tests in: C:\Users\Name\Documents\CEBT-Reports\

Name                Date         Duration  Health
workday-2024-03-10  2024-03-10   6h 30m    Excellent
weekend-2024-03-09  2024-03-09   5h 45m    Good
gaming-2024-03-08   2024-03-08   2h 48m    Fair
quick-2024-03-07    2024-03-07   2h 15m    Fair
old-2024-03-01      2024-03-01   4h 20m    Good
```

---

### `/L` – Open Last Report

```bash
cebt /L
```

Opens the most recent HTML report in your default browser.

**First time use:**
If `battery-reporter.html` is not found in the current folder, you'll be prompted:

```text
❌ battery-reporter.html not found!

Options:
[1] Manual download - Open GitHub page + instructions
[2] Auto-download - Save directly to this folder
[3] Cancel - Exit
```

**Choose:**
* **Option 1**: Browser opens to GitHub. Download and place file manually.
* **Option 2**: Downloads automatically to current folder.
* **Option 3**: Exit.

After the HTML file is in place, the report will open in your browser.

---

### `/O` – Set Output Folder

**Without path:**
```bash
cebt /O
```
Shows current output folder.

**With path:**
```bash
cebt /O "C:\path\to\folder"
cebt /O "D:\battery-tests"
cebt /O "/Users/name/battery-tests"
cebt /O "/home/name/battery-tests"
```

**Notes:**
* Folder is created automatically if it doesn't exist.
* Use quotes if path contains spaces.
* Setting persists across sessions.

---

### `/H` – Show Help

```bash
cebt /H
```

Displays this help information.

---

## Examples

### Basic Usage
```bash
# Start a test
cebt /S

# Set custom output folder
cebt /O "D:\my-battery-tests"

# View last results
cebt /R

# Compare all tests
cebt /C

# Open report in browser
cebt /L

# Show help
cebt /H
```

### Advanced Examples
```bash
# Start test with custom folder (one command)
cebt /O "C:\tests" && cebt /S

# View results and open report
cebt /R && cebt /L

# Check current folder before starting
cebt /O
```

---

## Exit Codes

| Code | Meaning |
|:---|:---|
| 0 | Success |
| 1 | Python not installed |
| 2 | Invalid command |
| 3 | HTML file missing (and not downloaded) |
| 4 | Output folder error |
| 5 | Test interrupted by user |

---

## Environment Variables

| Variable | Purpose |
|:---|:---|
| `CEBT_OUTPUT` | Default output folder (overrides config) |
| `CEBT_NO_COLOR` | Disable colored output (set to 1) |

**Example:**
```bash
export CEBT_OUTPUT="/custom/folder"
export CEBT_NO_COLOR=1
cebt /S
```

---

## Configuration File

Settings are stored in:
* **Windows:** `%USERPROFILE%\.cebt\config.json`
* **macOS/Linux:** `~/.cebt/config.json`

**Example config:**
```json
{
  "output_folder": "C:\\Users\\Name\\Documents\\CEBT-Reports",
  "stop_percent": 5,
  "theme": "dark"
}
```

---

## Need Help?
* **GitHub Issues:** [https://github.com/CreatorsEye/battery-reporter/issues](https://github.com/CreatorsEye/battery-reporter/issues)
* **Email:** Creatorseye@gmail.com
