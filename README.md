# Surprise-me-API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
API returns surprising responses, according to the parameters passed by the client. 

For running on localhost:
    - Clone the repository to your computer.
    - From the main folder, run the command: env\Scripts\activate
    - For running the API, run the command: python app.py
    - For running tests, run the command: python test.py
    
Routes:
    GET /api/stats
      Returns the number of previous requests to the /surprise route.
      
    GET /api/surprise
      Gets two parameters- name, birth year and return a suprising response:
      - 2015<=birth year --> Surprising Dog
      - 2010<=birth year<2015 --> Taco Recipe
      - birth year<=2000 --> Chuck Norris Joke
      - 2000<birth year<2010 AND name doesn't begin with A or Z --> Kanye West Quote
      - 2000<birth year<2010 AND name doesn't begin with Z --> User Name’s Sum
      - Otherwise --> Error
      example: http://localhost:5000/api/surprise?name=Shir&birth_year=1994

