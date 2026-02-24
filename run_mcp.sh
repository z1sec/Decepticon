#!/bin/bash

# Set the target directory path.
# You can use a path relative to the script's location like this:
# BASE_DIR=$(dirname "$0")
# TARGET_DIR="$BASE_DIR/src/tools/mcp"

# Or, you can specify the path directly.
TARGET_DIR="src/tools/mcp"

# Check if any .py files exist in the target directory.
if ! ls "$TARGET_DIR"/*.py &> /dev/null; then
    echo "Error: Could not find any Python (.py) files in the '$TARGET_DIR' directory."
    exit 1
fi

# Loop through all files ending with .py in the TARGET_DIR.
for file in "$TARGET_DIR"/*.py
do
  echo "Executing script '$file' in a new terminal window..."

  # Check the operating system (OS).
  if [[ "$(uname)" == "Darwin" ]]; then
    # This is macOS.
    # Use osascript to control Terminal.app and run the command.
    osascript -e "tell app \"Terminal\" to do script \"python3 '$file'; echo; read -p 'Script execution finished. Press Enter to close this window...'\"" &
  
  else
    # This is Linux (assuming GNOME Terminal, common in Ubuntu/Fedora).
    # If gnome-terminal is not available, you might need to change this to xterm, konsole, etc.
    gnome-terminal -- bash -c "python3 '$file'; echo; read -p 'Script execution finished. Press Enter to close this window...'; exec bash" &
  fi
done

echo "All script execution requests have been sent."