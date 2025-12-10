# Multi-GPU

This repo stores my notes on learning how to scale out to multiple devices.
I've covered:
- The main Collective Communication primitives (Scatter, Gather, AlltoAll, AllReduce, ReduceScatter, Reduce, Broadcast)
- How operations are calculated when the tensors in question are sharded across multiple devices (softmax, conv, gemm)
- TBA: Parallelism strats; DDP, FSDP, PP, EP

I find learning scale out much more appealing visually, so I hope to transcribe my scribbles (which have most of the notes) to excalidraw so I have a place to store them soon 
