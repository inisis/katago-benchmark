# katago-benchmark

nnEvals/s: the bigger the better

## 1.9.1 cuda b40-s985(cuda11.0)

```
./katago benchmark -config ../default_gtp.cfg  -model ../../weights/kata1-b40c256-s9854456576-d2405111631.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```

| |  A100PCIE   | A30  | GTX1080TI  | RTX2080TI  | RTX3080  | RTX3090  | V100| V100S |
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
|  nnEvals/s | 3558  | 2212  | 425  | 1225  | 1376  | 1607  | 1784  | 1773 |


## 1.10.0 tensorrt b40-s1080(cuda 11.0 tensorrt 8.0.0.3)

```
./katago benchmark -config ../test.cfg  -model ../kata1-b40c256-s10800760064-d2633359377.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```

| |  A100PCIE   | A30  | GTX1080TI  | RTX2080TI  | RTX3080  | RTX3090  | V100| V100S |
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
|  nnEvals/s  | 3986  | 2533  | 285  | 1975  |  2296 |  2590 | 2084  |  2070 |
