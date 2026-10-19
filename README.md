# \# Voice Order List

# 

# A Python project that converts spoken grocery orders into text and will eventually organize them into a structured grocery list.

# 

# \## Current Features

# 

# \- Transcribes audio using Faster-Whisper.

# \- Supports the first step of a voice-to-grocery-list workflow.

# 

# \## How to Run

# 

# 1\. Clone or download this repository.

# 2\. Create and activate a Python virtual environment (recommended).

# 3\. Install the dependencies:

# 

# &#x20;  ```bash

# &#x20;  pip install -r requirements.txt

# &#x20;  ```

# 

# 4\. Place your own supported audio file in the project folder and update the filename in `transcribe.py` if needed.

# 5\. Run:

# 

# &#x20;  ```bash

# &#x20;  python transcribe.py

# &#x20;  ```

# 

# \## Project Status

# 

# \- \*\*Step 1 — Speech-to-text:\*\* Completed.

# \- \*\*Step 2 — LLM extraction to structured JSON:\*\* Planned.

# \- \*\*Step 3 — Export grocery items to CSV:\*\* Planned.

# 

# This project is a work in progress.

# 

# \## Troubleshooting

# 

# If you encounter an error related to the `av` package and the `metadata\_errors` argument, try installing a compatible version:

# 

# ```bash

# python -m pip install "av<18"

# ```

# 

# The working environment used `av 17.1.0`.

# 

# \## Technologies

# 

# \- Python

# \- Faster-Whisper



