# APIs and IPAs

Our objective for this project was to explore the intricacies behind the entire ETL process. We were both intrigued by craft beers and beer styles, so we wanted to build a tool that gave you a full picture of each beer style, the most common descriptive words that each beer categorized under the style and a range of ABV (alcohol content) and IBU (quantifying bitterness).

To accomplish this, we used the following tools:


- BreweryDB RESTful API: API with access to extensive database of breweries and beers in the United States
- SQlite: Database
- SQLAlchemy: ORM
- Flask: Web Framework for displaying our results
- Plotly/Dash: Interactive visualizations

## ETL:

As mentioned, BreweryDB had quite an extensive list of data points available. For each beer, we accessed the name, beercode, display name, description, abv, ibu and food pairings. For each beer style, we accessed the style name, style shortname, category, description, ibuMin, ibuMax, abvMin and abvMax. For each ingredient, we accessed the name, ingredient code (“ingredient_id” in the API), category and category display name.
We retrieved this data for 4,800 beers, 175 styles of beer and 400 ingredients.



## SQL Database:

We used SQLalchemy to create and query a SQLite database, consisting of three primary classes: Beer, Beer Style and Ingredients. There is a many-to-many relationship between Beer and Ingredients, and one-to-many relationship between Beer Style and Beer. The Beer and Beer Styles were joined on the “style shortname” that was given in the Beer attribute directly from the API. The Ingredients were loaded by calling the API with a beercode (“beer_id” in the API) in the url and returning all ingredients for each beer code. We created a full list of all beers and their ingredients, then iterated through that list to append ingredients to each beer instance. Unfortunately, we consistently got timed out of the API for calling ingredients this way. See “Limitations” at the bottom.



## Dashboard:

Our dashboard is built upon Dash for front-end interactive visualizations and Flask and the backend framework. We used several callback methods to allow for interactivity between styles. We also made a custom stylesheet for a more aesthetically-pleasing appeal.
At the top of our dashboard is the Style Selector and Description of that style. Under it, our dashboard consisted of three main tabs that provided more information about the selected style. This was done with the Style callback that would find the associated routes and update the visual on each tab accordingly.

<img src="https://user-images.githubusercontent.com/39356742/48685594-12007e00-eb85-11e8-86f9-bf921cce1e05.png" width="90%"></img> 

Once a style is selected you can see the number of beers analyzed with the given style, and the most common descriptors of beers in that style.

<img src="https://user-images.githubusercontent.com/39356742/48685670-71f72480-eb85-11e8-9360-8f2ba350c58d.png" width="90%"></img> 

The second tab displays a few specific beers in the selected style, as well as a food pairings to go along with that style.

<img src="https://user-images.githubusercontent.com/39356742/48685718-b8e51a00-eb85-11e8-86ce-3af244c34a54.png" width="90%"></img> 

The third tab displays the spread of the alcohol content (ABV) in that particular style, as well as the average, min, and max alcohol content for that style.

<img src="https://user-images.githubusercontent.com/39356742/48685743-d914d900-eb85-11e8-8346-b833c1f0deb9.png" width="90%"></img> 


## Limitations:

We upgraded to “Hobbyist” access that allowed us access to the full database. However, this was a limited access that only allowed us 200 requests a day. We generated data for each beer by paginating through through the API that retrieved 50 beers per request. Those 200 requests timed out pretty quickly each time we loaded our database, therefore we unable to completely load each ingredient or successfully append a list of ingredients to each individual beer. This feature will be included in the future!!
