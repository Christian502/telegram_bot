from telegram import Update
from telegram.constants import ParseMode  # Aggiornato per importare ParseMode dal modulo corretto
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

# Inserisci il tuo nuovo token qui
TOKEN = '7483806465:AAG88AmFpbSHi6_Q6G9ooKblLgLhc2T2lqA'

# Definisci i messaggi da inviare
WELCOME_MESSAGE = """
🚀✨ Benvenuti nel nostro gruppo di crescita follower su Vinted! ✨🚀

👗👠 Siamo entusiasti di averti con noi! Se vuoi aumentare il tuo seguito su Vinted e ampliare la tua rete, sei nel posto giusto! 👠👗

🌟 Perché unirsi a noi?

• Crescita esclusiva di follower: Questo gruppo è dedicato SOLO alla crescita dei follower su Vinted.

• Comunità accogliente: Siamo una nuova community, pronti a crescere insieme passo dopo passo!

• Supporto reciproco: Ogni membro si impegna a seguire e supportare gli altri, creando un ambiente positivo e solidale.

🆕 Nuovo di zecca: Creato da poco e in espansione, il gruppo è l'occasione perfetta per diventare uno dei primi membri e vedere crescere il tuo profilo Vinted rapidamente!

🤝 Cosa puoi aspettarti:

🌈 Ambiente amichevole: Qui troverai persone positive e disponibili a dare una mano.
🚀 Crescita continua: Con il supporto reciproco, vedrai i tuoi follower aumentare in poco tempo.

🔗 Regole del gruppo:
• Segui e supporta gli altri membri.
• Rispetta tutti e mantieni un tono positivo.
• Niente spam o contenuti inappropriati.

💬 Partecipa attivamente: Non esitare a presentarti, condividere il tuo profilo Vinted e iniziare a interagire con gli altri membri!

👥💖 Cresciamo insieme, follower dopo follower! 💖👥

Se hai amici o persone da invitare fai pure 😊
"""

WELCOME_NEW_MEMBER = """
Ciao {mention}! 😊 Per scoprire tutte le informazioni sul nostro gruppo e conoscere le regole, clicca sul link qui sotto! 🔗📋 Se hai altre domande, siamo qui per aiutarti! 🌟👋

https://t.me/VintedBot2_bot
"""

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Ciao! Scrivi "info" per maggiori dettagli.')

async def info(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(WELCOME_MESSAGE)

async def new_member(update: Update, context: CallbackContext) -> None:
    print("Nuovo membro rilevato:", update.message.new_chat_members)
    for member in update.message.new_chat_members:
        if member.id != context.bot.id:  # Non menzionare il bot stesso
            mention = f'<a href="tg://user?id={member.id}">{member.first_name}</a>'
            welcome_message = WELCOME_NEW_MEMBER.format(mention=mention)
            await update.message.reply_text(welcome_message, parse_mode=ParseMode.HTML)

def main() -> None:
    # Crea l'Application e passa il token del bot
    application = Application.builder().token(TOKEN).build()

    # Aggiungi i gestori dei comandi
    application.add_handler(CommandHandler('start', start))

    # Aggiungi il gestore dei messaggi
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^info$'), info))

    # Aggiungi il gestore per i nuovi membri
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()
