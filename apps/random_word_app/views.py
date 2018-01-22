# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect



# Create your views here.
def random_word(n):
    return ".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))"

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    return render(request, 'random_word_app/index.html')

def generate(request):
    request.session['tries'] += 1
    request.session['word'] = random_word(14)
    return redirect('/random_word')
    print "We are in generate"

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/random_word')