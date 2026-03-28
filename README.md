# mike (for Zensical)

> [!NOTE]
>
> Don't know what Zensical is? Read the [announcement blog post](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/).

This fork makes [mike](https://github.com/jimporter/mike) compatible with
[Zensical](https://zensical.org), a modern static site generator built by the
Material for MkDocs team. Please note that this is part of our effort to
enable the MkDocs ecosystem to switch to Zensical as soon as possible, and
should be considered a temporary solution until Zensical provides
[native support for versioning](https://zensical.org/about/roadmap/#versioning)
in the coming months.

Zensical's upcoming native versioning will allow to deploy versioned
documentation anywhere, not only on GitHub Pages, and allow for more degrees
of freedom in how versions are deployed and served. All `mike` commands stay
the same. Limitations:

1. No theme support besides Zensical's default theme.
2. Installation must happen from GitHub – this fork won't be published on PyPI.
3. This fork is based on mike 2.2.0 - we only intend to provide bug fixes.

## Installation

```
pip install git+https://github.com/squidfunk/mike.git
```

## Usage

Please see mike's documentation for usage:
https://github.com/jimporter/mike?tab=readme-ov-file#mike

## Acknowledgements

[Jim Porter](https://github.com/jimporter/) has created and maintained mike for
years, and we are grateful for his work on this project, enabling users of
Material for MkDocs to deploy versioned documentation to GitHub Pages. This
fork is based on his work, and we will continue to maintain it until Zensical
provides native support for versioning.

## License

This project is licensed under the [BSD 3-clause license](LICENSE).
