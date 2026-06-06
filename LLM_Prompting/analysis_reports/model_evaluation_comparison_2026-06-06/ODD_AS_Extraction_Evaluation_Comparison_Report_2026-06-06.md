# ODD AS Extraction Evaluation Tables

Date: 2026-06-06

## Run Completeness

| Case | Condition | Model | Run_Count | Expected_Runs | Missing_Runs | Duplicate_Run_Count | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EV-parking | ODD+game | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| EV-parking | ODD+game | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| EV-parking | ODD+game | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |
| EV-parking | ODD-only | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| EV-parking | ODD-only | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| EV-parking | ODD-only | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |
| Electricity | ODD+game | DeepSeek-R1 | 30 | 30 |  | 0 | Complete |
| Electricity | ODD+game | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| Electricity | ODD+game | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| Electricity | ODD+game | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |
| Electricity | ODD-only | DeepSeek-R1 | 30 | 30 |  | 0 | Complete |
| Electricity | ODD-only | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| Electricity | ODD-only | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| Electricity | ODD-only | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |
| Water-use | ODD+game | DeepSeek-R1 | 30 | 30 |  | 0 | Complete |
| Water-use | ODD+game | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| Water-use | ODD+game | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| Water-use | ODD+game | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |
| Water-use | ODD-only | DeepSeek-R1 | 30 | 30 |  | 0 | Complete |
| Water-use | ODD-only | DeepSeek-V4-Pro | 30 | 30 |  | 0 | Complete |
| Water-use | ODD-only | Llama-3.3-70B | 30 | 30 |  | 0 | Complete |
| Water-use | ODD-only | Qwen2.5-7B | 30 | 30 |  | 0 | Complete |

## Overall Evaluation Results

| Case | Condition | Model | Runs | TP | FN | FP | Precision | Recall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-parking | ODD+game | DeepSeek-V4-Pro | 30 | 90 | 90 | 156 | 0.3659 | 0.5000 |
| EV-parking | ODD-only | DeepSeek-V4-Pro | 30 | 66 | 114 | 143 | 0.3158 | 0.3667 |
| EV-parking | ODD+game | Llama-3.3-70B | 30 | 57 | 123 | 31 | 0.6477 | 0.3167 |
| EV-parking | ODD-only | Llama-3.3-70B | 30 | 39 | 141 | 24 | 0.6190 | 0.2167 |
| EV-parking | ODD+game | Qwen2.5-7B | 30 | 81 | 99 | 101 | 0.4451 | 0.4500 |
| EV-parking | ODD-only | Qwen2.5-7B | 30 | 42 | 138 | 149 | 0.2199 | 0.2333 |
| Electricity | ODD+game | DeepSeek-R1 | 30 | 180 | 0 | 4 | 0.9783 | 1.0000 |
| Electricity | ODD-only | DeepSeek-R1 | 30 | 164 | 16 | 12 | 0.9318 | 0.9111 |
| Electricity | ODD+game | DeepSeek-V4-Pro | 30 | 91 | 89 | 10 | 0.9010 | 0.5056 |
| Electricity | ODD-only | DeepSeek-V4-Pro | 30 | 64 | 116 | 1 | 0.9846 | 0.3556 |
| Electricity | ODD+game | Llama-3.3-70B | 30 | 166 | 14 | 3 | 0.9822 | 0.9222 |
| Electricity | ODD-only | Llama-3.3-70B | 30 | 176 | 4 | 4 | 0.9778 | 0.9778 |
| Electricity | ODD+game | Qwen2.5-7B | 30 | 180 | 0 | 103 | 0.6360 | 1.0000 |
| Electricity | ODD-only | Qwen2.5-7B | 30 | 177 | 3 | 52 | 0.7729 | 0.9833 |
| Water-use | ODD+game | DeepSeek-R1 | 30 | 49 | 11 | 10 | 0.8305 | 0.8167 |
| Water-use | ODD-only | DeepSeek-R1 | 30 | 46 | 14 | 9 | 0.8364 | 0.7667 |
| Water-use | ODD+game | DeepSeek-V4-Pro | 30 | 20 | 40 | 23 | 0.4651 | 0.3333 |
| Water-use | ODD-only | DeepSeek-V4-Pro | 30 | 17 | 43 | 22 | 0.4359 | 0.2833 |
| Water-use | ODD+game | Llama-3.3-70B | 30 | 54 | 6 | 62 | 0.4655 | 0.9000 |
| Water-use | ODD-only | Llama-3.3-70B | 30 | 55 | 5 | 53 | 0.5093 | 0.9167 |
| Water-use | ODD+game | Qwen2.5-7B | 30 | 39 | 21 | 52 | 0.4286 | 0.6500 |
| Water-use | ODD-only | Qwen2.5-7B | 30 | 36 | 24 | 58 | 0.3830 | 0.6000 |

