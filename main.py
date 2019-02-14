from recommendations import critics
from engine import pearson_similarity, top_matches, get_recommendations

print('')
print('')

print('Pearson similarity between Lisa Rose and Gane Seymour')
print(pearson_similarity(critics, 'Lisa Rose', 'Gane Seymour'))
print('')
print('')

print('Top 2 matches for Michaes Phillips')
print top_matches(critics, 'Michael Phillips', 2)
print('')
print('')

print('Recommendations for Michael Phillips')
print get_recommendations(critics, 'Michael Phillips')
print('')
print('')
