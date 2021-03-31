from django.shortcuts import render , HttpResponseRedirect
from .models import Contact, Web_Mobile_Budget, Website_Budget, Mobile_Budget, Photography
from django.contrib import messages
from django.template.loader import  get_template
from django.core.mail import EmailMessage
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
import json
import requests


def index(request):
    return render(request, 'tech/index.html')

def about(request):

    return render(request, 'tech/about.html')

def faq(request):
    return render(request, 'tech/faqs.html')

def web_development(request):
    return render(request, 'tech/web_developement.html')

def digital_marketing(request):
    return render(request, 'tech/digital_marketing.html')

def app_development(request):
    return render(request, 'tech/app_developement.html')

def graphics(request):
    return render(request, 'tech/graphics.html')

def portfolio(request):
    return render(request, 'tech/portfolio.html')

def photography(request):
    photos = Photography.objects.filter(show=True)
    data = {"photos": photos}
    return render(request, 'tech/photography.html', data)

def gallery(request,**kwargs):
    category = kwargs.get('category')

    all_photos = Photography.objects.all()

    paginator = Paginator(all_photos, 10)
    page = request.GET.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(photos, index=1)

    page_range = list(paginator.page_range)[start_index:end_index]


    data = {"photos": photos, 'page_range': page_range, 'category':category}
    return render(request, 'tech/temp.html', data)

def contact(request):
    if request.method == 'POST':
        url = request.META["HTTP_REFERER"]
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # recaptcha stuff
        client_key = request.POST['g-recaptcha-response']
        secret_key = '6LfGhZYaAAAAAJZO7sDSHp9uyWhnGgSvcbEy8mDr'

        captchaData = {
                    'secret' : secret_key,
                    'response':client_key
                }
        req = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(req.text)
        verify = response['success']
        if verify:
            contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
            resp = sendmail(email, name)
            if resp == True:
                contact.save()
                error_msg = "Your message has been send.."
                messages.success(request, error_msg)
            else:
                error_msg = "Oops.. Something went wrong.."
                messages.error(request, error_msg)
            return HttpResponseRedirect(url)
    return render(request, 'tech/contact.html')

def budget(request):
    if request.method == "POST":
        url = request.META["HTTP_REFERER"]
        data = request.POST
        responsive = data.get('website-cost-responsive')
        template = data.get('website-cost-Template')
        type = data.get('website-cost-type')
        design = data.get('website-cost-design')
        pages = data.get('website-cost-pages')
        technologies = data.get('website-cost-Technologies')
        name = data.get('name')
        contact = data.get('full')
        email = data.get('email')
        message  = data.get( 'message')
        web = Website_Budget(
            responsive=responsive,
            template = template,
            type = type,
            design = design,
            pages = pages,
            technologies = technologies,
            name = name,
            contact = contact,
            email = email,
            message = message
                    )
        web.save()
        resp = sendmail(email, name)
        if resp == True:
            error_msg = "Your message has been send.."
            messages.success(request, error_msg)
        else:
            error_msg = "Oops.. Something went wrong.."
            messages.error(request, error_msg)


        return HttpResponseRedirect(url)
    return render(request, 'tech/budget.html')


def budget_app(request):
    if request.method == "POST":
        url = request.META["HTTP_REFERER"]
        data = request.POST
        responsive = data.get('application-cost-responsive')
        template = data.get('application-cost-Template')
        type = data.get('application-cost-type')
        design = data.get('application-cost-design')
        pages = data.get('application-cost-pages')
        database = data.get('application-cost-database')
        api = data.get('application-cost-api')
        name = data.get('name')
        contact = data.get('appfull')
        email = data.get('email')
        message = data.get('message')

        app = Mobile_Budget(
            responsive=responsive,
            template=template,
            type=type,
            design=design,
            pages=pages,
            database =database,
            api =api,
            name=name,
            contact=contact,
            email=email,
            message=message
        )
        app.save()
        resp = sendmail(email, name)
        if resp == True:
            error_msg = "Your message has been send.."
            messages.success(request, error_msg)
        else:
            error_msg = "Oops.. Something went wrong.."
            messages.error(request, error_msg)

        return HttpResponseRedirect(url)
    return render(request, 'tech/budget.html')



def budget_web_and_app(request):
    if request.method == "POST":
        url = request.META["HTTP_REFERER"]
        data = request.POST
        responsive = data.get('web-app-cost-responsive')
        template = data.get('web-app-cost-Template')
        technologies = data.get('web-app-cost-Technologies')
        type = data.get('web-app-cost-type')
        design = data.get('web-app-cost-design')
        pages = data.get('web-app-cost-pages')
        app_type = data.get('web-apps-cost-type')
        name = data.get('name')
        contact = data.get('webappfull')
        email = data.get('email')
        message = data.get('message')

        web = Web_Mobile_Budget(
            responsive=responsive,
            template=template,
            technologies=technologies,
            type=type,
            design=design,
            pages=pages,
            apptype=app_type,
            name=name,
            contact=contact,
            email=email,
            message=message
        )
        web.save()
        resp = sendmail(email, name)
        if resp == True:
            error_msg = "Your message has been send.."
            messages.success(request, error_msg)
        else:
            error_msg = "Oops.. Something went wrong.."
            messages.error(request, error_msg)

        return HttpResponseRedirect(url)
    return render(request, 'tech/budget.html')

def budget_dm(request):
    if request.method == 'POST':
        url = request.META["HTTP_REFERER"]
        data = request.POST
        print(data)
    return render(request, 'tech/budget.html')



def error_404(request, exception):

   return render(request,'tech/404.html')

def error_500(request):

   return render(request,'tech/404.html')


def sendmail(email, name):
    ctx = {
        'user': name,
        }
    try :
        message = get_template('tech/mail.html').render(ctx)
        msg = EmailMessage(
            'Subject',
            message,
            to=[email]
            )
        msg.content_subtype = "html"
        msg.send()
        return True
    except:
        return False




def proper_pagination(prods, index):
    start_index = 0
    end_index = 7
    if prods.number > index:
        start_index = prods.number - index
        end_index = start_index + end_index
    return (start_index,end_index)





