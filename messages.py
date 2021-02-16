import datetime

start_message = ("Hello! I am Blank's precious child. I am his first Python project and will eventually "
                 "replace his existing php bot! If you have any tips or questions or suggestions or queries"
                 "feel free to message me directly at @kuhakuna on Telegram or dm me directly at"
                 " https://twitter.com/kuhaku_ad!")

help_message = "Please contact @KuhakuNA."

rules_message = (
    "<code>/-~-/</code> Chastity 🔒 Furs <code>\-~-\\</code>\n"  # Command must always be passed under html parsing
    "<code>\-~-\</code>    CHAT RULES:   <code>/-~-/</code>\n\n"
    "1. This is an adult chatroom. No minors allowed.\n"
    "2. This is an English speaking chat.\n"
    "3. Both furry and IRL pictures are allowed.\n"
    "4. Try to keep content chastity related. Keep off topic brief. If you think it's topical"
    " and a turn on, share it!\n"
    "5. No posting extreme images. Over the top anal gifs will be subject to review, don't go overboard.\n"
    "6. Don't spam!\n"
    "7. Light RP only! Admins may ask for you to move it to private.\n"
    "8. Ask an admin before advertising, please.\n"
    "9. Limit voting links to two times a day.\n"
    "10. Don't kink shame.\n"
    "11. This place is drama-free.\n"
    "12. Teasing and name-calling is okay, but insults and hate speech are not tolerated.\n"
    "13. Chastity can be mentally challenging. Feel free to vent about frustrations!\n\n"
    "Group Links: \nt.me/ChastityFurs \n@ChastityFurs\n\nMessage @KuhakuNA or @HossRump "
    "if you need help!")

blank_cum_date = datetime.datetime(2021, 5, 24, 12, 0)
lockup_start = datetime.datetime(2021, 1, 10, 12, 0, 0)
now = datetime.datetime.now()
time_since_t = now - lockup_start
time_remaining = blank_cum_date - now

time_remaining_months = "{} months {} days".format(int(time_remaining.days / 30), time_remaining.days % 30)

amount_donated = 45
goal_amount = 100
blank_remaining_lockup_message = ("Blank currently is locked up for {} days :3 He will get to cum on {}/{}/{}!"
                                  " He has now been locked up for {} days, and has {} days to go! Go tease him! >:3"
                                  "\n"
                                  "\n"
                                  "Also, for every $1 USD donated to https://ko-fi.com/blankwoof, Blank will"
                                  "be adding an extra day to his lockup. \n\nCurrently up to 100 days (${}/${}"
                                  " accrued so far! $2/day for every dollar past $100, $3/day past "
                                  "$300)".format(time_since_t.days, blank_cum_date.month, blank_cum_date.day, blank_cum_date.year,
                                                 time_since_t.days,
                                                 time_remaining.days,
                                                 amount_donated, goal_amount))

blank_remaining_time_short_message = ("<code>Blank currently has been locked up for {} days!\n"
                                      "He will now get to cum on {}/{}/{} :3\n"
                                      "\nLast infraction: Cumming like a girl! o: +2 days.\n\n"
                                      "He now has {} remaining! Pooooor boy~</code>".format(time_since_t.days,
                                                                                            blank_cum_date.month,
                                                                                            blank_cum_date.day,
                                                                                            blank_cum_date.year,
                                                                                            time_remaining_months))
