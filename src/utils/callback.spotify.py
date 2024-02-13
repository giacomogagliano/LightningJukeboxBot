import asyncio_mqtt as aiomqtt
from telegram.ext import ContextTypes

import settings
import spotifyhelper
from spotifyhelper import spotifyFactory
import logging
import json


# Things added by @giacomo
from spotifyhelper import spotifyFactory
from spotifyhelper import callback_spotify_unhandled_exception


class CallbackSpotify:
    def __init__(self, now_playing_message) -> None:
        self.now_playing_message = now_playing_message

    async def callback_spotify(
        self, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """
        This function creates a message of the current playing track. It reschedules itself depending on the remaining time
        for the current playing track. Basically two seconds after the time, the first track has finished playing
        """
        interval = 300
        try:
            for key in settings.rds.scan_iter("group:*"):
                # logging.info(f"callback_spotify for group {key}")
                chat_id = key.decode("utf-8").split(":")[1]
                auth_manager = await spotifyhelper.get_auth_manager(
                    chat_id
                )
                if auth_manager is None:
                    # logging.warning("Auth manager is None in callback_spotify")
                    continue
                currenttrack = None
                try:
                    sp = spotifyFactory(auth_manager=auth_manager)
                    currenttrack = sp.current_user_playing_track()
                except:
                    # logging.info("Exception while querying the current playing track at spotify")
                    continue
                title = "Nothing playing at the moment"
                if (
                    currenttrack is not None
                    and "item" in currenttrack
                    and currenttrack["item"] is not None
                ):
                    title = spotifyhelper.get_track_title(
                        currenttrack["item"]
                    )
                    # update history
                    await spotifyhelper.update_history(
                        chat_id, title
                    )
                    newinterval = (
                        currenttrack["item"]["duration_ms"]
                        - currenttrack["progress_ms"]
                    ) / 1000 + 2
                    if newinterval < interval:
                        interval = newinterval
                elif currenttrack is not None:
                    logging.info(json.dumps(currenttrack))
                # update the title
                if chat_id in self.now_playing_message:
                    [message_id, prev_title] = (
                        self.now_playing_message[chat_id]
                    )
                    if prev_title != title:
                        try:
                            await context.bot.editMessageText(
                                title,
                                chat_id=chat_id,
                                message_id=message_id,
                            )
                            self.now_playing_message[chat_id] = [
                                message_id,
                                title,
                            ]
                            logging.info(
                                f"Now playing {title} in chat {chat_id}"
                            )
                        except:
                            # logging.error("Exception when refreshing now playing")
                            pass
                        try:
                            async with aiomqtt.Client(
                                "localhost"
                            ) as client:
                                await client.publish(
                                    f"{chat_id}/now_playing",
                                    payload=title,
                                )
                        except:
                            logging.error(
                                "Exception when publishing current track to mqtt"
                            )
                            pass
                else:
                    logging.info("Creating new pinned message")
                    try:
                        message = await context.bot.send_message(
                            text=title, chat_id=chat_id
                        )
                        await context.bot.pin_chat_message(
                            chat_id=chat_id, message_id=message.id
                        )
                        self.now_playing_message[chat_id] = [
                            message.id,
                            title,
                        ]
                    except:
                        logging.error(
                            "Exception when sending message to group"
                        )
        except:
            logging.error(callback_spotify_unhandled_exception)
        finally:
            if interval < 30 or interval > 300:
                interval = 30
            logging.info(f"Next run in {interval} seconds")
            context.job_queue.run_once(
                self.callback_spotify,
                interval,
                job_kwargs={"misfire_grace_time": None},
            )
