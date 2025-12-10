"""
AlltoAll (Many → Many)

A tensor split into chunks across nodes. After alltoall, each process
gets chunk i from every other process. Quite an expensive op! key in serving MoEs.

Before AlltoAll:
  Rank 0: [A0, A1, A2, A3]
  Rank 1: [B0, B1, B2, B3]
  Rank 2: [C0, C1, C2, C3]
  Rank 3: [D0, D1, D2, D3]

After AlltoAll:
  Rank 0: [A0, B0, C0, D0]  (chunk 0 from everyone)
  Rank 1: [A1, B1, C1, D1]  (chunk 1 from everyone)
  Rank 2: [A2, B2, C2, D2]  (chunk 2 from everyone)
  Rank 3: [A3, B3, C3, D3]  (chunk 3 from everyone)

Example:
  Before: rank 0 has [10,20,30,40], rank 1 has [50,60,70,80], etc.
  After:  rank 0 gets [10,50,90,130] (first element from each rank)

Pseudocode:
  # Each rank scatters its chunks and gathers chunks from others
  my_chunks = split(my_tensor, num_ranks)
  
  result = []
  for i in range(num_ranks):
      # Send chunk i to rank i
      send(my_chunks[i], dest=i)
      # Receive chunk at my position from rank i
      chunk = recv(source=i)
      result.append(chunk)

TODO: try with torch.distributed.all_to_all() or build from send/recv primitives
"""
