from telethon import TelegramClient, functions, types
import pandas as pd
import time
import asyncio

# 1. Your API credentials
api_id = YOUR_API_ID  # Get from https://my.telegram.org
api_hash = 'YOUR_API_HASH'  # Get from https://my.telegram.org

# 2. Connect to Telegram
client = TelegramClient('my_session', api_id, api_hash)

# 3. Load Excel
df = pd.read_excel('users.xlsx')
phone_numbers = df['phone number'].tolist()
print(f"Loaded {len(phone_numbers)} phone numbers from Excel")

# 4. Target group (username or ID)
target_group = 'Morning Service'  # Can be username or ID

async def add_users():
    await client.start()
    print(f"Connected to Telegram")
    print(f"Target group: {target_group}")
    
    for phone in phone_numbers:
        try:
            # Format phone number (ensure it starts with +)
            if not str(phone).startswith('+'):
                phone = '+' + str(phone)
            
            print(f"\nProcessing {phone}...")
            
            # Import contact
            user = types.InputPhoneContact(client_id=0, phone=str(phone), first_name='User', last_name='')
            result = await client(functions.contacts.ImportContactsRequest([user]))
            
            if not result.users:
                print(f"  ❌ User not found on Telegram: {phone}")
                continue
                
            user_id = result.users[0]
            print(f"  ✓ Found user: {user_id.first_name}")
            
            # Add to group
            await client(functions.channels.InviteToChannelRequest(
                channel=target_group,
                users=[user_id]
            ))
            print(f"  ✓ Added {phone} to group")
            time.sleep(5)  # Wait to avoid spam limits
            
        except Exception as e:
            print(f"  ❌ Failed to add {phone}: {e}")
    
    print("\n✅ Finished processing all users")

import asyncio

async def main():
    async with client:
        await add_users()

asyncio.run(main())
