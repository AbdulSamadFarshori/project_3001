from deepmultilingualpunctuation import PunctuationModel
model = PunctuationModel()
text = "I have really bad anxiety when travelling i get lots of palpitations feel nauseous pins and needles sweating i have no idea why this happens i have had anxiety for a long time i no problems holding down a pressurised job social gathering are not a problem but If i have to travel that's my problem even if its only short distances i have to go a function its only about half hour to get there and im dreading it i do take cipramil and tried beater blockers any one have any advice"
result = model.restore_punctuation(text)
print(result)