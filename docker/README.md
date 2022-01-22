# katogo-benchmark-docker

docker run -it --rm --gpus all -v /path/to/your/weights:/katago/data -e USER_NAME=YOURUSERNAME -e USER_PASSWORD=YOURPASSWORD -e BACKEND=TENSORRT -e WEIGHTS=kata1-b40c256-s5341126656-d1285996791.bin.gz yaphets4desmond/katago:11.0.3-cudnn8-runtime-ubuntu18.04-tenosrrt8.0.0.3-opencl-v2
