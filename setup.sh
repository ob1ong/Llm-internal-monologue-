#!/bin/bash

# Define variables
PROJECT_DIR="/home/zero/llm-monologue"
VENV_DIR="$PROJECT_DIR/ve"
PHOTO_DIR="$PROJECT_DIR/photos"
REQUIREMENTS_FILE="$PROJECT_DIR/requirements.txt"

# Step 1: Create project directory
mkdir -p "$PHOTO_DIR"
cd "$PROJECT_DIR" || exit

# Step 2: Create virtual environment
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# Step 3: Create requirements.txt
cat > "$REQUIREMENTS_FILE" <<EOF
openai
gTTS
pygame
EOF

# Step 4: Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Step 5: Confirm setup
echo "✅ Virtual environment created at $VENV_DIR"
echo "✅ Photos directory: $PHOTO_DIR"
echo "✅ Dependencies installed"
echo "➡️ To activate, run: source $VENV_DIR/bin/activate"
