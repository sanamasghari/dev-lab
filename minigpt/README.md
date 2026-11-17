# Mini-GPT from Scratch (PyTorch & Custom Tokenizers)

An educational, end-to-end implementation of a decoder-only Transformer language model (similar to GPT-2) built entirely from scratch using PyTorch. This project covers everything from raw text data engineering and custom Byte-Pair Encoding (BPE) tokenizers to a custom multi-head self-attention architecture and autoregressive text generation.

---

## Project Structure

```text
├── tokenizer1.py         # Character tokenizer & basic BPE training implementation
├── tokenizer2.py         # Production BPE tokenizer with GPT-2 regex pre-tokenization & Unicode NFKC normalization
├── data_pipeline.py      # Text cleaning, heuristic quality filtering, MinHash + LSH deduplication, sequence packing & dataloader
├── mini_gpt_torch.py     # Core Decoder-Only Transformer architecture, manual cross-entropy, training loop & generation
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Key Features Implemented

1. **Custom Tokenizers**:
   - Character-level mapping and custom BPE vocabulary training starting from 256 base UTF-8 bytes.
   - Non-overlapping pair merging algorithms.
   - GPT-2 regular expression pre-tokenization and special token management.

2. **Data Pipeline (`data_pipeline.py`)**:
   - HTML stripping, URL removal, non-ASCII noise filtering, and whitespace normalization.
   - Heuristic quality filtering (word count, caps ratio, special character density).
   - Near-duplicate document deduplication using **MinHash signatures** and **Locality-Sensitive Hashing (LSH)** with Jaccard similarity verification.
   - Token stream packing into fixed-length context windows with binary attention masks and a custom batch iterator.

3. **Decoder-Only Transformer (`mini_gpt_torch.py`)**:
   - Token & Positional embeddings.
   - Pre-LayerNorm architecture with manual Layer Normalization.
   - Multi-Head Self-Attention with causal autoregressive masking and manual scaled dot-product attention + softmax.
   - Position-wise Feed-Forward Networks (MLP) with ReLU activations.
   - Weight tying between token embeddings and the final linear projection layer.
   - Manual cross-entropy loss calculation via log-sum-exp trick.
   - Temperature-scaled text sampling using `torch.multinomial`.

---

## Installation & Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv gpt2_venv
   source gpt2_venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Code

- **Run Tokenizer 1 tests and demos:**
  ```bash
  python tokenizer1.py
  ```
- **Run Production Tokenizer 2 demos:**
  ```bash
  python tokenizer2.py
  ```
- **Run Data Pipeline preprocessing and statistics:**
  ```bash
  python data_pipeline.py
  ```
- **Run Mini-GPT training and generation:**
  ```bash
  python mini_gpt_torch.py
  ```