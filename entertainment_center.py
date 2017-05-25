#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:13:02 2017

@author: vmang
"""
import fresh_tomatoes
import media 

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print (toy_story.storyline)
print (toy_story.title)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY") 
#print (avatar.storyline)
#print (avatar.title)
#avatar.show_trailer()

GoT = media.Movie("Game of Thrones",
                     "t's the depiction of two powerful families -- kings and queens, knights and renegades, liars and honest men -- playing a deadly game for control of the Seven Kingdoms of Westeros, and to sit atop the Iron Throne.",
                     "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",
                     "https://www.youtube.com/watch?v=giYeaKsXnsI&t=28s") 
#GoT.show_trailer()
whiplash = media.Movie("Whiplash",
                           "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                           "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyLORvKKvCi7-vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",
                           "https://www.youtube.com/watch?v=tYkuvB2f5XU")


matrix = media.Movie("Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


man_of_steel = media.Movie("Man of Steel",
                     "Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction",
                     "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                     "https://www.youtube.com/watch?v=T6DJcgm3wNY")

movies = [toy_story, avatar, GoT, whiplash, matrix, man_of_steel]
fresh_tomatoes.open_movies_page(movies)