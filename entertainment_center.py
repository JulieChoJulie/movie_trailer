# import media to create instances and
# import fresh_tomatoes to takes in one list argument
# and it generates a html file called julie_fave_movies.html.
import media
import fresh_tomatoes

# Make new instances using media with the inputs:
# movie title, movie info, movie poster, and youtube link
thor_ragnarok = media.Movie(
    "Thor: Ragnarok",
    "<p>2017</p> <p>Fantasy/Science fiction<p> <p>2h 10m</p><p>7.9/10IMDb</p>",
    "http://www.movienewsletters.net/photos/256906R1.jpg",
    "https://www.youtube.com/watch?v=ue80QwXMRHg")
the_truman_show = media.Movie(
    "The Truman Show",
    "<p>1998</p> <p>Drama/Fantasy<p> <p>1h 47m</p><p>8.1/10IMDb</p>",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcTVCzcUF3QGonOAbPip75ZOdD"
    "G66wC912hkYANih_BjnOZee4F9",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=1s")
the_avengers = media.Movie(
    "The Avengers",
    "<p>2012</p> <p>Fantasy/Science fiction<p> <p>2h 23m</p><p>8.1/10IMDb</p>",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")
la_la_land = media.Movie(
    "La La Land",
    "<p>2016</p> <p>Drama/Romance<p> <p>2h 8m</p><p>8.1/10IMDb</p>",
    "http://www.movienewsletters.net/photos/209869R1.jpg",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")
the_butterfly_effect = media.Movie(
    "The Butterfly Effect",
    "<p>2004</p> <p>Thriller/Science Fiction<p> <p>1h 53m</p>"
    "<p>7.7/10IMDb</p>",
    "http://www.gstatic.com/tv/thumb/movieposters/31722/p31722_p_v8_ab.jpg",
    "https://www.youtube.com/watch?v=B8_dgqfPXFg")
the_notebook = media.Movie(
    "The Notebook",
    "<p>2004</p> <p>Drama/Romance<p> <p>2h 4m</p><p>7.9/10IMDb</p>",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQc8OYsNpuM1rOKxYzwtbA1"
    "cXJIOOETfFDIbU8ONel_sHaIEEf_",
    "https://www.youtube.com/watch?v=FC6biTjEyZw")
catch_me_if_you_can = media.Movie(
    "Catch Me If You Can",
    "<p>2002</p> <p>Drama/Crime<p> <p>2h 21m</p><p>8.1/10IMDb</p>",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Catch_Me_If_"
    "You_Can_2002_movie.jpg/220px-Catch_Me_If_You_Can_2002_movie.jpg",
    "https://www.youtube.com/watch?v=hFj3OXVL_wQ")
the_dark_knight = media.Movie(
    "The Dark Knight",
    "<p>2008</p> <p>Drama/Thriller<p> <p>2h 32m</p><p>9.0/10IMDb</p>",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSY2Tsn17pqz9OMpWv5Y_v5n"
    "i2yN-ymmdwS_"
    "mRaOUeYJDG0eU7A",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")
harry_potter_and_the_sorcerer_stone = media.Movie(
    "Harry Potter and the Sorcerer's Stone",
    "<p>2001</p> <p>Fantasy/Fiction<p> <p>2h 39m</p><p>7.6/10IMDb</p>",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcT_9nrOnN8sYfZZH"
    "J06EIBSoEO"
    "5qjx7uHHEs6VtKNplGVuGhZuC",
    "https://www.youtube.com/watch?v=PbdM1db3JbY")
the_matrix = media.Movie(
    "The Matrix",
    "<p>1999</p> <p>Fantasy/Science fiction<p> "
    "<p>2h 30m</p><p>8.7/10IMDb</p>",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-"
    "EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
    "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
inception = media.Movie(
    "Inception",
    "<p>2010</p> <p>Science fiction/Thriller<p> "
    "<p>2h 28m</p><p>8.8/10IMDb</p>",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBV"
    "CtlJnAnew9Ai26kEdrli0-tfmatmciD",
    "https://www.youtube.com/watch?v=d3A3-zSOBT4")
saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    "<p>1998</p> <p>Drama/Action<p> <p>2h 50m</p><p>8.6/10IMDb</p>",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcR0lDhR_dXAKTm9wysp3nWu"
    "6kP0V5skJBVbCNC_Q8ur"
    "AWcr4iF_",
    "https://www.youtube.com/watch?v=zwhP5b4tD6g")

# put all instances of movie class in the array
movies = [thor_ragnarok, the_truman_show, the_avengers,
          la_la_land, the_butterfly_effect, the_notebook,
          catch_me_if_you_can, the_dark_knight,
          harry_potter_and_the_sorcerer_stone, the_matrix,
          inception, saving_private_ryan]

# takes in one list argument above and it generates a html file
fresh_tomatoes.open_movies_page(movies)
