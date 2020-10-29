ash = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

pokeList = ash.split(" ")

def longest_seq(sequence):

    def recursion(pokemonS, previous_pokemon=None):
        # Creates an empty sequence which is valid
        yield []
        # Creates a new list of pokemons that will not consider the previous pokemon
        pokemonS = [pokemon for pokemon in pokemonS if pokemon != previous_pokemon] # Initialized as a generator
        for pokemon in pokemonS:
            # Checks if the pokemon going through the function is not a previous pokemon
            if not previous_pokemon or pokemon.startswith(previous_pokemon[-1]):
                for edge in recursion(pokemonS, previous_pokemon=pokemon):
                    yield [pokemon] + edge

    return max(recursion(sequence), key=len) # Returns the longest list

print(longest_seq(pokeList))

# Much slower than JC's dictionary method
# Takes 50 seconds to run