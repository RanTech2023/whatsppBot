from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# bot = ChatBot(
#     'Sakura',
#     storage_adapter='chatterbot.storage.MongoDatabaseAdapter'
# )
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.chinese")
# trainer.train("chatterbot.corpus.english")
def bot():
    bot = ChatBot("Zadis",logic_adapters=[{                       
                        'import_path': 'chatterbot.logic.BestMatch',
                        "statement_comparision_function": "chatterbot.comparisions.levenshtein_distance",
                        "response_selection_method": "chatterbot.response_selection.get_first_response"
                        }])
    # bot.set_trainer(ListTrainer)
    trainer=ChatterBotCorpusTrainer(bot)
    # bot.set_trainer(ChatterBotCorpusTrainer)
    trainer.train("chatterbot.corpus.chinese")
    return bot
