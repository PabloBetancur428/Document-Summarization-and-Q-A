#To see upload, summarization and Q&A
# Create your views here.

from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
from .utils import extract_text, generate_summary, answer_question


def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            #Extract text
            text = extract_text(document.file.path)
            #Generate a summary
            summary = generate_summary(text)
            return render(request, "results.html", {"summary": summary, "text": text})
    else:
        form = DocumentForm()

    return render(request, "upload.html", {"form": form})

def ask_question(request):
    if request.method == "POST":
        #Retrieve questions and context
        question = request.POST.get("question")
        context = request.POST.get("context")
        answer = answer_question(context, question) 
        return render(request, "qa_results.html", {"answer": answer})

    return render(request, "ask.html") 
    

