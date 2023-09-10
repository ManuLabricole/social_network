from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm

# A view that returns user data in JSON format


@api_view(['GET'])
def me(request):
    """
    Returns user data in JSON format.

    Args:
        request: The HTTP request object.

    Returns:
        JsonResponse: JSON response containing user information.
    """
    return JsonResponse({
        'id': request.user.id,     # Get the user's unique identifier.
        'name': request.user.name,  # Get the user's name.
        'email': request.user.email,  # Get the user's email address.
    })

# A view for user registration (sign-up)


@api_view(['POST'])
@authentication_classes([])  # Allow unauthenticated requests.
@permission_classes([])      # Allow unauthenticated requests.
def signup(request):
    """
    Handles user registration (sign-up) via a POST request.

    Args:
        request: The HTTP request object.

    Returns:
        JsonResponse: JSON response indicating success or error.
    """
    data = request.data  # Extract data from the HTTP request.
    print(data)
    # Create a form instance with the provided data for validation.
    form = SignupForm({
        # Get the email address from the data.
        'email': data.get('email'),
        'name': data.get('name'),         # Get the user's name from the data.
        # Get the first password from the data.
        'password1': data.get('password1'),
        # Get the second password from the data.
        'password2': data.get('password2'),
    })

    if form.is_valid():
        # If the form is valid, save the user registration data.
        form.save()  # Save the user to the database. This should commit the change
        message = 'success'

        # Additional logic to send a verification email can be added here.

    else:
        # If the form is not valid, there was an error during registration.
        message = 'error'
        

    # Return a JSON response indicating success or error.
    return JsonResponse({'message': message, 'errors': form.errors})
