from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_user_ratings, cosine_similarity

# List of usernames for testing (obtained from ChatGPT)
TOP_USERS = [
    "TomVasel",
    "ZeeGarcia",
    "rahdo",
    "EndersGame",
    "lukepryor",
    "smperez",
    "qwertymartin"
]

TOP_N_SIMILAR_USERS = 3  # Number of top similar users to return

@api_view(['GET'])
def similarity_view(request):
    """
    Endpoint: /similarity/?user1=<username>&user2=<username>
    Returns the similarity score between two users.
    """
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
    """
    Endpoint: /similar-users/?username=<username>
    Returns the top N most similar users to the given username.
    """
    username = request.GET.get('username')
    if not username:
        return Response({"error": "Missing username"}, status=400)

    # Optionally add the target user to dummy list if missing
    if username not in TOP_USERS:
        TOP_USERS.append(username)

    target_ratings = get_user_ratings(username)
    similarity_list = []

    # Compare with all other dummy users
    for other in TOP_USERS:
        if other == username:
            continue
        other_ratings = get_user_ratings(other)
        score = cosine_similarity(target_ratings, other_ratings)
        similarity_list.append({"username": other, "score": score})

    # Sort descending by similarity and take top N
    similarity_list.sort(key=lambda x: x["score"], reverse=True)
    top_similar_users = similarity_list[:TOP_N_SIMILAR_USERS]

    return Response({"similar_users": top_similar_users})