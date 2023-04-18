from django.shortcuts import render
from .forms import InquiryForm

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactus/thankyou.html')
    else:
        form = InquiryForm()
    return render(request, 'contactus/contact.html', {'form': form})
