import logging
import os
import random
import re

import telegram
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

import messages

chastity_chat_room_id = -1001313741176
testing_chat_room_id = -1001383387681
blank_user_id = 371746844
fielder_user_id = 460632920
chastity_verification_room_id = -1001226491088
can_i_scold_for_cum_flag = True

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=os.environ.get('TELEGRAM_BABY_BOT_TOKEN'), use_context=True)
job_queue = updater.job_queue
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=messages.start_message)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def send_sticker(update, context):
    sticker_id = update.effective_message.text[13:]
    context.bot.send_sticker(chat_id=chastity_chat_room_id, sticker=sticker_id)


sticker_handler = CommandHandler('sendsticker', send_sticker)
dispatcher.add_handler(sticker_handler)


def help_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=messages.help_message)


help_handler = CommandHandler('help', help_message)
dispatcher.add_handler(help_handler)


def rules_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=messages.rules_message, parse_mode="HTML")


rule_handler = CommandHandler('rules', rules_message)
dispatcher.add_handler(rule_handler)


def blank_lockup_time_remaining(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=messages.blank_remaining_lockup_message)


blank_lockup_time_remaining_handler = CommandHandler('blanktimeremaining', blank_lockup_time_remaining)
dispatcher.add_handler(blank_lockup_time_remaining_handler)


def cum_flag_status(update, context):
    global can_i_scold_for_cum_flag
    print("Can bot scold for cumming? Flag: {}".format(can_i_scold_for_cum_flag))
    context.bot.send_message(chat_id=testing_chat_room_id, text="Scold for cumming flag: {}"
                             .format(can_i_scold_for_cum_flag))


cum_flag_status_handler = CommandHandler('cumflagstatus', cum_flag_status, Filters.user(blank_user_id))
dispatcher.add_handler(cum_flag_status_handler)


def set_cum_flag_true(context: telegram.ext.CallbackContext):
    global can_i_scold_for_cum_flag
    can_i_scold_for_cum_flag = True


def set_cum_flag_true_no_params(update, context):
    global can_i_scold_for_cum_flag
    can_i_scold_for_cum_flag = True


set_cum_flag_false_handler = CommandHandler('setcumflagtrue', set_cum_flag_true_no_params)
dispatcher.add_handler(set_cum_flag_false_handler)


def set_cum_flag_false():
    global can_i_scold_for_cum_flag
    can_i_scold_for_cum_flag = False


def cum_response_picker():
    cum_response_list = ["No cumming!",
                         "Cum? No cumming in here.",
                         "No jerking off!",
                         "Good boys/girls don't cum :3",
                         "Send all cum to @kuhakuna :3"]
    r = random.randint(0, len(cum_response_list) - 1)
    return cum_response_list[r]


def cum_response(update, context):
    global can_i_scold_for_cum_flag
    if can_i_scold_for_cum_flag:
        context.bot.send_message(chat_id=update.effective_chat.id, text=cum_response_picker())
        set_cum_flag_false()
        job_queue.run_once(set_cum_flag_true, 60 * 60)


cum_response_handler = MessageHandler(Filters.regex(re.compile(r"cum", re.IGNORECASE))
                                      & Filters.chat(chastity_chat_room_id), cum_response)
dispatcher.add_handler(cum_response_handler)


def dab_sticker_picker():
    dab_sticker_list = ["CAADAQAD1RgAAq8ZYgdcB8lHzOVkygI",
                        "CAADAQAD7gEAAhEGqwlytbx1F2M-BgI",
                        "CAADAQADDwADcouvDUq7K8oFFbfHAg",
                        "CAADAQADEwADdcgBEzNe0p5iB_HLAg",
                        "CAADAQADHQEAAg8jgw4tPkvzKMG39QI",
                        "CAADAQADKlMAAq8ZYgfqc7TJmwx0SAI",
                        "CAADAQADQgIAAqxLwQUQxEd-TgF1aQI",
                        "CAADAQADRAIAAqxLwQXgDVdHsPdm2wI",
                        "CAADAQADwgADzTr1Big_0qJcXDGCAg",
                        "CAADAgADEgEAAvgFTgZaDCZDT0Wh2AI",
                        "CAADBAADLgAD4wMhCHn92P-fi8Ag",
                        "CAADBQADfAEAAvJpOhFtt3YGhwSvtwI",
                        "CAADAQADsgADpA-XCDviwRGhuxgeAg",
                        "CAADAQADsU8AAq8ZYge_9cJqfuLN9wI"]
    r = random.randint(0, len(dab_sticker_list) - 1)
    return dab_sticker_list[r]


def dab(update, context):
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=dab_sticker_picker())


dab_handler = CommandHandler('dab', dab)
dispatcher.add_handler(dab_handler)

rp_counter = 0


def rp_scolder(update, context):
    global rp_counter
    rp_counter += 1
    if rp_counter >= 3:
        context.bot.send_message(chat_id=chastity_chat_room_id, text="*Cums harder!*")
        rp_counter = 0


