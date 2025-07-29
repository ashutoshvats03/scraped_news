# views.py

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import News, Author, Published
from datetime import datetime
 # import at top level

# News.objects.all().delete()
# Author.objects.all().delete()
# Published.objects.all().delete()
# print("all deleted")
def index(request):
    from sel.ai_api import news 
    for key, value in news.items():
        author_instance, _ = Author.objects.get_or_create(name=value['author'])

        published_list = value['published']
        if published_list and isinstance(published_list[0], str):
            published_date = datetime.strptime(published_list[0], '%b %d, %Y').date()
        else:
            published_date = datetime.today().date()

        published_instance, _ = Published.objects.get_or_create(date=published_date)
        

        news_, created = News.objects.get_or_create(
            news_id=value['news_id'],
            defaults={
                'title': value['title'],
                'content': value['content'],
                'summary': value['summary'],
                'link': value['link']
            }
        )

        if created:
            news_.authors.add(author_instance)
            news_.published_dates.add(published_instance)
            print("news added")
        else:
            print("news already exists")

    return JsonResponse({"message": "No duplication."})


class NewsAPIView(APIView):
    def get(self, request):
        try:
            dic = []
            if News.objects.exists():
                for news in News.objects.all():
                # if news.news_id not in News.objects.values_list('news_id', flat=True):
                        author = news.authors.first()
                        published = news.published_dates.first()
                        dic.append({
                            "news_id": news.news_id,
                            "title": news.title,
                            "author": author.name if author else "N/A",
                            "published": published.date if published else "N/A",
                            "content": news.content,
                            "summary": news.summary,
                            "link": news.link
                        })
            return Response({"news_list": dic}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

