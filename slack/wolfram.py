import wolframalpha
from mtranslate.core import translate
import pprint

dicti1 = {'მოდული': 'absolute value of', 'უკვეცი': 'irreducible', 'ლოგარითმი': 'log',
 		'ინტეგრალი': 'integrate', 'სადაც': 'where', 'მნიშვნელობა': 'value', 'ნამდვილიდან ნამდვილ ცვლადშია': 'from real to real',
		'მეორე რიგის წარმოებული': 'second derivative', 'წარმოებული': 'derivative', 'მაქსიმალური მნიშვნელობა': 'maximum value',
 		'პი': 'pi', 'ციფრი': 'digit', 'ამოხსენი': 'solve', 'განსაზღვრული': 'definite', 'კონსტანტა': 'constant', 'განუსაზღვრელი': 'indefinite', 
		'დიფერენციალი': 'differential', 'ზღვარი': 'limit', 'უსასრულობა': '∞', 'გამოთვალე': 'calculate', 'მინიმალური მნიშვნელობა': 'minimum value'}



app_id = '8LJR68-JKELEXKH5X'
client = wolframalpha.Client(app_id)




def get_answer(question):
    trans = translate(question,'en','auto')
    res = client.query(trans)
    pprint.pprint(res)

    return [
       subprod['subpod']['plaintext'] for subprod in res["pod"][:3]
    ]

    # answer = res.results
    # return "/n".join([ for answer1 in answer])
