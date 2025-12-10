"""
Broadcast (1 → Many)

One process (usually rank 0) has some data and sends a copy to everyone.
Everyone ends up with the same thing.

Rank 0: [A, B, C, D]  -->  Broadcast  -->  All ranks: [A, B, C, D]

Example:
  Before: rank 0 has [10, 20, 30, 40], others have nothing/zeros
  After:  everyone has [10, 20, 30, 40]

Pseudocode:
  if rank == 0:
      for i in range(1, num_ranks):
          send(data, dest=i)
  else:
      data = recv(source=0)
"""
