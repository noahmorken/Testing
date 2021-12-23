def format_city(city, country, population=''):
    """Generates neatly formatted city information."""
    if population:
        formatted_layout = f"{city}, {country} - population {population}"
    else:
        formatted_layout = f"{city}, {country}"
    return formatted_layout.title()