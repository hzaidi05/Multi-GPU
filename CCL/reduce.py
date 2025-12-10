"""
Reduce (Many → 1)

Everyone has a tensor, we sum them and only one process
(usually rank 0) gets the result. Others keep their original data.

Rank 0: [1, 2]  } 
Rank 1: [3, 4]  }  Reduce  -->  Rank 0: [4, 6]  (1+3, 2+4)
Rank 2: [5, 6]  }  (sum)        Others: unchanged
Rank 3: [7, 8]  }

Example:
  Before: rank 0 has [1,2], rank 1 has [3,4], rank 2 has [5,6], rank 3 has [7,8]
  After:  rank 0 gets [16, 20] (sum of all), others keep their original

Pseudocode:
  if rank == 0:
      result = my_tensor
      for i in range(1, num_ranks):
          other_tensor = recv(source=i)
          result = result + other_tensor  # element-wise
  else:
      send(my_tensor, dest=0)
"""
