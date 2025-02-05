Count pairs from an array
# Python3 program for
# the above approach
MAXN = 100005

# Function to count required
# number of pairs
def countPairs(arr, N):

	# Stores count of pairs
	desiredPairs = 0

	# Initialize hash with 0
	hash = [0] * MAXN

	# Count frequency of
	# each element
	for i in range(N):
		hash[abs(arr[i])] += 1
	
	# Calculate desired number
	# of pairs
	for i in range(MAXN):
		desiredPairs += ((hash[i]) *
						(hash[i] - 1)) // 2
	
	# Print desired pairs
	print (desiredPairs)

# Driver Code
if __name__ == "__main__":

	# Given arr[]
	arr = [2, -2, 1, 1]

	# Size of the array
	N = len(arr)

	# Function Call
	countPairs(arr, N)

# This code is contributed by Chitranayal
