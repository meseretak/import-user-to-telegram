from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPhoneContact
import csv
import asyncio

api_id = YOUR_API_ID  # Get from https://my.telegram.org
api_hash = "YOUR_API_HASH"  # Get from https://my.telegram.org
group_link = "https://t.me/mesiak1"
client = TelegramClient("session", api_id, api_hash)

async def import_and_add_users():
    await client.start()

    # Load target group
    group = await client.get_entity(group_link)

    # Read phone numbers from CSV
    contacts = []
    with open("phones.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            phone = row["phone"].strip()
            contacts.append(InputPhoneContact(
                client_id=0,
                phone=phone,
                first_name="Imported",
                last_name=""
            ))

    # Step 1 → Import contacts to Telegram
    print("Importing contacts...")
    result = await client(ImportContactsRequest(contacts))
    print("Imported:", result)

    # Step 2 → Add each imported contact to group
    for user in result.users:
        try:
            await client(InviteToChannelRequest(group, [user]))
            print(f"Added: {user.first_name} ({user.id})")
        except Exception as e:
            print(f"Failed to add {user.id}: {e}")

asyncio.run(import_and_add_users())