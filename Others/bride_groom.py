
# A ceremony where a Bride chooses her Groom from an array of eligible bachelors is called
# Swayamvar. But this is a Swayamvar with difference. An array of Bride-to-be will choose
# from an array of Groom-to-be.

# The arrangement at this Swayamvar is as follows:

# Brides-to-be are organized such that the most eligible bachelorette will get first chance
# to choose her Groom. Only then, the next most eligible bachelorette will get a chance
# to choose her Groom
# If the initial most eligible bachelorette does not get a Groom of her choice, none of the
# Brides-to-be have any chance at all to get married. So, unless a senior bachelorette is
# out of the “queue”, the junior bachelorette does not get a chance to select her Groom-to-be
# Initial state of Grooms-to-be is such that most eligible bachelor is at the head of the
# “queue”. The next most eligible bachelor is next in the queue. So on and so forth.
# Now everything hinges on the choice of the bachelorette. The most eligible bachelorette
# will now meet the most eligible bachelor.
# If bachelorette selects the bachelor, both, the bachelorette and the bachelor are now
# Bride and Groom respectively and will no longer be a part of the Swayamvar activity.
# Now, the next most eligible bachelorette will get a chance to choose her Groom. Her
# first option is the next most eligible bachelor (relative to initial state)
# If the most eligible bachelorette passes the most eligible bachelor, the most eligible
# bachelor now moves to the end of the queue. The next most eligible bachelor is now
# considered by the most eligible bachelorette. Selection or Passing over will have the
# same consequences as explained earlier.
# If most eligible bachelorette reaches the end of bachelor queue, then the Swayamvar
# is over. Nobody can get married.


# Given a mix of Selection or Passing over, different pairs will get formed.

# The selection criteria is as follows

# Each person either drinks rum or mojito. Bride will choose groom only if he drinks
# the same drink as her.

# Note: There are equal number of brides and grooms for the Swayamvar.
# Tyrion as the hand of the king wants to know how many pairs will be left unmatched.
# Can you help Tyrion?


# Input Format:
# First line contains one integer N, which denotes the number of brides and grooms
# taking part in the Swayamvar.
# Second line contains a string in lowercase, of length N containing initial state
# of brides-to-be.
# Third line contains a string in lowercase, of length N containing initial state of
# grooms-to-be. Each string contains only lowercase 'r' and 'm' stating person at that index
# drinks "rum"(for 'r') or mojito(for 'm').


# Output:
# Output a single integer denoting the number of pairs left unmatched.

# Example:
# Input
# 4
# rrmm
# mrmr

# Output
# 0

# Explanation

# The bride at first place will only marry groom who drinks rum. So, the groom at first
# place will join the end of the queue. Updated groom's queue is "rmrm".

# Now the bride at first place will marry the groom at first place. Updated
# bride's queue is "rmm" and groom's queue is "mrm".

# The process continues and at last there are no pairs left. So answer is 0.

N = int(input())  # number of groom or bride
brides_to_be = list(input())
grooms_to_be = list(input())

number_of_pairs_left_unmatched = N

for bride in brides_to_be:
    if bride in grooms_to_be:
        # brides_to_be.remove(bride)
        grooms_to_be.remove(bride)
        number_of_pairs_left_unmatched -= 1
    else:
        break

print(number_of_pairs_left_unmatched)
