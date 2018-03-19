# Scholar Bibtex Keys

Convert bibtex keys to Google scholar style: `[first-author-last-name][year][title-first-word]`.

## Usage

See function `convert_bibtex_keys(input_file, output_file)`.

## Example

Before:

```[bibtex]
@INCOLLECTION{Sutton2000-bq,
  title     = "Policy Gradient Methods for Reinforcement Learning with Function
               Approximation",
  booktitle = "Advances in Neural Information Processing Systems 12",
  author    = "Sutton, Richard S and McAllester, David A and Singh, Satinder P
               and Mansour, Yishay",
  editor    = "Solla, S A and Leen, T K and M{\"u}ller, K",
  publisher = "MIT Press",
  pages     = "1057--1063",
  year      =  2000
}
```

After:

```[bibtex]
@INCOLLECTION{sutton2000policy,
    author = "Sutton, Richard S and McAllester, David A and Singh, Satinder P and Mansour, Yishay",
    editor = {Solla, S A and Leen, T K and M{\"u}ller, K},
    title = "Policy Gradient Methods for Reinforcement Learning with Function Approximation",
    booktitle = "Advances in Neural Information Processing Systems 12",
    publisher = "MIT Press",
    pages = "1057--1063",
    year = "2000"
}
```