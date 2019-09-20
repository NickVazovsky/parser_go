from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from ecoapp.models import Results
from ecoapp.forms import PostForm
from ecoapp.task import crawl, transfer_url, Urls
import datetime
import csv
import xlwt


# sudo fuser -k 8000/tcp

def list_view(request):
    title = Results.objects.values_list('url', 'title')
    keywords = Results.objects.values_list('url', 'keywords')
    description = Results.objects.values_list('url', 'description')
    h1 = Results.objects.values_list('url', 'h1')
    h2 = Results.objects.values_list('url', 'h2')
    link = Results.objects.values_list('url')
    google_adwords = Results.objects.values_list('url', 'google')
    yandex_metricks = Results.objects.values_list('url', 'yandex')
    return render(request, 'indes.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })


def contacts_view(request):
    return render(request, 'contact.html', {

    })


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['title', 'title_error', 'keywords', 'description', 'description_error', 'h1', 'h2',
                     'url', 'yandex_metricks', 'google_analytics', 'date'])
    users = Results.objects.filter(base_url=Urls.base_url).values_list('title_unique', 'title', 'keywords',
                                                                       'description_unique', 'description',
                                                                       'h1', 'h2', 'url', 'yandex', 'google',
                                                                       'date_add')
    for user in users:
        writer.writerow(user)
    return response


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('result of parsing')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['title', 'title_error', 'keywords', 'description', 'description_error', 'h1', 'h2',
               'url', 'yandex_metricks', 'google_analytics']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Results.objects.filter(base_url=Urls.base_url).values_list('title_unique', 'title', 'keywords',
                                                                      'description_unique', 'description',
                                                                      'h1', 'h2', 'url', 'yandex', 'google')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def about_view(request):
    return render(request, 'about.html', {

    })


def result_ruk(request):
    return render(request, 'result_ruk.html', {

    })


def result_ruk_seo(request):
    title = Results.objects.values_list('url', 'title')
    keywords = Results.objects.values_list('url', 'keywords')
    description = Results.objects.values_list('url', 'description')
    h1 = Results.objects.values_list('url', 'h1')
    h2 = Results.objects.values_list('url', 'h2')
    link = Results.objects.values_list('url')
    broken_links = Results.objects.values_list('url', 'broken_link')
    google_adwords = Results.objects.values_list('url', 'google')
    yandex_metricks = Results.objects.values_list('url', 'yandex')
    return render(request, 'result.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'broken_links': broken_links,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })


def result_ruk_index(request):
    return render(request, 'result_ruk_index.html', {

    })


def exportdate(request):
    return render(request, 'exportdate.html', {

    })


def start_proccess(request):
    pass

    # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "whereyourscrapysettingsare")


def result_view(request):
    title = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'title')
    keywords = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'keywords')
    description = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'description')
    h1 = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'h1')
    h2 = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'h2')
    link = Results.objects.filter(base_url=Urls.base_url).values_list('url')
    broken_links = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'broken_link')
    google_adwords = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'google')
    yandex_metricks = Results.objects.filter(base_url=Urls.base_url).values_list('url', 'yandex')
    return render(request, 'result_ruk.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'broken_links': broken_links,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })


def send_form(request):
    if request.method == 'POST':
        # date_adds = datetime.datetime.today()
        # Results.objects.exclude(date_add=date_adds).delete()

        url = request.POST['url']

        short_url = str(url).replace("http://", "").replace("https://", "").replace("/", "")
        Results.objects.filter(base_url=short_url).delete()
        # get_screen(url)
        crawl.delay(url, short_url)


        transfer_url(url, short_url)

        return HttpResponseRedirect('/result/')

    else:
        form = PostForm()
        return render(request, 'form.html', {
            'form': form
        })
