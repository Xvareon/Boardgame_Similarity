from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_user_ratings, cosine_similarity

SAMPLE_USERS = ['user1', 'user2', 'user3']  # Dummy sample users for /similar-users/

@api_view(['GET'])
def similarity_view(request):
    user1 = request.GET.get('user1')
    user2 = request.GET.get('user2')
    if not user1 or not user2:
        return Response({"error": "Missing username"}, status=400)

    ratings1 = get_user_ratings(user1)
    ratings2 = get_user_ratings(user2)
    score = cosine_similarity(ratings1, ratings2)
    return Response({"similarity_score": score})

@api_view(['GET'])
def similar_users_view(request):
    username = request.GET.get('username')
    if not username:
        return Response({"error": "Missing username"}, status=400)
    
    target_ratings = get_user_ratings(username)
    similarity_list = []
    for other in SAMPLE_USERS:
        if other == username:
            continue
        other_ratings = get_user_ratings(other)
        score = cosine_similarity(target_ratings, other_ratings)
        similarity_list.append({"username": other, "score": score})
    
    similarity_list.sort(key=lambda x: x["score"], reverse=True)
    return Response({"similar_users": similarity_list})
