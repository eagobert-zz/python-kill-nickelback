#  Define a set that contains tuples. Each tuple should contain two strings:

    #The name of an artist
    #A song by that artist
    #Make sure that some of the songs are from the band Nickelback.

song_list_a = {
    ('Beyonce', 'Single Ladies'),
    ('Beyonce', 'Ego'),
    ('Beyonce', 'Halo'),
    ('Nickelback', 'How You Remind Me'),
    ('Nickelback', 'That Power'),
    ('Nickelback', 'Animals')
}

#Note: List comprehensions offer a succinct way to create lists based on existing lists. Instead of lists, sets can also be used. With sets, lookup is faster and sets have the property that all its elements are unique

#  Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

song_list_b = {song for song in song_list_a if song[0] != 'Nickelback'}

print(song_list_b)