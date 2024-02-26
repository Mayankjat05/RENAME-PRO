
from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command('viewthumb'))
async def view_thumbnail(client, message):
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await client.send_photo(
            chat_id=message.chat.id,
            photo=thumb
        )
    else:
        await message.reply_text("😔 **You don't have any thumbnail**")

@Client.on_message(filters.private & filters.command('delthumb'))
async def remove_thumbnail(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌ **Your thumbnail successfully deleted**")

@Client.on_message(filters.private & filters.photo)
async def add_thumbnail(client, message):
    mkn = await message.reply_text("Please wait...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
    await mkn.edit("✅ **Your thumbnail successfully saved**")
