from imdb import IMDb

# creating an instance of the imdb library
ia = IMDb()

def get_movies_info_from_file(fileName = "C:/Users/GATEWAY/Desktop/MovieLibrary/mvs.txt"):
    # returns the info related to the movies as [title, year, quality] from the txt file given as argument
    f = open(fileName, 'r')
    text = f.readlines()
    f.close()

    lines = list()
    
    result = list()

    for line in text:
        lines.append(line.rstrip())
        words = line.split()
        title = ""
        quality = ""
        year = ""
        
        if '720' in words[-1]:
            quality = '720p'
            words.remove(words[-1])

        if '1080' in words[-1]:
            quality = '1080p'
            words.remove(words[-1])

        if words[-1][0] == '(' and words[-1][-1] == ')':
            year = str(words[-1][1:-1])
            words.remove(words[-1])

        for i in words:
            title = title + i + ' '
        title = title.strip()
        result.append([title, year, quality])

    return result
    

# a list containing all the movies from the txt file 
#movies = get_movies_info_from_file()

# for i in movies:
#     print(i)


def get_final_movie_info_list(movie_list):
    # the file that has the IMDb ids for the movies
    f = open("C:/Users/GATEWAY/Desktop/MovieLibrary/ids.txt", 'r')
    text = f.readlines()
    f.close()

    # getting a list like [movie imdb id, movie title, year]
    lines = list()
    info_list = list()
    
    for line in text:
        
        # print("line: ",line)
        temp = line.strip('\t').split()
        # print("temp : " ,temp)
        id = temp.pop(0)
        
        # print("id : ", id)
        year = temp.pop(-1)
        year = year[1:-1]
        movie_title = ""
        for i in range(len(temp)):
            movie_title += temp[i] + " "
        movie_title = movie_title.strip()
        info_list.append([id, movie_title, year])
        
    # for i in info_list:
    #     print(i)

    # creating a list with movie info as [id, title, year, quality, rating, director]
    final_movie_list = list()
    for movie in movie_list:
        movie_info = list()
        for info in info_list:
            if movie[0] == info[1]:
                
                movie_info.append(info[0])#id
                movie_info.append(movie[0])#title
                movie_info.append(movie[1])#year
                movie_info.append(movie[2])#quality

                mov = ia.get_movie(info[0])
                rating = mov['rating']
                movie_info.append(rating)#rating
                directors = mov.get('director')# this returns a list
                director_names = [director['name'] for director in directors[:1]]
                movie_info.append(director_names[0])#director

                final_movie_list.append(movie_info)

                #print(movie_info)
    return final_movie_list


#final = get_final_movie_info_list(get_movies_info_from_file())
# for i in final:
#     print(i)
