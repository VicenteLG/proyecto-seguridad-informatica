def user_data(request):
	user = request.user

	try:
		data = {
		'name': user.username,
		}

	except AttributeError as e:
		data = {}

	return data