import math

import pynewtonmath as newton
from MashaRoBot import dispatcher
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async


@run_async
def simplify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.simplify("{}".format(args[0])))


@run_async
def factor(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.factor("{}".format(args[0])))


@run_async
def derive(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.derive("{}".format(args[0])))


@run_async
def integrate(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.integrate("{}".format(args[0])))


@run_async
def zeroes(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.zeroes("{}".format(args[0])))


@run_async
def tangent(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.tangent("{}".format(args[0])))


@run_async
def area(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.area("{}".format(args[0])))


@run_async
def cos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))


@run_async
def sin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))


@run_async
def tan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))


@run_async
def arccos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))


@run_async
def arcsin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))


@run_async
def arctan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))


@run_async
def abs(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))


@run_async
def log(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))


__help__ = """
*INLINE*
Simple hacks of telegram that most of the Users don't know
 
*Use this @ tags for searching inline*

> @gif/@coub to search for GIFs

> @youtube/@vid to search videos on Youtube

> @bing/@pic to search images on Bing and Yandex

> @wiki to search for information on Wikipedia (opens link)

> @imdb to search movies info on IMDB

> @sticker to search for stickers using available emoji

> @bold to convert texts to bold, italic and formatted

> @dictrobot/@exactlyappbot to search for English dictionary definitions of words

> @iLyricsBot to search for Lyrics to any song

> @lutilbot to translate words/sentences into over 70 languages using InLine Translator

> @storebot to search for other bots in the store bot

> @the_musicbot  @vkm_bot sends you music files (only works in group and its own private chat)

> @mrbytebot is an AI bot that works in groups or its own private chat. Mr Byte can also work inline with reduced functionality. You can get results from Urban Dictionary, YouTube, 
Reddit, Wikipedia, Weather, e.t.c

> @my_ali_bot allows you to check prices and shop on AliExpress

> @getmediabot to search and download audio and video files

> @gamee/@gamebot to get a list of available Telegram games which play in-app

Credit Goes to Telegram 
"""



__mod_name__ = "INLINE"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("math", simplify)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", derive)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent)
AREA_HANDLER = DisableAbleCommandHandler("area", area)
COS_HANDLER = DisableAbleCommandHandler("cos", cos)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs)
LOG_HANDLER = DisableAbleCommandHandler("log", log)

dispatcher.add_handler(SIMPLIFY_HANDLER)
dispatcher.add_handler(FACTOR_HANDLER)
dispatcher.add_handler(DERIVE_HANDLER)
dispatcher.add_handler(INTEGRATE_HANDLER)
dispatcher.add_handler(ZEROES_HANDLER)
dispatcher.add_handler(TANGENT_HANDLER)
dispatcher.add_handler(AREA_HANDLER)
dispatcher.add_handler(COS_HANDLER)
dispatcher.add_handler(SIN_HANDLER)
dispatcher.add_handler(TAN_HANDLER)
dispatcher.add_handler(ARCCOS_HANDLER)
dispatcher.add_handler(ARCSIN_HANDLER)
dispatcher.add_handler(ARCTAN_HANDLER)
dispatcher.add_handler(ABS_HANDLER)
dispatcher.add_handler(LOG_HANDLER)
