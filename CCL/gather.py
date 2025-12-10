"""
Gather (Many → 1)

Opposite of scatter. All processes send their chunks to one process
(usually rank 0), which collects them into a single tensor.

Rank 0: [A]  } 
Rank 1: [B]  }  Gather  -->  Rank 0: [A, B, C, D]
Rank 2: [C]  }              (others keep their chunks)
Rank 3: [D]  }

Example:
  Before: rank 0 has [10], rank 1 has [20], rank 2 has [30], rank 3 has [40]
  After:  rank 0 gets [10, 20, 30, 40], others unchanged

Pseudocode:
  if rank == 0:
      result = [my_chunk]
      for i in range(1, num_ranks):
          chunk = recv(source=i)
          result.append(chunk)
  else:
      send(my_chunk, dest=0)
"""
