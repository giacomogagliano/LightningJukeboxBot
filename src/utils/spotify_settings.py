from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import ContextTypes
import settings
import re
import spotifyhelper


class SpotifySettings:
    def __init__(self, delete_message) -> None:
        self.delete_message = delete_message
        pass

    # connect a spotify player to the bot, the setclient secret and set client id commands
    async def spotify_settings(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        if update.message.chat.type != "private":
            bot_me = await context.bot.get_me()

            # direct the user to their private chat
            message = await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Like keeping your mnenomic seedphrase offline, it is better to perform these actions in a private chat with me.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                f"Take me there",
                                url=f"https://t.me/{bot_me.username}",
                            )
                        ]
                    ]
                ),
            )

            context.job_queue.run_once(
                self.delete_message,
                settings.delete_message_timeout_medium,
                data={"message": message},
            )
            return

        # get spotify settings for the user
        sps = await spotifyhelper.get_spotify_settings(
            update.effective_user.id
        )

        result = re.search(
            "/(setclientid|setclientsecret)\s+([a-z0-9]+)\s*$",
            update.message.text,
        )
        if result is None:
            message = await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Incorrect usage. ",
            )
            return

        # after validation
        command = result.groups()[0]
        value = result.groups()[1]

        bSave = False
        if command == "setclientid":
            sps.client_id = value
            bSave = True

        if command == "setclientsecret":
            sps.client_secret = value
            bSave = True

        if bSave == True:
            await spotifyhelper.save_spotify_settings(sps)
            message = await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Settings updated. Type /couple for current settings and instructions.",
            )
