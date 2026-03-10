#!/usr/bin/env python3
"""
CEBT - Creators Eye Battery Tester
Command line tool for battery testing
"""

import sys
import os
import time
import webbrowser
import urllib.request
import glob
from datetime import datetime
import platform
import json
from pathlib import Path

# Constants
HTML_FILENAME = "battery-reporter.html"
GITHUB_HTML_URL = "https://raw.githubusercontent.com/CreatorsEye/battery-reporter/main/GUI/HTML/battery-reporter.html"
GITHUB_PAGE_URL = "https://github.com/CreatorsEye/battery-reporter/blob/main/GUI/HTML/battery-reporter.html"
CONFIG_DIR = os.path.join(str(Path.home()), ".cebt")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    """Load configuration from file"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    """Save configuration to file"""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def get_default_output_folder():
    """Get default output folder based on OS"""
    home = str(Path.home())
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(home, "Documents", "CEBT-Reports")
    elif system == "Darwin":  # macOS
        return os.path.join(home, "Documents", "CEBT-Reports")
    else:  # Linux
        return os.path.join(home, "CEBT-Reports")

def check_html_file():
    """Check if HTML file exists in current directory"""
    return os.path.exists(HTML_FILENAME)

def handle_missing_html():
    """Offer options when HTML file is missing"""
    print("\n" + "="*60)
    print("❌ battery-reporter.html not found!")
    print("="*60)
    print("\nThis file is needed to display battery reports.")
    print(f"\nCurrent folder: {os.getcwd()}")
    print("\nOptions:")
    print("  [1] Manual download - Open GitHub page + instructions")
    print("  [2] Auto-download - Save directly to this folder")
    print("  [3] Cancel - Exit")
    print("\n" + "="*60)
    
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == "1":
            return manual_download()
        elif choice == "2":
            return auto_download()
        elif choice == "3":
            print("\n❌ Cancelled.")
            return False
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def manual_download():
    """Open browser with instructions for manual download"""
    webbrowser.open(GITHUB_PAGE_URL)
    
    target_folder = os.getcwd()
    target_path = os.path.join(target_folder, HTML_FILENAME)
    
    print("\n" + "="*60)
    print("📋 MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*60)
    print(f"\n1. Browser opened to GitHub page")
    print(f"2. Click the 'Raw' button or download icon")
    print(f"3. Save the file to this exact folder:")
    print(f"   {target_folder}")
    print(f"4. Make sure the file is named: {HTML_FILENAME}")
    print(f"5. Then press Enter to continue")
    print("\n" + "="*60)
    
    input("\nPress Enter after you've placed the file...")
    
    if os.path.exists(target_path):
        print(f"\n✅ File found! Continuing...")
        return True
    else:
        print(f"\n❌ File still not found at: {target_path}")
        retry = input("Try again? (y/n): ").lower()
        if retry == 'y':
            return manual_download()
        else:
            return False

def auto_download():
    """Auto-download HTML file from GitHub"""
    try:
        print("\n📥 Downloading battery-reporter.html...")
        urllib.request.urlretrieve(GITHUB_HTML_URL, HTML_FILENAME)
        print("✅ Download complete!")
        return True
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("Please try manual download instead.")
        return False

def start_test():
    """Start a new battery test"""
    config = load_config()
    output_folder = config.get("output_folder", get_default_output_folder())
    
    print("\n🔋 CEBT - Starting battery test...")
    print(f"📁 Output folder: {output_folder}")
    print("\n⚠️  This feature is under development.")
    print("Check back soon for the full implementation.")
    print("\nFor now, use the HTML GUI version:")
    print("https://github.com/CreatorsEye/battery-reporter/tree/main/GUI/HTML")

def show_results():
    """Show last test results"""
    print("\n📊 CEBT - Test Results")
    print("\n⚠️  This feature is under development.")
    print("Check back soon for the full implementation.")

def compare_tests():
    """Compare all tests"""
    print("\n📊 CEBT - Compare Tests")
    print("\n⚠️  This feature is under development.")
    print("Check back soon for the full implementation.")

def open_last_report():
    """Open the most recent HTML report"""
    print("\n📂 Opening last battery report...")
    
    # Check for HTML file first
    if not check_html_file():
        if not handle_missing_html():
            return
    
    # Get output folder from config
    config = load_config()
    reports_folder = config.get("output_folder", get_default_output_folder())
    
    if not os.path.exists(reports_folder):
        print(f"\n❌ No reports folder found at: {reports_folder}")
        print("Run a test first with: cebt /S")
        return
    
    report_files = list(Path(reports_folder).glob("*_report.html"))
    if not report_files:
        print("\n❌ No report files found.")
        print("Run a test first with: cebt /S")
        return
    
    # Get most recent
    latest_report = max(report_files, key=lambda p: p.stat().st_mtime)
    
    # Open in browser using the HTML file
    html_path = os.path.abspath(HTML_FILENAME)
    print(f"\n📄 Using viewer: {html_path}")
    print(f"📄 Opening report: {latest_report.name}")
    
    # Open the HTML file
    webbrowser.open(f"file://{html_path}")
    print("✅ Report opened in your browser")

def set_output():
    """Set output folder"""
    config = load_config()
    
    if len(sys.argv) < 3:
        current = config.get("output_folder", get_default_output_folder())
        print(f"\n📁 Current output folder: {current}")
        print("\nTo change: cebt /O \"C:\\your\\folder\"")
        return
    
    folder = sys.argv[2]
    
    # Create folder if it doesn't exist
    try:
        os.makedirs(folder, exist_ok=True)
        config["output_folder"] = folder
        save_config(config)
        print(f"\n✅ Output folder set to: {folder}")
    except Exception as e:
        print(f"\n❌ Error creating folder: {e}")

def show_help():
    """Show help information"""
    print("""
╔════════════════════════════════════╗
║   CEBT - Creators Eye Battery Tester   ║
╚════════════════════════════════════╝

COMMANDS:
  cebt /S              Start a new battery test
  cebt /R              Show last test results
  cebt /C              Compare all tests
  cebt /L              Open last report in browser
  cebt /O "folder"     Set output folder
  cebt /H              Show this help

EXAMPLES:
  cebt /S
  cebt /O "C:\\my-tests"
  cebt /L

NOTES:
  - First time using /L? The tool will help you get battery-reporter.html
  - Reports are saved to: Documents/CEBT-Reports/ (can be changed with /O)
  - All data stays on your device - 100% offline

For more information, visit:
https://github.com/CreatorsEye/battery-reporter
""")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("cebt /H for help")
        return
    
    cmd = sys.argv[1].upper()
    
    if cmd == "/S":
        start_test()
    elif cmd == "/R":
        show_results()
    elif cmd == "/C":
        compare_tests()
    elif cmd == "/L":
        open_last_report()
    elif cmd == "/O":
        set_output()
    elif cmd == "/H":
        show_help()
    else:
        print(f"Unknown command: {cmd}")
        print("Use: cebt /H for help")

if __name__ == "__main__":
    main()
