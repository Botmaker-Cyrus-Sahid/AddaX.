# Save the code as 'instagram-report' (no extension)
nano $PREFIX/bin/instagram-report

# Paste the code, then make executable
chmod +x $PREFIX/bin/instagram-report

# Install dependencies (if you add real functionality)
pkg install python
pip install requests   # example

# Run it
instagram-report --username example_user --action info --verbose
