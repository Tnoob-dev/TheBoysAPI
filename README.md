## The Boys API

This API allows you to access information about characters and episodes from the series "The Boys".

Features:

* Characters: Get information about each character, including their name, alias, description, affiliation, and photo.
* Episodes: Find details of each episode, including its title, description, air date, and main cast.

How to use the API:

1. Authentication: The API does not require authentication.
2. Endpoints:
    * Characters: /characters
        * Example: /characters (to get information about all characters)
        * Example: /characters/{character_id} (to get information about a specific character by his ID)
    * Episodes: /episodes
        * Example: /episodes (to get information about all episodes)
        * Example: /episodes/{episode_id} (to get information about a specific episode by his ID)

Example response:
```json
{
  "id": 3,
  "description": "Homelander is the main antagonist of the Amazon series The Boys, a recurring antagonist of its spin-off series The Boys Presents: Diabolical and one of the overarching antagonists of the spin-off series Gen V.  Homelander is the leader of The Seven, the strongest Supe in the world, and the archenemy of Billy Butcher and The Boys. With the face of a movie star and the powers of a god, Homelander is considered the greatest superhero alive. Not only can he fly, but he possesses super strength and super durability far beyond the capacity of other superheroes, super senses (sight, hearing, etc.), X-ray vision and laser vision.  On the surface, he's affable, modest, and sincere; the ultimate boy scout, an American treasure, a God-loving patriot. But just like regular mortals, even superheroes have secrets.",
  "name": "Homelander",
  "actor_name": "Antony Starr",
  "full_name": "John",
  "image_url": "https://static.wikia.nocookie.net/amazons-the-boys/images/5/5b/Homelander-S4.png",
  "gender": "Male"
}
```
Installation:

No installation is required. The API is available online.

Examples:

* https://theboysapi.onrender.com/docs

Contribution:

Contributions are welcome. To contribute, please contact cristiandeleonmonzon@gmail.com.

License:

This API is licensed under the MIT license.

Note:

This API is for educational purposes only and is not intended for commercial use. The information provided is for entertainment purposes only and may not be accurate.

# Credits to:
## Images, names, descriptions and full names of characters -> the-boys.fandom.com
## All info about episodes -> imdb.com
