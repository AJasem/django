from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
            listing_id = request.POST['listing_id']
            listing = request.POST.get('listing', '')
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            user_id = request.POST['user_id']
            realtor_email = request.POST['realtor_email']
            # checkif user has made inquiry already
            if request.user.is_authenticated:
                  user_id = request.user.id
                      
                  has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
                  if has_contacted:
                        messages.error(request,'You have already made an inquiry for this listing')
                        return redirect('/listings/'+ listing_id)
                  

            contact = Contact(
                listing=listing,
                listing_id=listing_id,
                name=name,
                email=email,
                phone=phone,
                message=message,
                user_id=user_id
            )
            contact.save()
            send_mail(
                'Property Listing Inquiry',
                f'There has been an inquiry for {listing}. Sign into the admin panel for more info.',
                'contact@ahmads.dev',
                ['ajassem.ahmad@gmail.com'],
                fail_silently=False,
            )
            send_mail(
                  'Confirmation Notice',
                  f'Thank you {name} for you interest in {listing} property, an agent will get back to you soon!',
                  'contact@ahmads.dev',
                  [email],
                  fail_silently=False
            )



            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon!')
            return redirect('/listings/' + listing_id)

        