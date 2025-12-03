# Telegram User Import Tool

A Python script to import users from Excel/CSV files to Telegram groups.

## Setup

1. Install Python 3.10+
2. Install dependencies:
   ```
   pip install telethon pandas openpyxl
   ```

3. Get your Telegram API credentials:
   - Go to https://my.telegram.org/auth
   - Login with your phone number
   - Click "API development tools"
   - Create an application
   - Copy your `api_id` and `api_hash`

4. Update the credentials in the script files

5. Prepare your Excel file (`users.xlsx`) with a column named "phone number"

## Usage

Run the script:
```
python "add user.py"
```

Or double-click `run.bat` on Windows.

## Files

- `add user.py` - Main script for adding users
- `TelegramClient.py` - Alternative implementation
- `users.xlsx` - Excel file with phone numbers (not included)

## Important Notes

- Never share your API credentials publicly
- Respect Telegram's rate limits
- You need admin permissions in the target group
- Phone numbers should include country code