## ODD+game Minus ODD-only

| Case | Model | Delta_TP | Delta_FN | Delta_FP | Delta_Precision | Delta_Recall |
| --- | --- | --- | --- | --- | --- | --- |
| EV-parking | DeepSeek-V4-Pro | 24.0000 | -24.0000 | 13.0000 | +0.0501 | +0.1333 |
| EV-parking | Llama-3.3-70B | 18.0000 | -18.0000 | 7.0000 | +0.0287 | +0.1000 |
| EV-parking | Qwen2.5-7B | 39.0000 | -39.0000 | -48.0000 | +0.2252 | +0.2167 |
| Electricity | DeepSeek-R1 | 16.0000 | -16.0000 | -8.0000 | +0.0464 | +0.0889 |
| Electricity | DeepSeek-V4-Pro | 27.0000 | -27.0000 | 9.0000 | -0.0836 | +0.1500 |
| Electricity | Llama-3.3-70B | -10.0000 | 10.0000 | -1.0000 | +0.0045 | -0.0556 |
| Electricity | Qwen2.5-7B | 3.0000 | -3.0000 | 51.0000 | -0.1369 | +0.0167 |
| Water-use | DeepSeek-R1 | 3.0000 | -3.0000 | 1.0000 | -0.0059 | +0.0500 |
| Water-use | DeepSeek-V4-Pro | 3.0000 | -3.0000 | 1.0000 | +0.0292 | +0.0500 |
| Water-use | Llama-3.3-70B | -1.0000 | 1.0000 | 9.0000 | -0.0437 | -0.0167 |
| Water-use | Qwen2.5-7B | 3.0000 | -3.0000 | -6.0000 | +0.0456 | +0.0500 |

## Aggregate Evaluation Results

| Model | Condition | Case_Count | Runs | TP | FN | FP | Precision | Recall | Cases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DeepSeek-R1 | ODD+game | 2 | 60 | 229 | 11 | 14 | 0.9424 | 0.9542 | Electricity,Water-use |
| DeepSeek-R1 | ODD-only | 2 | 60 | 210 | 30 | 21 | 0.9091 | 0.8750 | Electricity,Water-use |
| DeepSeek-V4-Pro | ODD+game | 3 | 90 | 201 | 219 | 189 | 0.5154 | 0.4786 | EV-parking,Electricity,Water-use |
| DeepSeek-V4-Pro | ODD-only | 3 | 90 | 147 | 273 | 166 | 0.4696 | 0.3500 | EV-parking,Electricity,Water-use |
| Llama-3.3-70B | ODD+game | 3 | 90 | 277 | 143 | 96 | 0.7426 | 0.6595 | EV-parking,Electricity,Water-use |
| Llama-3.3-70B | ODD-only | 3 | 90 | 270 | 150 | 81 | 0.7692 | 0.6429 | EV-parking,Electricity,Water-use |
| Qwen2.5-7B | ODD+game | 3 | 90 | 300 | 120 | 256 | 0.5396 | 0.7143 | EV-parking,Electricity,Water-use |
| Qwen2.5-7B | ODD-only | 3 | 90 | 255 | 165 | 259 | 0.4961 | 0.6071 | EV-parking,Electricity,Water-use |
