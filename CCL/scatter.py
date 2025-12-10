"""
Scatter (1 → Many)

One process (usually rank 0) has a full tensor and splits it up, sending
different chunks to different processes.

Rank 0: [A, B, C, D]  -->  Scatter  -->  Rank 0: [A]
                                         Rank 1: [B]
                                         Rank 2: [C]
                                         Rank 3: [D]

Example:
  Before: rank 0 has [10, 20, 30, 40]
  After:  rank 0 gets [10], rank 1 gets [20], rank 2 gets [30], rank 3 gets [40]

Pseudocode:
  if rank == 0:
      # split data into chunks
      chunks = split(data, num_ranks)
      for i in range(num_ranks):
          send(chunks[i], dest=i)
  else:
      my_chunk = recv(source=0)
"""
