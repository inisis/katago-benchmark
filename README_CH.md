[English Version](README.md)

katago-benchmark

nnEvals/s: 数值越大代表性能越好

## 1.9.1 cuda b40-s985(cuda11.0)

```
./katago benchmark -config ../default_gtp.cfg  -model ../../weights/kata1-b40c256-s9854456576-d2405111631.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```

| |  A100PCIE   | A30  | GTX1080TI  | RTX2080TI  | RTX3080  | RTX3090  | V100| V100S | A40 | A5000 |
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
|  nnEvals/s | 3558  | 2212  | 425  | 1225  | 1376  | 1607  | 1784  | 1773 |  2473 |  1548 |


## 1.10.0 tensorrt b40-s1080(cuda 11.0 tensorrt 8.0.0.3)

```
./katago benchmark -config ../test.cfg  -model ../kata1-b40c256-s10800760064-d2633359377.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```

| |  A100PCIE   | A30  | GTX1080TI  | RTX2080TI  | RTX3080  | RTX3090  | V100| V100S | A40 | A5000 |
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
|  nnEvals/s  | 3986  | 2533  | 285  | 1975  |  2296 |  2590 | 2084  |  2070 |  2920 |  2323 |


## 1.10.0 opencl b40-s1080

```
./katago benchmark -config ../test.cfg  -model ../kata1-b40c256-s10800760064-d2633359377.bin.gz -v 5000 -t 32,48,64,80,96,112,128
```

| |  A100PCIE   | GTX1080TI  | RTX2080TI | RTX3090  | V100 | V100S | Mac Air M1 | A40 | A5000 |
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----  |
|  nnEvals/s  | 2230 | 315  | 1086 |  1959 | 1509  |  1634 | 93  | 1788  | 1500  |