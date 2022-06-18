from django.http import JsonResponse


def response(data: dict, message: str = '', success: bool = True, status: int = 200):
    return JsonResponse({
        'data': data,
        'success': success,
        'message': message,
    }, status=status)