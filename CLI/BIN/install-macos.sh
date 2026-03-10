#!/bin/bash
# CEBT Installer for macOS

echo "========================================"
echo "   CEBT - Creators Eye Battery Tester"
echo "   macOS Installation"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed!"
    echo ""
    echo "Please install Python 3.6 or higher from:"
    echo "https://www.python.org/downloads/"
    echo ""
    echo "After installing Python, run this installer again."
    echo ""
    echo "Or use the HTML GUI version instead:"
    echo "https://github.com/CreatorsEye/battery-reporter/tree/main/GUI/HTML"
    exit 1
fi

echo "[OK] Python 3 is installed."
echo ""

# Create installation folder
INSTALL_DIR="$HOME/CEBT"
mkdir -p "$INSTALL_DIR"
echo "[OK] Created folder: $INSTALL_DIR"
echo ""

# Copy cebt.py
cp cebt.py "$INSTALL_DIR/"
echo "[OK] Copied cebt.py"
echo ""

# Create wrapper in /usr/local/bin
WRAPPER_PATH="/usr/local/bin/cebt"
sudo tee "$WRAPPER_PATH" > /dev/null << EOF
#!/bin/bash
python3 "$INSTALL_DIR/cebt.py" "\$@"
EOF

sudo chmod +x "$WRAPPER_PATH"
echo "[OK] Created cebt command in /usr/local/bin"
echo ""

echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "You can now use 'cebt' from any terminal:"
echo ""
echo "  cebt /S     Start a new test"
echo "  cebt /R     Show last results"
echo "  cebt /C     Compare all tests"
echo "  cebt /L     Open last report in browser"
echo "  cebt /O     Set output folder"
echo "  cebt /H     Show help"
echo ""
echo "Reports will be saved to:"
echo "  $HOME/Documents/CEBT-Reports/"
echo ""
echo "========================================"
