from rest_framework.response import Response

def get_tweet(Object,pk):
    """ an utility function to get the current user or return a json response if user does not exist"""
    try:
        instance = Object.objects.get(pk=pk)
    except Object.DoesNotExist:
        return [False, Response({"error":"User does not exist"}, status.HTTP_404_NOT_FOUND)]
    return [True, instance]