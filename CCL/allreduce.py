"""
AllReduce (Many → Many)

Each node has a tensor, we combine them (usually sum), and everyone gets
the same result. Most common op in distributed training.

Rank 0: [1, 2]  } 
Rank 1: [3, 4]  }  AllReduce  -->  all nodes: [16, 20]  (sum of all)
Rank 2: [5, 6]  }  (sum)
Rank 3: [7, 8]  }

Example:
  Before: rank 0 has [1,2], rank 1 has [3,4], rank 2 has [5,6], rank 3 has [7,8]
  After:  everyone has [16, 20] (element-wise sum: 1+3+5+7, 2+4+6+8)

Pseudocode:
  # Can be done as reduce + broadcast
  if rank == 0:
      result = my_tensor
      for i in range(1, num_ranks):
          result = result + recv(source=i)
      # now broadcast result to everyone
      for i in range(1, num_ranks):
          send(result, dest=i)
  else:
      send(my_tensor, dest=0)
      result = recv(source=0)

# But real implementations use smarter algorithms (ring, tree, etc. which will be explored below)

TODO: try with torch.distributed.all_reduce() or build from send/recv primitives
"""
