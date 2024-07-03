const pokemonIds = [2, 4, 7];

function fetchPokemon(id) {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
        .then(response => response.json())
        .catch(error => console.error('Error fetching Pokémon:', error));
}

Promise.all(pokemonIds.map(id => fetchPokemon(id)))
    .then(pokemon_list => {
        pokemon_list.forEach(pokemon => console.log(pokemon.name));
    })
    .catch(error => console.error('Error fetching Pokémon:', error));