<!DOCTYPE html>
<html>
<head>
    <title>{{ song.title }}</title>
</head>
<body>
    <h1>{{ song.title }}</h1>
    <p>Artist: {{ song.artist }}</p>
    <p>Genre: {{ song.genre }}</p>
    <p>{{ song.description }}</p>
    
    <iframe width="560" height="315" src="{{ song.audio_url | replace('watch?v=', 'embed/') }}" frameborder="0" allowfullscreen></iframe>
    
    <h2>Recommended Songs</h2>
    <ul>
        {% for rec in recommendations %}
        <li>
            <a href="{{ url_for('song_detail', song_id=rec.id) }}">
                {{ rec.title }} - {{ rec.artist }}
            </a>
        </li>
        {% endfor %}
    </ul>

    <p><a href="{{ url_for('index') }}">Back to list</a></p>
</body>
</html>