rp_scolder_handler = MessageHandler(Filters.regex(r"^\*.*\*$"), rp_scolder)
dispatcher.add_handler(rp_scolder_handler)


def add_group(update, context):
    for _ in update.message.new_chat_members:
        update.message.reply_text(messages.rules_message, parse_mode="HTML")


new_member_handler = MessageHandler(Filters.status_update.new_chat_members, add_group)
dispatcher.add_handler(new_member_handler)


def blank_time_remaining_short(update, context):
    update.message.reply_text(messages.blank_remaining_time_short_message, parse_mode="HTML")


blank_lockup_time_remaining_short_handler = CommandHandler('blanklockupshort', blank_time_remaining_short)
dispatcher.add_handler(blank_lockup_time_remaining_short_handler)


def is_blank(id):
    return id == blank_user_id


def bot_speak(update, context, reply_id=0):
    effective_message = ""
    pattern = re.compile(r'/botspeak(?:.id:(\d*))*.(.*)')
    regex_message = re.search(pattern, update.effective_message.text)
    if regex_message:
        reply_id = regex_message.group(1)
        effective_message = regex_message.group(2)

    print(effective_message)
    print(reply_id)

    debug_message = "Reply ID:{}, Message:{}".format(reply_id, effective_message)
    context.bot.send_message(chat_id=chastity_chat_room_id, text=effective_message, parse_mode="HTML",
                             reply_to_message_id=reply_id)


bot_speak_handler = CommandHandler('botspeak', bot_speak, Filters.user(blank_user_id))
dispatcher.add_handler(bot_speak_handler)


def extract_sticker_info(update, context):
    context.bot.send_message(chat_id=testing_chat_room_id,
                             text="Sticker info extracted to console. Sticker ID: {}"
                             .format(update.message.sticker.file_id))


extract_sticker_info_handler = MessageHandler(Filters.sticker & Filters.chat(testing_chat_room_id),
                                              extract_sticker_info)
dispatcher.add_handler(extract_sticker_info_handler)


def nighty(update, context):
    update.message.reply_text("<code>Good night! :3</code>", parse_mode="HTML")


nighty_handler = MessageHandler(Filters.regex(re.compile(r"night", re.IGNORECASE)) & (~Filters.command) &
                                (Filters.user(username="The_FielderThe_Fielder") | Filters.user(
                                    username="KuhakuNA") | Filters.user(username="HossRump")),
                                nighty)
dispatcher.add_handler(nighty_handler)


def extract_user_info(update, context):
    print(update)
    context.bot.send_message(chat_id=testing_chat_room_id, text="User info extracted to console. User ID: {}"
                             .format(update.message.forward_from.id))


extract_user_info_handler = MessageHandler(Filters.forwarded & Filters.chat(testing_chat_room_id), extract_user_info)
dispatcher.add_handler(extract_user_info_handler)


def dave(update, context):
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker="CAACAgEAAx0CUnTSIQACAcpgDfS8cVXWwnvfpR4faaDL7WMQ3wACy1AAAq8ZYgecUnbotF0GiB4E",
                             reply_to_message_id=update.effective_message.message_id)


dave_handler = CommandHandler('dave', dave)
dispatcher.add_handler(dave_handler)


# Prints incoming text messages to console
def message_logger(update, context):
    global rp_counter
    rp_counter = 0
    message = update.effective_message
    if update.message:
        print("Chat ID:{} Chat:{} User ID:{} User:{} Message ID:{} Message:{}".format(update.effective_chat.id,
                                                                                      update.effective_chat.title,
                                                                                      message.from_user.id,
                                                                                      message.from_user.full_name,
                                                                                      message.message_id,
                                                                                      update.message.text))


message_printer = MessageHandler(Filters.text, message_logger)
dispatcher.add_handler(message_printer)


# Prints incoming photos to console
def photo_logger(update, context):
    message = update.effective_message
    print("Chat ID:{} Chat:{} User ID:{} User:{}, Got a photo!".format(update.effective_chat.id,
                                                                       update.effective_chat.title,
                                                                       message.from_user.id,
                                                                       message.from_user.full_name, ))


photo_logger_printer = MessageHandler(Filters.photo, photo_logger)
dispatcher.add_handler(photo_logger_printer)


# Prints incoming stickers to the console
def sticker_logger(update, context):
    message = update.effective_message
    print(
        "Chat ID:{} Chat:{} User ID:{} User:{} Got a sticker! ID:{}\nUnique id:{}".format(
            update.effective_chat.id,
            update.effective_chat.title,
            message.from_user.id,
            message.from_user.full_name,
            message.sticker.file_id,
            message.sticker.file_unique_id))


sticker_logger_printer = MessageHandler(Filters.sticker, sticker_logger)
dispatcher.add_handler(sticker_logger_printer)

if __name__ == '__main__':
    updater.start_polling()
    print("I'm running papa!")
