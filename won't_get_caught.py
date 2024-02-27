def small_players_to_remove(heights, k):
  count = 0
  for height in heights: #Applying for loop for each number (height) 
    if height > k: 
      count += 1 #if height is smaller than k increasing the count

  return count #Returning the count

T = int(input()) #asking for the input in integer type

for _ in range(T): 
  N, K = map(int, input().split()) # reading number of players and height
  heights = list(map(int, input().split())) # reading it into a list
  result = small_players_to_remove(heights, K) # Calling the function to find the minimum numbers of players to remove
  print(result)
