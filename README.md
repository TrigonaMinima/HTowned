HTowned
=======

A small python script which generates the kml file having the coordinates of the hometowns of my FB friends. This kml file is then fed to the [indiemapper](indiemapper.com/app/) to plot all the points on the world map.

Tools used-  
1. [facebook graph API][1] (using facepy)  
2. [google geocoding service][2] (using geopy)  
3. [indiemapper][4]

###Requirements-  
Install requirements by running,
```
pip install facepy
pip install simplekml
pip install geopy
```

**What is it doing?**  
It is using *facepy* which uses **facebook graph API** to fetch the results from Facebook. It has to be given an *access_token* (your access token, not mine) which will authenticate the script to fetch results on your behalf.  

After fetching the hometowns of each friend it uses the **google geocoding service** via *geopy* to convert the hometowns into lattitudes and longitudes.  

These lats and longs are then written in a *friends_hometown.kml* file using the *simplekml* module. The [kml][3] (keyhole markup language) is an XML notation for expressing geographic annotation and visualization within Internet-based, two-dimensional maps and three-dimensional Earth browsers (It's the wiki definition BTW). ;)

Now, that we have our data in the required format we can plot it however we want. I just wanted to plot them on the World map, so I used [Indiemapper][4], which is a good mapping platform if you have the data.



[1]: https://developers.facebook.com/docs/graph-api/    
[2]: https://developers.google.com/maps/documentation/javascript/geocoding?hl=en
[3]: https://en.wikipedia.org/wiki/Keyhole_Markup_Language
[4]: http://indiemapper.com/