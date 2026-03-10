#!/bin/bash
echo "Installing CEBT (Creators Eye Battery Tester) for macOS..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
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

# Create installation folder
mkdir -p ~/CEBT
cp cebt.py ~/CEBT/

# Create wrapper in /usr/local/bin
sudo tee /usr/local/bin/cebt > /dev/null << 'EOF'
#!/bin/bash
python3 ~/CEBT/cebt.py "$@"
EOF

sudo chmod +x /usr/local/bin/cebt

echo "✅ CEBT installed successfully!"
echo ""
echo "You can now use 'cebt' from any terminal:"
echo "  cebt /S    - Start test"
echo "  cebt /R    - Show results"
echo "  cebt /C    - Compare tests"
echo "  cebt /L    - Open last report"
echo "  cebt /O    - Set output folder"
echo "  cebt /H    - Show help"
echo ""
