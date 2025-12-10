"""
ReduceScatter (Many → Many)

Everyone has a tensor, we sum them, then split up the
result so each process gets a different chunk. More efficient than doing
reduce then scatter separately.

Rank 0: [1, 2]  } 
Rank 1: [3, 4]  }  ReduceScatter  -->  Rank 0: [4]   (sum of first elements)
Rank 2: [5, 6]  }                      Rank 1: [6]   (sum of second elements)
Rank 3: [7, 8]  }                       Rank 2: [12]  (sum of third elements)
                                       Rank 3: [14]  (sum of fourth elements)

Example:
  Before: rank 0 has [1,2], rank 1 has [3,4], rank 2 has [5,6], rank 3 has [7,8]
  After:  rank 0 gets [16] (sum of all first elements), rank 1 gets [20] (sum of all second elements), etc.

Pseudocode:
  # First reduce (sum) all tensors
  if rank == 0:
      total = my_tensor
      for i in range(1, num_ranks):
          total = total + recv(source=i)
  else:
      send(my_tensor, dest=0)
      total = recv(source=0)
  
  # Then scatter the result
  chunks = split(total, num_ranks)
  my_chunk = chunks[rank]

TODO: try with torch.distributed.reduce_scatter() or build from send/recv primitives
"""
