from django.shortcuts import render
from .forms import InquiryForm


def contact(request):
    """
    This function handles a contact form submission and saves
    the data if it is valid, then renders a thank you page
    or the contact page with the form.
    :param request: The request object represents the HTTP request
    that the user made to access the view. It contains information
    about the request, such as the HTTP method used (GET, POST, etc.),
    any data submitted in the request, and the user's session information.
    The view uses this object to determine how to handle
    :return: a rendered HTML template with a form for user input. If the
    request method is POST and the form is valid, the function saves the
    form data and returns a rendered HTML template for a thank you message.
    """
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactus/thankyou.html')
    else:
        form = InquiryForm()
    return render(request, 'contactus/contact.html', {'form': form})
