from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contato.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['julio@juliobs.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/contato/ok/')
    else:
        form = ContactForm()

    return render(request, 'contato.html', {'form': form})
