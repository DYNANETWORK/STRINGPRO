from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
๐๐ฒ๐ ๐คจ {}
Welcome to {}
๐ฌ๐ผ๐ ๐๐ฎ๐ป ๐จ๐๐ฒ ๐ ๐ฒ ๐ง๐ผ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ฒ ๐ฃ๐๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ ๐๐ป๐ฑ ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป ๐ฆ๐๐ฟ๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป. ๐จ๐๐ฒ ๐๐ฒ๐น๐ผ๐ ๐๐๐๐๐ผ๐ป๐ ๐ง๐ผ ๐๐ฒ๐ฎ๐ฟ๐ป ๐ ๐ผ๐ฟ๐ฒ !
By @MAMBA_X_SUPPORT
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("๐ฅ ๐ฆ๐๐ฎ๐ฟ๐ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป ๐ฅ", callback_data="generate")],
        [InlineKeyboardButton(text="๐  Return Home ๐ ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฅ ๐ฆ๐๐ฎ๐ฟ๐ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป ๐ฅ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ฅ ๐ฆ๐๐ฎ๐ฟ๐ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป ๐ฅ", callback_data="generate")],
        [InlineKeyboardButton("๐ค ๐๐ผ๐ ๐ง๐ผ ๐จ๐๐ฒ ๐ ๐ฒ ๐ค", callback_data="help")],
        [InlineKeyboardButton("โฅ ๐ฆ๐ผ๐๐ฟ๐ฐ๐ฒ ๐๐ป๐ฑ ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐ โฅ", url="https://t.me/MAMBA_X_SUPPORT")],
    ]

    # Help Message
    HELP = """
โจ **Available Commands** โจ
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""
