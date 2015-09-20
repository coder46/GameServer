from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from games.models import Game
from games.serializers import GameSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
@csrf_exempt
def games_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def game_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GameSerializer(game, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=204)

@csrf_exempt
def game_search(request, pk):
   games = Game.objects.all()
   if request.method == 'GET':
      query = pk
      res = []
      queries = query.split('_')
      for i in range(len(games)):
	 game = GameSerializer(games[i]).data

	 cats = map(lambda x: x.lower(), game['gameCats'].split(','))
	 title = map(lambda x: x.lower(), game['title'].split())
	 for q in queries:
	    if q.lower() in cats or q.lower() in title:
	       res.append(game)
      serializer = GameSerializer(res, many=True)
      return JSONResponse(serializer.data)

@csrf_exempt
def topgames(request):
   games = Game.objects.all()
   if request.method == 'GET':
      games = games[:10]
      serializer = GameSerializer(games, many=True)
      return JSONResponse(serializer.data)


@csrf_exempt
def newgames(request):
   games = Game.objects.all()
   if request.method == 'GET':
      games = games[10:20]
      serializer = GameSerializer(games, many=True)
      return JSONResponse(serializer.data)

@csrf_exempt
def banners(request):
   if request.method == 'GET':
      bans = [{'imgPath':'http://www.geekaygames.com/a/home/images/fifa-16-po.jpg'},{'imgPath':'http://www.geekaygames.com/a/home/images/fifa-16-ps4-bundle-po.jpg'},{'imgPath':'http://www.geekaygames.com/a/home/images/fifa-16-xbox-one-bundle-po.jpg'}, {'imgPath':'http://www.geekaygames.com/a/home/images/201509-xbox-live-card.jpg?'}, {'imgPath':'http://www.geekaygames.com/a/home/images/xbox-one-1tb-forza-6-nr.jpg'},{'imgPath':'http://www.geekaygames.com/a/home/images/pes-16-nr.jpg'}]
      return JSONResponse(bans)



