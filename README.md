FlaskMan:
This is my game in Flask.
After finishing the Python beginner course, I started working on the Flask framework,
and uploaded it to my local machine with a few changes from the original py-console game:

1. input changed to HTML post requests, as there is no input
2. there is a built-in words bank, as the site would eventually not require access to user folders on their machine
3. there is no main function, 
I have broken it into smaller function which get checked constantly at the "lettercheck" function
4. at lettercheck, because I wanted everything to be rendered in real time, 
I did not group all of the show_hidden_word+ num_of_tries + insert new letter in another function,
so for every control-flow condition - everything is rendered in real-time and that's why it looks kinda messy

Also, to have this work on the python-anywhere hosting service at deanpysrael.pythonanywhere.com,
I had to remove the random_secret_word func outside the "if name == __main__" condition,
as apparently the pythonanywhere WSGI server is set run without this condition, where as it was crucial for running on my local machine.

Enjoy :)


