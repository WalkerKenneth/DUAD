const pokemonIds = [2, 4, 7];

function fetchPokemon(id) {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
        .then(response => response.json())
        .catch(error => console.error('Error fetching Pokémon:', error));
}

Promise.any(pokemonIds.map(id => fetchPokemon(id)))
    .then(pokemon => {
        console.log(pokemon.name);
    })
    .catch(error => console.error('Error fetching Pokémon:', error));