#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '5295632717:AAGyXD4XTk4_7ifu331ncp5KSrk6Fj_hAI8'

def start(update, context):
    update.message.reply_text("""
Bienvenue sur le bot officiel de NOM BOT.

Les commandes disponibles sont :
- site
- dns
- requetes
    """)


def site(update, context):
    update.message.reply_text('Voici la dernière adresse de TireXo : https://www2.tirexo.art/')


def dns(update, context):
    update.message.reply_text('Problèmes de DNS ? \n Il y a une solution à ton problème juste ici :\n\n*Windows :*\nhttps://telegra.ph/TirexDNS-02-02\n\n*Linux :*\nhttps://telegra.ph/TirexDNS-Linux-02-02\n\n*MacOS :*\nhttps://telegra.ph/TirexDNS-MacOS-02-02\n')


def pas_compris(update, context):
    update.message.reply_text('Je n\'ai pas compris votre message', update.message.text)

def requetes(update, context):
    update.message.reply_text('Si tu veux faire une requête c\'est ici : https://www2.tirexo.art/?do=req_listes')

def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(TOKEN, use_context=True)

    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("start","help", start))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("dns", dns))
    dp.add_handler(CommandHandler(('requetes', 'req',), requetes))
    
    # Pour gérer les autres messages qui ne sont pas des commandes
    dp.add_handler(MessageHandler(Filters.text, pas_compris))

    # Sert à lancer le bot
    updater.start_polling()

    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()

def new_func():
    return ''

