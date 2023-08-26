from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import openai
from chatbot.models import Review 
from django.views.generic.base import TemplateView
import os
from dotenv import load_dotenv

# Create your views here.

openai.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

prompt_context = "create a reply for the following google review for a pub in London called 'The George Inn', ensure the reply is professional but informal enough to make it indistinguishable from a human response, if a review is negative - ask the customer to contact via email at 7781@greeneking.co.uk. Also finish each reply with a signature of the pub managers full name which is Jason Giardelli" 

def chatbot_response(user_input):
    stop_sequences = ["Giardelli"]
    prompt=f"{prompt_context} {user_input}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=2,
        stop=stop_sequences,
    )
    #return response["choices"][0]["text"]
    text = response["choices"][0]["text"]
    text_with_linebreaks = text.replace(".", ".\n\n") #delete this line if need be
    return text_with_linebreaks


class ChatbotView(TemplateView):
    template_name = 'chatbotpre.html'
    def post(self, request):
        #user_input = request.POST["user_input"]
        user_input = request.POST.get("user_input", "")
        #response = chatbot_response(user_input)
        response = ""
        if user_input:
            #Review.objects.all().delete()
            response = chatbot_response(user_input)
            review = Review.objects.create(text=user_input)
        return render(request,'chatbotpre.html',{'response':response})
        pass

    def get(self, request):
        user_input = request.GET.get("user_input", "")
        #response = chatbot_response(user_input)
        response = ""
        if user_input:
            #Review.objects.all().delete()
            response = chatbot_response(user_input)
            review = Review.objects.create(text=user_input)
        return render(request,'chatbotpre.html',{'response':response})
        pass

def summary_report(request):
    #Review.objects.all().delete()
    reviews = Review.objects.all()

    review_text = " ".join({review.text for review in reviews})

    report_prompt = "create a report of a few paragraphs summarising the following google review data for a pub, the report will be for the pub manager to give insights about what customers are saying about the venue and for the manager to know areas of success/praise and areas for improvement.:" + review_text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=report_prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    summary = response["choices"][0]["text"]

    return render(request, 'summary_report.html', {'summary': summary})

