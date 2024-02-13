from starlette.responses import (
    PlainTextResponse,
    Response,
    RedirectResponse,
    HTMLResponse,
    JSONResponse,
)
from starlette.requests import Request
import logging
import base64
import re


# Things added by @giacomo
import spotifyhelper
import userhelper
from spotifyhelper import spotifyFactory
from spotifyhelper import SpotifyOauthError
from spotifyhelper import SpotifyException
from spotifyhelper import makeConnectMessage
from spotifyhelper import validateSearch
from spotifyhelper import spotifyOauthErrorText
from spotifyhelper import spotifyException
from spotifyhelper import spotifyExceptionWarning
from spotifyhelper import callback_spotify_unhandled_exception
from spotifyhelper import callback_spotify_info
from spotifyhelper import callback_spotify_nocode
from spotifyhelper import make_callback_spotify_infoText
from spotifyhelper import callback_spotify_connected
from spotifyhelper import validateTrackId
from spotifyhelper import addSpotifyPrefix
from spotifyhelper import sp_is_none


class SpotifyCallback:
    def __init__(self, application) -> None:
        self.application = application

    async def spotify_callback(
        self, request: Request
    ) -> PlainTextResponse:
        """
        This function handles the callback from spotify when authorizing request to an account
        """

        logging.info(callback_spotify_info)

        if "code" not in request.query_params:
            logging.error(callback_spotify_nocode)
            # callback without code
            return Response()

        code = request.query_params["code"]
        if not re.search("^[A-Za-z0-9\-\_]+$", code):
            logging.warning(
                "authorisation code does not match regex"
            )
            return Response()

        state = request.query_params["state"]
        if not re.search("^[0-9A-Za-z\-]+", state):
            logging.warning("state parameter does not match regex")
            return Response()

        try:
            state = base64.b64decode(state.encode("ascii")).decode(
                "ascii"
            )
            [chatid, userid] = state.split(":")
            chatid = int(chatid)
            userid = int(userid)
        except:
            logging.error(
                "Failure during state query parameter parsing"
            )
            return Response()

        logging.info(
            make_callback_spotify_infoText(chatid, userid, code)
        )

        try:
            auth_manager = await spotifyhelper.get_auth_manager(
                chatid
            )
            if auth_manager is not None:
                auth_manager.get_access_token(code)
                await userhelper.set_group_owner(chatid, userid)
                await self.application.bot.send_message(
                    chat_id=userid, text=callback_spotify_connected
                )
        except Exception as e:
            logging.error(e)
            logging.error(
                "Failure during auth_manager instantiation"
            )
            return Response()

        return Response(
            """    
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Authorisation succesfull!</title>
  <link rel="stylesheet" href="/jukebox/assets/JukeboxBot.css">
</head>
<body>
  <div class="container">
    <div class="image-container">
      <div class="image-content">
        <img src="/jukebox/assets/auth_success.png" alt="JukeboxBot" />
    </div>
  </div>
</body>
</html>    
"""
        )
