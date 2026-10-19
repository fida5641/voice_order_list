# Voice Order List

A Python project that converts spoken grocery orders into text, with the goal of organizing them into a structured grocery list.

## Current Features

- Transcribes audio files using Faster-Whisper.
- Runs locally without requiring an API key for transcription.
- Implements the speech-to-text stage of a voice-to-grocery-list pipeline.

## Example

**Input:** `order.mp3` — a voice recording of a grocery order.

**Transcribed output:**

```text
I need 1 kilo tomato, 2 packets of milk, half a kilo onion and a dozen eggs.
```

## How to Run

1. Clone this repository and open the project folder in your terminal.
2. Create and activate a virtual environment on Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Place your own supported audio file in the project folder. Update the filename in `transcribe.py` if needed.
5. Run the script:

   ```bash
   python transcribe.py
   ```

## Project Status

- **Step 1 — Speech-to-text:** Completed.
- **Step 2 — LLM extraction to structured JSON:** Planned.
- **Step 3 — Export grocery items to CSV:** Planned.

This project is a work in progress.

## Troubleshooting

If you encounter this error:

```text
TypeError: open() got an unexpected keyword argument 'metadata_errors'
```

Try installing a compatible version of `av`:

```bash
python -m pip install "av<18"
```

The working environment used `av 17.1.0`.

## Technologies

- Python
- Faster-Whisper
