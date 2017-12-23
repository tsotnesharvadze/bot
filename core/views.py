# from django.shortcuts import render

import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import wolframalpha
from mtranslate.core import translate

from django.db.models import Q

from .models import QuestionMix,Question
#  ------------------------ Fill this with your page access token! -------------------------------

dicti1 = {'მოდული': 'absolute value of', 'უკვეცი': 'irreducible', 'ლოგარითმი': 'log',
 		'ინტეგრალი': 'integrate', 'სადაც': 'where', 'მნიშვნელობა': 'value', 'ნამდვილიდან ნამდვილ ცვლადშია': 'from real to real',
		'მეორე რიგის წარმოებული': 'second derivative', 'წარმოებული': 'derivative', 'მაქსიმალური მნიშვნელობა': 'maximum value',
 		'პი': 'pi', 'ციფრი': 'digit', 'ამოხსენი': 'solve', 'განსაზღვრული': 'definite', 'კონსტანტა': 'constant', 'განუსაზღვრელი': 'indefinite', 
		'დიფერენციალი': 'differential', 'ზღვარი': 'limit', 'უსასრულობა': '∞', 'გამოთვალე': 'calculate', 'მინიმალური მნიშვნელობა': 'minimum value'}


# Create your views here.
class Index(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


def post(self, requests, *args, **kwargs):
    app_id = '8LJR68-JKELEXKH5X'

    trans = translate(quest,'en','auto')


    client = wolframalpha.Client(app_id)
    res = client.query(trans)
    answer = res.results # ლისტია
    pasuxi = translate(answer1,'ka','auto')
    