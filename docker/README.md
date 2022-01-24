# katago-benchmark-docker

```
docker run -itd --rm --name=KATAGO --gpus all -v /Your/Path/to/Weights:/katago/data -e USER_NAME=USER_NAME -e USER_PASSWORD=USER_PASSWORD -e BACKEND=CUDA -e WEIGHTS=kata1-b40c256-s5341126656-d1285996791.bin.gz -e LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64 yaphets4desmond/katago:11.0.3-cudnn8-runtime-ubuntu18.04-tenosrrt8.0.0.3-opencl-stable bash -c "cd /katago && ./run.sh"

```

> * BACKEND can be CUDA, TENOSRRT or OPENCL
> * WEIGHTS must be included in your weights folder, you can use weight_downloader.py to download your weight first
