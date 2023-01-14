def find_country(countries, country):
    &quot;&quot;&quot;
    Countries within a dictionary. country is the key.
    Code by the principle EAFP.
    &quot;&quot;&quot;
    
    try:
        return countries[country]
    except KeyError:
        return None

