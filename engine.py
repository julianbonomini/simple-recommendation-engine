from math import sqrt


# Returns the Pearson correlation coefficient for person1 and person2
def pearson_similarity(prefs, person1, person2):
    # Get the list of shared_items
    shared_items = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            shared_items[item] = 1

    # Finde the number of ellements
    number_of_shared_items = len(shared_items)

    # if they have no ratings in common, return 0
    if number_of_shared_items == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[person1][item] for item in shared_items])
    sum2 = sum([prefs[person2][item] for item in shared_items])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[person1][item], 2) for item in shared_items])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in shared_items])

    # Sum up the products
    products_sum = sum([prefs[person1][item]*prefs[person2][item]
                        for item in shared_items])

    # Callculate Paerson score
    num = products_sum-(sum1*sum2/number_of_shared_items)
    den = sqrt((sum1Sq-pow(sum1, 2)/number_of_shared_items)
               * (sum2Sq-pow(sum2, 2)/number_of_shared_items))
    if den == 0:
        return 0
    return num/den


# Returns the best matches for the person from the the dictionary
def top_matches(prefs, person, n=5):
    scores = [(pearson_similarity(prefs, person, other), other)
              for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


# Get recommendations for a person by using weighted average of other users rankings
def get_recommendations(prefs, person):
    totals = {}
    similarity_sums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue
        sim = pearson_similarity(prefs, person, other)
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                similarity_sums.setdefault(item, 0)
                similarity_sums[item] += sim

    # Create the normalized list
    rankings = [(total/similarity_sums[item], item)
                for item, total in totals.items()]

    # Return sorted list
    rankings.sort()
    rankings.reverse()
    return rankings
