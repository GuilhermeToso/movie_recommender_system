# Movie Recommender System
-------------------------------------------------

This is a Data Science Project of a movie/series recommender system. The system is build on a data science web application called Dash using a model that extracted text features from the [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/shivamb/netflix-shows) and applied the cosine similarity on them. After entering the movie or tv show name, which must be a register from the dataset mentioned earlier, the system returns the ten films and TV shows with the highest score (cosine similarity).


# Project Tree
---------------------

<pre>
<code>
    movie_recommender_system 
    |
    |---- data
    |---- notebooks
    |---- app.mp4
    |---- app.py
    
</code>
</pre>

The **data** directory contain all the data files used and generated in the project development process, including the original [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/shivamb/netflix-shows) and the cleaned one, to generate the file that contain the cosine similarity, I advise to run the *save_data.py*. Despite this file stores the cosine similarity of the counter vectorizer method of all the information (director, cast country, genre, rating, description, etc) of the movies/Tv shows, several models have been developed that contain the consine similarities using different extraction methods (Count Vectorizer or TF-IDF Transformer) of three different texts (movie/tv show description, movie/tv show director, cast, country, rating and genre, movie/tv show all information), and these tests were performed on the file in the following directory.
The **notebooks** directory contain the *data_analysis.ipynb* file, which describes all the projects' steps, since an introduction, the goal to be achieved, data analysis and models tests. Next, the *app.mp4* file is used in this file to demonstrate the launch and usage of the movie recommender system. Finally, **app.py** file is our Dash application.
