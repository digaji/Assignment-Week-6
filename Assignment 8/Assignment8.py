ash = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

pokeList = ash.split(" ")

pokeDict = {}
for name in pokeList:
    if name[0] not in pokeDict:
        pokeDict[name[0]] = [name]
    else:
        pokeDict[name[0]].append(name)


def longest_seq(sequence):
    longest_chain = []

    def recursion(chain):
        nonlocal longest_chain
        if len(chain) > len(longest_chain):
            longest_chain = chain
        if chain[-1][-1] in pokeDict:
            for name in pokeDict[chain[-1][-1]]:
                if name not in chain:
                    recursion(chain + [name])

    for pokemon in sequence:
        recursion([pokemon])
    return longest_chain


print(longest_seq(pokeList))